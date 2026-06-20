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

    ladyVengence = Region("Lady Vengence", world.player, world.multiworld)
    reapersCoast = Region("Reaper's Coast", world.player, world.multiworld)
    stonegarden = Region("Stonegarden", world.player, world.multiworld)
    theBlackpits = Region("The Blackpits", world.player, world.multiworld)
    driftwood = Region("Driftwood", world.player, world.multiworld)
    reapersBluffs = Region("Reaper's Bluffs", world.player, world.multiworld)
    cloisterwood = Region("Cloisterwood", world.player, world.multiworld)
    theMeadows = Region("The Meadows", world.player, world.multiworld)
    theCullwoods = Region("The Cullwoods", world.player, world.multiworld)
    paradiseDowns = Region("Paradise Downs", world.player, world.multiworld)
    bloodmoonIsland = Region("Bloodmoon Island", world.player, world.multiworld)

    namelessIsle = Region("The Nameless Isle", world.player, world.multiworld)

    regions = [merryweather, fortJoy, eastReapersEye, finalReapersEye, ladyVengence, reapersCoast, stonegarden, theBlackpits, driftwood, reapersBluffs, cloisterwood, theMeadows, theCullwoods, paradiseDowns, bloodmoonIsland, namelessIsle]

    world.multiworld.regions += regions

def connect_regions(world: DOS2World) -> None:
    merryweather = world.get_region("Merryweather")
    fortJoy = world.get_region("Fort Joy")
    eastReapersEye = world.get_region("East Reaper's Eye")
    finalReapersEye = world.get_region("North-east Reaper's Eye")

    ladyVengence = world.get_region("Lady Vengence")
    reapersCoast = world.get_region("Reaper's Coast")
    stonegarden = world.get_region("Stonegarden")
    theBlackpits = world.get_region("The Blackpits")
    driftwood = world.get_region("Driftwood")
    reapersBluffs = world.get_region("Reaper's Bluffs")
    cloisterwood = world.get_region("Cloisterwood")
    theMeadows = world.get_region("The Meadows")
    theCullwoods = world.get_region("The Cullwoods")
    paradiseDowns = world.get_region("Paradise Downs")
    bloodmoonIsland = world.get_region("Bloodmoon Island")

    namelessIsle = world.get_region("The Nameless Isle")

    merryweather.connect(fortJoy, "Merryweather to Fort Joy", lambda state: state.has("Level Up", world.player))
    fortJoy.connect(eastReapersEye, "Fort Joy to East Reaper's Eye", lambda state: state.has("Level Up", world.player, 2))
    eastReapersEye.connect(finalReapersEye, "East Reaper's Eye to North-east Reaper's Eye", lambda state: state.has("Level Up", world.player, 3) and state.has("Purging Wand", world.player))
    if(world.options.goal != world.options.goal.option_escape_reapers_eye and world.options.goal != world.options.goal.option_reapers_eye_hit_list):
        finalReapersEye.connect(ladyVengence, "North-east Reaper's Eye to Lady Vengence")
        ladyVengence.connect(reapersCoast, "Lady Vengence to Reaper's Coast")
        reapersCoast.connect(stonegarden, "Reaper's Coast to Stonegarden", lambda state: state.has("Level Up", world.player, 4))
        reapersCoast.connect(driftwood, "Reaper's Coast to Driftwood")
        reapersCoast.connect(theMeadows, "Reaper's Coast to The Meadows", lambda state: state.has("Level Up", world.player, 5))
        stonegarden.connect(theCullwoods, "Stonegarden to The Cullwoods", lambda state: state.has("Level Up", world.player, 5))
        stonegarden.connect(paradiseDowns, "Stonegarden to Paradise Downs", lambda state: state.has("Level Up", world.player, 6))
        paradiseDowns.connect(theBlackpits, "Paradise Downs to The Blackpits", lambda state: state.has("Level Up", world.player, 6))
        driftwood.connect(reapersBluffs, "Driftwood to Reaper's Bluffs", lambda state: state.has("Level Up", world.player, 4))
        reapersBluffs.connect(cloisterwood, "Reaper's Bluffs to Cloisterwood", lambda state: state.has("Level Up", world.player, 5))
        cloisterwood.connect(theMeadows, "Cloisterwood to The Meadows", lambda state: state.has("Level Up", world.player, 5))
        theMeadows.connect(theCullwoods, "The Meadows to The Cullwoods", lambda state: state.has("Level Up", world.player, 5))
        theMeadows.connect(bloodmoonIsland, "The Meadows to Bloodmoon Island", lambda state: state.has("Level Up", world.player, 7))
        theCullwoods.connect(paradiseDowns, "The Cullwoods to Paradise Downs", lambda state: state.has("Level Up", world.player, 6))
        if(world.options.goal != world.options.goal.option_leave_reapers_coast and world.options.goal != world.options.goal.option_reapers_coast_hit_list):
            ladyVengence.connect(namelessIsle, "Lady Vengence to The Nameless Isle", lambda state: state.has("Level Up", world.player, 7))
