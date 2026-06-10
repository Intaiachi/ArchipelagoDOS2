# Divinity Orignial Sin 2

## What does randomization do to this game?

All quest completions and hostile enemy killed will have a radomized reward.

## What is the goal when randomized

The only goal currently is to defeat Bishop Alexander and esacpe Reaper's Eye. This will be expanded upon in later versions.

## What items and locations get shuffled?

The locations include all hostile enemy killed, and every quest completion that is found in the journal.

The items that get shuffled consist of:
- Gold
- Special Arrows
- Scrolls
- Skillbooks
- Level Ups
- Attribute Points
- Combat Ability Points
- Civil Ability Points
- Talent Points
- Max Source Points
- Purging Wand

## Which items can be in another player's world?

All items listed in the above list.

## What does another world's item look like in Divinity?

No information will be presented in the game, the client is the only current way to see incoming and outgoing items.

## What happends when I receive an item?

If its an item, it will appear in the current controlled party members inventory. If its the first of its type to be obtained, a pop up in the middle of the screen will the item recieved.
If its any of the stats, it will be given to each party member and can be spent when opening up the character menu. Level ups will make their usual effects and sounds but the rest will be silent, keep your eyes open!

## Whats this Archipelago Sync spell?

In the yaml, there is an option that determinds when the game will sync with Archipelago. When the option "On Spell" is selected, the character you started as will learn the "Archipelago Sync" Spell.
This spell mimics the effects of the spell "Bless", but instead of blessing anything, you will receive all Archipelago items that are unclaimed. This spell has unlimited uses and uses no memory slot.

## This quest didn't send an item upon completion, why?

Some quests seem not to have events that the current system uses to check if the player has completed a quest, and some quests even share some.
The known quests that seem to lack (or can't use these for some reason) are:
- Nothing But Child's Play
- The Eternal Worshipper
- Hot Under the Collar

And uniquely, "Healing Touch" and "Most Dangerous When Cornered" share the same location, so completing either of these quests will fulfill this location, but only one total between the two.

If you believe you have a case that is an execption to these, please let Intaiachi know in the Discord to see if he can fix it for furture releases.

## I see that I received an item, but its not in my inventory, why?

Items are sent to the currently controlled character, so if you swap control such as in combat, who is holding the item can be vague, so make sure to check all inventories.
If you checked and you didn't receive the item, let Intaiachi in the Discord know what item seemed not to work so he can fix it for furture releases.

## The client doesn't say I'm sending anything, why?

You must open and connect the client to the multiworld before starting the game. You can stay on the main menu, but starting or loading a save without the client connected beforehand will not work.