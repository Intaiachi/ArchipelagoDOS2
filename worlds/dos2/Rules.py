from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState

from ..generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .World import DOS2World


def set_all_rules(world: DOS2World) -> None:
    set_all_entrance_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: DOS2World) -> None:
    pass

def set_completion_condition(world: DOS2World) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)