from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import Items

if TYPE_CHECKING:
    from .World import DOS2World

#A lot of the FTJ ones came from @chaotic and @JeyKey09, thank you!
DOS2_KILL_LIST = [
    # --- merryweather ---
    ["S_TUT_TopDeckVoidling10_bd0123ae-26fd-4dad-8326-b6ae9a3fc1c5", ["Merryweather: Voidling 1"], 0],
    ["S_TUT_TopDeckVoidling11_2fcb5b84-875f-42bd-ac80-6f8495c6a47c", ["Merryweather: Voidling 2"], 0],
    # --- fort joy ---
    #beach voidlings
    ["S_FTJ_BeachVw_001_08348b3a-bded-4811-92ce-f127aa4310e0", ["Fort Joy: Voidling 1 (158, 325)"], 0],
    ["S_FTJ_BeachVw_002_1832a661-0e21-421f-acaa-a7e66e813b14", ["Fort Joy: Voidling 2 (157, 330)"], 0],
    #dirt mound zombie //not confident on this one
    ["S_FTJ_DirtMoundZombie_eb499ae9-21df-41e9-9d89-968a88ceb3ad", ["Fort Joy: Freshly Buried Corpse (225, 287)"], 0],
    #beach turtles
    ["S_FTJ_SpikedTurtle_01_abd3afae-a6e5-452c-a94a-db57826dd082", ["Fort Joy: Turtle 1 (258, 363)"], 0],
    ["S_FTJ_SpikedTurtle_03_fb4618f9-9c61-4640-a32c-e4735783e878", ["Fort Joy: Ancient Turtle (271, 365)"], 0],
    ["S_FTJ_SpikedTurtle_04_f37cb16e-027e-4a21-8504-d6cab12d9098", ["Fort Joy: Turtle 2 (283, 349)"], 0],
    #teleport crocs
    ["S_FTJ_TeleporteQuestrCroc_001_bc1a10a1-51b6-42c5-b517-827565f6512b", ["Fort Joy: Saltwater Crocodile 1 (113, 217)"], 0],
    ["S_FTJ_TeleporteQuestrCroc_002_6be95689-ab8f-4edf-ba46-77a068594a19", ["Fort Joy: Saltwater Crocodile 2 (124, 224)"], 0],
    ["S_FTJ_TeleporteQuestrCroc_003_7cf7d4d4-de1a-4ac7-999a-1f128fac3789", ["Fort Joy: Saltwater Crocodile 3 (116, 231)"], 0],
    #frogs
    ["S_FTJ_FrogAmbush_Melee_01_747af1e4-d204-4564-9a50-9f1955dd4723", ["Fort Joy: Charged Amphibian (528, 489)"], 0],
    ["S_FTJ_FrogAmbush_Ranged_02_ffae5e44-ac8a-4f43-ab14-2e684b60d87b", ["Fort Joy: Venomous Amphibian 1 (503, 491)"], 0],
    ["S_FTJ_FrogAmbush_Ranged_03_18d2b17c-a400-4e1d-991f-d1cbb44cfac4", ["Fort Joy: Venomous Amphibian 2 (518, 504)"], 0],
    #arena of the one 
    ["S_FTJ_Arena_Gladiator_001_51a8d141-c7df-4d56-8d28-ca403033ca16", ["Fort Joy: Gedeon, the Tenacious One (69, 562)"], 0],
    ["S_FTJ_Arena_Gladiator_002_31fcfd4c-1417-4ac8-8817-1dfb8a5b8e7b", ["Fort Joy: Veerle, the Avid One (64, 566)"], 0],
    ["S_FTJ_Arena_Gladiator_003_b81cb546-05b1-404c-ae00-d76a0702bb86", ["Fort Joy: Ailsa, the Cultured One (64, 559)"], 0],
    ["S_FTJ_Arena_Gladiator_004_d2a430fc-8f01-4962-b455-93f883c287d0", ["Fort Joy: Rex (72, 566)"], 0],
    #holding cell
    ["S_FTJ_OlgoCellarMagister_001_402470db-ad49-4de7-8a60-7f69c8e5d26e", ["Fort Joy: Magister Houndmaster (276, 654)"], 0],
    ["S_FTJ_OlgoCellarMagister_002_6d6b84bf-e940-4c28-a2b6-12516d049792", ["Fort Joy: Magister Swordsman 3 (276, 651)"], 0],
    ["S_FTJ_OlgoCellarMagister_003_e8c14f56-b34a-41c3-adb3-dda318c5bdc1", ["Fort Joy: Magister Ranger 6 (280, 651)"], 0],
    ["S_FTJ_OlgoCellarMagister_004_2955b578-1a8e-4ecd-aa7f-5f084c428e25", ["Fort Joy: Magister Ranger 7 (279, 663)"], 0],
    #prison
    ["S_FTJ_MagisterTorturer_1d1c0ba0-a91e-4927-af79-6d8d27e0646b", ["Fort Joy: Kniles the Flenser (384, 630)"], 0],
    ["S_FTJ_Torturer_Golem_01_584db8ce-8dcf-4906-bc6f-e51eb057de08", ["Fort Joy: Meat Golem 1 (389, 641)"], 0],
    ["S_FTJ_Torturer_Golem_02_aff8be39-58b0-4bff-8fa6-7cf501b5060b", ["Fort Joy: Meat Golem 2 (370, 639)"], 0],
    ["S_FTJ_Torturer_Golem_03_d32d32b2-c05b-4acd-944c-f2b802ec7234", ["Fort Joy: Meat Golem 3 (389, 620)"], 0],
    ["S_FTJ_SilentMonk_002_01343cec-09ab-48eb-9226-ce6b2880a6c0", ["Fort Joy: Agitated Silent Monk 1 (386, 651)"], 0],
    ["S_FTJ_SilentMonk_004_652ac6e3-9778-42d3-81d1-35d88ffb2e8d", ["Fort Joy: Agitated Silent Monk 2 (389, 635)"], 0],
    ["S_FTJ_SilentMonk_010_aa03733a-861f-4814-8bf8-ba0c1cabb876", ["Fort Joy: Agitated Silent Monk 3 (379, 614)"], 0],
    #magisters in fort
    ["S_FTJ_ChapelMagister_001_068d4518-9b23-4e2c-a160-8d978d1f78ff", ["Fort Joy: Magister Ranger 1 (293, 197)"], 0],
    ["S_FTJ_ChapelMagister_002_090d7104-97f7-4603-a114-47dceaf021e5", ["Fort Joy: Magister Swordsman 1 (258, 164)"], 0],
    ["S_FTJ_ChapelMagister_003_b5cb12b2-f347-4415-95ac-8d5ac4fc464b", ["Fort Joy: Magister Ranger 2 (302, 173)"], 0],
    ["S_FTJ_ChapelMagister_004_8f330be0-a442-408f-850e-c7fd94e74ada", ["Fort Joy: Magister Ranger 3 (262, 196)"], 0],
    ["S_FTJ_ChapelMagister_005_d5ea5e99-2406-4bb9-b2df-5fd975f1b63e", ["Fort Joy: Magister Swordsman 2 (260, 198)"], 0],
    ["S_FTJ_ChapelMagister_Captain_c4d751d4-20ff-4281-baf4-8ddeb1383e7e", ["Fort Joy: Magister Captian Trippel (279, 196)"], 0],
    #harbor near fort
    ["S_FTJ_HarbourSilentMonk_001_f7bd3244-e1e7-4079-ac95-fef6145a236e", ["Fort Joy: Silent Monk 1 (328, 224)"], 0],
    ["S_FTJ_HarbourSilentMonk_002_54b9a81b-7926-46b1-ad0d-6213c0d77749", ["Fort Joy: Silent Monk 2 (326, 224)"], 0],
    ["S_FTJ_HarbourSilentMonk_003_61bf204e-ba2e-412f-ac86-e132a3930105", ["Fort Joy: Silent Monk 3 (323, 224)"], 0],
    ["S_FTJ_HarbourSilentMonk_004_753d80ce-a515-43e3-8085-8ceacb3ceb4f", ["Fort Joy: Silent Monk 4 (321, 224)"], 0],
    ["S_FTJ_HarbourSilentMonk_005_4149080d-9cc5-424d-a8fc-c52222bb463a", ["Fort Joy: Silent Monk 5 (331, 224)"], 0],
    ["S_FTJ_HarbourMagister_001_d6a4e8d9-67bc-4961-95ce-c7016357ea64", ["Fort Joy: Magister Ranger 4 (324, 244)"], 0],
    ["S_FTJ_HarbourMagister_002_14581b6d-9423-4e2c-8d19-8f1b222ab760", ["Fort Joy: Magister Inquisitor (323 246)"], 0],
    ["S_FTJ_HarbourMagister_003_75ffb9bd-5ddb-4c2c-8ad0-55c00b34be7b", ["Fort Joy: Magister Ranger 5 (322, 244)"], 0],
    ["S_FTJ_HarbourMagister_004_97492757-bbe8-42d8-af6d-35ca0ae96d36", ["Fort Joy: Magister Knight (333, 235)"], 0],
    ["S_FTJ_HarbourMagister_005_55c5c79e-2260-40bd-ab1d-c2d05fe31d45", ["Fort Joy: Magister Dayve (321, 225)"], 0],
    #court room
    ["S_FTJ_CourtRoomGuard_001_c51d581d-9245-431f-a1eb-88adc8149827", ["Fort Joy: Magister Courtroom Swordsman 1 (276, 139)"], 0],
    ["S_FTJ_CourtRoomGuard_002_bb9fd6c4-4231-44ac-a24d-5955dc300147", ["Fort Joy: Magister Courtroom Swordsman 2 (289, 139)"], 0],
    ["S_FTJ_HighPriest_2a09f30c-0a3b-495f-8386-5390a6c4c08d", ["Fort Joy: High Judge Orivand (283, 129)"], 0],
    ["S_FTJ_AnkhPriestess_dfca80ec-cd31-48ed-abfc-801514f1bd8e", ["Fort Joy: Magister Cryomancer (280, 126)"], 0],
    ["S_FTJ_AnkhPriest_f06d709f-335c-4c34-b959-9ae753bc7d68", ["Fort Joy: Magister Pyromancer (284, 126)"], 0],
    #trap soulroom
    ["S_FTJ_SoulJarTrapSkeleton_001_0375d94c-b588-4a1d-bd62-e8dfbd614df4", ["Fort Joy: Pyromancer Guardian (372, 577)"], 0],
    ["S_FTJ_SoulJarTrapSkeleton_002_20d96b30-c279-4f94-8815-8114e48f261e", ["Fort Joy: Blademaster Guardian (385, 566)"], 0],
    ["S_FTJ_SoulJarTrapSkeleton_003_5ef951b7-a893-4b48-9ee2-7e5d754c6a83", ["Fort Joy: Cryomancer Guardian (390, 577)"], 0],
    ["S_FTJ_SoulJarTrapSkeleton_004_40850e09-8b9f-4b38-8f90-a9499bcb054c", ["Fort Joy: Aeromancer Guardian (371, 556)"], 0],
    ["S_FTJ_SoulJarTrapSkeleton_005_b104ee53-94a5-4d2b-a9ed-5345327a4e42", ["Fort Joy: Blademaster Guardian (378, 565)"], 0],
    ["S_FTJ_SoulJarTrapSkeleton_006_a46127af-ff0f-452f-a2e1-260abd2a1001", ["Fort Joy: Eagle-Eyed Guardian (379, 577)"], 0],
    ["S_FTJ_SoulJarTrapSkeleton_007_deffe0d5-11f5-44a9-b50f-497f200ad4f7", ["Fort Joy: Traitorous Guardian (370, 550)"], 0],
    #windego
    ["S_GLO_Windego_d783285f-d3be-4cba-8333-db8976cef182", ["East Reaper's Eye: Windego (357, 192)"], 0],
    #swamp
    ["S_FTJ_SwampBuildup_A_Undead_Assassin_a54a04a3-8507-4a37-a8b6-068fd0ec8146", ["East Reaper's Eye: Decomposing Assassin (379, 152)"], 0],
    ["S_FTJ_SwampBuildup_A_Undead_Melee_01_8b70b76c-24f8-4b3c-aae8-3c78c93ab2bb", ["East Reaper's Eye: Decomposing Swashbuckler (386, 155)"], 0],
    ["S_FTJ_SwampBuildup_A_Undead_Terra_01_7dee6a3d-ef4f-4281-a311-a65d483e13d1", ["East Reaper's Eye: Decomposing Terramancer (389, 151)"], 0],
    ["S_FTJ_SwampBuildup_B_Undead_Melee_01_e45ec44b-4033-4994-b6a4-f236dea40561", ["East Reaper's Eye: Decomposing Swashbuckler 2 (391, 206)"], 0],
    ["S_FTJ_SwampBuildup_B_Undead_Ranger_01_1195a59b-ba51-4662-afa7-7602b224cfc8", ["East Reaper's Eye: Decomposing Markswoman (401, 213)"], 0],
    ["S_FTJ_SwampBuildup_B_Undead_Ranger_02_5468e7d7-8f83-4245-94fc-7303c11612b5", ["East Reaper's Eye: Decomposing Marksman 1 (396, 216)"], 0],
    ["S_FTJ_SwampBuildup_B_Undead_Sword_9ee2fb19-5483-42a5-9037-c8147e9695fd", ["East Reaper's Eye: Decomposing Swashbuckler 3 (395, 210)"], 0],
    #ambush
    ["S_FTJ_VoidlingAmbush_000_d61a5845-383b-4759-9fe3-99f519dec4dc", ["East Reaper's Eye: Viscous Voidling 1 (461, 105)"], 0],
    ["S_FTJ_VoidlingAmbush_001_eedb56aa-aad1-4de2-8097-3fd7241be1ec", ["East Reaper's Eye: Viscous Voidling 2 (443, 118)"], 0], 
    ["S_FTJ_VoidlingAmbush_002_a8318c72-e603-4a08-b01d-09232110bccc", ["East Reaper's Eye: Viscous Voidling 3 (441, 98)"], 0], 
    ["S_FTJ_VoidlingAmbush_003_53680e8b-a4ee-4b00-9419-3860e91e76e6", ["East Reaper's Eye: Viscous Voidling 4 (464, 109)"], 0], 
    ["S_FTJ_VoidlingAmbush_004_3fe3a69c-97b6-42d5-b1db-bc646a66ab15", ["East Reaper's Eye: Viscous Voidling 5 (466, 115)"], 0], 
    ["S_FTJ_VoidlingAmbush_005_03ed2bcc-3b3b-4e9c-bfd1-54c7f6a1bcaa", ["East Reaper's Eye: Viscous Voidling 6 (451, 114)"], 0], 
    ["S_FTJ_VoidlingAmbush_006_0cf5424e-2183-4c52-980e-de156c31f5e4", ["East Reaper's Eye: Viscous Voidling 7 (453, 92)"], 0], 
    ["S_FTJ_VoidlingAmbush_007_1aa2f181-c36b-4e9e-ae5e-9652fe038824", ["East Reaper's Eye: Viscous Voidling 8 (447, 95)"], 0], 
    ["S_FTJ_VoidlingAmbush_008_8c83992f-328d-405d-bebd-0f5461d027ad", ["East Reaper's Eye: Viscous Voidling 9 (447, 120)"], 0], 
    ["S_FTJ_VoidlingAmbush_009_811f904d-4822-463c-b77e-d658a0fb3380", ["East Reaper's Eye: Viscous Voidling 10 (454, 96)"], 0], 
    ["S_FTJ_VoidlingAmbush_010_7dfba778-1b94-4cf7-8b26-663dfcb760d3", ["East Reaper's Eye: Viscous Voidling 11 (460, 114)"], 0], 
    ["S_FTJ_VoidlingAmbush_011_a01a4838-c65a-452e-bde5-dc7b8e3dca27", ["East Reaper's Eye: Viscous Voidling 12 (440, 102)"], 0], 
    ["S_FTJ_VoidlingAmbush_012_360a68c3-e5f1-4834-aa9e-7dc7497d9301", ["East Reaper's Eye: Viscous Voidling 13 (464, 106)"], 0],
    #salamander
    ["S_FTJ_SW_ShelterBackSalamander1_26d2a05f-bd32-408c-adab-c01767271bbf", ["East Reaper's Eye: Void Salamander (492, 94)"], 0],
    ["S_FTJ_SW_ShelterBackSalamander2_e3812c55-7530-4d74-b79b-e8f3c91558a4", ["East Reaper's Eye: Noxious Void Salamander (494, 86)"], 0],
    ["S_FTJ_SW_ShelterBackSalamander3_62ac9493-260e-40bf-a615-5cdf475208d9", ["East Reaper's Eye: Void Salamander (485, 82)"], 0],
    #saving Gareth fight
    ["S_FTJ_CorneringMagister1_324e8aca-3b0b-430e-b8bb-2f6e9edac3fe", ["East Reaper's Eye: Magister Inquisitor (471, 254)"], 0],
    ["S_FTJ_CorneringMagister2_f278b94b-78ac-4cd7-9d8a-1c61e673ead3", ["East Reaper's Eye: Magister Ranger 1 (469, 253)"], 0],
    ["S_FTJ_CorneringMagister3_34996c94-6294-45e7-9659-f6fce2a95ea5", ["East Reaper's Eye: Magister Ranger 2 (464, 254)"], 0],
    ["S_FTJ_CorneringMagister4_96f35d8a-d38a-4fc1-9b23-bdf4349a16ec", ["East Reaper's Eye: Magister Swordsman 1 (462, 254)"], 0],
    ["S_FTJ_OutsideMagister1_51825365-42fd-4b0c-9f35-d21ae40833a3", ["East Reaper's Eye: Magister Knight (469, 230)"], 0],
    ["S_FTJ_OutsideMagister2_d3091599-a583-44b8-8ce7-3b7e9d88fdaa", ["East Reaper's Eye: Magister Ranger 3 (469, 228)"], 0],
    ["S_FTJ_OutsideMagister3_d584fdbb-1cfa-46d4-add2-5587eafd3e29", ["East Reaper's Eye: Magister Swordsman 2 (460, 231)"], 0],
    ["S_FTJ_OutsideMagister4_0a2cf9d4-6631-44c3-aea4-cc5a13f3419b", ["East Reaper's Eye: Magister Ranger 4 (460, 229)"], 0],
    #skeleton near tower //these might not work
    ["S_FTJ_SW_BurningSkeleton1_0b0d054f-aba2-4fac-b89b-473f59cb085e", ["East Reaper's Eye: Incandescent Decapitator (529, 93)"], 0],
    ["S_FTJ_SW_BurningSkeleton2_11e95a85-9877-403f-944e-16b2c4e9a4b3", ["East Reaper's Eye: Incandescent Scorcher (539, 94)"], 0],
    ["S_FTJ_SW_BurningSkeleton3_d53d04be-e7d7-4b37-8b93-2807921fb58a", ["East Reaper's Eye: Incandescent Marksman (529, 100)"], 0],
    #trompdoy
    ["S_FTJ_SW_IllusionistAtEntrance_e01c3723-872a-454d-a59b-d798b21183cd", ["East Reaper's Eye: Trompdoy (676, 487)"], 0],
    ["S_FTJ_SW_IllusionistFinal_1a3b44d4-0ba4-4289-b158-a54111b83e1d", ["East Reaper's Eye: Trompdoy (700, 497)"], 0],
    #deep dweller and friends //migth not work
    ["S_FTJ_SW_VWBoss_Mage_01_5cf41c21-bfed-499e-a6fe-6eda7c24b118", ["East Reaper's Eye: Decomposing Aeromancer (494, 170)"], 0],
    ["S_FTJ_SW_VWBoss_Mage_02_2f619e60-5cfc-4323-a094-e285ea922903", ["East Reaper's Eye: Decomposing Cryomancer (480, 159)"], 0],
    ["S_FTJ_SW_VWBoss_Melee_01_961c827b-43d1-43c8-8553-6d1d4c8e8aed", ["East Reaper's Eye: Decomposing Swashbuckler 4 (481, 164)"], 0],
    ["S_FTJ_SW_VWBoss_Melee_02_8644ff57-7eb3-4ed7-a496-00e977227b53", ["East Reaper's Eye: Decomposing Swashbuckler 5 (502, 167)"], 0],
    ["S_FTJ_SW_VWBoss_Ranger_01_e8ad5533-b8f0-4c55-a261-4192f5cf1e48", ["East Reaper's Eye: Decomposing Marksman 1 (482, 175)"], 0],
    ["S_FTJ_SW_VWBoss_VoidWoken_112f8c17-ea77-4658-ac72-239154772fb8", ["East Reaper's Eye: Voidwoken Deep-dweller (499, 157)"], 0],
    #witch
    ["S_FTJ_SW_Witch_4014aee0-56f1-47e0-a8eb-89c4b5a1da83", ["East Reaper's Eye: Radeka the Witch (691, 602)"], 0],
    ["S_FTJ_SW_Witch_Beetle_01_e973d472-f53a-4dee-be60-cd335f3dad7d", ["East Reaper's Eye: Carrion Beetle (697, 620)"], 0],
    ["S_FTJ_SW_Witch_Beetle_02_ea698437-fdcc-470f-8f9e-e7640c438690", ["East Reaper's Eye: Carrion Beetle (690, 597)"], 0],
    ["S_FTJ_SW_Witch_Beetle_03_a70281cd-a226-434b-b6a6-98ddedd42575", ["East Reaper's Eye: Carrion Beetle (679, 611)"], 0],
    ["S_FTJ_SW_Witch_BloodZombie_02_9d512d08-5e51-45ec-b06e-ff90fea7f6de", ["East Reaper's Eye: Bloody Corpse (687, 611)"], 0],
    ["S_FTJ_SW_Witch_BloodZombie_03_5549433c-5dec-4701-9733-8fb06009dfff", ["East Reaper's Eye: Bloody Corpse (694, 614)"], 0],
    ["S_FTJ_SW_Witch_BloodZombie_04_b714cbca-6c44-4d4d-918c-50269f773584", ["East Reaper's Eye: Bloody Corpse (689, 600)"], 0],
    ["S_FTJ_SW_Witch_Zombie_daa5de44-d3b9-47c3-aed5-9969ca29ce61", ["East Reaper's Eye: Undead Medat (693, 602)"], 0],
    #final reaper's eye fight
    ["S_FTJ_SW_FinalBattleMagister_000_c283e820-0166-4668-8ad4-842085d58de9", ["North-east Reaper's Eye: Magister Metamorph (552, 301)"], 0],
    ["S_FTJ_SW_FinalBattleMagister_001_165f1353-a916-4291-940a-293efbe8f187", ["North-east Reaper's Eye: Magister Assassin (570, 299)"], 0],
    ["S_FTJ_SW_FinalBattleMagister_002_0b7282f6-a131-4441-a113-8f3ea62fa9e3", ["North-east Reaper's Eye: Magister Markswoman (567, 309)"], 0],
    ["S_FTJ_SW_FinalBattleMagister_003_b5dd6af4-6b34-482e-bc0a-72bd6269aaf5", ["North-east Reaper's Eye: Magister Knight (570, 304)"], 0],
    ["S_FTJ_SW_FinalBattleMagister_Gheist_06082187-829f-43e1-b3bb-f3242a70904d", ["North-east Reaper's Eye: Gheist (564, 306)"], 0],
    ["S_FTJ_SW_FinalBattle_Voidwoken_7dcf3cc2-d015-4aff-9949-71fc539fcc73", ["North-east Reaper's Eye: Voidwoken Drillworm (594, 408)"], 0],
    ["S_GLO_Alexandar_03e6345f-1bd3-403c-80e2-a443a74f6349", ["North-east Reaper's Eye: Bishop Alexander (564, 306)"], 0]
]

#All of the FTJ ones came from @chaotic and @JeyKey09, thank you!
DOS2_LOCATION_LIST = [
    #i dont think Nothing but Child's Play, and The Eternal Worshipper have flags
    ["Quest-TUT_ShipInvestigation", ["Merryweather: Death Belowdecks - Complete"], 0],
    ["Quest-TUT_ShipMurder", ["Merryweather: Troubled Waters - Complete"], 0],
    ["Quest-FTJ_Escape", ["Fort Joy: Escape From Fort Joy - Complete"], 0],
    ["Quest-FTJ_Escape_Island", ["North-east Reaper's Eye: Escape From Reaper's Eye - Complete", "Victory_Escape_Reapers_Eye"], 0],
    ["Quest-FTJ_Escape_Island_SUBA", ["North-east Reaper's Eye: Talk to Malady - Complete"], 0],
    #["Quest-FTJ_Escape_Island_SUBB", ["placeholder4"], 0], I have no idea what these are
    #["Quest-FTJ_Escape_Island_SUBC", ["placeholder5"], 0],
    ["Quest-FTJ_Voice", ["East Reaper's Eye: The Voices - Complete"], 0],
    #["Quest-FTJ_Godwoken", ["placeholder7"], 0], I dont know what this is
    #["Quest-FTJ_Hunted", ["placeholder8"], 0], #dont know
    #["Quest-FTJ_Seeker", ["placeholder9"], 0], #I dont know
    ["Quest-RC_FTJ_OlgoSaheila", ["Fort Joy: The Imprisioned Elf - Complete"], 0],
    ["Quest-RC_FTJ_MurderousGheist", ["Fort Joy: The Murderous Gheist - Complete"], 0],
    ["Quest-FTJ_SourceHounds", ["Fort Joy: Finding Emmie - Complete"], 0],
    ["Quest-FTJ_Arena", ["Fort Joy: The Arena of Fort Joy - Complete"], 0],
    ["Quest-RC_FTJ_SoulJar", ["Fort Joy: Withermoore's Soul Jar - Complete"], 0],
    #["Quest-FTJ_SaheilaFate", ["placeholder15"], 0], #these two probably are related to act 2 (Saheila's People / The Elven Seer)
    #["Quest-RC_FTJ_SaheilaSignet", ["placeholder16"], 0],
    ["Quest-FTJ_Teleporter", ["Fort Joy: The Teleporter - Complete"], 0],
    ["Quest-FTJ_Elodi", ["Fort Joy: The Shakedown - Complete"], 0],
    ["Quest-FTJ_SW_Illusionist", ["East Reaper's Eye: The Vault of Braccus Rex - Complete"], 0],
    ["Quest-FTJ_SW_HurtSeekers", ["East Reaper's Eye: Healing Touch/Most Dangerous When Cornered - Complete"], 0], #same flag as Dangerous When Cornered for some reason
    #["Quest-FTJ_SW_StuckHaunting", ["placeholder21"], 0], #looking at more flags, this does seem to be The Eternal Worshipper, haven't got the flag to shoot outside of leaving act 1
    ["Quest-FTJ_SW_Necromancers", ["East Reaper's Eye: A Fate Worse Than Death - Complete"], 0],
    ["Quest-FTJ_SW_BraccusArmory", ["East Reaper's Eye: The Armoury - Complete"], 0],
    ["Quest-FTJ_SW_CursedRing", ["East Reaper's Eye: The Cursed Ring - Complete"], 0],
    ["Quest-FTJ_SW_UndeadTowerMaze", ["East Reaper's Eye: The Gargoyle's Maze - Complete"], 0],
    ["Quest-FTJ_SW_CursedPig", ["East Reaper's Eye: The Burning Pigs - Complete"], 0],
    ["Quest-FTJ_SW_PurgedDragon", ["East Reaper's Eye: The Purged Dragon - Complete"], 0],
    ["Quest-FTJ_SW_CallToArms", ["East Reaper's Eye: Call to Arms - Complete"], 0],
    ["Quest-FTJ_SW_Shriekers", ["East Reaper's Eye: The Shreikers - Complete"], 0],
    ["Quest-FTJ_SW_Tyrant", ["North-east Reaper's Eye: Artefacts of the Tyrant - Complete"], 0],
    #["Quest-ContaminationArmour", ["Seed of Power - Complete"], 0], This isn't completeable till act 4
    #["Quest-FTJ_SW_BatteredAndCornered", ["placeholder32"], 0], Youd think that this is Most Dangerous When Cornered but no (fires off on act exit)
    ["Quest-CaptainArmour", ["North-east Reaper's Eye: Threads of a Curse - Complete"], 0],
    #-- Act 2 -- #A Trial for all Seasons lacks flags, same with Burial Rites, Burying the Past
    ["Quest-LV_Main", ["Lady Vengence: Lady o' War - Complete"], 1],
    ["Quest-LV_HoE_Main", ["Lady Vengence: To The Hall of Echoes - Complete"], 1],
    ["Quest-RC_DW_WreckedCaravan", ["Reaper's Coast: The Wrecked Caravan - Complete"], 1],
    ["Quest-RC_DU_HeroicRescue", ["Reaper's Coast: They Shall Not Pass - Complete"], 1],
    #["Quest-RC_DU_Storm", ["placeholer3"], 1], #these two only have questclose events im pretty sure theyll never proc. Didnt even fire on act exit, probably nothing
    #["Quest-RC_DU_EmptyCamp", ["placeholder4"], 1],
    ["Quest-RC_DW_ShadowOverDriftwood", ["Driftwood: Shadow Over Driftwood - Complete"], 1],
    ["Quest-RC_WH_SeaGodStatue", ["Reaper's Bluffs: The Burning Prophet - Complete"], 1],
    ["Quest-RC_WH_BottledWish", ["Reaper's Bluffs: Wishful Thinking - Complete"], 1],
    ["Quest-RC_WC_TheDeadTrader", ["Reaper's Bluffs: Aggressive Takeover - Complete"], 1],
    #["Quest-RC_ThreeAltars", ["Driftwood Fields: The Three Altars - Complete"], 1], #according to the wiki, this quest doesnt actually close and is just recorded in The Eternal Proimse, so this probably doesnt work (wiki was right, closes on act leave)
    ["Quest-RC_DW_GarvanSupplies", ["Driftwood: Red Ink in the Ledger - Complete"], 1],
    #["Quest-RC_DW_GrandmasterArrest", ["placeholder11"], 1], idk, none fired on act exit
    #["Quest-RC_DW_Looter", ["placeholder12"], 1],
    #["Quest-RC_DW_TrappedHusband", ["placeholder13"], 1],
    #["Quest-RC_DW_BridgeDog", ["placeholder14"], 1],
    ["Quest-RC_DW_FunnyMeat", ["Driftwood: The Missing Magisters - Complete"], 1],
    #["Quest-RC_DW_FunnyMeat_SUBA", ["placeholder16"], 1], these are different routes the quest can take, ie annoying missabled, the main fire on all of them anyway
    #["Quest-RC_DW_FunnyMeat_SUBB", ["placeholder17"], 1],
    #["Quest-RC_DW_FunnyMeat_SUBC", ["placeholder18"], 1],
    ["Quest-RC_DW_HidingTinkerer", ["Driftwood: Strange Cargo - Complete"], 1],
    ["Quest-RC_DW_Dock_Kids", ["Driftwood: Hide & Seek - Complete"], 1],
    ["Quest-RC_DW_FishScholar", ["Driftwood: Grebb the Scholar - Complete"], 1],
    #["Quest-RC_DW_CaptiansGhost", ["placeholder22"], 1], notably not Drowning Her Sorrows, dosnt fire on act exit
    ["Quest-RC_DW_FishermanRing", ["Reaper's Bluffs: Lost and Found - Complete"], 1],
    #["Quest-RC_DW_Harmon", ["placeholder24"], 1], no idea, doest fire on act exit
    ["Quest-RC_DW_SpidersKiss", ["Driftwood - A Web of Desire - Complete"], 1],
    ["Quest-RC_DW_TheDrunkenSailor", ["Driftwood: Drowning Her Sorrows - Complete"], 1],
    ["Quest-RC_DW_Arena", ["Driftwood: The Driftwood Arena - Complete"], 1],
    ["Quest-RC_DW_SurpriseDate", ["Driftwood: Love Has a Price - Complete"], 1],
    #["Quest-RC_DW_MissingEquipment", ["placeholder29"], 1], no idea, doesnt fire on act exit
    ["Quest-RC_DW_VoidwokenChicks", ["Reaper's Coast: Counting your Chickens - Complete"], 1],
    ["Quest-RC_DW_DwarvenCriminals", ["Driftwood: The Law of the Order - Complete"], 1],
    ["Quest-RC_DW_DwarvenCriminals_SUB_RottenGoods", ["Driftwood: Fishy Business - Complete"], 1],
    ["Quest-RC_DW_Meistr", ["Lady Vengence: Powerful Awakening - Complete", "Victory_Leave_Reapers_Coast"], 1],
    ["Quest-RC_DW_Meistr_SUBA", ["Reaper's Bluffs: Mordus Awakens - Complete"], 1],
    ["Quest-RC_DW_Meistr_SUBB", ["Stonegarden: Waking Ryker - Complete"], 1],
    ["Quest-RC_DW_Meistr_SUBC", ["Cloisterwood: Jahan's Lesson - Complete"], 1],
    ["Quest-RC_DW_Meistr_SUBD", ["Cloisterwood: Hannag's Bargin - Complete"], 1],
    ["Quest-RC_DW_Meistr_SUBE", ["Bloodmoon Island: The Demon's Advocate - Complete"], 1],
    ["Quest-RC_DW_Meistr_SUBF", ["The Cullwoods: Saheila's Reward - Complete"], 1],
    ["Quest-RC_DW_Meistr_SUBG", ["Paradise Downs: Almira's Dowry - Complete"], 1],
    ["Quest-RC_OIL_Main", ["The Blackpits: The Midnight Oil - Complete"], 1],
    ["Quest-RC_DF_PolyLovers", ["Driftwood Fields: Treated Like Cattle - Complete"], 1],
    ["Quest-RC_DF_UndeadTrader", ["Cloisterwood: Eithne the Trader - Complete"], 1],
    ["Quest-RC_DF_TrollBridge", ["Cloisterwood: Business Rivals - Complete"], 1], #cant get both paths in one save, keeping the main and nothnig else
    #["Quest-RC_DF_TrollBridge_SUBA", ["placeholder45"], 1],
    #["Quest-RC_DF_TrollBridge_SUBB", ["placeholder46"], 1],
    ["Quest-RC_GY_RykersContract", ["Stonegarden: A Generous Offer - Complete"], 1],
    ["Quest-RC_GY_RykersSpider", ["Stonegarden: The Weaver - Complete"], 1],
    ["Quest-RC_GY_PurgedDaughter", ["Stonegarden: A Danger to Herself and Others - Complete"], 1],
    ["Quest-RC_GY_LizardSpeakingLizard", ["Stonegarden: Speaking In Forked Tongues - Complete"], 1],
    ["Quest-RC_GY_FavoritePet", ["Stonegarden: Popularity Contest - Complete"], 1],
    ["Quest-RC_GY_TurtleLove", ["Stonegarden: Opposites Attract - Complete"], 1],
    ["Quest-RC_GY_BuriedLizard", ["Stonegarden: Stranger in a Strange Land - Complete"], 1],
    ["Quest-RC_GY_MemorialOfHeroes", ["Stonegarden: Heroes' Rest - Complete"], 1],
    ["Quest-RC_GY_UglyBird", ["Driftwood Fields: The Ugly Little Bird - Complete"], 1],
    ["Quest-RC_GY_DeerGhost", ["Stonegarden: A Prize Kill - Complete"], 1],
    ["Quest-RC_GY_Godslayer", ["Stonegarden: All In The Family - Complete"], 1],
    ["Quest-RC_GY_WronglyBuried", ["Stonegarden: An Existential Crisis - Complete"], 1],
    ["Quest-RC_GY_KillRyker", ["Stonegarden: The Reluctant Servants - Complete"], 1],
    ["Quest-RC_DF_PaladinCheckpoint", ["Driftwood Fields: Dark Dealings in the Blackpits - Complete"], 1],
    ["Quest-RC_OIL_FourthHouse", ["The Blackpits: No Way Out - Complete"], 1],
    ["Quest-RC_FL_BrokenPromises", ["Paradise Downs: Unlikely Lovers - Complete"], 1],
    ["Quest-RC_FL_TabletForAlmira", ["Paradise Downs: Almira's Request - Complete"], 1],
    ["Quest-RC_BF_ThePresence", ["Cloisterwood: A Hunter of Wicked Things - Complete"], 1],
    #["Quest-RC_BI_TheTruth", ["placeholder65"], 1], #The Secrets of Bloodmoon Island? cant be completed till act 4 if so (nvm fires on act exit i have no idea what this is)
    ["Quest-RC_BI_TheVaults", ["Bloodmoon Island: The Forgotten and the Damned - Complete"], 1],
    ["Quest-RC_BI_TheVaults_SUBA", ["Bloodmoon Island: Delusions of Gradeur - Comeplete"], 1],
    ["Quest-RC_BI_TheVaults_SUBB", ["Bloodmoon Island: Silent as the Grave - Complete"], 1],
    ["Quest-RC_BI_TheVaults_SUBC", ["Bloodmoon Island: The Sweet Shackles of Pain - Complete"], 1], 
    #["Quest-RC_BI_TheVaults_SUBD", ["placeholder70"], 1], #Metalwork? never popped
    #["Quest-RC_BI_TheVaultGodwoken", ["placeholder71"], 1], none of them fired
    #["Quest-RC_BI_TheVaultKid", ["placeholder72"], 1],
    #["Quest-RC_BI_TheVaultAdventurer", ["placeholder73"], 1],
    ["Quest-RC_BI_Druid", ["Bloodmoon Island: The Druid - Complete"], 1],
    #["Quest-RC_MIL_War", ["placeholder75"], 1], no idea, doesnt fire on act exit
    ["Quest-RC_MIL_SyrusOates", ["The Cullwoods: The Stoic Spirit - Complete"], 1],
    ["Quest-RC_MIL_BlackWidowMaker", ["The Cullwoods: Bitter Tonic - Complete"], 1],
    ["Quest-RC_MIL_EdieEngrym", ["The Cullwoods: Old Flames - Complete"], 1],
    ["Quest-RC_MIL_Mudbarrow", ["The Cullwoods: No Laughing Matter - Complete"], 1],
    ["Quest-RC_MIL_SavingCorbin", ["The Cullwoods: Press-Ganged - Complete"], 1],
    ["Quest-RC_DW_SourceLich", ["Reaper's Bluffs: A Taste of Freedom - Complete"], 1],
    ["Quest-RC_BF_CorneredSourcerer", ["Cloisterwood: Window of Opportunity - Complete"], 1],
    ["Quest-RC_BI_ThePresence", ["Bloodmoon Island: The Advocate - Complete"], 1],
    ["Quest-FTJ_SaheilaFate", ["The Cullwoods: Saheila's People - Complete"], 1],
    ["Quest-RC_MIL_RescuingSaheila", ["The Cullwoods: The Elven Seer/Vengeance for the Fallen - Complete"], 1],
    ["Quest-RC_MIL_GhostRevenge", ["The Cullwoods: An Eye for an Eye - Complete"], 1],
    ["Quest-RC_MIL_SelenHead", ["The Cullwoods: Finder's Fee - Complete"], 1],
    ["Quest-RC_MIL_GhostLog", ["The Cullwoods: The Bark's Bite - Complete"], 1],
    #["Quest-DevourerArmour", ["A Hunger From Beyond - Complete"], 1], Cant be completed until act 4
    ["Quest-VultureArmour", ["Reaper's Bluffs: Keep Calm and Carrion - Complete"], 1],
    ["Quest-RC_DW_SnoozingAdventurer", ["Driftwood: The Snoozing Adventurer - Complete"], 1],
    ["Quest-RC_DW_RichMerchant", ["Driftwood: The Merchant - Complete"], 1],
    ["Quest-RC_DW_Beggar", ["Driftwood: A Man and His Dog - Complete"], 1],
    #["Quest-RC_FL_GarethFarm", ["placeholder93"], 1], #fires when killing jonathan in the first encounter with gareth, no where else in Burying the Past. Every other path doesnt fire until act exit, opting to omit this one
    #["Quest-RC_FL_GarethParents", ["placeholder94"], 1], #This is whatever the one is for killing voidwoken at gareths parents behest, obnoixously missable, probably wont include, doesn't fire on act exit either
    #["Quest-RC_MIL_ElvenBurial", ["placeholder95"], 1], Confident this is Burial Rites, no flag sent when completeing burial rites (fires on leaving reapers coast)
    #["Quest-RC_MIL_ElfTest", ["placeholder96"], 1], #fires on act exit, not a clue though
    ["Quest-RC_MIL_AvengingSaheila", ["The Cullwoods: The Elven Seer/Vengeance for the Fallen - Complete"], 1],
    ["Quest-RC_OIL_ThirdHouse", ["The Blackpits: On the Ropes - Complete"], 1],
    ["Quest-RC_DW_Meistr_SUBI", ["Driftwood: The Gift of the Blackroot - Complete"], 1],
] + DOS2_KILL_LIST

LOCATION_NAME_ID_REGION = [
    ["Merryweather: Death Belowdecks - Complete", 1, "Merryweather"],
    ["Merryweather: Troubled Waters - Complete", 2, "Merryweather"],
    ["Merryweather: Voidling 1", 3, "Merryweather"],
    ["Merryweather: Voidling 2", 4, "Merryweather"],
    ["Fort Joy: Voidling 1 (158, 325)", 5, "Fort Joy"],
    ["Fort Joy: Voidling 2 (157, 330)", 6, "Fort Joy"],
    ["Fort Joy: Freshly Buried Corpse (225, 287)", 7, "Fort Joy"],
    ["Fort Joy: Turtle 1 (258, 363)", 8, "Fort Joy"],
    ["Fort Joy: Ancient Turtle (271, 365)", 9, "Fort Joy"],
    ["Fort Joy: Turtle 2 (283, 349)", 10, "Fort Joy"],
    ["Fort Joy: Saltwater Crocodile 1 (113, 217)", 11, "Fort Joy"],
    ["Fort Joy: Saltwater Crocodile 2 (124, 224)", 12, "Fort Joy"],
    ["Fort Joy: Saltwater Crocodile 3 (116, 231)", 13, "Fort Joy"],
    ["Fort Joy: Charged Amphibian (528, 489)", 14, "Fort Joy"],
    ["Fort Joy: Venomous Amphibian 1 (503, 491)", 15, "Fort Joy"],
    ["Fort Joy: Venomous Amphibian 2 (518, 504)", 16, "Fort Joy"],
    ["Fort Joy: Gedeon, the Tenacious One (69, 562)", 17, "Fort Joy"],
    ["Fort Joy: Veerle, the Avid One (64, 566)", 18, "Fort Joy"],
    ["Fort Joy: Ailsa, the Cultured One (64, 559)", 19, "Fort Joy"],
    ["Fort Joy: Rex (72, 566)", 20, "Fort Joy"],
    ["Fort Joy: Magister Houndmaster (276, 654)", 21, "Fort Joy"],
    ["Fort Joy: Magister Swordsman 3 (276, 651)", 22, "Fort Joy"],
    ["Fort Joy: Magister Ranger 6 (280, 651)", 23, "Fort Joy"],
    ["Fort Joy: Magister Ranger 7 (279, 663)", 24, "Fort Joy"],
    ["Fort Joy: Kniles the Flenser (384, 630)", 27, "Fort Joy"],
    ["Fort Joy: Meat Golem 1 (389, 641)", 28, "Fort Joy"],
    ["Fort Joy: Meat Golem 2 (370, 639)", 29, "Fort Joy"],
    ["Fort Joy: Meat Golem 3 (389, 620)", 30, "Fort Joy"],
    ["Fort Joy: Agitated Silent Monk 1 (386, 651)", 31, "Fort Joy"],
    ["Fort Joy: Agitated Silent Monk 2 (389, 635)", 32, "Fort Joy"],
    ["Fort Joy: Agitated Silent Monk 3 (379, 614)", 33, "Fort Joy"],
    ["Fort Joy: Magister Ranger 1 (293, 197)", 34, "Fort Joy"],
    ["Fort Joy: Magister Swordsman 1 (258, 164)", 35, "Fort Joy"],
    ["Fort Joy: Magister Ranger 2 (302, 173)", 36, "Fort Joy"],
    ["Fort Joy: Magister Ranger 3 (262, 196)", 37, "Fort Joy"],
    ["Fort Joy: Magister Swordsman 2 (260, 198)", 38, "Fort Joy"],
    ["Fort Joy: Magister Captian Trippel (279, 196)", 40, "Fort Joy"],
    ["Fort Joy: Silent Monk 1 (328, 224)", 41, "Fort Joy"],
    ["Fort Joy: Silent Monk 2 (326, 224)", 42, "Fort Joy"],
    ["Fort Joy: Silent Monk 3 (323, 224)", 43, "Fort Joy"],
    ["Fort Joy: Silent Monk 4 (321, 224)", 44, "Fort Joy"],
    ["Fort Joy: Silent Monk 5 (331, 224)", 45, "Fort Joy"],
    ["Fort Joy: Magister Ranger 4 (324, 244)", 46, "Fort Joy"],
    ["Fort Joy: Magister Inquisitor (323 246)", 47, "Fort Joy"],
    ["Fort Joy: Magister Ranger 5 (322, 244)", 48, "Fort Joy"],
    ["Fort Joy: Magister Knight (333, 235)", 49, "Fort Joy"],
    ["Fort Joy: Magister Dayve (321, 225)", 50, "Fort Joy"],
    ["Fort Joy: Magister Courtroom Swordsman 1 (276, 139)", 51, "Fort Joy"],
    ["Fort Joy: Magister Courtroom Swordsman 2 (289, 139)", 52, "Fort Joy"],
    ["Fort Joy: High Judge Orivand (283, 129)", 53, "Fort Joy"],
    ["Fort Joy: Magister Cryomancer (280, 126)", 54, "Fort Joy"],
    ["Fort Joy: Magister Pyromancer (284, 126)", 55, "Fort Joy"],
    ["Fort Joy: Pyromancer Guardian (372, 577)", 56, "Fort Joy"],
    ["Fort Joy: Blademaster Guardian (385, 566)", 57, "Fort Joy"],
    ["Fort Joy: Cryomancer Guardian (390, 577)", 58, "Fort Joy"],
    ["Fort Joy: Aeromancer Guardian (371, 556)", 59, "Fort Joy"],
    ["Fort Joy: Blademaster Guardian (378, 565)", 60, "Fort Joy"],
    ["Fort Joy: Eagle-Eyed Guardian (379, 577)", 61, "Fort Joy"],
    ["Fort Joy: Traitorous Guardian (370, 550)", 62, "Fort Joy"],
    ["East Reaper's Eye: Windego (357, 192)", 63, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Assassin (379, 152)", 64, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Swashbuckler (386, 155)", 65, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Terramancer (389, 151)", 66, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Swashbuckler 2 (391, 206)", 67, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Markswoman (401, 213)", 68, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Marksman 1 (396, 216)", 69, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Swashbuckler 3 (395, 210)", 70, "East Reaper's Eye"],
    ["East Reaper's Eye: Viscous Voidling 1 (461, 105)", 71, "East Reaper's Eye"],
    ["East Reaper's Eye: Viscous Voidling 2 (443, 118)", 72, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling 3 (441, 98)", 73, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling 4 (464, 109)", 74, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling 5 (466, 115)", 75, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling 6 (451, 114)", 76, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling 7 (453, 92)", 77, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling 8 (447, 95)", 78, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling 9 (447, 120)", 79, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling 10 (454, 96)", 80, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling 11 (460, 114)", 81, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling 12 (440, 102)", 82, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling 13 (464, 106)", 83, "East Reaper's Eye"],
    ["East Reaper's Eye: Void Salamander (492, 94)", 84, "East Reaper's Eye"],
    ["East Reaper's Eye: Noxious Void Salamander (494, 86)", 85, "East Reaper's Eye"],
    ["East Reaper's Eye: Void Salamander (485, 82)", 86, "East Reaper's Eye"],
    ["East Reaper's Eye: Magister Inquisitor (471, 254)", 87, "East Reaper's Eye"],
    ["East Reaper's Eye: Magister Ranger 1 (469, 253)", 88, "East Reaper's Eye"],
    ["East Reaper's Eye: Magister Ranger 2 (464, 254)", 89, "East Reaper's Eye"],
    ["East Reaper's Eye: Magister Swordsman 1 (462, 254)", 90, "East Reaper's Eye"],
    ["East Reaper's Eye: Magister Knight (469, 230)", 91, "East Reaper's Eye"],
    ["East Reaper's Eye: Magister Ranger 3 (469, 228)", 92, "East Reaper's Eye"],
    ["East Reaper's Eye: Magister Swordsman 2 (460, 231)", 93, "East Reaper's Eye"],
    ["East Reaper's Eye: Magister Ranger 4 (460, 229)", 94, "East Reaper's Eye"],
    ["East Reaper's Eye: Incandescent Decapitator (529, 93)", 95, "East Reaper's Eye"],
    ["East Reaper's Eye: Incandescent Scorcher (539, 94)", 96, "East Reaper's Eye"],
    ["East Reaper's Eye: Incandescent Marksman (529, 100)", 97, "East Reaper's Eye"],
    ["East Reaper's Eye: Trompdoy (676, 487)", 98, "East Reaper's Eye"],
    ["East Reaper's Eye: Trompdoy (700, 497)", 99, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Aeromancer (494, 170)", 100, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Cryomancer (480, 159)", 101, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Swashbuckler 4 (481, 164)", 102, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Swashbuckler 5 (502, 167)", 103, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Marksman 1 (482, 175)", 104, "East Reaper's Eye"],
    ["East Reaper's Eye: Voidwoken Deep-dweller (499, 157)", 105, "East Reaper's Eye"],
    ["East Reaper's Eye: Radeka the Witch (691, 602)", 106, "East Reaper's Eye"],
    ["East Reaper's Eye: Carrion Beetle (697, 620)", 107, "East Reaper's Eye"],
    ["East Reaper's Eye: Carrion Beetle (690, 597)", 108, "East Reaper's Eye"],
    ["East Reaper's Eye: Carrion Beetle (679, 611)", 109, "East Reaper's Eye"],
    ["East Reaper's Eye: Bloody Corpse (687, 611)", 110, "East Reaper's Eye"],
    ["East Reaper's Eye: Bloody Corpse (694, 614)", 111, "East Reaper's Eye"],
    ["East Reaper's Eye: Bloody Corpse (689, 600)", 112, "East Reaper's Eye"],
    ["East Reaper's Eye: Undead Medat (693, 602)", 113, "East Reaper's Eye"],
    ["North-east Reaper's Eye: Magister Metamorph (552, 301)", 114, "North-east Reaper's Eye"],
    ["North-east Reaper's Eye: Magister Assassin (570, 299)", 115, "North-east Reaper's Eye"],
    ["North-east Reaper's Eye: Magister Markswoman (567, 309)", 116, "North-east Reaper's Eye"],
    ["North-east Reaper's Eye: Magister Knight (570, 304)", 117, "North-east Reaper's Eye"],
    ["North-east Reaper's Eye: Gheist (564, 306)", 118, "North-east Reaper's Eye"],
    ["North-east Reaper's Eye: Voidwoken Drillworm (594, 408)", 119, "North-east Reaper's Eye"],
    ["Fort Joy: Escape From Fort Joy - Complete", 120, "Fort Joy"],
    ["North-east Reaper's Eye: Escape From Reaper's Eye - Complete", 121, "North-east Reaper's Eye"],
    ["North-east Reaper's Eye: Talk to Malady - Complete", 122, "North-east Reaper's Eye"],
    #["placeholder4", 123, "Fort Joy"],
    #["placeholder5", 124, "Fort Joy"],
    ["East Reaper's Eye: The Voices - Complete", 125, "East Reaper's Eye"],
    #["placeholder7", 126, "Fort Joy"],
    #["placeholder8", 127, "Fort Joy"],
    #["placeholder9", 128, "Fort Joy"],
    ["Fort Joy: The Imprisioned Elf - Complete", 129, "Fort Joy"],
    ["Fort Joy: The Murderous Gheist - Complete", 130, "Fort Joy"],
    ["Fort Joy: Finding Emmie - Complete", 131, "Fort Joy"],
    ["Fort Joy: The Arena of Fort Joy - Complete", 132, "Fort Joy"],
    ["Fort Joy: Withermoore's Soul Jar - Complete", 133, "Fort Joy"],
    #["placeholder15", 134, "Fort Joy"],
    #["placeholder16", 135, "Fort Joy"],
    ["Fort Joy: The Teleporter - Complete", 136, "Fort Joy"],
    ["Fort Joy: The Shakedown - Complete", 137, "Fort Joy"],
    ["East Reaper's Eye: The Vault of Braccus Rex - Complete", 138, "East Reaper's Eye"],
    ["East Reaper's Eye: Healing Touch - Complete/Most Dangerous When Cornered", 139, "East Reaper's Eye"],
    #["placeholder21", 140, "Fort Joy"],
    ["East Reaper's Eye: A Fate Worse Than Death - Complete", 141, "East Reaper's Eye"],
    ["East Reaper's Eye: The Armoury - Complete", 142, "East Reaper's Eye"],
    ["East Reaper's Eye: The Cursed Ring - Complete", 143, "East Reaper's Eye"],
    ["East Reaper's Eye: The Gargoyle's Maze - Complete", 144, "East Reaper's Eye"],
    ["East Reaper's Eye: The Burning Pigs - Complete", 145, "East Reaper's Eye"],
    ["East Reaper's Eye: The Purged Dragon - Complete", 146, "East Reaper's Eye"],
    ["East Reaper's Eye: Call to Arms - Complete", 147, "East Reaper's Eye"],
    ["East Reaper's Eye: The Shreikers - Complete", 148, "East Reaper's Eye"],
    ["North-east Reaper's Eye: Artefacts of the Tyrant - Complete", 149, "North-east Reaper's Eye"],
    #["placeholder31", 150, "Fort Joy"],
    #["placeholder32", 151, "Fort Joy"],
    ["North-east Reaper's Eye: Threads of a Curse - Complete", 152, "North-east Reaper's Eye"],
    ["North-east Reaper's Eye: Bishop Alexander (564, 306)", 153, "North-east Reaper's Eye"],
    #-- Act 2 --
    ["Lady Vengence: Lady o' War - Complete", 154, "Lady Vengence"],
    ["Lady Vengence: To The Hall of Echoes - Complete", 155, "Lady Vengence"],
    ["Reaper's Coast: The Wrecked Caravan - Complete", 156, "Reaper's Coast"],
    ["Reaper's Coast: They Shall Not Pass - Complete", 157, "Reaper's Coast"],
    #["placeholder3", 158, "Reaper's Coast"],
    #["placeholder4", 159, "Reaper's Coast"],
    ["Driftwood: Shadow Over Driftwood - Complete", 160, "Driftwood"],
    ["Reaper's Bluffs: The Burning Prophet - Complete", 161, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Wishful Thinking - Complete", 162, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Aggressive Takeover - Complete", 163, "Reaper's Bluffs"],
    #["Driftwood Fields: The Three Altars - Complete", 164, "Driftwood Fields"],
    ["Driftwood: Red Ink in the Ledger - Complete", 165, "Driftwood"],
    #["placeholder11", 166, "Reaper's Coast"],
    #["placeholder12", 167, "Reaper's Coast"],
    #["placeholder13", 168, "Reaper's Coast"],
    #["placeholer14", 169, "Driftwood"],
    ["Driftwood: The Missing Magisters - Complete", 170, "Driftwood"],
    #["placeholder16", 171, "Reaper's Coast"],
    #["placeholder17", 172, "Reaper's Coast"],
    #["placeholder18", 173, "Reaper's Coast"],
    ["Driftwood: Strange Cargo - Complete", 174, "Driftwood"],
    ["Driftwood: Hide & Seek - Complete", 175, "Driftwood"],
    ["Driftwood: Grebb the Scholar - Complete", 176, "Driftwood"],
    #["placeholder22", 177, "Driftwood"],
    ["Reaper's Bluffs: Lost and Found - Complete", 178, "Reaper's Bluffs"],
    #["placeholder24", 179, "Reaper's Coast"],
    ["Driftwood - A Web of Desire - Complete", 180, "Driftwood"],
    ["Driftwood: Drowning Her Sorrows - Complete", 181, "Driftwood"],
    ["Driftwood: The Driftwood Arena - Complete", 182, "Driftwood"],
    ["Driftwood: Love Has a Price - Complete", 183, "Driftwood"],
    #["placeholder29", 184, "Reaper's Coast"],
    ["Reaper's Coast: Counting your Chickens - Complete", 185, "Reaper's Coast"],
    ["Driftwood: The Law of the Order - Complete", 186, "Driftwood"],
    ["Driftwood: Fishy Business - Complete", 187, "Driftwood"],
    ["Lady Vengence: Powerful Awakening - Complete", 188, "Lady Vengence"],
    ["Reaper's Bluffs: Mordus Awakens - Complete", 189, "Reaper's Bluffs"],
    ["Stonegarden: Waking Ryker - Complete", 190, "Stonegarden"],
    ["Cloisterwood: Jahan's Lesson - Complete", 191, "Cloisterwood"],
    ["Cloisterwood: Hannag's Bargin - Complete", 192, "Cloisterwood"],
    ["Bloodmoon Island: The Demon's Advocate - Complete", 193, "Bloodmoon Island"],
    ["The Cullwoods: Saheila's Reward - Complete", 194, "The Cullwoods"],
    ["Paradise Downs: Almira's Dowry - Complete", 195, "Paradise Downs"],
    ["The Blackpits: The Midnight Oil - Complete", 196, "The Blackpits"],
    ["Driftwood Fields: Treated Like Cattle - Complete", 197, "Driftwood Fields"],
    ["Cloisterwood: Eithne the Trader - Complete", 198, "Cloisterwood"],
    ["Cloisterwood: Business Rivals - Complete", 199, "Cloisterwood"],
    #["placeholder45", 200, "Reaper's Coast"],
    #["placeholder46", 201, "Reaper's Coast"],
    ["Stonegarden: A Generous Offer - Complete", 202, "Stonegarden"],
    ["Stonegarden: The Weaver - Complete", 203, "Stonegarden"],
    ["Stonegarden: A Danger to Herself and Others - Complete", 204, "Stonegarden"],
    ["Stonegarden: Speaking In Forked Tongues - Complete", 205, "Stonegarden"],
    ["Stonegarden: Popularity Contest - Complete", 206, "Stonegarden"],
    ["Stonegarden: Opposites Attract - Complete", 207, "Stonegarden"],
    ["Stonegarden: Stranger in a Strange Land - Complete", 208, "Stonegarden"],
    ["Stonegarden: Heroes' Rest - Complete", 209, "Stonegarden"],
    ["Driftwood Fields: The Ugly Little Bird - Complete", 210, "Driftwood Fields"],
    ["Stonegarden: A Prize Kill - Complete", 211, "Stonegarden"],
    ["Stonegarden: All In The Family - Complete", 212, "Stonegarden"],
    ["Stonegarden: An Existential Crisis - Complete", 213, "Stonegarden"],
    ["Stonegarden: The Reluctant Servants - Complete", 214, "Stonegarden"],
    ["Driftwood Fields: Dark Dealings in the Blackpits - Complete", 215, "Driftwood Fields"],
    ["The Blackpits: No Way Out - Complete", 216, "The Blackpits"],
    ["Paradise Downs: Unlikely Lovers - Complete", 217, "Paradise Downs"],
    ["Paradise Downs: Almira's Request - Complete", 218, "Paradise Downs"],
    ["Cloisterwood: A Hunter of Wicked Things - Complete", 219, "Cloisterwood"],
    #["placeholder65", 220, "Reaper's Coast"],
    ["Bloodmoon Island: The Forgotten and the Damned - Complete", 221, "Bloodmoon Island"],
    ["Bloodmoon Island: Delusions of Gradeur - Comeplete", 222, "Bloodmoon Island"],
    ["Bloodmoon Island: Silent as the Grave - Complete", 223, "Bloodmoon Island"],
    ["Bloodmoon Island: The Sweet Shackles of Pain - Complete", 224, "Bloodmoon Island"],
    #["placeholder70", 225, "Reaper's Coast"],
    #["placeholder71", 226, "Reaper's Coast"],
    #["placeholder72", 227, "Reaper's Coast"],
    #["placeholder73", 228, "Reaper's Coast"],
    ["Bloodmoon Island: The Druid - Complete", 229, "Bloodmoon Island"],
    #["placeholder75", 230, "Reaper's Coast"],
    ["The Cullwoods: The Stoic Spirit - Complete", 231, "The Cullwoods"],
    ["The Cullwoods: Bitter Tonic - Complete", 232, "The Cullwoods"],
    ["The Cullwoods: Old Flames - Complete", 233, "The Cullwoods"],
    ["The Cullwoods: No Laughing Matter - Complete", 234, "The Cullwoods"],
    ["The Cullwoods: Press-Ganged - Complete", 235, "The Cullwoods"],
    ["Reaper's Bluffs: A Taste of Freedom - Complete", 236, "Reaper's Bluffs"],
    ["Cloisterwood: Window of Opportunity - Complete", 237, "Cloisterwood"],
    ["Bloodmoon Island: The Advocate - Complete", 238, "Bloodmoon Island"],
    ["The Cullwoods: Saheila's People - Complete", 239, "The Cullwoods"],
    ["The Cullwoods: The Elven Seer/Vengeance for the Fallen - Complete", 240, "The Cullwoods"],
    ["The Cullwoods: An Eye for an Eye - Complete", 241, "The Cullwoods"],
    ["The Cullwoods: Finder's Fee - Complete", 242, "The Cullwoods"],
    ["The Cullwoods: The Bark's Bite - Complete", 243, "The Cullwoods"],
    #["placeholderDA", 244, "Driftwood"],
    ["Reaper's Bluffs: Keep Calm and Carrion - Complete", 245, "Reaper's Bluffs"],
    ["Driftwood: The Snoozing Adventurer - Complete", 246, "Driftwood"],
    ["Driftwood: The Merchant - Complete", 247, "Driftwood"],
    ["Driftwood: A Man and His Dog - Complete", 248, "Driftwood"],
    #["placeholder93", 249, "Driftwood"],
    #["placeholder94", 250, "Driftwood"],
    #["placeholder95", 251, "Driftwood"],
    #["placeholder96", 252, "Driftwood"],
    ["The Blackpits: On the Ropes - Complete", 254, "The Blackpits"],
    ["Driftwood: The Gift of the Blackroot - Complete", 255, "Driftwood"],
]

LOCATION_NAME_TO_ID = {item[0]: item[1] for item in LOCATION_NAME_ID_REGION}

DOS2_LOCATION_TO_AP_LOCATIONS = {item[0]: item[1] for item in DOS2_LOCATION_LIST}

class DOS2Location(Location):
    game = "Divinity Original Sin 2"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: DOS2World) -> None:
    create_regular_locations(world)

def create_regular_locations(world: DOS2World) -> None:
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
    driftwoodFields = world.get_region("Driftwood Fields")
    theCullwoods = world.get_region("The Cullwoods")
    paradiseDowns = world.get_region("Paradise Downs")
    bloodmoonIsland = world.get_region("Bloodmoon Island")

    merryweatherLocationNames = []
    for loc in LOCATION_NAME_ID_REGION:
        if(loc[2] == "Merryweather"):
            merryweatherLocationNames.append(loc[0])
    merryweatherLocations = get_location_names_with_ids(merryweatherLocationNames)
    merryweather.add_locations(merryweatherLocations, DOS2Location)

    fortJoyLocationNames = []
    for loc in LOCATION_NAME_ID_REGION:
        if(loc[2] == "Fort Joy"):
            fortJoyLocationNames.append(loc[0])
    fortJoyLocations = get_location_names_with_ids(fortJoyLocationNames)
    fortJoy.add_locations(fortJoyLocations, DOS2Location)

    eastReapersEyeLocationNames = []
    for loc in LOCATION_NAME_ID_REGION:
        if(loc[2] == "East Reaper's Eye"):
            eastReapersEyeLocationNames.append(loc[0])
    eastReapersEyeLocations = get_location_names_with_ids(eastReapersEyeLocationNames)
    eastReapersEye.add_locations(eastReapersEyeLocations, DOS2Location)
    
    finalReapersEyeLocationNames = []
    for loc in LOCATION_NAME_ID_REGION:
        if(loc[2] == "North-east Reaper's Eye"):
            finalReapersEyeLocationNames.append(loc[0])
    finalReapersEyeLocations = get_location_names_with_ids(finalReapersEyeLocationNames)
    finalReapersEye.add_locations(finalReapersEyeLocations, DOS2Location)

    if(world.options.goal != world.options.goal.option_escape_reapers_eye):
        ladyVengenceLocationNames = []
        for loc in LOCATION_NAME_ID_REGION:
            if(loc[2] == "Lady Vengence"):
                ladyVengenceLocationNames.append(loc[0])
        ladyVengenceLocations = get_location_names_with_ids(ladyVengenceLocationNames)
        ladyVengence.add_locations(ladyVengenceLocations, DOS2Location)

        reapersCoastLocationNames = []
        for loc in LOCATION_NAME_ID_REGION:
            if(loc[2] == "Reaper's Coast"):
                reapersCoastLocationNames.append(loc[0])
        reapersCoastLocations = get_location_names_with_ids(reapersCoastLocationNames)
        reapersCoast.add_locations(reapersCoastLocations, DOS2Location)

        stonegardenLocationNames = []
        for loc in LOCATION_NAME_ID_REGION:
            if(loc[2] == "Stonegarden"):
                stonegardenLocationNames.append(loc[0])
        stonegardenLocations = get_location_names_with_ids(stonegardenLocationNames)
        stonegarden.add_locations(stonegardenLocations, DOS2Location)

        theBlackpitsLocationNames = []
        for loc in LOCATION_NAME_ID_REGION:
            if(loc[2] == "The Blackpits"):
                theBlackpitsLocationNames.append(loc[0])
        theBlackpitsLocations = get_location_names_with_ids(theBlackpitsLocationNames)
        theBlackpits.add_locations(theBlackpitsLocations, DOS2Location)

        driftwoodLocationNames = []
        for loc in LOCATION_NAME_ID_REGION:
            if(loc[2] == "Driftwood"):
                driftwoodLocationNames.append(loc[0])
        driftwoodLocations = get_location_names_with_ids(driftwoodLocationNames)
        driftwood.add_locations(driftwoodLocations, DOS2Location)

        reapersBluffsLocationNames = []
        for loc in LOCATION_NAME_ID_REGION:
            if(loc[2] == "Reaper's Bluffs"):
                reapersBluffsLocationNames.append(loc[0])
        reapersBluffsLocations = get_location_names_with_ids(reapersBluffsLocationNames)
        reapersBluffs.add_locations(reapersBluffsLocations, DOS2Location)

        cloisterwoodLocationNames = []
        for loc in LOCATION_NAME_ID_REGION:
            if(loc[2] == "Cloisterwood"):
                cloisterwoodLocationNames.append(loc[0])
        cloisterwoodLocations = get_location_names_with_ids(cloisterwoodLocationNames)
        cloisterwood.add_locations(cloisterwoodLocations, DOS2Location)

        driftwoodFieldsLocationNames = []
        for loc in LOCATION_NAME_ID_REGION:
            if(loc[2] == "Driftwood Fields"):
                driftwoodFieldsLocationNames.append(loc[0])
        driftwoodFieldsLocations = get_location_names_with_ids(driftwoodFieldsLocationNames)
        driftwoodFields.add_locations(driftwoodFieldsLocations, DOS2Location)

        theCullwoodsLocationNames = []
        for loc in LOCATION_NAME_ID_REGION:
            if(loc[2] == "The Cullwoods"):
                theCullwoodsLocationNames.append(loc[0])
        theCullwoodsLocations = get_location_names_with_ids(theCullwoodsLocationNames)
        theCullwoods.add_locations(theCullwoodsLocations, DOS2Location)

        paradiseDownsLocationNames = []
        for loc in LOCATION_NAME_ID_REGION:
            if(loc[2] == "Paradise Downs"):
                paradiseDownsLocationNames.append(loc[0])
        paradiseDownsLocations = get_location_names_with_ids(paradiseDownsLocationNames)
        paradiseDowns.add_locations(paradiseDownsLocations, DOS2Location)

        bloodmoonIslandLocationNames = []
        for loc in LOCATION_NAME_ID_REGION:
            if(loc[2] == "Bloodmoon Island"):
                bloodmoonIslandLocationNames.append(loc[0])
        bloodmoonIslandLocations = get_location_names_with_ids(bloodmoonIslandLocationNames)
        bloodmoonIsland.add_locations(bloodmoonIslandLocations, DOS2Location)



    if(world.options.goal == world.options.goal.option_escape_reapers_eye):
        finalReapersEye.add_event("Victory_Escape_Reapers_Eye", "Victory", location_type = DOS2Location, item_type = Items.DOS2Item)
    elif(world.options.goal == world.options.goal.option_leave_reapers_coast):
        ladyVengence.add_event("Victory_Leave_Reapers_Coast", "Victory", location_type = DOS2Location, item_type = Items.DOS2Item)