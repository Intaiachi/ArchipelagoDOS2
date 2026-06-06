from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .World import DOS2World

def create_and_connect_regions(world: DOS2World) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: DOS2World) -> None:
    merryweather = Region("Merryweather", world.player, world.multiworld)
    fortJoy = Region("Fort Joy", world.player, world.multiworld)
    eastReapersEye = Region("East Reaper's Eye", world.player, world.multiworld)
    finalReapersEye = Region("North-east Reaper's Eye", world.player, world.multiworld)

    regions = [merryweather, fortJoy, eastReapersEye, finalReapersEye]

    world.multiworld.regions += regions

def connect_regions(world: DOS2World) -> None:
    merryweather = world.get_region("Merryweather")
    fortJoy = world.get_region("Fort Joy")
    eastReapersEye = world.get_region("East Reaper's Eye")
    finalReapersEye = world.get_region("North-east Reaper's Eye")

    merryweather.connect(fortJoy, "Merryweather to Fort Joy", lambda state: state.has("Level Up", world.player))
    fortJoy.connect(eastReapersEye, "Fort Joy to East Reaper's Eye", lambda state: state.has("Level Up", world.player, 2))
    eastReapersEye.connect(finalReapersEye, "East Reaper's Coast to North-east Reaper's Eye", lambda state: state.has("Level Up", world.player, 3) and state.has("Purging Wand", world.player))
