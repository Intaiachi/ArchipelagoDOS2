from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, OptionSet, Visibility

class Goal(Choice):
    """
    Determines what constitutes a victory.
    These will determine the length of the game and thus what items and locations are avaliable
    Escape Reaper's Eye: Goal is to defeat Alexander and board the Lady Vengeance and escape Reaper's Eye. All items and locations will be limited to the Merryweather and Reaper's Eye.
    Leave Reaper's Coast: Goal is to master source and leave Reaper's Coast. All items and locations will be limited to the Merryweather, Reaper's Eye, Lady Vengeance, and Reaper's Coast.
    Escape The Nameless Isle: Goal is to escape The Nameless Isle after Dallis sabotages your ascension. All items and locations will be limited to the Merryweather, Reaper's Eye, Lady Vengeance, Reaper's Coast, and The Nameless Isle.
    Defeat Braccus Rex: Goal is to defeat the final boss and complete the game. All items and locations are included.
    Reaper's Eye Hit List: Goal is to kill a defined group of enemies set in the following option. Hits limited to Reaper's Eye.
    Reaper's Coast Hit List: Goal is to kill a defined group of enemies set in the following option. Hits limited to Reaper's Eye and Reaper's Coast.
    The Nameless Isle Hit List: Goal is to kill a defined group of enemies set in the following option. Hits limited to Reaper's Eye, Reaper's Coast, and The Nameless Isle.
    Arx Hit List: Goal is to kill a defined group of enemies set in the following option. All hits are allowed.
    """

    display_name = "Goal"

    option_escape_reapers_eye = 0
    option_leave_reapers_coast = 1
    option_escape_the_nameless_isle = 2
    option_defeat_braccus_rex = 3
    option_reapers_eye_hit_list = 4
    option_reapers_coast_hit_list = 5
    option_the_nameless_isle_hit_list = 6
    option_arx_hit_list = 7

class HitList(OptionSet):
    """
    If a hit list is set as a goal, select which kills are required to complete the goal.
    Enemies selected that aren't available in the acts selected will be ignored
    Reaper's Eye: Windego, Voidwoken Deep-dweller, Radeka the Witch, Bishop Alexander
    Reaper's Coast: Lich, Lamenting Abomination, Alice Alisceon, Harbinger of Doom, The Eternal Aetera, "Ghalann, Scion of the Elves", Ryker, Mordus
    The Nameless Isle: The Great Guardian, Source Titan
    Arx: Loic the Immaculate, Voidwoken Bloodfury, Sanguinia Tell, Karon, Isbeil, Thorny Suncaller, Lord Linder Kemm, Adramahlihk, Contaminated Horror, Braccus Rex
    """
    valid_keys = [
        "Windego",
        "Voidwoken Deep-dweller",
        "Radeka the Witch",
        "Bishop Alexander",
        "Lich",
        "Lamenting Abomination",
        "Alice Alisceon",
        "Harbinger of Doom",
        "The Eternal Aetera",
        "Ghalann, Scion of the Elves",
        "Ryker",
        "Mordus",
        "The Great Guardian",
        "Source Titan",
        "Loic the Immaculate",
        "Voidwoken Bloodfury",
        "Sanguinia Tell",
        "Karon",
        "Isbeil",
        "Thorny Suncaller",
        "Lord Linder Kemm",
        "Adramahlihk",
        "Contaminated Horror",
        "Braccus Rex"
    ]
    display_name = "User Defined Hit List"
    default = {
        "Windego",
        "Voidwoken Deep-dweller",
        "Radeka the Witch",
        "Bishop Alexander",
        "Lich",
        "Lamenting Abomination",
        "Alice Alisceon",
        "Harbinger of Doom",
        "The Eternal Aetera",
        "Ghalann, Scion of the Elves",
        "Ryker",
        "Mordus",
        "The Great Guardian",
        "Source Titan",
        "Loic the Immaculate",
        "Voidwoken Bloodfury",
        "Sanguinia Tell",
        "Karon",
        "Isbeil",
        "Thorny Suncaller",
        "Lord Linder Kemm",
        "Adramahlihk",
        "Contaminated Horror",
        "Braccus Rex"
    }

class ContainerSanity(Choice):
    """
    !!!!WORK IN PROGRESS, I DO NOT RECOMMEND TURNING THIS ON!!!!
    When enabled, opening a container will send a check.
    Chests Only: Only proper chests will be added as checks
    Everything: If its a container that can be looted, its a check. Does not include containers that are not apart of the map such as the corpses of once alive enemies or smuggled barrels.
    The check will also be sent out if the container is destroyed (it takes a couple seconds though be patient)
    """

    display_name = "ContainerSanity"

    option_disabled = 0
    option_chests = 1
    option_everything = 2

class Deathlink(Toggle):
    """
    If a player with this setting dies, all who also have this setting dies
    """

    display_name = "Deathlink"
    default = False

class DeathlinkStyleIn(Choice):
    """
    This determines if the entire party dies, or only one party member dies when recieving a deathlink.
    Need to have deathlink enabled to do anything.
    Party: The whole party dies when recieving a deathlink
    Random: One random party member dies when recieving a deathlink
    Player Controlled: Kills the currently controlled character when recieving a deathlink
    """

    display_name = "Deathlink Recieve Style"

    option_party = 0
    option_random_death = 1
    option_player_controlled = 2

class DeathlinkStyleOut(Choice):
    """
    This determines rather a deathlink is sent out on a full party wipe or a singular party members death.
    Needs to have deathlink enabled to do anything.
    Party: A deathlink is sent out when the full party dies
    Singular: A deathlink is sent out when a single party member dies
    """

    display_name = "Deathlink Send Style"

    option_party = 0
    option_singular = 1

class SyncOption(Choice):
    """
    This setting changes when the game will recieve items from the Archipelago server.
    On Spell: A custom spell called "Sync Archipelago" will be given to you, and casting it will claim all unclaimed Archipelago items.
    Normally: You will claim items as they get sent to the server.
    This is mainly to avoid recieving items that encumber you in combat.
    """

    display_name = "Sync Options"

    option_on_spell = 0
    option_normally = 1

class TrapPercentage(Range):
    """
    Enables and sets the percent of filler items that wll be replaced with traps.
    These traps gives a random status effect for either 1 turn (minor), 2 turns (moderate), 3 turns (severe).
    Not recommened if using on spell sync option
    """
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 0

class TrapStyle(Choice):
    """
    Determines if a trap applies its status to all party members or one random party member.
    Does nothing if traps aren't enabled
    """

    display_name = "Trap Style"
    option_party = 0
    option_random_party_member = 1

@dataclass
class DOS2Options(PerGameCommonOptions):
    goal: Goal
    hitList: HitList
    containerSanity: ContainerSanity
    death_link: Deathlink
    deathlinkStyleIn: DeathlinkStyleIn
    deathlinkStyleOut: DeathlinkStyleOut
    syncOption: SyncOption
    trapPercentage: TrapPercentage
    trapStyle: TrapStyle