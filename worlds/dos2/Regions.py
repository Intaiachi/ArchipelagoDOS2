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
    endAct1 = Region("End Act 1", world.player, world.multiworld)

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

    namelessIsle = Region("The Nameless Isle", world.player, world.multiworld)
    arenaOfTheOne = Region("Arena Of The One", world.player, world.multiworld)

    arxOutskirts = Region("Arx Outskirts", world.player, world.multiworld)
    arx = Region("Arx", world.player, world.multiworld)
    tombOfLucian = Region("Tomb of Lucian", world.player, world.multiworld)
    arxOutskirtsPlus = Region("Arx Outskirts+", world.player, world.multiworld)
    endAct4 = Region("End Act 4", world.player, world.multiworld)

    regions = [merryweather, fortJoyGhetto, fortJoy, theHollowMarshes, finalReapersEye, endAct1, ladyVengeance, reapersCoast, stonegarden, theBlackpits, driftwood, reapersBluffs, cloisterwood, theMeadows, theCullwoods, paradiseDowns, bloodmoonIsland, endAct2, namelessIsle, arenaOfTheOne, arxOutskirts, arx, arxOutskirtsPlus, tombOfLucian, endAct4]

    world.multiworld.regions += regions

def connect_regions(world: DOS2World) -> None:
    merryweather = world.get_region("Merryweather")
    fortJoyGhetto = world.get_region("Fort Joy Ghetto")
    fortJoy = world.get_region("Fort Joy")
    theHollowMarshes = world.get_region("The Hollow Marshes")
    finalReapersEye = world.get_region("North-east Reaper's Eye")
    endAct1 = world.get_region("End Act 1")

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

    namelessIsle = world.get_region("The Nameless Isle")
    arenaOfTheOne = world.get_region("Arena Of The One")

    arxOutskirts = world.get_region("Arx Outskirts")
    arx = world.get_region("Arx")
    tombOfLucian = world.get_region("Tomb of Lucian")
    arxOutskirtsPlus = world.get_region("Arx Outskirts+")
    endAct4 = world.get_region("End Act 4")

    merryweather.connect(fortJoyGhetto, "Merryweather to Fort Joy Ghetto")
    fortJoyGhetto.connect(fortJoy, "Fort Joy Ghetto to Fort Joy")
    fortJoy.connect(theHollowMarshes, "Fort Joy to The Hollow Marshes")
    theHollowMarshes.connect(finalReapersEye, "The Hollow Marshes to North-east Reaper's Eye")
    finalReapersEye.connect(endAct1, "North-east Reaper's Eye to End Act 1")

    endAct1.connect(ladyVengeance, "North-east Reaper's Eye to Lady Vengeance")
    ladyVengeance.connect(reapersCoast, "Lady Vengeance to Reaper's Coast")
    reapersCoast.connect(driftwood, "Reaper's Coast to Driftwood")
    reapersCoast.connect(theMeadows, "Reaper's Coast to The Meadows")
    reapersCoast.connect(stonegarden, "Reaper's Coast to Stonegarden")
    stonegarden.connect(theCullwoods, "Stonegarden to The Cullwoods")
    stonegarden.connect(paradiseDowns, "Stonegarden to Paradise Downs")
    stonegarden.connect(theMeadows, "Stonegarden to The Meadows")
    paradiseDowns.connect(theBlackpits, "Paradise Downs to The Blackpits")
    paradiseDowns.connect(theCullwoods, "Paradise Downs to The Cullwoods")
    driftwood.connect(reapersBluffs, "Driftwood to Reaper's Bluffs")
    reapersBluffs.connect(cloisterwood, "Reaper's Bluffs to Cloisterwood")
    reapersBluffs.connect(driftwood, "Reaper's Bluffs to Driftwood")
    cloisterwood.connect(reapersBluffs, "Cloisterwood to Reaper's Bluffs")
    cloisterwood.connect(bloodmoonIsland, "Cloisterwood to Bloodmoon Island")
    theMeadows.connect(theCullwoods, "The Meadows to The Cullwoods")
    theMeadows.connect(cloisterwood, "The Meadows to Cloisterwood")
    theMeadows.connect(bloodmoonIsland, "The Meadows to Bloodmoon Island")
    theCullwoods.connect(paradiseDowns, "The Cullwoods to Paradise Downs")
    ladyVengeance.connect(endAct2, "Lady Vengeance to End Act 2")

    endAct2.connect(namelessIsle, "Lady Vengeance to The Nameless Isle")
    namelessIsle.connect(arenaOfTheOne, "The Nameless Isle to Arena Of The One")

    arenaOfTheOne.connect(arxOutskirts, "Lady Vengeance to Arx Outskirts")
    arxOutskirts.connect(arx, "Arx Outskirts to Arx")
    arx.connect(tombOfLucian, "Arx to Tomb of Lucian")
    arxOutskirts.connect(arxOutskirtsPlus, "Arx Outskirts to Arx Outskirts+")
    tombOfLucian.connect(endAct4, "Tomb of Lucian to End Act 4")