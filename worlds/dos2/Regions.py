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

    regions = [merryweather]

    world.multiworld.regions += regions

def connect_regions(world: DOS2World) -> None:
    pass