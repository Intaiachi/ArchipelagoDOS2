from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if(TYPE_CHECKING):
    from .World import DOS2World

FILLER_ITEMS = [
    ["Gold", "1c3c9c74-34a1-4685-989e-410dc080be6f"]
]

USEFUL_ITEMS = [
    ["Chain Lightning Skillbook", "bc95a621-7b62-4a3f-bf34-0e4631988cae"],
    ["Teleportation Skillbook", "26d5c4bb-0182-4f29-ab14-36db839b294f"],
    ["Tornado Skillbook", "e0d4e3f4-141e-4675-b323-9f5233c5911f"],
    ["Apportation Skillbook", "bb4242cd-2866-4279-849d-fbacb3c7746"],
    ["Blessed Smoke Cloud Skillbook", "557ff98b-5af4-4d33-8347-0c3c82e561f0"],
    ["Blinding Radiance Skillbook", "5f01504c-0b7c-4cca-ba59-4ec09205f199"],
    ["Breathing Bubble Skillbook", "83cfc525-f810-4dff-9f2b-6d6a381fef2b"],
    ["Cursed Electric Infusion Skillbook", "a0cf63ce-4cfa-4b04-8246-312d137fbde"],
    ["Dazing Bolt Skillbook", "7b0113b7-03d5-46e2-b3db-bf1288017510"],
    ["Electric Fence Skillbook", "c7538f38-c2a9-457b-aadb-7a9abd81db7e"],
    ["Electric Infusion Skillbook", "eea2a2a2-571b-4b2a-9e46-e8b9d056b310"],
    ["Evasive Aura Skillbook", "ef6651cc-95a0-42bf-be0b-d4e2d9c2801b"],
    ["Evasive Maneuver Skillbook", "5b11b1cb-87be-4a00-aa60-0cabd6d66793"],
    ["Favourable Wind Skillbook", "af67492d-77dd-4e07-bb06-01779c2f6b0e"],
    ["Jellyfish Skin Skillbook", "3df50ba4-d0d0-4b3c-bc0d-799025abe"],
    ["Lightning Skillbook", "92262321-b1b7-43a0-6502-29f88adabd45"],
    ["Lightning Bolt Skillbook", "8b820d2d-76ee-4ec7-a7ee-6169fc81df38"],
    ["Mass Breathing Bubbles Skillbook", "5817cd39-a40f-4bb7-89d5-9f6445cbeb71"],
    ["Netherswap Skillbook", "34634252-35fc-44ea-9c1d-4a21302b0f30"],
    ["Pressure Spike Skillbook", "67372ab5-674b-4ee8-bd03-e2f960f79f9a"],
    ["Shocking Touch Skillbook", "7063e6d4-b5ea-42b6-a3f7-d0c23fca72e5"],
    ["SmokeCover Skillbook", "74adc1a7-7dc7-420d-8ba1-e71efb07d886"],
    ["Superconductor Skillbook", "b063ae17-3705-431c-8269-49c1df4618bd"],
    ["Vacuum Aura Skillbook", "22f11215-1c98-462d-b7d3-ce0ff506a690"],
    ["Vacuum Touch Skillbook", "bcd7aa00-77ed-4ad7-a9ee-397e5e57236"],
    ["Vaporize Skillbook", "08bf6dff-c1e0-4441-b4f5-1de534e89731"],
    ["Windwalker Skillbook", "5dea75d4-7487-435c-b679-2a8e60e02fb8"],
    ["Acid Infusion Skillbook", "a0969593-ef7a-427b-8158-9f50b52b8f78"],
    ["Acid Spores Skillbook", "ae22a78746d3-43e0-6998-4c7eade68110"],
    ["Artillery Plant Skillbook", "2d1dc69f-40a8-4ff1-ab1f-410df41ae637"],
    ["Condense Skillbook", "73507ba6-22d5-43c0-ad5b-e3fda728a664"],
    ["Contamination Skillbook", "25654041-51fc-495d-85d4-6ec45fcc7e11"],
    ["Corrosive Spray Skillbook", "cff44010-b803-4a81-a1e9-639d767dfc3e"],
    ["Corrosive Touch Skillbook", "5b5ffe55-b8d5-4bbb-9e45-a25a31484e2a"],
    ["Dust Blast Skillbook", "5b5807a1-0bfe-4443-9782-7466c4e6b5ef"],
    ["Earthquake Skillbook", "1ca41f7d-6c40-4426-8098-511b37697410"],
    ["Fortify Skillbook", "cb963736-247a-4f39-94a1-5144c6851598"],
    ["LivingWall Skillbook", "630681f7-3fbb-4d81-a3e6-7d499e857762"],
    ["Mass Oily Carapace Skillbook", "fa258fde-321c-4662-8062-c08f6c8a5f26"],
    ["Mend Metal Skillbook", "831fa280-4eff-43c7-a277-8430f669ea27"],
    ["Oily Carapace Skillbook", "f93d201e-386d-4cdf-b1c8-2eef2312d5de"],
    ["Poison Dart Skillbook", "e23f2893-1aef-44aa-8288-2eebf2a3caaa"],
    ["Poison Infusion Skillbook", "1789c173-53da-46af-aa81-4541cdaf985e"],
    ["Poisonous Skin Skillbook", "39511a41-231c-493b-9fa8-5ee320d57597"],
    ["Poison Wave Skillbook", "df73bc8-d156-4d9c-8e90-a571a7da3fdb"],
    ["Pyroclastic Eruption Skillbook", "186af633-ba25-46b1-866-367738346e7b"],
    ["Pyroclastic Rock Skillbook", "cbc25845-125f-4170-a160-479d584db3ae"],
    ["Reactive Armor Skillbook", "cf6354b0-875b-42b7-910e-6e9580ae6c02"],
    ["Rock Spikes Skillbook", "ede89604-3755-4723-9971-316b8d7ca9dc"],
    ["Siphon Poison Skillbook", "4c26b290-4c4c-494e-a4d7-f197a1c2ced"],
    ["Throw Dust Skillbook", "e8f68547-633e-4555-aaf2-82d7a16a8ef3"],
    ["Venom Coating Skillbook", "7b59499-6905-4e93-b2f3-9f3f7ecca62d"],
    ["Venomous Aura Skillbook", "e3a358cc-d082-4d91-bd16-07e9c3e0b921"],
    ["Worm Tremor Skillbook", "834a8c82-fc18-4a3e-be2b-d8c0cbcbc9d4"],
    ["Burn My Eyes Skillbook", "5bb56ca7-af0e-4ec9-a846-70e69c491325"],
    ["Corpse Explosion Skillbook", "67720f85-237-4f7f-b4b3-d11d90c7a9bf"],
    ["Deploy Mass Traps Skillbook", "720f21f3-0f9d-4a4b-841b-abb2888e57a5"],
    ["Fireball Skillbook", "d41c0497-86f1-4fba-9e29-43deed2456ae"],
    ["Fireblood Skillbook", "42b68832-2c87-442a-b35f-bfff01c86b18"],
    ["Fire Brand Skillbook", "99abc6f3-953c-42c1-a8f5-7e83a43e201c"],
    ["Fire Infusion Skillbook", "0bb04617-526b-495a-96d6-c11bf543e473"],
    ["Fire Slug Skillbook", "e9603823-9258-45e0-80b2-49aba65ab4bb"],
    ["Fire Whip Skillbook", "b7778fc6-22fc-4735-b71c-09f89e75e160"],
    ["Flaming Crescendo Skillbook", "f7f65ffc-df6d-4b78-9ba7-081cd9c09595"],
    ["Flaming Daggers Skillbook", "e2b8eae9-a9ad-45e5-bf3f-d8572a4610e2"],
    ["Flaming Skin Skillbook", "b516121c-8335-44cb-8793-b9f3b2384418"],
    ["Flaming Tongues Skillbook", "5bc388a3-49e2-4f56-a531-6f1a11b88597"],
    ["Haste Skillbook", "a02ecabc-7a5b-4590-b66b-c7569e9fd5a8"],
    ["Ignition Skillbook", "8618d073-2a58-42e7-8527-c6f512e1a751"],
    ["Infectious Flame Skillbook", "7be51ea9-2722-405e-9978-487bda5e60b8"],
    ["Laser Ray Skillbook", "bfb4ca0c-43a4-4050-a6ae-fe524b79071"],
    ["Launch Explosive Trap Skillbook", "aace8d2a-5ddf-4891-9619-d35dc9c617b"],
    ["Mass Corpse Explosion Skillbook", "cff60186-2fe2-4ebd-82a1-5e88c70fc9cd"],
    ["Mass Sabotage Skillbook", "5c4ca011-4383-4410-8ca2-591af5502d77"],
    ["Master Of Sparks Skillbook", "3236433a-16fc-4a7c-a73b-87bc0d53414"],
    ["Meteor Shower Skillbook", "c8912baa-6c8e-4866-a789-342bc5ac4af3"],
    ["Necrofire Infusion Skillbook", "84467775-625b-498b-b341-56011792a953"],
    ["Sabotage Skillbook", "2babe986-fe6b-459c-ba6b-3afe6352af20"],
    ["Sparking Swings Skillbook", "88ce199a-cccd-4c31-972a-67efb07dcf91"],
    ["Spontaneous Combustion Skillbook", "a8777c7c-11c3-44ab-b97-361d7acf3f26"],
    ["Supernova Skillbook", "a6370cb1-6cbe-407b-b005-a13558581b34"],
    ["Black Shroud Skillbook", "b12a442a-cc2f-4387-995e-7ce14826fa55"],
    ["Bloated Corpse Skillbook", "57ab0717-756e-4456-86b2-1de27deba116"],
    ["Blood Bubble Skillbook", "3004f9b9-0369-4f16-b659-1b77d89f8f83"],
    ["Bone Cage Skillbook", "d54c4e70-5796-48cf-b9e6-9b95b96cea4b"],
    ["Bone Pile Skillbook", "dcf5c008-c89b-42b9-8e3b-d5722e5230ad"],
    ["Deaths Door Skillbook", "ac09144a-dd65-485a-962-810a5a731710"],
    ["Death Wish Skillbook", "21085dcc-ec4a-4ffe-9877-5ee503341658"],
    ["Decaying Touch Skillbook", "ac14dff6-8a90-488a-8b2e-e9bcc2dc5b4d"],
    ["Grasp Of The Starved Skillbook", "880d084e-20aa-4a50-9a4c-294d46399ed6"],
    ["Infect Skillbook", "591cb46f-0336-4d34-aad7-026d61f164c6"],
    ["Last Rites Skillbook", "3ec31ae8-c176-4477-bfc8-25aa2cc855ba"],
    ["Mosquito Swarm Skillbook", "c64162ff-114c-4dd4-80d3-0194d317e9a3"],
    ["Necromancer Totems Skillbook", "aef6baab-29fb-42d3-96e9-63250af7b2af"],
    ["Rain Of Blood Skillbook", "4dede91d-3ddd-446f-9711-dd60ea93fba3"],
    ["Shackles Of Pain Skillbook", "99fa47fa-a40a-4dc1-b34b-ec3c987ab3d5"],
    ["Silencing Stare Skillbook", "5b903a84-4fc3-4d1b-998c-b5a11474c152"],
    ["Apotheosis Skillbook", "32630703-facd-4008-a3a4-54e81194049"],
    ["Bull Horns Skillbook", "8cc87c12fbff-4aad-8ce6-8597d74de717"],
    ["Chameleon Skin Skillbook", "5257a424-4aa7-4910-a964-bacf9df0141b"],
    ["Chicken Touch Skillbook", "e8c712ce-6927-4578-abff-742407dd3ad2"],
    ["Demonic Bargain Skillbook", "5e8b4369-8406-495-9761-550218e975c7"],
    ["Equalize Skillbook", "1ceb48aa-5f4e-4432-a18e-c74242fdf618"],
    ["Launch Oil Blob Skillbook", "680e5f32-a663-4c7b-a1aa-52334449b8c3"],
    ["Medusa Head Skillbook", "630f5666-0d89-4539-bae5-8ffc8aedc7ec"],
    ["Shed Skin Skillbook", "cac0c495-916e-490e-8f86-105783eb17fa"],
    ["Spider Legs Skillbook", "5288c06-a265-4f8d-bbc5-5fbb4249046c"],
    ["Steel Skin Skillbook", "22b90ab3-330f-4367-9dab-d48b6791482c"],
    ["Strip Resistance Skillbook", "902e02e6-b28e-4d0e-b6ff-cbda43b48bac"],
    ["Swap Ground Skillbook", "1abba567-1cb7-4719-a4e9-cb1e207866ca"],
    ["Tentacle Lash Skillbook", "916121ce-bde1-4e3b-934c-96a0e3fb3169"],
    ["Wings Skillbook", "dad38e23-6ad4-4899-9c92-0c022b3ea752"],
    ["Arrow Spray Skillbook", "871ef655-5a2a-41c6-ac18-018c5c22d63e"],
    ["Ballistic Shot Skillbook", "49ebd42e-42a8-46c3-bd32-a3f5b0dcddd5"],
    ["Elemental Arrowheads Skillbook", "e57b2904-0203-445-ba4c-86145aeb4955"],
    ["Farsight Skillbook", "682663f1-f19f-47e6-be8e-df344533d949"],
    ["First Aid Skillbook", "e14201d7-3ba5-4481-a849-620a7bf5fd68"],
    ["Mark Skillbook", "6e0fcc26-8e87-4739-8bba-4b86e81801b1"],
    ["Multishot Skillbook", "bd927e3d-a06d-4c67-8b2e-c39fd6ea6fa0"],
    ["Piercing Shot Skillbook", "4a0aaf3b-bfe8-46c5-b9d5-da019c8640fb"],
    ["Pin Down Skillbook", "9548461b-55d5-412-6082-9331c38a599"],
    ["Rain Of Arrows Skillbook", "f44f4c83b545-4931-a3de-846e624239a2"],
    ["Reaction Shot Skillbook", "31884d0f-d65b-4bdd-aba1-71408ff37b44"],
    ["Ricochet Skillbook", "1e754971-4ae6-49dd-8798-9c4febee16a3"],
    ["Sky Shot Skillbook", "65b155c9-4c7c-4353-90c1-ca7e12773e94"],
    ["Snipe Skillbook", "02dab1ba-14a8-462d-bdfd-d68317f8b4e0"],
    ["Tactical Retreat Skillbook", "8034c1e6-ab1d-4d43-86e4-4daa029b53e8"],
    ["Adrenaline Skillbook", "2361e63f-dc80-4c63-892a-e8e658c4d832"],
    ["Chloroform Skillbook", "6b352396-1e74-446a-94c7-2a762db9ef63"],
    ["Cloak And Dagger Skillbook", "68984f13-9e02-43eb-a95f-8cd339dfcebc"],
    ["Corrupted Blade Skillbook", "2bec772-bea2-4465-8ac3-81a6a69927a"],
    ["Daggers Drawn Skillbook", "58e7824d-Od4f-4331-86f1-d36976577315"],
    ["Fan Of Knives Skillbook", "89d0e9c5-d538-4300-8504-2a5c93c7c90c"],
    ["Fatality Skillbook", "36384e38-bc56-434b-bbba-37a679ec5220"],
    ["Gag Order Skillbook", "dae871c3fcfc-4e24-9302-359f0505fb0d"],
    ["Knee Breaker Skillbook", "a297e33e-7214-495a-838d-1d437237969"],
    ["Launch Bomber Skillbook", "3a291754-71e6-496b-8038-69f0d0b2adca"],
    ["Serrated Edge Skillbook", "3896c4ee-243c-4628-adce-cc7e0ee6db2"],
    ["Sleeping Arms Skillbook", "5240dd04-e97c-464e-b150-4455876cd6bb"],
    ["Terrifying Cruelty Skillbook", "5da557fe-1823-438-9140-6a59f104ca61"],
    ["Throwing Knife Skillbook", "78ddb7e3-0328-4c3f-8895-6dc77dcf3c2f"],
    ["Vault Skillbook", "813f7c41-4766-455d-bf32-66c0da7a81df"],
    ["Voidwoken Charm Skillbook", "9373ffa1-8285-49a7-91aaf714934157b"],
    ["Cannibalize Skillbook", "ad1f38d3-d7c9-4dea-88e5-cb52c31892ea"],
    ["Charm Skillbook", "510fe3cd-4370-4e0f-b88c-fe8792062eab"],
    ["Close The Door Skillbook", "f46f480d-678d-4af7-935d-b437a2715060"],
    ["Dimensional Bolt Skillbook", "b8cb5184-b8ad-46d0-96fe-1c4801fd582e"],
    ["Ethereal Skillbook", "298d9977-10fa-45e2-882f-aee1b64ac38e"],
    ["Hamony Skillbook", "ea6e34fe-7234-460e-96bb-9d0e1f7ea6fd"],
    ["Incarnate Skillbook", "84c1c61a-77dd-4d22-9a1c-83adaa58be31"],
    ["Inner Demon Skillbook", "7c1d4c29-5e16-4fc3-8ee0-afe771fbd367"],
    ["Planar Gateway Skillbook", "27c01b16-bf05-4794-9a4b-073e2e249b5f"],
    ["Power Infusion Skillbook", "469109ba-ffe6-4348-8598-589135ebb3"],
    ["Ranged Infusion Skillbook", "ea057307-256d-4fa9-b971-1ccb8fc3c2c7"],
    ["Shadow Infusion Skillbook", "0984bcde-b2cf-43d6-599-68665c1dfd8a"],
    ["Soul Mate Skillbook", "4d353813-037e-448-8826-4bfc818e4025"],
    ["Supercharge Skillbook", "702b8cc0-16a8-47ee-99bc-b1e6c4c993a9"],
    ["Totem From Surface Skillbook", "4622fd45-f016-41a2-b5e7-d4f7e48708d7"],
    ["Warp Infusion Skillbook", "422bdb9-6eb7a-4913-b26e-7ad91a43f87c"],
    ["Battering Ram Skillbook", "dea0f7d4-705f-47db-b797-f8ecd69a88be"],
    ["Blink Strike Skillbook", "86fc9d54-877f-4ad8-9e49-166a4acf6602"],
    ["Bouncing Shield Skillbook", "95451a8e-536b-43c4-80b8-b24e1598da5f"],
    ["Challenge Skillbook", "afe91aca-115d-41e1-ba65-d8be94b7a4f9"],
    ["Crippling Blow Skillbook", "0379bd08-c28b-4477-9900-d523de77aa0c"],
    ["Deflective Barier Skillbook", "c0e91778-1ad2-4c85-b3a0-6ca455a206ca"],
    ["Enrage Skillbook", "731973a2-fc24-4494-aada-74b56c6f15e9"],
    ["Flury Skillbook", "f319cf58-944e-4545-9de8-ad6c1cd7ed1"],
    ["Ground Smash Skillbook", "d47a4597-ce6d-4172-b14e-a52228c2df22"],
    ["Guardian Angel Skillbook", "84eb703-e386-4d8b-bb3c-431573e4ea2a"],
    ["Overpower Skillbook", "c034b576-8379-4796-b03d-616c3c22c998"],
    ["Phoenix Dive Skillbook", "5513cf32-5f89-415a-8a02-13c52c579a59"],
    ["Taunt Skillbook", "0774d0c4-fd3c-4062-b371-78129344e0ee"],
    ["Thick Of The Fight Skillbook", "4bf493df-6684-4b49-aa34-8d244bc55439"],
    ["Whirlwind Skillbook", "03a001b9-4f0a-9348-b971546c23ea"],
    ["Arcane Stitch Skillbook", "e8ae046a-9780-42a1-839c-9c51beeab0bb"],
    ["Blood Storm Skillbook", "4fd6849b-b2cb-416b-9094-05c55d56c88e"],
    ["Chain Heal Skillbook", "a4d37aea-d9b8-4ba6-bd0b-aaaad48d13aa"],
    ["Cleanse Wounds Skillbook", "9def4e2e-e1bd-4a32-82b8-02b5b26a88a0"],
    ["Cryogenic Stasis Skillbook", "a3a4900c-32f4-4288-ba15-30c741f86fdb"],
    ["Cryotherapy Skillbook", "e9d33b75-125a-4537-a06e-5ed9358c18f9"],
    ["Frost Aura Skillbook", "d550c530-99ba-430c-9df0-6a32657259da"],
    ["Frosty Shell Skillbook", "7b703887-6680-419a-b9c1-656200fb709c"],
    ["Global Cooling Skillbook", "b2db6248-342f-4066-b000-9a8321e1dbc2"],
    ["Hail Attack Skillbook", "f3b278b6-aff3-47e7-a8f7-823ebb6759e6"],
    ["Hail Strike Skillbook", "1850ec4f-c1dd-4859-8b83-a2a2343c2b8c"],
    ["Healing Tears Skillbook", "65339679-9eb6-4a17-9fcd-9857ef9ca931"],
    ["Ice Breaker Skillbook", "850f7646-6c0d-4af9-850c-94cd6d818575"],
    ["Ice Fan Skillbook", "87fcd775-240e-4175-bc69-a413b26942e4"],
    ["Ice Infusion Skillbook", "bb6e9b6a-dbc0-4eb9-bb06-9e3272e715e4"],
    ["Ice Skin Skillbook", "21875884-6c62-4ec6-b259-c4b415ba3958"],
    ["Mass Cleanse Wounds Skillbook", "c05fe2f6-ff5e-4a4d-8ff3-8172bdfcae33"],
    ["Mass Cryotherapy Skillbook", "da5a4e3d-48fe-498d-9f3e-840152a78828"],
    ["Rain Skillbook", "aab17859-7e1a-4298-9b97-5fdd69132ecd"],
    ["Restoration Skillbook", "179a1a74-60db-434-b9cc-35905c4d1cfa"],
    ["Shatter Skillbook", "29db00fb-0266-4a87-a7ea-673ea84e03c5"],
    ["Steam Lance Skillbook", "9f1e1389-a6e8-4acc-a239-026a973ad11a"],
    ["Vampiric Hunger Skillbook", "a672d6a7-2576-4826-b7ec-d6ed1db91fb7"],
    ["Vampiric Hunger Aura Skillbook", "2398983b-d9f3-40ca-9269-9a4fb0860931"],
    ["Water Infusion Skillbook", "4b64e46b-ce85-4b1a-8c3c-72e6ba24dc42"],
    ["Winter Blast Skillbook", "b90ab93a-a9f0-4774-8750-a0735ebee18c"]
]

#0 - jort joy, 1 - reapers eye, tbd for future locations
PROGRESSION_ITEMS = [
    ["Level Up", "levelUp", 1, ItemClassification.progression, 0],
    ["Purging Wand", "2b4412a5-467a-44ae-9d7b-bf39a06794b2", 2, ItemClassification.progression, 1]
]

#item name, id in game, id in ap, classification, level
ITEM_TUPLES = [
    ["Level Up", "levelUp", 1, ItemClassification.progression, 0],
    ["Purging Wand", "2b4412a5-467a-44ae-9d7b-bf39a06794b2", 2, ItemClassification.progression, 1],
] + [[item[0], item[1], index + 1000, ItemClassification.useful, 0] for index, item in enumerate(USEFUL_ITEMS)] \
  + [[item[0], item[1], index + 3000, ItemClassification.filler, 0] for index, item in enumerate(FILLER_ITEMS)]

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