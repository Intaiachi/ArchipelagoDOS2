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
    fortJoyGhetto = Region("Fort Joy Ghetto", world.player, world.multiworld)
    fortJoy = Region("Fort Joy", world.player, world.multiworld)
    theHollowMarshes = Region("The Hollow Marshes", world.player, world.multiworld)
    finalReapersEye = Region("North-east Reaper's Eye", world.player, world.multiworld)

    ladyVengeance = Region("Lady Vengeance", world.player, world.multiworld)
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
    endAct2 = Region("End Act 2", world.player, world.multiworld)
    cloisterwoodPlus = Region("Cloisterwood+", world.player, world.multiworld)
    theBlackpitsPlus = Region("The Blackpits+", world.player, world.multiworld)
    stonegardenMinus = Region("Stonegarden-", world.player, world.multiworld)
    reapersBluffsPlus = Region("Reaper's Bluffs+", world.player, world.multiworld)

    namelessIsle = Region("The Nameless Isle", world.player, world.multiworld)

    arxOutskirts = Region("Arx Outskirts", world.player, world.multiworld)
    arx = Region("Arx", world.player, world.multiworld)
    tombOfLucian = Region("Tomb of Lucian", world.player, world.multiworld)
    arxOutskirtsPlus = Region("Arx Outskirts+", world.player, world.multiworld)

    regions = [merryweather, fortJoyGhetto, fortJoy, theHollowMarshes, finalReapersEye, ladyVengeance, reapersCoast, stonegarden, stonegardenMinus, theBlackpits, theBlackpitsPlus, driftwood, reapersBluffs, reapersBluffsPlus, cloisterwood, cloisterwoodPlus, theMeadows, theCullwoods, paradiseDowns, bloodmoonIsland, endAct2, namelessIsle, arxOutskirts, arx, arxOutskirtsPlus, tombOfLucian]

    world.multiworld.regions += regions

def connect_regions(world: DOS2World) -> None:
    merryweather = world.get_region("Merryweather")
    fortJoyGhetto = world.get_region("Fort Joy Ghetto")
    fortJoy = world.get_region("Fort Joy")
    theHollowMarshes = world.get_region("The Hollow Marshes")
    finalReapersEye = world.get_region("North-east Reaper's Eye")

    ladyVengeance = world.get_region("Lady Vengeance")
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
    endAct2 = world.get_region("End Act 2")
    cloisterwoodPlus = world.get_region("Cloisterwood+")
    theBlackpitsPlus = world.get_region("The Blackpits+")
    stonegardenMinus = world.get_region("Stonegarden-")
    reapersBluffsPlus = world.get_region("Reaper's Bluffs+")

    namelessIsle = world.get_region("The Nameless Isle")

    arxOutskirts = world.get_region("Arx Outskirts")
    arx = world.get_region("Arx")
    tombOfLucian = world.get_region("Tomb of Lucian")
    arxOutskirtsPlus = world.get_region("Arx Outskirts+")

    merryweather.connect(fortJoyGhetto, "Merryweather to Fort Joy Ghetto", lambda state: state.has("Level Up", world.player))
    fortJoyGhetto.connect(fortJoy, "Fort Joy Ghetto to Fort Joy", lambda state: state.has("Level Up", world.player, 3))
    fortJoy.connect(theHollowMarshes, "Fort Joy to The Hollow Marshes", lambda state: state.has("Level Up", world.player, 6))
    theHollowMarshes.connect(finalReapersEye, "The Hollow Marshes to North-east Reaper's Eye", lambda state: state.has("Level Up", world.player, 8) and state.has("Purging Wand", world.player))
    if(world.options.goal != world.options.goal.option_escape_reapers_eye and world.options.goal != world.options.goal.option_reapers_eye_hit_list):
        finalReapersEye.connect(ladyVengeance, "North-east Reaper's Eye to Lady Vengeance", lambda state: state.has("Level Up", world.player, 8))
        ladyVengeance.connect(reapersCoast, "Lady Vengeance to Reaper's Coast", lambda state: state.has("Level Up", world.player, 9))
        reapersCoast.connect(stonegarden, "Reaper's Coast to Stonegarden", lambda state: state.has("Level Up", world.player, 11))
        reapersCoast.connect(driftwood, "Reaper's Coast to Driftwood", lambda state: state.has("Level Up", world.player, 9))
        reapersCoast.connect(theMeadows, "Reaper's Coast to The Meadows", lambda state: state.has("Level Up", world.player, 12))
        stonegarden.connect(theCullwoods, "Stonegarden to The Cullwoods", lambda state: state.has("Level Up", world.player, 13))
        stonegarden.connect(paradiseDowns, "Stonegarden to Paradise Downs", lambda state: state.has("Level Up", world.player, 13))
        paradiseDowns.connect(theBlackpits, "Paradise Downs to The Blackpits", lambda state: state.has("Level Up", world.player, 14))
        driftwood.connect(reapersBluffs, "Driftwood to Reaper's Bluffs", lambda state: state.has("Level Up", world.player, 10))
        reapersBluffs.connect(cloisterwood, "Reaper's Bluffs to Cloisterwood", lambda state: state.has("Level Up", world.player, 11))
        cloisterwood.connect(theMeadows, "Cloisterwood to The Meadows", lambda state: state.has("Level Up", world.player, 12))
        theMeadows.connect(theCullwoods, "The Meadows to The Cullwoods", lambda state: state.has("Level Up", world.player, 13))
        theMeadows.connect(bloodmoonIsland, "The Meadows to Bloodmoon Island", lambda state: state.has("Level Up", world.player, 15))
        theCullwoods.connect(paradiseDowns, "The Cullwoods to Paradise Downs", lambda state: state.has("Level Up", world.player, 13))
        ladyVengeance.connect(endAct2, "Lady Vengeance to End Act 2", lambda state: state.has("Level Up", world.player, 15) and state.has("Max Source Point", world.player, 2))
        cloisterwood.connect(cloisterwoodPlus, "Cloisterwood to Cloisterwood+", lambda state: state.has("Level Up", world.player, 13))
        theBlackpits.connect(theBlackpitsPlus, "The Blackpits to The Blackpits+", lambda state: state.has("Level Up", world.player, 15) and state.has("Max Source Point", world.player, 1))
        reapersCoast.connect(stonegardenMinus, "Reaper's Coast to Stonegarden-", lambda state: state.has("Level Up", world.player, 9))
        reapersBluffs.connect(reapersBluffsPlus, "Reaper's Bluffs to Reaper's Bluffs+", lambda state: state.has("Level Up", world.player, 14))
        if(world.options.goal != world.options.goal.option_leave_reapers_coast and world.options.goal != world.options.goal.option_reapers_coast_hit_list):
            endAct2.connect(namelessIsle, "Lady Vengeance to The Nameless Isle", lambda state: state.has("Level Up", world.player, 16))
            if(world.options.goal != world.options.goal.option_escape_the_nameless_isle and world.options.goal != world.options.goal.option_the_nameless_isle_hit_list):
                endAct2.connect(arxOutskirts, "Lady Vengeance to Arx Outskirts", lambda state: state.has("Level Up", world.player, 17))
                arxOutskirts.connect(arx, "Arx Outskirts to Arx", lambda state: state.has("Level Up", world.player, 18))
                arx.connect(tombOfLucian, "Arx to Tomb of Lucian", lambda state: state.has("Level Up", world.player, 20) and state.has("Source Amulet", world.player) and state.has("Scroll Of Atonement", world.player))
                arxOutskirts.connect(arxOutskirtsPlus, "Arx Outskirts to Arx Outskirts+", lambda state: state.has("Level Up", world.player, 19))
