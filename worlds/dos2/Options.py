from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, OptionSet, Visibility

class Goal(Choice):
    """
    Determines what constitutes a victory.
    These will determine the length of the game and thus what items and locations are avaliable
    Defeat Alexander: Goal is to defeat Alexander and board the Lady Vengeance and escape Fort Joy. All items and locations will be limited to the Merryweather and Fort Joy.
    """

    display_name = "Goal"

    option_defeat_alexander = 0

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
    Loading a previous save will give items that were not yet granted at that time, do not worry about permanently losing items when using normal mode.
    """

    display_name = "Sync Options"

    option_on_spell = 0
    option_normally = 1

@dataclass
class DOS2Options(PerGameCommonOptions):
    goal: Goal
    death_link: Deathlink
    deathlinkStyleIn: DeathlinkStyleIn
    deathlinkStyleOut: DeathlinkStyleOut
    syncOption: SyncOption