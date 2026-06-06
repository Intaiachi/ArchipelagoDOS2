from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import Items

if TYPE_CHECKING:
    from .World import DOS2World

DOS2_KILL_LIST = [
    ["S_TUT_TopDeckVoidling10_bd0123ae-26fd-4dad-8326-b6ae9a3fc1c5", ["Merryweather: Voidling 1"], 0],
    ["S_TUT_TopDeckVoidling11_2fcb5b84-875f-42bd-ac80-6f8495c6a47c", ["Merryweather: Voidling 2"], 0],
]

DOS2_LOCATION_LIST = [
    ["Quest-TUT_ShipInvestigation", ["Merryweather: Death Belowdecks - Complete"], 0],
    ["Quest-TUT_ShipMurder", ["Merryweather: Troubled Waters - Complete"], 0]
] + DOS2_KILL_LIST

LOCATION_NAME_ID_REGION = [
    ["Merryweather: Death Belowdecks - Complete", 1, "Merryweather"],
    ["Merryweather: Troubled Waters - Complete", 2, "Merryweather"],
    ["Merryweather: Voidling 1", 3, "Merryweather"],
    ["Merryweather: Voidling 2", 4, "Merryweather"],
    ]

LOCATION_NAME_TO_ID = {item[0]: item[1] for item in LOCATION_NAME_ID_REGION}

DOS2_LOCATION_TO_AP_LOCATIONS = {item[0]: item[1] for item in DOS2_LOCATION_LIST}

class DOS2Location(Location):
    game = "Divinity Original Sin 2"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: DOS2World) -> None:
    create_regular_locations(world)

def create_regular_locations(world: DOS2World) -> None:
    merryweather = world.get_region("Merryweather")

    merryweather_location_names = []
    for loc in LOCATION_NAME_ID_REGION:
        if(loc[2] == "Merryweather"):
            merryweather_location_names.append(loc[0])
    merryweather_locations = get_location_names_with_ids(merryweather_location_names)
    merryweather.add_locations(merryweather_locations, DOS2Location)

    if(world.options.goal == world.options.goal.option_defeat_alexander):
        merryweather.add_event("Victory_Alexander", "Victory", location_type = DOS2Location, item_type = Items.DOS2Item) #dummy goal