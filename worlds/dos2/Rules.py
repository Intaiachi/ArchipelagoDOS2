from __future__ import annotations

from typing import TYPE_CHECKING
from functools import reduce

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, CanReachLocation, CanReachRegion
from rule_builder.field_resolvers import FromOption

from .Options import RegionBarriers, Act1Keys, Act2Keys, Act3Keys, Act4Keys

if TYPE_CHECKING:
    from .World import DOS2World

def hasRegion(region):
    return (OptionFilter(RegionBarriers, False) | Has(region + " Unlock"))

def isLevel(level):
    return Has("Level Up", count = level)


def set_all_rules(world: DOS2World) -> None:
    set_all_entrance_rules(world)
    set_completion_condition(world)
    set_all_location_rules(world)

def set_all_entrance_rules(world: DOS2World) -> None:

    def ent(name):
        return world.get_entrance(name)

    world.set_rule(ent("Merryweather to Fort Joy Ghetto"), isLevel(1))
    world.set_rule(ent("Fort Joy Ghetto to Fort Joy"), isLevel(3) & hasRegion("Fort Joy"))
    world.set_rule(ent("Fort Joy to The Hollow Marshes"), isLevel(6) & hasRegion("The Hollow Marshes"))
    world.set_rule(ent("The Hollow Marshes to North-east Reaper's Eye"), isLevel(8) & hasRegion("North-east Reaper's Eye") & Has("Purging Wand"))
    world.set_rule(ent("North-east Reaper's Eye to End Act 1"), CanReachLocation("North-east Reaper's Eye: Escape From Reaper's Eye - Complete", "North-east Reaper's Eye"))
    if(world.options.goal != world.options.goal.option_escape_reapers_eye and world.options.goal != world.options.goal.option_reapers_eye_hit_list):
        world.set_rule(ent("North-east Reaper's Eye to Lady Vengeance"), isLevel(8))
        world.set_rule(ent("Lady Vengeance to Reaper's Coast"), isLevel(9))
        world.set_rule(ent("Reaper's Coast to Stonegarden"), isLevel(11) & hasRegion("Stonegarden"))
        world.set_rule(ent("Reaper's Coast to Driftwood"), isLevel(9) & hasRegion("Driftwood"))
        world.set_rule(ent("Reaper's Coast to The Meadows"), isLevel(12) & hasRegion("The Meadows"))
        world.set_rule(ent("Stonegarden to The Cullwoods"), isLevel(13) & hasRegion("The Cullwoods"))
        world.set_rule(ent("Stonegarden to Paradise Downs"), isLevel(13) & hasRegion("Paradise Downs"))
        world.set_rule(ent("Stonegarden to The Meadows"), isLevel(12) & hasRegion("The Meadows"))
        world.set_rule(ent("Paradise Downs to The Blackpits"), isLevel(14) & hasRegion("The Blackpits"))
        world.set_rule(ent("Paradise Downs to The Cullwoods"), isLevel(13) & hasRegion("The Cullwoods"))
        world.set_rule(ent("Driftwood to Reaper's Bluffs"), isLevel(10) & hasRegion("Reaper's Bluffs"))
        world.set_rule(ent("Reaper's Bluffs to Cloisterwood"), isLevel(11) & hasRegion("Cloisterwood"))
        world.set_rule(ent("Reaper's Bluffs to Driftwood"), isLevel(9) & hasRegion("Driftwood"))
        world.set_rule(ent("Cloisterwood to Reaper's Bluffs"), isLevel(10) & hasRegion("Reaper's Bluffs"))
        world.set_rule(ent("Cloisterwood to Bloodmoon Island"), isLevel(15) & hasRegion("Bloodmoon Island"))
        world.set_rule(ent("The Meadows to The Cullwoods"), isLevel(13) & hasRegion("The Cullwoods"))
        world.set_rule(ent("The Meadows to Cloisterwood"), isLevel(11) & hasRegion("Cloisterwood"))
        world.set_rule(ent("The Meadows to Bloodmoon Island"), isLevel(15) & hasRegion("Bloodmoon Island"))
        world.set_rule(ent("The Cullwoods to Paradise Downs"), isLevel(13) & hasRegion("Paradise Downs"))
        world.set_rule(ent("Lady Vengeance to End Act 2"), CanReachLocation("Lady Vengeance: Powerful Awakening - Complete", "Lady Vengeance"))
        world.multiworld.register_indirect_condition(world.get_region("Reaper's Bluffs"), ent("Lady Vengeance to End Act 2"))
        world.multiworld.register_indirect_condition(world.get_region("Cloisterwood"), ent("Lady Vengeance to End Act 2"))
        world.multiworld.register_indirect_condition(world.get_region("Driftwood"), ent("Lady Vengeance to End Act 2"))
        world.multiworld.register_indirect_condition(world.get_region("Stonegarden"), ent("Lady Vengeance to End Act 2"))
        world.multiworld.register_indirect_condition(world.get_region("The Cullwoods"), ent("Lady Vengeance to End Act 2"))
        world.multiworld.register_indirect_condition(world.get_region("Paradise Downs"), ent("Lady Vengeance to End Act 2"))
        world.multiworld.register_indirect_condition(world.get_region("The Blackpits"), ent("Lady Vengeance to End Act 2"))
        world.multiworld.register_indirect_condition(world.get_region("Bloodmoon Island"), ent("Lady Vengeance to End Act 2"))
        if(world.options.goal != world.options.goal.option_leave_reapers_coast and world.options.goal != world.options.goal.option_reapers_coast_hit_list):
            world.set_rule(ent("Lady Vengeance to The Nameless Isle"), isLevel(16))
            world.set_rule(ent("The Nameless Isle to Arena Of The One"), CanReachLocation("The Nameless Isle: The Academy - Complete", "The Nameless Isle"))
            if(world.options.goal != world.options.goal.option_escape_the_nameless_isle and world.options.goal != world.options.goal.option_the_nameless_isle_hit_list):
                world.set_rule(ent("Lady Vengeance to Arx Outskirts"), isLevel(17))
                world.set_rule(ent("Arx Outskirts to Arx"), isLevel(18) & hasRegion("Arx"))
                world.set_rule(ent("Arx to Tomb of Lucian"), isLevel(20) & CanReachLocation("Arx: Wisdom of the Keeper/The Righteous - Complete", "Arx"))
                world.set_rule(ent("Arx Outskirts to Arx Outskirts+"), isLevel(19))
                world.set_rule(ent("Tomb of Lucian to End Act 4"), Has("Arx Key", count = FromOption(Act4Keys)))

def set_all_location_rules(world: DOS2World) -> None:

    def loc(name):
        return world.get_location(name)

    toReapersBluffs = [
        "Driftwood: Skeletal Hailcaster (496, 812)",
        "Driftwood: Skeletal Graverobber (483, 826)",
        "Driftwood: Skeletal Flameweaver (499, 842)",
        "Driftwood: Skeletal Stormbinder (513, 831)",
        "Driftwood: Skeletal Skullcrusher (496, 835)"
    ]
    toReapersBluffsChests = [
        "Driftwood: Acid-Stained Chest (497, 824)"
    ]
    toReapersBluffsContainer = [
        "Driftwood: Vase (516, 783)",
        "Driftwood: Vase (514, 783)",
        "Driftwood: Vase (498, 786)",
        "Driftwood: Vial Rack (492, 804)",
        "Driftwood: Vase (509, 818)",
        "Driftwood: Vase (514, 831)",
        "Driftwood: Assortment of Books (515, 835)",
        "Driftwood: Assortment of Books (515, 839)",
        "Driftwood: Vase (499, 841)",
        "Driftwood: Vase (497, 835)",
        "Driftwood: Chest (498, 829)",
        "Driftwood: Vase (496, 812)",
        "Driftwood: Vase (484, 835)",
        "Driftwood: Vase (484, 824)",
        "Driftwood: Tomb (482, 817)",
        "Driftwood: Tomb (482, 824)",
        "Driftwood: Tomb (482, 829)",
        "Driftwood: Tomb (482, 835)"
    ]
    cloisterwoodPlus = [
        "Cloisterwood: Old Gray Wolf (127, 273)",
        "Cloisterwood: Black Wolf (110, 273)",
        "Cloisterwood: Black Wolf (129, 267)",
        "Cloisterwood: Black Wolf (116, 276)",
        "Cloisterwood: Black Wolf (122, 262)",
        "Cloisterwood: Lamenting Abomination (112, 267)",
        "Cloisterwood: Alice Alisceon (221, 316)",
    ]
    toTheBlackpits = [
        "The Meadows: Shadowcloak Skullcrusher (468, 233)",
        "The Meadows: Shadowcloak Heartpiercer (484, 227)",
        "The Meadows: Shadowcloak Deadeye (490, 230)",
        "The Meadows: Shadowcloak Deadeye (464, 216)",
        "The Meadows: Shadowcloak Spellweaver (475, 238)",
        "The Meadows: Shadowcloak Spellweaver (492, 216)",
        "Stonegarden: Masked Servant (517, 182)/Masked Servant (573, 767)",
        "Stonegarden: Masked Servant (498, 178)/Masked Servant (566, 771)",
        "Stonegarden: Masked Servant (505, 184)/Masked Servant (567, 783)",
        "Stonegarden: Ryker (516, 181)",
        "Stonegarden: Waking Ryker - Complete",
        "Cloisterwood: Hannag's Bargin - Complete",
        "Stonegarden: A Generous Offer - Complete",
        "Stonegarden: The Reluctant Servants - Complete",
        "The Meadows: Dark Dealings in the Blackpits - Complete",
        "Paradise Downs: Almira's Request - Complete"
    ]
    theBlackpitsPlus = [
        "The Blackpits: Silent Watcher (351, 76)",
        "The Blackpits: Silent Watcher (351, 82)",
        "The Blackpits: Source Hound (623, 62)",
        "The Blackpits: Source Hound (638, 58)",
        "The Blackpits: Magister Vorrh (629, 60)"
    ]
    theBlackpitsPlusChests = [
        "The Blackpits: Well-worn Chest (621, 62)"
    ]
    theBlackpitsPlusContainer = [
        "The Blackpits: Crate (637, 69)",
        "The Blackpits: Sacks (635, 69)",
        "The Blackpits: Crate (630, 66)",
        "The Blackpits: Crate (625, 69)",
        "The Blackpits: Crate (620, 68)",
        "The Blackpits: Sacks (621, 69)",
        "The Blackpits: Sacks 2 (621, 69)",
        "The Blackpits: Sacks (620, 67)",
        "The Blackpits: Sacks 2 (620, 67)",
        "The Blackpits: Sacks (621, 60)",
        "The Blackpits: Crate (621, 56)",
        "The Blackpits: Coin Purse (628, 55)",
        "The Blackpits: Crate (638, 57)",
        "The Blackpits: Crate (638, 55)",
        "The Blackpits: Pile Of Body Parts (632, 52)",
        "The Blackpits: Pile Of Limbs (636, 48)",
        "The Blackpits: Dismembered Corpse (633, 50)",
        "The Blackpits: Dismembered Corpse (632, 48)"
    ]
    stonegardenMinus = [
        "Stonegarden: Venom-Wing Voidwoken (503, 52)",
        "Stonegarden: Noxious Voidwoken (497, 52)",
        "Stonegarden: Noxious Voidwoken (499, 58)",
        "Stonegarden: Venom-Wing Voidwoken (511, 48)",
    ]
    stonegardenMinusChest = [
        "Stonegarden: Mari Pruitt's Chest (481, 69)",
        "Stonegarden: Chest (87, 604)"
    ]
    stonegardenMinusContainer = [
        "Stonegarden: Sack (501, 65)",
        "Stonegarden: Closet (501, 64)",
        "Stonegarden: Cupboard (493, 64)",
        "Stonegarden: Basket (490, 67)",
        "Stonegarden: Basket (490, 71)",
        "Stonegarden: Sacks (490, 72)",
        "Stonegarden: Shelf (490, 73)",
        "Stonegarden: Closet (504, 74)",
        "Stonegarden: Closet (488, 65)",
        "Stonegarden: Desk (483, 64)",
        "Stonegarden: Closet (478, 65)",
        "Stonegarden: Closet (480, 75)",
        "Stonegarden: Cupboard (488, 77)",
        "Stonegarden: Cupboard (489, 80)",
        "Stonegarden: Desk (485, 82)",
        "Stonegarden: Sacks (479, 76)",
        "Stonegarden: Assortment of Books (478, 83)",
        "Stonegarden: Barrel (477, 83)",
        "Stonegarden: Barrel (106, 596)",
        "Stonegarden: Crate (107, 596)",
        "Stonegarden: Barrel (109, 595)",
        "Stonegarden: Basket (108, 588)",
        "Stonegarden: Basket (108, 587)",
        "Stonegarden: Sacks (102, 592)",
        "Stonegarden: Basket (102, 588)",
        "Stonegarden: Basket (100, 587)",
        "Stonegarden: Cupboard (97, 588)",
        "Stonegarden: Basket (97, 588)",
        "Stonegarden: Basket (96, 586)",
        "Stonegarden: Crate (84, 594)",
        "Stonegarden: Crate (94, 592)",
        "Stonegarden: Crate 2 (94, 592)",
        "Stonegarden: Sack (92, 604)",
        "Stonegarden: Sack (93, 604)",
        "Stonegarden: Barrel (108, 599)",
        "Stonegarden: Barrel (98, 632)"
    ]
    arxOutskirtsPlus = [
        "Arx Outskirts: Volatile Voidling (377, 1)",
        "Arx Outskirts: Volatile Voidling (371, 3)",
        "Arx Outskirts: Volatile Voidling (367, 1)",
        "Arx Outskirts: Volatile Voidling (373, -1)",
        "Arx Outskirts: Necro-Wing Voidwoken (377, -6)",
        "Arx Outskirts: Necro-Wing Voidwoken (374, -15)",
        "Arx Outskirts: Necro-Wing Voidwoken (360, -5)",
        "Arx Outskirts: Awakened Construct (381, -18)",
        "Arx Outskirts: Loic the Immaculate (356, -7)",
        "Arx Outskirts: Abyssal Void Flayer (450, 136)",
        "Arx Outskirts: Abyssal Void Flayer (463, 99)",
        "Arx Outskirts: Abyssal Void Devourer (450, 100)",
        "Arx Outskirts: Kraken (475, 125)"
    ]
    arxOutskirtsPlusChests = [
        "Arx Outskirts: Well-worn Chest (363, 5)",
        "Arx Outskirts: Elaborate Chest (473, 733)",
        "Arx Outskirts: Ornate Chest (517, 118)",
        "Arx Outskirts: Chest (445, 92)",
        "Arx Outskirts: Chest (381, 22)",
        "Arx Outskirts: Ornate Chest (386, -13)"
    ]
    arxOutskirtsPlusContainer = [
        "Arx Outskirts: Sack (386, 23)",
        "Arx Outskirts: Barrel (385, 10)",
        "Arx Outskirts: Barrel (368, -4)",
        "Arx Outskirts: Barrel (363, -9)",
        "Arx Outskirts: Barrel (451, 151)",
        "Arx Outskirts: Crate (451, 152)",
        "Arx Outskirts: Barrel (463, 83)",
        "Arx Outskirts: Barrel (465, 83)",
        "Arx Outskirts: Barrel (467, 83)",
        "Arx Outskirts: Barrel (470, 84)",
        "Arx Outskirts: Barrel (471, 84)",
        "Arx Outskirts: Barrel (471, 83)",
        "Arx Outskirts: Barrel (476, 87)",
        "Arx Outskirts: Barrel (480, 94)",
        "Arx Outskirts: Barrel (481, 94)",
        "Arx Outskirts: Sack (489, 91)",
        "Arx Outskirts: Barrel (493, 93)",
        "Arx Outskirts: Sacks (494, 91)",
        "Arx Outskirts: Barrel (503, 101)",
        "Arx Outskirts: Box (478, 758)",
        "Arx Outskirts: Box (479, 759)",
        "Arx Outskirts: Basket (486, 763)",
        "Arx Outskirts: Box (486, 764)",
        "Arx Outskirts: Box (486, 765)",
        "Arx Outskirts: Box (469, 771)",
        "Arx Outskirts: Box (469, 766)",
        "Arx Outskirts: Box (469, 764)",
        "Arx Outskirts: Box (470, 764)",
        "Arx Outskirts: Box (473, 764)",
        "Arx Outskirts: Barrel (456, 109)",
        "Arx Outskirts: Sacks (461, 107)",
        "Arx Outskirts: Sacks (459, 142)",
        "Arx Outskirts: Barrel (469, 143)",
        "Arx Outskirts: Barrel (469, 142)",
        "Arx Outskirts: Barrel (471, 142)",
        "Arx Outskirts: Pouch (468, 150)",
        "Arx Outskirts: Barrel (475, 154)",
        "Arx Outskirts: Barrel (476, 154)",
        "Arx Outskirts: Barrel (503, 155)",
        "Arx Outskirts: Barrel (504, 157)",
        "Arx Outskirts: Sacks (508, 158)",
        "Arx Outskirts: Barrel (511, 158)",
        "Arx Outskirts: Sacks (514, 154)",
        "Arx Outskirts: Barrel (503, 131)",
        "Arx Outskirts: Barrel (497, 119)",
        "Arx Outskirts: Barrel (503, 117)",
        "Arx Outskirts: Barrel (504, 117)",
        "Arx Outskirts: Barrel (503, 115)",
        "Arx Outskirts: Barrel (507, 116)",
        "Arx Outskirts: Barrel (507, 115)",
        "Arx Outskirts: Barrel (513, 120)",
        "Arx Outskirts: Barrel (513, 125)",
        "Arx Outskirts: Sacks (511, 125)",
        "Arx Outskirts: Box (477, 744)",
        "Arx Outskirts: Barrel (473, 742)",
        "Arx Outskirts: Box (484, 742)",
        "Arx Outskirts: Box (485, 741)",
        "Arx Outskirts: Barrel (485, 739)",
        "Arx Outskirts: Barrel (485, 734)",
        "Arx Outskirts: Barrel (480, 734)",
        "Arx Outskirts: Fish Bucket (478, 733)",
        "Arx Outskirts: Backpack (469, 735)",
        "Arx Outskirts: Fish Bucket (480, 728)",
        "Arx Outskirts: Fish Bucket (479, 728)",
        "Arx Outskirts: Crate (468, 727)",
        "Arx Outskirts: Reinforced Crate (468, 727)",
        "Arx Outskirts: Reinforced Crate (468, 729)",
        "Arx Outskirts: Box (476, 725)",
        "Arx Outskirts: Box (472, 724)",
        "Arx Outskirts: Box (472, 722)",
        "Arx Outskirts: Shelf (471, 723)",
        "Arx Outskirts: Reinforced Crate (480, 723)",
        "Arx Outskirts: Reinforced Crate 2 (480, 723)",
        "Arx Outskirts: Desk (472, 718)",
        "Arx Outskirts: Shelf (476, 717)",
        "Arx Outskirts: Barrel (485, 720)",
        "Arx Outskirts: Crate (485, 719)"
    ]
    toBloodmoonIsland = [
        "Cloisterwood: Jahan's Lesson - Complete",
        "Stonegarden: All In The Family - Complete",
        "Cloisterwood: A Hunter of Wicked Things - Complete"
    ]

    world.set_rule(loc("North-east Reaper's Eye: Escape From Reaper's Eye - Complete"), Has("Reaper's Eye Key", count = FromOption(Act1Keys)))
    world.set_rule(loc("Fort Joy Ghetto: Finding Emmie - Complete"), CanReachRegion("Fort Joy"))
    world.set_rule(loc("Fort Joy Ghetto: Withermoore's Soul Jar - Complete"), CanReachRegion("Fort Joy"))
    world.set_rule(loc("The Hollow Marshes: The Shreikers - Complete"), CanReachRegion("North-east Reaper's Eye"))

    if(world.options.goal != world.options.goal.option_escape_reapers_eye and world.options.goal != world.options.goal.option_reapers_eye_hit_list):
        world.set_rule(loc("Lady Vengeance: Powerful Awakening - Complete"), 
                    isLevel(15) &
                    Has("Reaper's Coast Key", count = FromOption(Act2Keys)) & 
                    Has("Max Source Point", count = 2) & 
                    hasRegion("Driftwood") & 
                    hasRegion("The Meadows") & 
                    CanReachLocation("Reaper's Bluffs: Mordus Awakens - Complete") &
                    CanReachLocation("Stonegarden: Waking Ryker - Complete") &
                    CanReachLocation("Cloisterwood: Jahan's Lesson - Complete") &
                    CanReachLocation("Cloisterwood: Hannag's Bargin - Complete") &
                    CanReachLocation("Bloodmoon Island: The Demon's Advocate - Complete") &
                    CanReachLocation("The Cullwoods: Saheila's Reward - Complete") &
                    CanReachLocation("Paradise Downs: Almira's Dowry - Complete") &
                    CanReachLocation("Cloisterwood: The Gift of the Blackroot - Complete"))
        
        world.set_rule(loc("Reaper's Coast: The Wrecked Caravan - Complete"), CanReachRegion("Driftwood"))
        world.set_rule(loc("Reaper's Coast: They Shall Not Pass - Complete"), hasRegion("Stonegarden"))
        world.set_rule(loc("Driftwood: Shadow Over Driftwood - Complete"), CanReachRegion("Reaper's Bluffs"))
        world.set_rule(loc("Driftwood: Drowning Her Sorrows - Complete"), CanReachRegion("Reaper's Bluffs"))
        world.set_rule(loc("Driftwood: The Law of the Order - Complete"), CanReachRegion("Reaper's Bluffs"))
        world.set_rule(loc("Stonegarden: Heroes' Rest - Complete"), CanReachRegion("The Cullwoods") & CanReachRegion("Paradise Downs") & CanReachRegion("The Blackpits"))
        world.set_rule(loc("Driftwood: A Taste of Freedom - Complete"), CanReachRegion("Reaper's Bluffs") & CanReachRegion("Cloisterwood"))
        world.set_rule(loc("Reaper's Bluffs: Keep Calm and Carrion - Complete"), isLevel(14))
        world.set_rule(loc("Reaper's Coast: Counting your Chickens - Complete"), CanReachRegion("The Cullwoods"))
        world.set_rule(loc("Reaper's Bluffs: Aggressive Takeover - Complete"), CanReachRegion("Driftwood"))
        world.set_rule(loc("Reaper's Bluffs: Red Ink in the Ledger - Complete"), CanReachRegion("Driftwood"))
        world.set_rule(loc("The Blackpits: The Midnight Oil - Complete"), CanReachRegion("Stonegarden"))
        world.set_rule(loc("Reaper's Bluffs: Mordus Awakens - Complete"), CanReachRegion("Driftwood"))
        world.set_rule(loc("Cloisterwood: Hannag's Bargin - Complete"), CanReachRegion("The Blackpits"))
        
        for location in toReapersBluffs:
            world.set_rule(loc(location), CanReachRegion("Reaper's Bluffs"))

        for location in cloisterwoodPlus:
            world.set_rule(loc(location), isLevel(13))

        for location in toTheBlackpits:
            world.set_rule(loc(location), CanReachRegion("The Blackpits"))
        
        for location in theBlackpitsPlus:
            world.set_rule(loc(location), isLevel(15) & Has("Max Source Point", count = 1))
        
        for location in stonegardenMinus:
            world.set_rule(loc(location), hasRegion("Stonegarden"))

        for location in toBloodmoonIsland:
            world.set_rule(loc(location), CanReachRegion("Bloodmoon Island"))

        if(world.options.containerSanity == world.options.containerSanity.option_chests or world.options.containerSanity == world.options.containerSanity.option_everything):
            for location in toReapersBluffsChests:
                world.set_rule(loc(location), CanReachRegion("Reaper's Bluffs"))

            for location in theBlackpitsPlusChests:
                world.set_rule(loc(location), isLevel(15) & Has("Max Source Point", count = 1))

            for location in stonegardenMinusChest:
                world.set_rule(loc(location), hasRegion("Stonegarden"))

        if(world.options.containerSanity == world.options.containerSanity.option_everything):
            for location in toReapersBluffsContainer:
                world.set_rule(loc(location), CanReachRegion("Reaper's Bluffs"))

            for location in theBlackpitsPlusContainer:
                world.set_rule(loc(location), isLevel(15) & Has("Max Source Point", count = 1))
            
            for location in stonegardenMinusContainer:
                world.set_rule(loc(location), hasRegion("Stonegarden"))

        if(world.options.goal != world.options.goal.option_leave_reapers_coast and world.options.goal != world.options.goal.option_reapers_coast_hit_list):

            world.set_rule(loc("The Nameless Isle: The Academy - Complete"), Has("The Nameless Isle Key", count = FromOption(Act3Keys)))
            world.set_rule(loc("The Nameless Isle: The Arena of the One - Complete"), CanReachRegion("Arena Of The One"))
            world.set_rule(loc("The Nameless Isle: Source Titan (-211, 1027)"), CanReachRegion("Arena Of The One"))

            if(world.options.goal != world.options.goal.option_escape_the_nameless_isle and world.options.goal != world.options.goal.option_the_nameless_isle_hit_list):

                world.set_rule(loc("Arx: Wisdom of the Keeper/The Righteous - Complete"), Has("Source Amulet") & Has("Scroll Of Atonement") & hasRegion("Tomb of Lucian"))
                world.set_rule(loc("Arx: Past Mistakes - Complete"), CanReachRegion("Tomb of Lucian"))
                world.set_rule(loc("Arx: Saeva the Many-faced (148, 763)"), CanReachRegion("Tomb of Lucian"))
                world.set_rule(loc("Arx: Sahun Woundbinder (148, 735)"), CanReachRegion("Tomb of Lucian"))
                world.set_rule(loc("Arx: Urrha the Snake Charmer (177, 753)"), CanReachRegion("Tomb of Lucian"))
                world.set_rule(loc("Arx: Kajun Frozenheart (177, 736)"), CanReachRegion("Tomb of Lucian"))
                world.set_rule(loc("Arx: Karon (163, 750)"), CanReachRegion("Tomb of Lucian"))
                world.set_rule(loc("Tomb of Lucian: Hammerfall - Complete"), CanReachRegion("End Act 4"))
                world.set_rule(loc("Tomb of Lucian: Braccus Rex (581, 284)"), CanReachRegion("End Act 4"))
                world.set_rule(loc("Tomb of Lucian: End Times - Complete"), CanReachRegion("End Act 4"))


                for location in arxOutskirtsPlus:
                    world.set_rule(loc(location), isLevel(19))

                if(world.options.containerSanity == world.options.containerSanity.option_chests or world.options.containerSanity == world.options.containerSanity.option_everything):
                    for location in arxOutskirtsPlusChests:
                        world.set_rule(loc(location), isLevel(19))

                if(world.options.containerSanity == world.options.containerSanity.option_everything):
                    for location in arxOutskirtsPlusContainer:
                        world.set_rule(loc(location), isLevel(19))

    if(world.options.goal == world.options.goal.option_reapers_eye_hit_list or world.options.goal == world.options.goal.option_reapers_coast_hit_list or world.options.goal == world.options.goal.option_the_nameless_isle_hit_list or world.options.goal == world.options.goal.option_arx_hit_list):
        selectedHits = world.options.hitList
        hitReference = [
            ["Kniles the Flenser", "Fort Joy: Kniles the Flenser (384, 630)", 1, "Fort Joy"],
            ["Windego", "The Hollow Marshes: Windego (357, 192)", 1, "The Hollow Marshes"],
            ["Voidwoken Deep-dweller", "The Hollow Marshes: Voidwoken Deep-dweller (499, 157)", 1, "The Hollow Marshes"],
            ["Radeka the Witch", "The Hollow Marshes: Radeka the Witch (691, 602)", 1, "The Hollow Marshes"],
            ["Bishop Alexandar", "North-east Reaper's Eye: Bishop Alexandar (564, 306)", 1, "North-east Reaper's Eye"],

            ["Lamenting Abomination", "Cloisterwood: Lamenting Abomination (112, 267)", 2, "Cloisterwood"],
            ["Alice Alisceon", "Cloisterwood: Alice Alisceon (221, 316)", 2, "Cloisterwood"],
            ["Harbinger of Doom", "Paradise Downs: Harbinger of Doom (679, 437)", 2, "Paradise Downs"],
            ["The Eternal Aetera", "The Blackpits: The Eternal Aetera (411, 671)", 2, "The Blackpits"],
            ["Ghalann, Scion of the Elves", "Stonegarden: Ghalann, Scion of the Elves (106, 540)", 2, "Stonegarden"],
            ["Ryker", "Stonegarden: Ryker (516, 181)", 2, "The Blackpits"],
            ["Mordus", "Reaper's Bluffs: Mordus Awakens - Complete", 2, "Reaper's Bluffs"],

            ["The Great Guardian", "The Nameless Isle: The Great Guardian (549, 923)", 3, "The Nameless Isle"],
            ["Source Titan", "The Nameless Isle: Source Titan (-211, 1027)", 3, "The Nameless Isle"],

            ["Loic the Immaculate", "Arx Outskirts: Loic the Immaculate (356, -7)", 4, "Arx Outskirts"],
            ["Voidwoken Bloodfury", "Arx Outskirts: Voidwoken Bloodfury (302, 172)", 4, "Arx Outskirts"],
            ["Kraken", "Arx Outskirts: Kraken (475, 125)", 4, "Arx Outskirts"],
            ["Sanguinia Tell", "Arx: Sanguinia Tell (419, 298)", 4, "Arx"],
            ["Karon", "Arx: Karon (163, 750)", 4, "Tomb of Lucian"],
            ["Isbeil", "Arx: Isbeil (280, 672)", 4, "Arx"],
            ["Thorny Suncaller", "Arx: Thorny Suncaller (101, 286)", 4, "Arx"],
            ["Lord Linder Kemm", "Arx: Lord Linder Kemm (325, 263)", 4, "Arx"],
            ["Adramahlihk", "Arx: Adramahlihk (387, 418)", 4, "Arx"],
            ["Contaminated Horror", "Arx: Contaminated Horror (172, 136)", 4, "Arx"],
            ["Braccus Rex", "Tomb of Lucian: Braccus Rex (581, 284)", 4, "Tomb of Lucian"]
        ]
        collectiveRule = []
        selectedLocations = []
        for hit in selectedHits:
            for reference in hitReference:
                if(hit == reference[0]):
                    selectedLocations.append(reference)
                    break
        if(world.options.goal == world.options.goal.option_reapers_eye_hit_list):
            for hit in selectedLocations:
                if(hit[2] == 1):
                    collectiveRule.append(CanReachLocation(hit[1], hit[3]))
            if(collectiveRule):
                world.set_rule(loc("Victory_All_Hits"), reduce(lambda a, b: a & b, collectiveRule))
        elif(world.options.goal == world.options.goal.option_reapers_coast_hit_list):
            for hit in selectedLocations:
                if(hit[2] == 1 or hit[2] == 2):
                    collectiveRule.append(CanReachLocation(hit[1], hit[3]))
            if(collectiveRule):
                world.set_rule(loc("Victory_All_Hits"), reduce(lambda a, b: a & b, collectiveRule))
        elif(world.options.goal == world.options.goal.option_the_nameless_isle_hit_list):
            for hit in selectedLocations:
                if(hit[2] == 1 or hit[2] == 2 or hit[2] == 3):
                    collectiveRule.append(CanReachLocation(hit[1], hit[3]))
            if(collectiveRule):
                world.set_rule(loc("Victory_All_Hits"), reduce(lambda a, b: a & b, collectiveRule))
        else:
            for hit in selectedLocations:
                collectiveRule.append(CanReachLocation(hit[1], hit[3]))
            if(collectiveRule):
                world.set_rule(loc("Victory_All_Hits"), reduce(lambda a, b: a & b, collectiveRule))  

                   
def set_completion_condition(world: DOS2World) -> None:
    world.set_completion_rule(Has("Victory"))