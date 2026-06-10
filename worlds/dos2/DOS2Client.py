from __future__ import annotations
from itertools import count

import os
import sys
import asyncio
import typing
from typing import Tuple, List, Iterable, Dict

from .World import DOS2World
from .Items import AP_ITEM_TO_DOS2_ID, IS_DUPEABLE
from .Locations import DOS2_LOCATION_TO_AP_LOCATIONS, LOCATION_NAME_TO_ID

import ModuleUpdate
ModuleUpdate.update()

import Utils
import json
import logging

if __name__ == "__main__":
    Utils.init_logging("DOS2Client", exception_logger = "Client")

from NetUtils import ClientStatus
from CommonClient import gui_enabled, logger, get_base_parser, ClientCommandProcessor, \
    CommonContext, server_loop

goal = -1
bad_states = []
buggedLocations = ["Victory_Escape_Reapers_Eye"]

class DOS2ClientCommandProcessor(ClientCommandProcessor):
    def _cmd_resync(self):
        """Manually resync"""
        self.output(f"Syncing items...")
        self.syncing = True

    def _cmd_deathlink(self):
        if(isinstance(self.ctx, DOS2Context)):
            self.ctx.has_death_link = not self.ctx.has_death_link
            Utils.async_start(self.ctx.update_death_link(self.ctx.has_death_link), name = "Update Deathlink")
            if(self.ctx.has_death_link):
                path = os.path.join(self.ctx.comm_file_directory, self.ctx.deathlink_out)
                if(os.path.exists(path)):
                    with open(path, 'w') as f:
                        f.write("[]")
                self.output(f"Deathlink enabled.")
            else:
                path = os.path.join(self.ctx.comm_file_directory, self.ctx.deathlink_in)
                if(os.path.exists(path)):
                    with open(path, 'w') as f:
                        f.write("[]")
                self.output(f"Deathlink disabled.")
    
class DOS2Context(CommonContext):
    command_processor = DOS2ClientCommandProcessor
    game = "Divinity Original Sin 2"
    items_handling = 0b111 #full remote
    has_death_link: bool = False
    comm_file_sent_items = "apIn.json"
    comm_file_locations_checked = "apOut.json"
    sync_option = "apOptions.json"
    deathlink_in = "deathlinkIn.json"
    deathlink_out = "deathlinkOut.json"
    seed_name = ""
    comm_file_directory = "" #os.path.join(os.path.expanduser("~"), "Documents", "Larian Studios", "Divinity Original Sin 2 Definitive Edition", "Osiris Data")

    def __init__(self, server_address, password):
        super(DOS2Context, self).__init__(server_address, password)
        self.send_index: int = 0
        self.syncing = False
        self.awaiting_bridge = False
        game_options = DOS2World.settings
        if(game_options and getattr(game_options, "root_directory", None)):
            print(f"trying to see if {getattr(game_options, "root_directory", None)} is the right directory")
            try:
                self.comm_file_directory = game_options.root_directory
            except FileNotFoundError:
                self.comm_file_directory = ""
        else:
            self.comm_file_directory = ""

        # if(not os.path.isfile(os.path.join(self.comm_file_directory, self.comm_file_sent_items))):
        #     with open(self.comm_file_sent_items, "w") as file:
        #         file.write("[]")
        # if(not os.path.isfile(os.path.join(self.comm_file_directory, self.comm_file_locations_checked))):
        #     with open(self.comm_file_locations_checked, "w") as file:
        #         file.write("[]")
        
    def on_deathlink(self, data: typing.Dict[str, typing.Any]) -> None:
        with open(os.path.join(self.comm_file_directory, self.deathlink_in), 'w') as file:
            file.write('["Deathlink"]')
        super(DOS2Context, self).on_deathlink(data)

    async def server_auth(self, password_request: bool = False):
        if(password_request and not self.password):
            await super(DOS2Context, self).server_auth(password_request)
        await self.get_username()
        await self.send_connect()

    async def connection_closed(self):
        await super(DOS2Context, self).connection_closed()
        self.checked_locations.clear()
        self.server_locations.clear()
        self.finished_game = False

    @property
    def endpoints(self):
        if(self.server):
            return [self.server]
        else:
            return []
        
    async def shutdown(self):
        await super(DOS2Context, self).shutdown()
        self.checked_locations.clear()
        self.server_locations.clear()
        self.finished_game = False
    
    def remove_comm_files(self):
        for root, dirs, files in os.walk(os.path.join(os.path.expanduser("~"), "Documents", "Larian Studios", "Divinity Original Sin 2 Definitive Edition", "Osiris Data")):
            for file in files:
                if(file.find("apIn") != -1 or file.find("apOut") != -1 or file.find("deathlink") != -1 or file.find("apOptions") != -1):
                    os.remove(file)

    def run_gui(self):
        from kvui import GameManager

        class DOS2Manager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Divinity Orginal Sin 2 Client"
        
        self.ui = DOS2Manager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name = "UI")
    
    def on_package(self, cmd: str, args: dict):
        if(cmd in {"Connected"}):
            slot_data = args["slot_data"]
            if("seed_name" in args and args["seed_name"]):
                self.seed_name = args["seed_name"]
            self.has_death_link = slot_data.get("death_link", False)
            Utils.async_start(self.update_death_link(self.has_death_link), name = "Update Deathlink")
            global goal
            goal = slot_data["goal"]
            sync_option_path = os.path.join(self.comm_file_directory, self.sync_option)
            with open(sync_option_path, 'w') as f:
                json.dump(slot_data, f)
            received_items = [AP_ITEM_TO_DOS2_ID[self.item_names.lookup_in_game(network_item.item)] for network_item in self.items_received]
            with open(os.path.join(self.comm_file_directory, self.seed_name + self.comm_file_sent_items), 'w') as f:
                json.dump(received_items, f)
            
        if cmd in {"RoomInfo"}:
            if("seed_name" in args and args["seed_name"]):
                self.seed_name = args["seed_name"]
        
        if(cmd in {"ReceivedItems"}):
            received_items = [AP_ITEM_TO_DOS2_ID[self.item_names.lookup_in_game(network_item.item)] for network_item in self.items_received]
            fillercounter = count()
            received_items = [f"Dupe-{next(fillercounter):04}-{item}" if IS_DUPEABLE.get(item, False)
                              else item for item in received_items]
            with open(os.path.join(self.comm_file_directory, self.seed_name + self.comm_file_sent_items), 'w') as f:
                json.dump(received_items, f)
        
        if(cmd in {"RoomUpdate"}):
            pass

async def game_watcher(ctx: DOS2Context):
    while not ctx.exit_event.is_set():
        try:
            if ctx.syncing == True:
                sync_msg = [{'cmd': 'Sync'}]
                await ctx.send_msgs(sync_msg)
                ctx.syncing = False
            sending = []
            victory = False
            dos2LocationsToSend = []

            if(ctx.seed_name is not None):
                path = os.path.join(ctx.comm_file_directory, ctx.seed_name + ctx.comm_file_locations_checked)
                if(os.path.isfile(path)):
                    with open(path, 'r') as f:
                        dos2LocationsToSend = json.load(f)
                else:
                    with open(path, 'w') as f:
                        f.write("[]")
                if(goal != -1):
                    if(goal not in [0]):
                        logger.error(goal)
                    for loc in dos2LocationsToSend:
                        if(loc in DOS2_LOCATION_TO_AP_LOCATIONS):
                            for apLoc in DOS2_LOCATION_TO_AP_LOCATIONS[loc]:
                                if(apLoc not in ctx.checked_locations and apLoc in LOCATION_NAME_TO_ID):
                                    sending += [LOCATION_NAME_TO_ID[apLoc]]
                                    ctx.checked_locations.add(LOCATION_NAME_TO_ID[apLoc])
                                if(apLoc not in LOCATION_NAME_TO_ID and apLoc not in buggedLocations):
                                    logger.error(f"Something went wrong with location {apLoc}")
                                    buggedLocations.append(apLoc)
                                if(apLoc == "Victory_Escape_Reapers_Eye" and goal == 0):
                                    victory = True
                                elif(apLoc == "Bad_State"):
                                    logger.error(f"Something occured that made locations unreachable, an earlier save might be needed")
                                    bad_states.append[loc]
                message = [{"cmd": 'LocationChecks', "locations": sending}]
                await ctx.send_msgs(message)
                if(not ctx.finished_game and victory):
                    await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                    ctx.finished_game = True
                path = os.path.join(ctx.comm_file_directory, ctx.deathlink_out)
                if(os.path.isfile(path) and ctx.has_death_link):
                    with open(path, 'r') as file:
                        deaths = json.load(file)
                        if(ctx.slot is not None):
                            for death in deaths:
                                await ctx.send_death(f"{ctx.player_names[ctx.slot]} had {death} become food for the voidwoken")
                    with open(path, 'w') as file:
                        json.dump([], file)
            await asyncio.sleep(3)
        except Exception as err:
            logger.error("Exception in communication thread, a check may have not sent: " + str(err))

def print_error_and_close(msg):
    logger.error("Error: " + msg)
    Utils.messagebox("Error", msg, error = True)
    sys.exit(1)

def launch_dos2_client(*launch_args: str):
    async def main():
        args = parser.parse_args(launch_args)
        ctx = DOS2Context(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name = "server loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        progression_watcher = asyncio.create_task(game_watcher(ctx), name = "DOS2ProgressWatcher")
        await ctx.exit_event.wait()
        ctx.server_address = None
        await progression_watcher
        await ctx.shutdown()
    
    import colorama
    parser = get_base_parser(description = "DOS2 Client, for text interfacing.")
    colorama.just_fix_windows_console()
    asyncio.run(main())
    colorama.deinit()