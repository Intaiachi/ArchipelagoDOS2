from collections.abc import Mapping
from typing import Any, ClassVar

from worlds.AutoWorld import World

from . import Items, Locations, Options, Regions, Rules, WebWorld, Settings

class DOS2World(World):
    """
    Divinity Original Sin 2 is a turn based tactical RPG in which you control the Godwoken to fight against the Voidwoken
    """

    game = "Divinity Original Sin 2"
    web = WebWorld.DOS2WebWorld()
    options_dataclass = Options.DOS2Options
    options: Options.DOS2Options
    settings: ClassVar[Settings.DOS2Settings]

    location_name_to_id = Locations.LOCATION_NAME_TO_ID
    item_name_to_id = Items.ITEM_NAME_TO_ID

    origin_region_name = "Merryweather"

    def create_regions(self) -> None:
        Regions.create_and_connect_regions(self)
        Locations.create_all_locations(self)

    def set_rules(self) -> None:
        Rules.set_all_rules(self)

    def create_items(self) -> None:
        Items.create_all_items(self)

    def create_item(self, name: str) -> Items.DOS2Item:
        return Items.create_item_with_correct_classification(self, name)
    
    def get_filler_item_name(self) -> str:
        return Items.get_random_filler_item_name(self)
    
    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = self.options.as_dict(
            "goal", "death_link", "syncOption", "deathlinkStyleIn", "deathlinkStyleOut"
        )
        slot_data["death_link"] = slot_data.pop("death_link")
        slot_data["seed_name"] = str(self.multiworld.seed_name)
        return slot_data