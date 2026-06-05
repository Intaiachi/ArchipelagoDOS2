from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if(TYPE_CHECKING):
    from .World import DOS2World

FILLER_ITEMS = [
    ["Gold", "1c3c9c74-34a1-4685-989e-410dc080be6f"]
]

#item name, id in game, id in ap, classification, level
ITEM_TUPLES = [
    [item[0], item[1], index + 1000, ItemClassification.filler, 0] for index, item in enumerate(FILLER_ITEMS)
]

ITEM_NAME_TO_ID = {item[0]: item[2] for item in ITEM_TUPLES}
ID_TO_ITEM_NAME = {item[2]: item[0] for item in ITEM_TUPLES}
AP_ITEM_TO_DOS2_ID = {item[0]: item[1] for item in ITEM_TUPLES}
ID_TO_AP_ITEM = {item[2]: item[1] for item in ITEM_TUPLES}
DEFAULT_ITEM_CLASSIFICATIONS = {item[0]: item[3] for item in ITEM_TUPLES}
IS_DUPEABLE = {item[1]: True for item in FILLER_ITEMS}

class DOS2Item(Item):
    game = "Divinity Original Sin 2"

def get_random_filler_item_name(world: DOS2World) -> str:
    index = world.random.randint(0, len(FILLER_ITEMS) - 1)
    return FILLER_ITEMS[index][0]

def create_item_with_correct_classification(world: DOS2World, name: str) -> DOS2Item:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return DOS2Item(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: DOS2World) -> None:
    itempool: list[Item] = []

    number_of_items = len(itempool)
    number_of_filler = len(world.multiworld.get_unfilled_locations(world.player)) - number_of_items
    itempool += [world.create_filler() for _ in range(number_of_filler)]

    world.multiworld.itempool += itempool