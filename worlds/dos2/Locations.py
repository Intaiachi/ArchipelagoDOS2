from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import Items

if TYPE_CHECKING:
    from .World import DOS2World

#A lot of the FTJ ones came from @chaotic and @JeyKey09, thank you!
DOS2_KILL_LIST = [
    # --- merryweather ---
    ["S_TUT_TopDeckVoidling10_bd0123ae-26fd-4dad-8326-b6ae9a3fc1c5", ["Merryweather: Voidling (27, 16)"], 0],
    ["S_TUT_TopDeckVoidling11_2fcb5b84-875f-42bd-ac80-6f8495c6a47c", ["Merryweather: Voidling (28, 18)"], 0],
    # --- fort joy ---
    #beach voidlings
    ["S_FTJ_BeachVw_001_08348b3a-bded-4811-92ce-f127aa4310e0", ["Fort Joy: Voidling (158, 325)"], 0],
    ["S_FTJ_BeachVw_002_1832a661-0e21-421f-acaa-a7e66e813b14", ["Fort Joy: Voidling (157, 330)"], 0],
    #dirt mound zombie //not confident on this one
    ["S_FTJ_DirtMoundZombie_eb499ae9-21df-41e9-9d89-968a88ceb3ad", ["Fort Joy: Freshly Buried Corpse (225, 287)"], 0],
    #beach turtles
    ["S_FTJ_SpikedTurtle_01_abd3afae-a6e5-452c-a94a-db57826dd082", ["Fort Joy: Turtle (258, 363)"], 0],
    ["S_FTJ_SpikedTurtle_03_fb4618f9-9c61-4640-a32c-e4735783e878", ["Fort Joy: Ancient Turtle (271, 365)"], 0],
    ["S_FTJ_SpikedTurtle_04_f37cb16e-027e-4a21-8504-d6cab12d9098", ["Fort Joy: Turtle (283, 349)"], 0],
    #teleport crocs
    ["S_FTJ_TeleporteQuestrCroc_001_bc1a10a1-51b6-42c5-b517-827565f6512b", ["Fort Joy: Saltwater Crocodile 1 (113, 217)"], 0],
    ["S_FTJ_TeleporteQuestrCroc_002_6be95689-ab8f-4edf-ba46-77a068594a19", ["Fort Joy: Saltwater Crocodile 2 (124, 224)"], 0],
    ["S_FTJ_TeleporteQuestrCroc_003_7cf7d4d4-de1a-4ac7-999a-1f128fac3789", ["Fort Joy: Saltwater Crocodile 3 (116, 231)"], 0],
    #frogs
    ["S_FTJ_FrogAmbush_Melee_01_747af1e4-d204-4564-9a50-9f1955dd4723", ["Fort Joy: Charged Amphibian (528, 489)"], 0],
    ["S_FTJ_FrogAmbush_Ranged_02_ffae5e44-ac8a-4f43-ab14-2e684b60d87b", ["Fort Joy: Venomous Amphibian (503, 491)"], 0],
    ["S_FTJ_FrogAmbush_Ranged_03_18d2b17c-a400-4e1d-991f-d1cbb44cfac4", ["Fort Joy: Venomous Amphibian (518, 504)"], 0],
    #arena of the one 
    ["S_FTJ_Arena_Gladiator_001_51a8d141-c7df-4d56-8d28-ca403033ca16", ["Fort Joy: Gedeon, the Tenacious One (69, 562)"], 0],
    ["S_FTJ_Arena_Gladiator_002_31fcfd4c-1417-4ac8-8817-1dfb8a5b8e7b", ["Fort Joy: Veerle, the Avid One (64, 566)"], 0],
    ["S_FTJ_Arena_Gladiator_003_b81cb546-05b1-404c-ae00-d76a0702bb86", ["Fort Joy: Ailsa, the Cultured One (64, 559)"], 0],
    ["S_FTJ_Arena_Gladiator_004_d2a430fc-8f01-4962-b455-93f883c287d0", ["Fort Joy: Rex (72, 566)"], 0],
    #holding cell
    ["S_FTJ_OlgoCellarMagister_001_402470db-ad49-4de7-8a60-7f69c8e5d26e", ["Fort Joy: Magister Houndmaster (276, 654)"], 0],
    ["S_FTJ_OlgoCellarMagister_002_6d6b84bf-e940-4c28-a2b6-12516d049792", ["Fort Joy: Magister Swordsman (276, 651)"], 0],
    ["S_FTJ_OlgoCellarMagister_003_e8c14f56-b34a-41c3-adb3-dda318c5bdc1", ["Fort Joy: Magister Ranger (280, 651)"], 0],
    ["S_FTJ_OlgoCellarMagister_004_2955b578-1a8e-4ecd-aa7f-5f084c428e25", ["Fort Joy: Magister Ranger (279, 663)"], 0],
    #prison
    ["S_FTJ_MagisterTorturer_1d1c0ba0-a91e-4927-af79-6d8d27e0646b", ["Fort Joy: Kniles the Flenser (384, 630)"], 0],
    ["S_FTJ_Torturer_Golem_01_584db8ce-8dcf-4906-bc6f-e51eb057de08", ["Fort Joy: Meat Golem (389, 641)"], 0],
    ["S_FTJ_Torturer_Golem_02_aff8be39-58b0-4bff-8fa6-7cf501b5060b", ["Fort Joy: Meat Golem (370, 639)"], 0],
    ["S_FTJ_Torturer_Golem_03_d32d32b2-c05b-4acd-944c-f2b802ec7234", ["Fort Joy: Meat Golem (389, 620)"], 0],
    ["S_FTJ_SilentMonk_002_01343cec-09ab-48eb-9226-ce6b2880a6c0", ["Fort Joy: Agitated Silent Monk (386, 651)"], 0],
    ["S_FTJ_SilentMonk_004_652ac6e3-9778-42d3-81d1-35d88ffb2e8d", ["Fort Joy: Agitated Silent Monk (389, 635)"], 0],
    ["S_FTJ_SilentMonk_010_aa03733a-861f-4814-8bf8-ba0c1cabb876", ["Fort Joy: Agitated Silent Monk (379, 614)"], 0],
    #magisters in fort
    ["S_FTJ_ChapelMagister_001_068d4518-9b23-4e2c-a160-8d978d1f78ff", ["Fort Joy: Magister Ranger (293, 197)"], 0],
    ["S_FTJ_ChapelMagister_002_090d7104-97f7-4603-a114-47dceaf021e5", ["Fort Joy: Magister Swordsman (258, 164)"], 0],
    ["S_FTJ_ChapelMagister_003_b5cb12b2-f347-4415-95ac-8d5ac4fc464b", ["Fort Joy: Magister Ranger (302, 173)"], 0],
    ["S_FTJ_ChapelMagister_004_8f330be0-a442-408f-850e-c7fd94e74ada", ["Fort Joy: Magister Ranger (262, 196)"], 0],
    ["S_FTJ_ChapelMagister_005_d5ea5e99-2406-4bb9-b2df-5fd975f1b63e", ["Fort Joy: Magister Swordsman (260, 198)"], 0],
    ["S_FTJ_ChapelMagister_Captain_c4d751d4-20ff-4281-baf4-8ddeb1383e7e", ["Fort Joy: Magister Captian Trippel (279, 196)"], 0],
    #harbor near fort
    ["S_FTJ_HarbourSilentMonk_001_f7bd3244-e1e7-4079-ac95-fef6145a236e", ["Fort Joy: Silent Monk (328, 224)"], 0],
    ["S_FTJ_HarbourSilentMonk_002_54b9a81b-7926-46b1-ad0d-6213c0d77749", ["Fort Joy: Silent Monk (326, 224)"], 0],
    ["S_FTJ_HarbourSilentMonk_003_61bf204e-ba2e-412f-ac86-e132a3930105", ["Fort Joy: Silent Monk (323, 224)"], 0],
    ["S_FTJ_HarbourSilentMonk_004_753d80ce-a515-43e3-8085-8ceacb3ceb4f", ["Fort Joy: Silent Monk (321, 224)"], 0],
    ["S_FTJ_HarbourSilentMonk_005_4149080d-9cc5-424d-a8fc-c52222bb463a", ["Fort Joy: Silent Monk (331, 224)"], 0],
    ["S_FTJ_HarbourMagister_001_d6a4e8d9-67bc-4961-95ce-c7016357ea64", ["Fort Joy: Magister Ranger (324, 244)"], 0],
    ["S_FTJ_HarbourMagister_002_14581b6d-9423-4e2c-8d19-8f1b222ab760", ["Fort Joy: Magister Inquisitor (323 246)"], 0],
    ["S_FTJ_HarbourMagister_003_75ffb9bd-5ddb-4c2c-8ad0-55c00b34be7b", ["Fort Joy: Magister Ranger (322, 244)"], 0],
    ["S_FTJ_HarbourMagister_004_97492757-bbe8-42d8-af6d-35ca0ae96d36", ["Fort Joy: Magister Knight (333, 235)"], 0],
    ["S_FTJ_HarbourMagister_005_55c5c79e-2260-40bd-ab1d-c2d05fe31d45", ["Fort Joy: Magister Dayve (321, 225)"], 0],
    #court room
    ["S_FTJ_CourtRoomGuard_001_c51d581d-9245-431f-a1eb-88adc8149827", ["Fort Joy: Magister Courtroom Swordsman (276, 139)"], 0],
    ["S_FTJ_CourtRoomGuard_002_bb9fd6c4-4231-44ac-a24d-5955dc300147", ["Fort Joy: Magister Courtroom Swordsman (289, 139)"], 0],
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
    ["S_GLO_Windego_d783285f-d3be-4cba-8333-db8976cef182", ["East Reaper's Eye: Windego (357, 192)"], 0], #kill list candidate
    #swamp
    ["S_FTJ_SwampBuildup_A_Undead_Assassin_a54a04a3-8507-4a37-a8b6-068fd0ec8146", ["East Reaper's Eye: Decomposing Assassin (379, 152)"], 0],
    ["S_FTJ_SwampBuildup_A_Undead_Melee_01_8b70b76c-24f8-4b3c-aae8-3c78c93ab2bb", ["East Reaper's Eye: Decomposing Swashbuckler (386, 155)"], 0],
    ["S_FTJ_SwampBuildup_A_Undead_Terra_01_7dee6a3d-ef4f-4281-a311-a65d483e13d1", ["East Reaper's Eye: Decomposing Terramancer (389, 151)"], 0],
    ["S_FTJ_SwampBuildup_B_Undead_Melee_01_e45ec44b-4033-4994-b6a4-f236dea40561", ["East Reaper's Eye: Decomposing Swashbuckler (391, 206)"], 0],
    ["S_FTJ_SwampBuildup_B_Undead_Ranger_01_1195a59b-ba51-4662-afa7-7602b224cfc8", ["East Reaper's Eye: Decomposing Markswoman (401, 213)"], 0],
    ["S_FTJ_SwampBuildup_B_Undead_Ranger_02_5468e7d7-8f83-4245-94fc-7303c11612b5", ["East Reaper's Eye: Decomposing Marksman (396, 216)"], 0],
    ["S_FTJ_SwampBuildup_B_Undead_Sword_9ee2fb19-5483-42a5-9037-c8147e9695fd", ["East Reaper's Eye: Decomposing Swashbuckler (395, 210)"], 0],
    #ambush
    ["S_FTJ_VoidlingAmbush_000_d61a5845-383b-4759-9fe3-99f519dec4dc", ["East Reaper's Eye: Viscous Voidling (461, 105)"], 0],
    ["S_FTJ_VoidlingAmbush_001_eedb56aa-aad1-4de2-8097-3fd7241be1ec", ["East Reaper's Eye: Viscous Voidling (443, 118)"], 0], 
    ["S_FTJ_VoidlingAmbush_002_a8318c72-e603-4a08-b01d-09232110bccc", ["East Reaper's Eye: Viscous Voidling (441, 98)"], 0], 
    ["S_FTJ_VoidlingAmbush_003_53680e8b-a4ee-4b00-9419-3860e91e76e6", ["East Reaper's Eye: Viscous Voidling (464, 109)"], 0], 
    ["S_FTJ_VoidlingAmbush_004_3fe3a69c-97b6-42d5-b1db-bc646a66ab15", ["East Reaper's Eye: Viscous Voidling (466, 115)"], 0], 
    ["S_FTJ_VoidlingAmbush_005_03ed2bcc-3b3b-4e9c-bfd1-54c7f6a1bcaa", ["East Reaper's Eye: Viscous Voidling (451, 114)"], 0], 
    ["S_FTJ_VoidlingAmbush_006_0cf5424e-2183-4c52-980e-de156c31f5e4", ["East Reaper's Eye: Viscous Voidling (453, 92)"], 0], 
    ["S_FTJ_VoidlingAmbush_007_1aa2f181-c36b-4e9e-ae5e-9652fe038824", ["East Reaper's Eye: Viscous Voidling (447, 95)"], 0], 
    ["S_FTJ_VoidlingAmbush_008_8c83992f-328d-405d-bebd-0f5461d027ad", ["East Reaper's Eye: Viscous Voidling (447, 120)"], 0], 
    ["S_FTJ_VoidlingAmbush_009_811f904d-4822-463c-b77e-d658a0fb3380", ["East Reaper's Eye: Viscous Voidling (454, 96)"], 0], 
    ["S_FTJ_VoidlingAmbush_010_7dfba778-1b94-4cf7-8b26-663dfcb760d3", ["East Reaper's Eye: Viscous Voidling (460, 114)"], 0], 
    ["S_FTJ_VoidlingAmbush_011_a01a4838-c65a-452e-bde5-dc7b8e3dca27", ["East Reaper's Eye: Viscous Voidling (440, 102)"], 0], 
    ["S_FTJ_VoidlingAmbush_012_360a68c3-e5f1-4834-aa9e-7dc7497d9301", ["East Reaper's Eye: Viscous Voidling (464, 106)"], 0],
    #salamander
    ["S_FTJ_SW_ShelterBackSalamander1_26d2a05f-bd32-408c-adab-c01767271bbf", ["East Reaper's Eye: Void Salamander (492, 94)"], 0],
    ["S_FTJ_SW_ShelterBackSalamander2_e3812c55-7530-4d74-b79b-e8f3c91558a4", ["East Reaper's Eye: Noxious Void Salamander (494, 86)"], 0],
    ["S_FTJ_SW_ShelterBackSalamander3_62ac9493-260e-40bf-a615-5cdf475208d9", ["East Reaper's Eye: Void Salamander (485, 82)"], 0],
    #saving Gareth fight
    ["S_FTJ_CorneringMagister1_324e8aca-3b0b-430e-b8bb-2f6e9edac3fe", ["East Reaper's Eye: Magister Inquisitor (471, 254)"], 0],
    ["S_FTJ_CorneringMagister2_f278b94b-78ac-4cd7-9d8a-1c61e673ead3", ["East Reaper's Eye: Magister Ranger (469, 253)"], 0],
    ["S_FTJ_CorneringMagister3_34996c94-6294-45e7-9659-f6fce2a95ea5", ["East Reaper's Eye: Magister Ranger (464, 254)"], 0],
    ["S_FTJ_CorneringMagister4_96f35d8a-d38a-4fc1-9b23-bdf4349a16ec", ["East Reaper's Eye: Magister Swordsman (462, 254)"], 0],
    ["S_FTJ_OutsideMagister1_51825365-42fd-4b0c-9f35-d21ae40833a3", ["East Reaper's Eye: Magister Knight (469, 230)"], 0],
    ["S_FTJ_OutsideMagister2_d3091599-a583-44b8-8ce7-3b7e9d88fdaa", ["East Reaper's Eye: Magister Ranger (469, 228)"], 0],
    ["S_FTJ_OutsideMagister3_d584fdbb-1cfa-46d4-add2-5587eafd3e29", ["East Reaper's Eye: Magister Swordsman (460, 231)"], 0],
    ["S_FTJ_OutsideMagister4_0a2cf9d4-6631-44c3-aea4-cc5a13f3419b", ["East Reaper's Eye: Magister Ranger (460, 229)"], 0],
    #skeleton near tower //these might not work
    ["S_FTJ_SW_BurningSkeleton1_0b0d054f-aba2-4fac-b89b-473f59cb085e", ["East Reaper's Eye: Incandescent Decapitator (529, 93)"], 0],
    ["S_FTJ_SW_BurningSkeleton2_11e95a85-9877-403f-944e-16b2c4e9a4b3", ["East Reaper's Eye: Incandescent Scorcher (539, 94)"], 0],
    ["S_FTJ_SW_BurningSkeleton3_d53d04be-e7d7-4b37-8b93-2807921fb58a", ["East Reaper's Eye: Incandescent Marksman (529, 100)"], 0],
    #trompdoy
    #["S_FTJ_SW_IllusionistAtEntrance_e01c3723-872a-454d-a59b-d798b21183cd", ["East Reaper's Eye: Trompdoy (676, 487)"], 0], #these arent even the hostile one why did i add these
    #["S_FTJ_SW_IllusionistFinal_1a3b44d4-0ba4-4289-b158-a54111b83e1d", ["East Reaper's Eye: Trompdoy (700, 497)"], 0],
    ["S_FTJ_SW_ChestRoomIllusionist_001_d656548b-329c-4ce4-ae61-984feb732503", ["East Reaper's Eye: Trompdoy (629, 496)"], 0],
    ["S_FTJ_SW_ChestRoomIllusionist_002_0e5779db-8418-4be9-9fdf-7f52c38b67bc", ["East Reaper's Eye: Trompdoy (631, 482)"], 0],
    ["S_FTJ_SW_ChestRoomIllusionist_003_f5b0ab9f-f99e-4360-b455-a2f7043349a8", ["East Reaper's Eye: Trompdoy (643, 496)"], 0],
    ["S_FTJ_TrueIllusionist_a3b10150-1871-48a4-9d64-f51c84316b6d", ["East Reaper's Eye: Trompdoy (669, 538)"], 0],
    #deep dweller and friends //migth not work
    ["S_FTJ_SW_VWBoss_Mage_01_5cf41c21-bfed-499e-a6fe-6eda7c24b118", ["East Reaper's Eye: Decomposing Aeromancer (494, 170)"], 0],
    ["S_FTJ_SW_VWBoss_Mage_02_2f619e60-5cfc-4323-a094-e285ea922903", ["East Reaper's Eye: Decomposing Cryomancer (480, 159)"], 0],
    ["S_FTJ_SW_VWBoss_Melee_01_961c827b-43d1-43c8-8553-6d1d4c8e8aed", ["East Reaper's Eye: Decomposing Swashbuckler (481, 164)"], 0],
    ["S_FTJ_SW_VWBoss_Melee_02_8644ff57-7eb3-4ed7-a496-00e977227b53", ["East Reaper's Eye: Decomposing Swashbuckler (502, 167)"], 0],
    ["S_FTJ_SW_VWBoss_Ranger_01_e8ad5533-b8f0-4c55-a261-4192f5cf1e48", ["East Reaper's Eye: Decomposing Marksman (482, 175)"], 0],
    ["S_FTJ_SW_VWBoss_VoidWoken_112f8c17-ea77-4658-ac72-239154772fb8", ["East Reaper's Eye: Voidwoken Deep-dweller (499, 157)"], 0], #kill list candidate
    #witch
    ["S_FTJ_SW_Witch_4014aee0-56f1-47e0-a8eb-89c4b5a1da83", ["East Reaper's Eye: Radeka the Witch (691, 602)"], 0], #kill list candidate
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
    ["S_GLO_Alexandar_03e6345f-1bd3-403c-80e2-a443a74f6349", ["North-east Reaper's Eye: Bishop Alexander (564, 306)"], 0], #kill list candidate
    #seed of power boat
    ["CON01_MagisterPriest_c1c1f470-5786-4297-8a89-38fe2a3348a7 attackerOwner", ["Fort Joy: Magister Ellwin (337, 359)"], 0],
    ["CON01_Magister_Leader_d0db4856-e955-44b4-af73-0e16beecf90b", ["Fort Joy: Magister Krendt (340, 361)"], 0],
    ["CON01_MagisterWarrior_df34380d-030b-4d57-a5e5-855c88b714ab attackerOwner", ["Fort Joy: Magister Swentin (340, 365)"], 0],
    ["CON01_SourceHound1_93c3bd2d-5106-4a16-bb63-8641dd7cdcb3 attackerOwner", ["Fort Joy: Source Hound Phyllip (332, 367)"], 0],
    #-- Reaper's Coast --
    ["S_RC_DU_Abduction_Combat1_04d4d854-8474-4c32-887e-43f395508392", ["Reaper's Coast: Viscous Voidling (423, -4)"], 1],
    ["S_RC_DU_Abduction_Combat2_bede8cbd-a5c9-4bd0-9e48-43f3b41d5a32", ["Reaper's Coast: Viscous Voidling (407, 1)"], 1],
    ["S_RC_DU_Abduction_Combat3_eae4231d-28cc-4c99-833d-6e6680a48675", ["Reaper's Coast: Viscous Voidling (408, -2)"], 1],
    ["S_RC_DU_Abduction_Combat4_87ba9148-d75e-4d31-a872-ca4fb6e8b6dd", ["Reaper's Coast: Viscous Voidling (423, -8)"], 1],
    ["S_RC_DU_Abduction_Combat5_9c6d0ca3-42e0-4ff9-a60d-6a396103149d", ["Reaper's Coast: Volatile Voidling (425, -6)"], 1],
    ["S_RC_DU_Abduction_Combat6_555176fb-7adf-4b60-8549-8cedf209073b", ["Reaper's Coast: Volatile Voidling (408, 0)"], 1],
    #siva guards
    ["S_RC_DW_MeistrGuard_SilentMonk_01_b4e39447-8186-4917-9cfa-766b825d3b13", ["Reaper's Coast: Silent Watcher (442, 151)"], 1],
    ["S_RC_DW_MeistrGuard_8a8a83dd-de7b-42aa-8ab9-d4fc1e878126", ["Reaper's Coast: Executioner Ninyan (438, 148)"], 1],
    #eggs
    ["S_RC_DW_VC_EggThiefVoidwoken_059fbb9c-0967-481c-a732-faacf13ab9a6", ["Reaper's Coast: Venom-Wing Voidwoken (461, 157)"], 1],
    #fish factory (these deserve a test too)
    ["S_RC_DW_FishFactory_Creep_01_e1eaf78a-a444-46f3-bac7-3353771192f8", ["Driftwood: Viscous Voidling (222, 611)"], 1],
    ["S_RC_DW_FishFactory_Creep_02_ef4f8f41-fcfe-4f77-be03-95846b82c8f4", ["Driftwood: Viscous Voidling (226, 612)"], 1],
    ["S_RC_DW_FishFactory_Creep_03_8348b9b4-82fe-4214-9251-02a926f025de", ["Driftwood: Viscous Voidling (221, 614)"], 1],
    ["S_RC_DW_FishFactory_Creep_01_Explosive_43b4c6a1-7d91-4bfe-87ad-0a4f903a420a", ["Driftwood: Volatile Voidling (227, 616)"], 1],
    ["S_RC_DW_FishFactory_Creep_02_Explosive_3772d2f7-fc28-4a48-8716-5c4e22989cae", ["Driftwood: Volatile Voidling (230, 614)"], 1],
    ["S_RC_DW_FishFactory_Creep_03_Explosive_d645dacb-6626-407e-81a8-ffca5cd65891", ["Driftwood: Volatile Voidling (223, 618)"], 1],
    ["S_RC_DW_FishFactory_Creep_04_Explosive_103d4aa2-e618-477e-8dda-3eba5c5f6264", ["Driftwood: Volatile Voidling (227, 609)"], 1],
    ["S_RC_DW_FishFactory_Creep_05_Explosive_75280a26-a7ba-41ec-8f05-0366b7310b34", ["Driftwood: Volatile Voidling (211, 609)"], 1],
    ["S_RC_DW_FishFactory_Creep_06_Explosive_0555501d-2132-44bd-8f50-2e03e0d4461c", ["Driftwood: Volatile Voidling (212, 617)"], 1],
    ["S_RC_DW_FishFactory_Creep_07_Explosive_f082fa9c-5837-4a09-9261-55be773e6670", ["Driftwood: Volatile Voidling (217, 598)"], 1],
    ["S_RC_DW_FishFactory_Creep_08_Explosive_c4f98683-7a38-40e2-9feb-7b630dce47b6", ["Driftwood: Volatile Voidling (235, 608)"], 1],
    ["S_RC_DW_FishFactory_Creep_09_Explosive_e90c5400-6e58-402c-8dc6-1c03f6f4bcf8", ["Driftwood: Volatile Voidling (236, 614)"], 1],
    ["S_RC_DW_FishFactory_Creep_10_Explosive_72f273ae-eef2-4294-93bb-e9f388be8cd1", ["Driftwood: Volatile Voidling (235, 603)"], 1],
    #arena
    ["S_RC_DW_ArenaTrial_Archer_a2766c17-61de-4089-9fc7-f1bbe4234c7f", ["Driftwood: Jeroen, the Mindful One (414, 861)"], 1],
    ["S_RC_DW_ArenaTrial_Tank_6200751e-b592-406f-a184-c163b395e7f1", ["Driftwood: Kenna, the Persistent One (417, 863)"], 1],
    ["S_RC_DW_ArenaTrial_Knight_6bb27978-0e50-45f6-bf4a-d4bad1c26730", ["Driftwood: Jada, the Rash One (415, 862)"], 1],
    ["S_RC_DW_ArenaTrial_Mage_a2b1c3f5-857c-40c0-a93f-584afee6866e", ["Driftwood: Layali, the Wily One (412, 861)"], 1],
    ["S_RC_DW_ArenaTrial_Rogue_d6fad21f-2d32-4269-a599-625acc568bb4", ["Driftwood: Amr, the Veiled One (411, 861)"], 1],
    ["RC_DW_Tavern_ArenaChamp_InArena_aa7f67da-aece-4487-83cf-96f10a018ed1", ["Driftwood: Murga (420, 862)"], 1],
    ["S_RC_DW_UnderTavern_Voidwoken_13bb467b-de20-4726-8afd-757705352361", ["Driftwood: Captive Deep-Dweller (413, 855)"], 1],
    #lich
    ["S_RC_DW_SourceLich_adf5b715-1e96-4e48-88a7-d68a5b6d0351", ["Driftwood: Dessicated Undead (490, 828)"], 1], #kill list candidate
    ["S_RC_DW_LichGuards_1_bd4a02c1-cfa5-40d9-82ab-b49a8fa34bd8", ["Driftwood: Skeletal Hailcaster (496, 812)"], 1],
    ["S_RC_DW_LichGuards_2_25f65683-0e7f-495a-baca-01bd5e2a589f", ["Driftwood: Skeletal Flameweaver (499, 842)"], 1],
    ["S_RC_DW_LichGuards_3_75858ba9-e7d0-42df-93a2-97626dd982b5", ["Driftwood: Skeletal Graverobber (483, 826)"], 1],
    ["S_RC_DW_LichGuards_4_d2047c21-749a-4273-bb8f-a9832eb350b0", ["Driftwood: Skeletal Stormbinder (513, 831)"], 1],
    ["S_RC_DW_LichGuards_5_87508e7a-19a5-4093-a1f6-24be400faa0a", ["Driftwood: Skeletal Skullcrusher (496, 835)"], 1],
    #fishermans ring
    ["S_RC_DW_RingVoidwoken_02_e7ee6c94-eaa1-4d7c-86a3-f1224ee2d5d5", ["Reaper's Bluffs: Slippery Voidling (245, 50)"], 1],
    ["S_RC_DW_RingVoidwoken_03_65c457b5-9842-49a3-b177-bf6d125cc84c", ["Reaper's Bluffs: Slippery Voidling (246, 67)"], 1],
    ["S_RC_DW_RingVoidwoken_04_ae5bf582-3eb9-47a2-af35-858e5a22f9fe", ["Reaper's Bluffs: Slippery Voidling (243, 48)"], 1],
    ["S_RC_DW_RingVoidwoken_05_e88b7dce-d88c-48a0-b584-410b8c4a3f48", ["Reaper's Bluffs: Slippery Voidling (248, 69)"], 1],
    ["S_RC_DW_RingVoidwoken_06_cb9ed186-97aa-47d3-9de0-bba4ceef5363", ["Reaper's Bluffs: Slippery Voidling (247, 62)"], 1],
    ["S_RC_DW_RingVoidwoken_01_28cab511-8239-4d94-b0ec-84ad7ae3a46d", ["Reaper's Bluffs: Voidwoken Deep-Dweller (249, 57)"], 1],
    #bluffs ambushes
    ["RC_WH_Ambush01_DwarfRanger_6fe51a7e-7a70-4151-9f0b-b1d21ffd9dc1", ["Reaper's Bluffs: Possessed Marksman (186, 108)"], 1],
    ["S_RC_WH_Ambush01_DwarfCaster_ade0ee22-8fb7-422b-9c32-978a1f5f79ca", ["Reaper's Bluffs: Possessed Elementalist (207, 95)"], 1],
    ["S_RC_WH_Ambush02_DwarfSummoner_01_7c63431f-4a27-4e63-acfe-f24f23745b52", ["Reaper's Bluffs: Possessed Summoner (161, 72)"], 1],
    ["S_RC_WH_Ambush02_DwarfCaster_01_516967c7-315b-499d-8779-255482b3106e", ["Reaper's Bluffs: Possessed Elementalist (171, 77)"], 1],
    ["S_RC_WH_Ambush02_DwarfRanger_01_d8103bb4-79b5-4b2a-a5df-2681261acfc6", ["Reaper's Bluffs: Possessed Markswoman (165, 50)"], 1],
    ["S_RC_WH_Ambush02_DwarfSummoner_02_cc677d58-8ec6-4046-8d3d-d03bdb620e09", ["Reaper's Bluffs: Possessed Summoner (162, 47)"], 1],
    #outside wreckers cave
    ["RC_WH_RuinsCliff_DwarfWarrior_c66d98b2-c033-4e78-9414-536e323f1b03", ["Reaper's Bluffs: Possessed Warmaiden (111, 107)"], 1],
    ["RC_WH_RuinsCliff_DwarfHealer_a6a8dab1-70a3-41b5-b982-f9da92003bac", ["Reaper's Bluffs: Possessed Cleric (118, 121)"], 1],
    ["RC_WH_RuinsCliff_DwarfBattleMage_16e9c979-5936-49f4-9dcd-b68ba562c968", ["Reaper's Bluffs: Possessed Battlemage (109, 118)"], 1],
    ["RC_WH_RuinsCliff_DwarfRanger_01_39a11236-cfc6-493d-98a6-b1f3dc42fd18", ["Reaper's Bluffs: Possessed Arbalist (113, 132)"], 1],
    ["RC_WH_RuinsCliff_DwarfRanger_02_4a7b6122-3e3d-4cd8-ac46-e4551c2d1dfe", ["Reaper's Bluffs: Possessed Arbalist (119, 125)"], 1],
    ["RC_WH_RuinsCliff_Voidwoken_91852d6c-07ca-4244-b2b4-6001de35054c", ["Reaper's Bluffs: Venom-Wing Voidwoken (113, 112)"], 1],
    #wreckers cave (every enemy in the mordus boss is technically missable as killng mordus first despawns the ads, and letting mordus transform or live makes mordus missable. The eggs are also missable once they hatch)
    #mordus potential kill list candidate, i feel like having the goal to kill him and missing him is the players fault at that point. he transforms back when defeated to converse so kill list should still be fine
    ["S_Hive_Guardian_Bat_01_0819d46d-a3ce-4214-8c42-f4d20c76d01b", ["Reaper's Bluffs: Vampiric Voidwoken (722, 671)"], 1],
    ["S_Hive_Guardian_Bat_02_1af2c6b2-9479-43d8-8938-cf7019202d65", ["Reaper's Bluffs: Vampiric Voidwoken (743, 655)"], 1],
    ["S_Hive_Guardian_InsectW_01_c19ac6db-960d-496b-bcb9-2f16e521134c", ["Reaper's Bluffs: Storm-Wing Voidwoken (724, 685)"], 1],
    ["RC_WC_Corridor_Voidwoken_01_23ef85fb-e5a1-4631-8e91-1f2587f3e791", ["Reaper's Bluffs: Vampiric Voidwoken (702, 676)"], 1],
    ["S_RC_DW_WC_IndivFight_Voidwoken_001_8dd20fd8-f410-4791-8805-f2a4ef1fae8c", ["Reaper's Bluffs: Cold-crawler Voidwoken (647, 607)"], 1],
    ["S_RC_DW_WC_IndivFight_Voidwoken_003_1fa986d6-0e4e-41a9-b34b-b007d70fea72", ["Reaper's Bluffs: Cold-crawler Voidwoken (659, 656)"], 1],
    ["S_RC_DW_WC_BarrelChamber_PossessedDwarf_000_f40e9760-f9aa-43bc-8f3a-e8106599a9e5", ["Reaper's Bluffs: Possessed Rogue (672, 687)"], 1],
    ["S_RC_DW_WC_BarrelChamber_PossessedDwarf_001_579d36bf-8118-4548-bdc7-687f5aa3e3f1", ["Reaper's Bluffs: Possessed Elementalist (674, 684)"], 1],
    ["S_RC_DW_WC_IndivFight_Voidwoken_002_a67141bb-8f48-4b41-99ea-67af7627d123", ["Reaper's Bluffs: Cold-crawler Voidwoken (717, 597)"], 1],
    ["S_RC_WC_PossessedDwarf_01_a6ebba9d-2b70-4f04-b0d0-56d7581548d6", ["Reaper's Bluffs: Possessed Markswoman (738, 553)"], 1],
    ["S_RC_WC_PossessedDwarf_02_3b1417dc-b796-4b38-975e-4c3f33baf5c6", ["Reaper's Bluffs: Possessed Elementalist (725, 552)"], 1],
    ["S_RC_DW_WC_IndivFight_Voidwoken_004_46bab1fd-001d-411e-a2c3-677051da2dc1", ["Reaper's Bluffs: Cold-crawler Voidwoken (656, 533)"], 1],
    ["S_RC_WC_MordusOffice_Shark_cd9732b8-f89a-4326-af93-d28d7a8435aa", ["Reaper's Bluffs: Shark (77, 782)"], 1],
    #cloisterwood (hannag and the magisters are missable depending on how Window of Opportunity goes)
    #hannag is also a kill list candidate for the same reason mordus is
    #["S_RC_BF_CorneredSourcerer_Sourcerer_b201a72c-8ead-4bbf-8612-fcd8c0944e52", ["Cloisterwood: Hannag (201, 259)"], 1], #kill list exclusive
    ["S_RC_BF_Altar_Wolf_Black_000_d3f23369-9e96-47f8-bf1c-4b2307537552", ["Cloisterwood: Old Gray Wolf (127, 273)"], 1],
    ["S_RC_BF_Altar_Wolf_Black_001_0d22cb95-db90-4678-b6c7-ce528ed672d1", ["Cloisterwood: Black Wolf (110, 273)"], 1],
    ["S_RC_BF_Altar_Wolf_Black_002_8a34ce03-d69f-46d9-aa6b-b8d31b022d6a", ["Cloisterwood: Black Wolf (129, 267)"], 1],
    ["S_RC_BF_Altar_Wolf_Black_003_3f7d0a8e-be6b-4259-9d98-95b3dc29c7a0", ["Cloisterwood: Black Wolf (116, 276)"], 1],
    ["S_RC_BF_Altar_Wolf_Black_004_0fea5dc4-2b31-426c-adbf-f1eaaf4ef588", ["Cloisterwood: Black Wolf (122, 262)"], 1],
    ["S_RC_BF_Altar_Werewolf_000_8fe2d805-39b6-42ad-a5ef-bc0b9d647466", ["Cloisterwood: Lamenting Abomination (112, 267)"], 1], #kill list candidate
    ["S_RC_BF_PolyServants_BurningWitch_73ffd67d-1536-41eb-b96d-be3c03515913", ["Cloisterwood: Alice Alisceon (221, 316)"], 1], #kill list candidate
    #the meadows
    ["S_RC_DF_Scarecrow_000_88c4581e-30c9-4dc7-a7a8-eec8244e7531", ["The Meadows: Enchanted Scarecrow (394, 211)"], 1],
    ["S_RC_DF_Scarecrow_001_6091c03c-1ca2-474b-8f24-9cb0a1fa0b2c", ["The Meadows: Enchanted Scarecrow (399, 217)"], 1],
    ["S_RC_DF_Scarecrow_002_8721af9f-91c3-4b4f-a232-a021f96725c1", ["The Meadows: Enchanted Scarecrow (418, 194)"], 1],
    ["S_RC_DF_Scarecrow_003_3493ef82-7bf6-45fb-a320-87e1466d83c9", ["The Meadows: Enchanted Scarecrow (416, 206)"], 1],
    ["S_RC_DF_Scarecrow_3bda7938-578f-49fc-a655-50b1b24db065", ["The Meadows: Restless Scarecrow (413, 199)"], 1],
    #paladin bridge
    ["S_RC_DF_PaladinAttack_Undead_Warrior_63d19461-87fc-4117-9fa8-8ee938f8c14f", ["The Meadows: Shadowcloak Skullcrusher (468, 233)"], 1],
    ["S_RC_DF_PaladinAttack_Undead_Rogue_1_c0e247d0-0664-470b-8aaf-91cb1f9abdc0", ["The Meadows: Shadowcloak Heartpiercer (484, 227)"], 1],
    ["S_RC_DF_PaladinAttack_Undead_Ranger_1_122afb13-2502-48e0-ad94-490712a818b6", ["The Meadows: Shadowcloak Deadeye (490, 230)"], 1],
    ["S_RC_DF_PaladinAttack_Undead_Ranger_2_8109e13d-90b4-400e-896d-d36bebf720ef", ["The Meadows: Shadowcloak Deadeye (464, 216)"], 1],
    ["S_RC_DF_PaladinAttack_Undead_Caster_1_e16b848c-9b2e-4e66-9dca-d4cc406b6df8", ["The Meadows: Shadowcloak Spellweaver (475, 238)"], 1],
    ["S_RC_DF_PaladinAttack_Undead_Caster_2_525996fb-0242-4896-9f55-ff848b5a22ab", ["The Meadows: Shadowcloak Spellweaver (492, 216)"], 1],
    #the cullwoods
    ["S_RC_MIL_Altar_Deer_Void_000_7cce0a94-e072-4f19-9c04-0eaf2cdd1358", ["The Cullwoods: Void-touched Deer (489, 261)"], 1],
    ["S_RC_MIL_ElfSkeletonSummer_c8b5ffdb-9ec2-4af1-b887-83d0e7c8a443", ["The Cullwoods: Challenger of Summer (448, 346)"], 1],
    ["S_RC_MIL_ElfSkeletonSpring_ec8cfcb5-5504-4d03-b643-9d4865a62599", ["The Cullwoods: Challenger of Spring (454, 340)"], 1],
    ["S_RC_MIL_ElfSkeletonWinter_377a0093-0f41-49ca-a3e0-b9c671f23ed7", ["The Cullwoods: Challenger of Winter (447, 335)"], 1],
    ["S_RC_MIL_ElfSkeletonAutumn_5af0a2d5-427c-4b14-9d23-b9d7438f49ed", ["The Cullwoods: Challenger of Autumn (441, 340)"], 1],
    #mill
    ["S_RC_MIL_RoostWolf1_a1e74099-ea1d-4a93-b841-78ea1af31cc5", ["The Cullwoods: Lady (139, 751)"], 1],
    ["S_RC_MIL_RoostWolf2_eb2ddf7e-bd6a-4f79-bb52-3a09a5011639", ["The Cullwoods: Lord (145, 751)"], 1],
    ["S_RC_MIL_Roost_6fffadfe-b2a8-4e12-a664-ba84c0b0a3a3", ["The Cullwoods: Roost Anlon (141, 748)"], 1],
    ["S_RC_MIL_RoostGuard1_d5b28c37-16d0-43cb-bbb4-b67e77905b95", ["The Cullwoods: Bodyguard (139, 743)"], 1],
    ["S_RC_MIL_RoostGuard2_4edaa723-4a39-4fde-b141-86437550db44", ["The Cullwoods: Shadow (145, 743)"], 1],
    ["S_RC_MIL_Sharpshooter1_31fc7260-d0d9-4290-a2b1-fcd23c431d61", ["The Cullwoods: Deadeye (517, 415)"], 1],
    ["S_RC_MIL_GuardWolf1_dd6de19c-bcce-40d3-b4ce-522a735e4fee", ["The Cullwoods: Pigsbane (507, 412)"], 1],
    ["S_RC_MIL_GuardWolf2_c55778a5-fa1f-484d-86d2-dc625d51ca59", ["The Cullwoods: Naptooth (511, 412)"], 1],
    ["S_RC_MIL_Sharpshooter2_a0f76bb6-2935-44fd-a66f-13198a10260d", ["The Cullwoods: Firewater (503, 415)"], 1],
    ["S_RC_MIL_LoneWolfF_cecf1eb8-1ff8-425f-8859-91482edb9eb6", ["The Cullwoods: Honeyhook (508, 447)"], 1],
    ["S_RC_MIL_LoneWolf2_49413cc0-7439-48c8-b5fc-375794243b7f", ["The Cullwoods: Slumberjack (478, 442)"], 1],
    ["S_RC_MIL_LizardWolf_3e69ef2b-3fa8-4e26-8117-2fec05c4d9a9", ["The Cullwoods: Snakeroot (504, 447)"], 1],
    ["S_RC_MIL_DwarfWolfM_9e42d7db-c8d3-4ef3-889b-99f78f95d715", ["The Cullwoods: Elixir Mixer (486, 463)"], 1],
    ["S_RC_MIL_DwarfWolf_18352a24-4b55-4fa5-ba9f-e6d347336d6e", ["The Cullwoods: Mummie Dearest (478, 427)"], 1],
    #paradise down
    #house
    ["S_RC_FL_ShatteredHouse_Alchemist_85327fc2-2e11-4bbc-89df-0fa931d7927a", ["Paradise Downs: Alchemist Looter (604, 375)"], 1],
    ["S_RC_FL_ShatteredHouse_Rogue_fa31e18c-89a5-477c-b35b-6637d3eb2dab", ["Paradise Downs: Assassin Looter (600, 379)"], 1],
    ["S_RC_FL_ShatteredHouse_Archer_8a4080d6-5f92-4ec7-9bef-05ab4500b9ab", ["Paradise Downs: Crossbowman Looter (599, 396)"], 1],
    ["S_RC_FL_ShatteredHouse_Chef_4890000e-78cc-42b8-b571-7ab7ed93f70c", ["Paradise Downs: Chief Looter (604, 396)"], 1],
    #harbinger of doom
    ["S_RC_FL_AlanBoss_ef0adba7-2471-4972-9feb-ceb4c7547141", ["Paradise Downs: Harbinger of Doom (679, 437)"], 1], #kill list candidate
    ["S_RC_FL_AlanBoss_NPC_01_143d8d41-883e-4498-bc77-1b21954043c2", ["Paradise Downs: Dead Magister Knight (675, 437)"], 1],
    ["S_RC_FL_AlanBoss_NPC_02_d4befb98-3743-4d61-a84a-e5f7014cd410", ["Paradise Downs: Dead Magister Swordsman (678, 439)"], 1],
    ["S_RC_FL_AlanBoss_NPC_03_b3c6b4b8-266e-44ac-b2b6-f842eb21129a", ["Paradise Downs: Dead Magister Knight (676, 432)"], 1],
    ["S_RC_FL_AlanBoss_NPC_04_2bc702d4-4b39-41db-a033-eced5d793a13", ["Paradise Downs: Dead Magister Inquisitor (674, 434)"], 1],
    #elders
    ["S_RC_FL_Lowlands_SkeletonSummoner_4b019f90-e955-4edc-bab0-028e9b16ad46", ["Paradise Downs: Elder of Passing (608, 289)"], 1],
    ["S_RC_FL_Lowlands_SkeletonFire_6b3890b5-cd75-40d6-9b40-18051f8269d7", ["Paradise Downs: Elder of Enkindling (624, 305)"], 1],
    ["S_RC_FL_Lowlands_SkeletonHealer_beb1b0e9-2366-49b6-88c6-654c07662059", ["Paradise Downs: Elder of Mending (616, 302)"], 1],
    #healers house all of them are missable
    #blackpits most of the magister fights are missable, as not engaging will lead to all of them despawning sans 3 in the entrance to the cave, which are also missable
    #The gate guards arent exactly hostile either so its hard to include them too.
    #Johnathan is always missable as he can die without credit in Burying the Past
    #This area is a mess, as most of these fights you really have to intentionally ingore yet I feel like I can't include them in good faith
    #I feel like I can include them thanks to saves too, I'm conflicted
    #I will include the fight after saving gwydian as that is a lucritive one and gague feelings about this
    #I have decieded to include these assuming often saves making this not that bad to go back to
    ["S_RC_OIL_InnerField_Magister_4_acb7ad5c-fe9b-4926-8130-19d37bf19ab2", ["The Blackpits: Magister Knight (714, 88)"], 1],
    ["S_RC_OIL_InnerField_Magister_6_5694bda3-9413-4e02-b6ec-81f028748995", ["The Blackpits: Magister Ranger (711, 110)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W1_Small_01_699862de-3a17-40b5-8b62-d6bbef9d4089", ["The Blackpits: Oil Voidling (719, 72)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W1_Small_02_0127579c-4174-405b-a403-bdf9538aa024", ["The Blackpits: Oil Voidling (729, 113)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W1_Small_03_32ffd555-6170-49f3-9fb9-03aa029c9369", ["The Blackpits: Oil Voidling (710, 122)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W1_Small_04_7276c7a1-989e-42b9-98dd-1c307028b0d6", ["The Blackpits: Oil Voidling (705, 82)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W1_Small_05_ab1f6cf8-c59b-4147-9f36-2aaf75041e9e", ["The Blackpits: Oil Voidling (692, 86)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W1_Small_06_eafe0006-98c0-4e0e-a4aa-153120c56d86", ["The Blackpits: Oil Voidling (694, 109)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W2_Big_01_4492ae99-8a12-4cf6-ae53-49175b4e03e8", ["The Blackpits: Primordial Oil Voidling (731, 115)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W2_Big_02_16da4ed3-d78e-48fa-bf55-0e07aa54b75c", ["The Blackpits: Primordial Oil Voidling (693, 113)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W2_Small_01_326b9a26-bfb0-41aa-b845-abcb747cd148", ["The Blackpits: Oil Voidling (699, 80)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W2_Small_02_dc215b13-f604-4fd4-b7f7-65b0c6ead331", ["The Blackpits: Oil Voidling (731, 110)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W2_Small_03_e3080aef-4223-4e83-b70c-967af23a7814", ["The Blackpits: Oil Voidling (729, 117)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W2_Small_04_073bcb4b-d891-4531-9fa2-12de0de44d41", ["The Blackpits: Oil Voidling (692, 110)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W2_Small_05_0fc9d760-6848-46a3-b779-74eb4baf1771", ["The Blackpits: Oil Voidling (694, 85)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W2_Small_06_53bc85af-19ed-41fc-8fb6-cee3f19f9537", ["The Blackpits: Oil Voidling (717, 72)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W3_FireBig_01_50d7ff90-8423-448c-a33b-4159eaccb693", ["The Blackpits: Primordial Fire Voidling (731, 112)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W3_FireBig_02_22a1608a-3d5c-4eb6-b5c6-3d08d11a5522", ["The Blackpits: Primordial Fire Voidling (695, 106)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W3_Fire_01_373ee6a6-0ed7-4029-8235-7442398a1b73", ["The Blackpits: Fire Voidling (692, 107)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W3_Fire_02_87e02e0f-ab15-42da-9ef0-a6b39b8965b0", ["The Blackpits: Fire Voidling (702, 79)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W3_Fire_03_f719095f-f4cc-41d4-8246-d18bd4e3d8f0", ["The Blackpits: Fire Voidling (695, 111)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W3_Fire_04_4ced02df-5aff-4dfb-bd8d-72b5e797d27b", ["The Blackpits: Fire Voidling (718, 73)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W3_Fire_05_9dcbb70d-b193-4baf-bc27-637af86f55f6", ["The Blackpits: Fire Voidling (733, 111)"], 1],
    ["S_RC_OIL_VoidwokenAttack_VW_W3_Fire_06_a5623263-a308-4cac-8af0-17e011947621", ["The Blackpits: Fire Voidling (729, 111)"], 1],
    #first voidwoken
    ["S_RC_OIL_FirstHouse_Magister_1_4ff391b4-d899-47d5-b794-3cbfd8d6dd6c", ["The Blackpits: Magister Ranger (724, 229)"], 1], #missable
    ["S_RC_OIL_FirstHouse_Magister_2_4c8b850c-f7d5-43c1-a0e3-1eaaec83316f", ["The Blackpits: Magister Axeman (731, 238)"], 1], #missable
    ["S_RC_OIL_FirstHouse_Creep_1_63228783-4d87-4cee-a5cf-c26ea92d0e96", ["The Blackpits: Void-touched Boar (725, 233)"], 1],
    ["S_RC_OIL_FirstHouse_Creep_2_ec9c8959-1e51-4121-bcc1-464cc57a3346", ["The Blackpits: Venom-Wing-Voidwoken (717, 236)"], 1],
    ["S_RC_OIL_FirstHouse_Creep_3_d960b7d7-08ee-4c44-aff1-fae865bb229b", ["The Blackpits: Void-touched Boar (729, 235)"], 1],
    ["S_RC_OIL_FirstHouse_Creep_4_5d111bc8-988e-4018-a654-14462773db2d", ["The Blackpits: Venom-Wing-Voidwoken (725, 244)"], 1],
    #third house all missable
    ["S_RC_OIL_ThirdHouse_Magister1_5d2a2f6a-6cbf-45cc-8c74-3a1617778ba3", ["The Blackpits: Magister Executioner (679, 173)"], 1],
    ["S_RC_OIL_ThirdHouse_Magister2_55a6a526-7d4b-4445-b96e-bfcd0ed71776", ["The Blackpits: Magister Inquisitor (679, 176)"], 1],
    ["S_RC_OIL_SilentWatcher_Ranger_1adcb57b-4eaa-415e-80cd-0750e1b00120", ["The Blackpits: Silent Watcher (685, 176)"], 1],
    ["S_RC_OIL_SilentWatcher_Mage_c2600226-7154-4033-889a-2d1509b2654a", ["The Blackpits: Silent Watcher (683, 169)"], 1],
    #fourth house all missable
    ["S_RC_OIL_FourthHouse_Magister_1_24f3611e-549b-407f-b952-fcfb682e8cb7", ["The Blackpits: Magister Assassin (653, 142)"], 1],
    ["S_RC_OIL_FourthHouse_Magister_2_65038967-e128-477f-bcac-0e6748e3ae5a", ["The Blackpits: Magister Inquisitor (653, 146)"], 1],
    ["S_RC_OIL_FourthHouse_Magister_3_2252e1cf-7333-4fb2-9872-e75c32e2b462", ["The Blackpits: Magister Ranger (653, 144)"], 1],
    #gate guards
    ["S_RC_OIL_InnerField_Magister_1_f4d44f84-fb56-40b3-91f9-3be60584eab3", ["The Blackpits: Magister Grimes (679, 126)"], 1],
    ["S_RC_OIL_InnerField_Magister_2_0d0b738a-6db2-47e3-9d71-c79d9fba7c1f", ["The Blackpits: Magister Markswoman (683, 129)"], 1],
    ["S_RC_OIL_InnerField_Magister_7_6e8f0ecb-22e3-4add-8a64-d91955410d87", ["The Blackpits: Magister Marksman (672, 123)"], 1],
    #dock
    ["S_RC_DW_WhiteMagister_SilentMonk_01_112e6755-131d-4eac-8ac9-e07c0a1eca3a", ["The Blackpits: Silent Watcher (351, 76)"], 1],
    ["S_RC_DW_WhiteMagister_SilentMonk_02_c09bc858-fd51-4ab1-8e47-6acdbcacc44e", ["The Blackpits: Silent Watcher (351, 82)"], 1],
    ["S_RC_OIL_Docks_Hound_03_f8593986-be91-4f06-a271-2c02ace99ead", ["The Blackpits: Source Hound (623, 62)"], 1],
    ["S_RC_OIL_Docks_Hound_01_adfec5a9-f65e-44c5-9661-963d82475890", ["The Blackpits: Source Hound (638, 58)"], 1],
    ["S_RC_OIL_Docks_WhiteMagister_01_f1e8c0fd-a1e8-4576-b3cf-59cfe01499f4", ["The Blackpits: Magister Vorrh (629, 60)"], 1],
    ["S_RC_DW_WhiteMagister_b1bdd004-a286-4ad5-9826-a763d672b2a7", ["The Blackpits: Magister Reimond (355, 77)"], 1],
    #blackpits caverns
    ["S_RC_OIL_Workshop_Spitter1_ff8bd373-c076-4446-83c7-cc169251d2e7", ["The Blackpits: Armoured Voidling (290, 598)"], 1],
    #["S_RC_OIL_Workshop_Spitter2_41926e48-1e0f-4b74-9a2d-f29b21183e60", ["The Blackpits: Fluorescent Voidling (309, 601)"], 1], #suicide doesnt send checks
    #["S_RC_OIL_Workshop_Spitter3_ff318373-4cfd-42f1-9491-3b824d35abac", ["The Blackpits: Fluorescent Voidling (295, 591)"], 1], #suicide doesnt send checks
    ["S_RC_OIL_Workshop_Spitter4_ef36af9c-8b6a-4e61-86f0-405b342d9ee5", ["The Blackpits: Armoured Voidling (320, 599)"], 1],
    ["S_RC_OIL_Workshop_Spitter5_f8701acb-6095-49a9-967d-86b054b2ebc9", ["The Blackpits: Armoured Voidling (313, 604)"], 1],
    ["S_RC_OIL_Cave_MagisterFight_Spitter_01_f52018a8-6bb3-4253-9e99-d6c9214d4bfb", ["The Blackpits: Armoured Voidling (423, 561)"], 1],
    #["S_RC_OIL_Cave_MagisterFight_Spitter_02_9e94bad2-1e19-48f9-8bf1-47006fd69228", ["The Blackpits: Fluorescent Voidling (415, 566)"], 1], #suicide doesnt send checks
    #["S_RC_OIL_Cave_MagisterFight_Spitter_03_f2794f9b-de1e-44aa-885b-64d828b42831", ["The Blackpits: Fluorescent Voidling (432, 549)"], 1], #suicide doesnt send checks
    ["S_RC_OIL_Cave_MagisterFight_Spitter_04_c4b282a3-ca84-4bbb-ae9b-017029388e2c", ["The Blackpits: Armoured Voidling (409, 555)"], 1],
    ["S_RC_OIL_Cave_MagisterFight_VampireBat1_f9e3de44-8833-4caa-9973-f2dbbce1f7ec", ["The Blackpits: Vampiric Voidwoken (409, 550)"], 1],
    ["S_RC_OIL_Cave_MagisterFight_VampireBat2_5e45efb6-88a2-4e5b-bb41-3a7a9026a513", ["The Blackpits: Vampiric Voidwoken (429, 558)"], 1],
    ["S_RC_OIL_Cave_MagisterCombatLeader_e0c0e47e-84d1-4e71-8da4-9bae87c1f553", ["The Blackpits: Magister Gremory (413, 557)"], 1],
    ["S_RC_OIL_Cave_Magister_01_3421edf4-9183-4c04-984c-1a92a1edd00c", ["The Blackpits: Silent Watcher (416, 561)"], 1],
    ["S_RC_OIL_Cave_Magister_02_930f1222-445f-457d-8bfb-d01b91ba6b24", ["The Blackpits: Silent Watcher (420, 547)"], 1],
    ["S_RC_OIL_Cave_Magister_03_e731333c-c1f8-4704-9684-e7047d522085", ["The Blackpits: Silent Watcher (410, 547)"], 1],
    ["S_RC_OIL_Wall_Monk1_87bf9286-f494-40d3-9a7c-69b0634f23f8", ["The Blackpits: Weaponised Monk (472, 614)"], 1],
    ["S_RC_OIL_Wall_Monk2_63e4bba1-264c-4068-97bb-d441e31f3fa5", ["The Blackpits: Weaponised Monk (467, 599)"], 1],
    ["S_RC_OIL_Wall_Magister1_0592c117-c506-4241-8439-1ca498045576", ["The Blackpits: Magister Knight (473, 599)"], 1],
    ["S_RC_OIL_Wall_Magister2_e220513f-8df4-4a42-bfcf-676847cdc45c", ["The Blackpits: Silent Watcher (468, 588)"], 1],
    ["S_RC_OIL_Wall_EnslavedBR_01_05e270f5-a5a7-44f1-8ec8-de2086a63d88", ["The Blackpits: Possessed Black Ring Reaver (475, 603)"], 1],
    ["S_RC_OIL_Wall_EnslavedBR_02_0d1584eb-bded-4b11-8a67-e26f5e53dd76", ["The Blackpits: Possessed Black Ring Reaver (471, 604)"], 1],
    ["S_RC_OIL_Wall_Boss_61df0b93-6498-414d-8c43-d08df9f40785", ["The Blackpits: White Magister (472, 601)"], 1],
    ["S_RC_OIL_Tomb_Ataraxian_Doggy_01_84213369-e09e-4589-b4d5-7e8bbbba8d18", ["The Blackpits: Eternal Stalker (419, 673)"], 1],
    ["S_RC_OIL_Tomb_Ataraxian_Doggy_02_6ed136a3-0f28-4b58-a9df-82f6c9d949dd", ["The Blackpits: Eternal Stalker (420, 665)"], 1],
    ["S_RC_OIL_Tomb_Ataraxian_Doggy_03_efa12e2c-a6b8-4bd7-a3cb-bc161940f306", ["The Blackpits: Eternal Stalker (408, 673)"], 1],
    ["S_RC_OIL_Tomb_Ataraxian_Doggy_04_753d4374-ec3c-4d1f-ba60-c8d8c350baed", ["The Blackpits: Eternal Stalker (408, 665)"], 1],
    ["S_RC_OIL_Tomb_Ataraxian_b844294c-62c2-4ff8-82f1-f874b9e4352d", ["The Blackpits: The Eternal Aetera (411, 671)"], 1], #kill list candidate
    #stonegarden
    #hero rest might want to test the p2 parts
    ["S_RC_GY_Memorial_Lizard_c58aa84d-c95e-4f4f-87b6-d69aebdbe66c", ["Stonegarden: Vydia (584, 137)"], 1],
    ["S_RC_GY_Memorial_Human_a8331e8a-dbe8-4595-887a-ef3d5deaa6da", ["Stonegarden: Garrick (592, 146)"], 1],
    ["S_RC_GY_Memorial_Elf_77ddb0cc-d623-46dd-97d7-b108db8394ee", ["Stonegarden: Halla (597, 142)"], 1],
    ["S_RC_GY_Memorial_Dwarf_7d1620d7-9039-4368-b6dc-3142a8fcebc6", ["Stonegarden: Bromley (588, 133)"], 1],
    ["S_RC_GY_Memorial_Lizard_Phase2_fec94203-562e-456d-aae4-24d503fea891", ["Stonegarden: Vydia Phase 2 (584, 137)"], 1],
    ["S_RC_GY_Memorial_Human_Phase2_4ceea501-acfd-49e4-989b-4600c7e33d22", ["Stonegarden: Garrick Phase 2 (592, 146)"], 1],
    ["S_RC_GY_Memorial_Elf_Phase2_9c784155-a60f-4247-9c64-1259234f8289", ["Stonegarden: Halla Phase 2 (597, 142)"], 1],
    ["S_RC_GY_Memorial_Dwarf_Phase2_3dc8d524-5ca3-4f21-84d6-f5586ed9a73b", ["Stonegarden: Bromley Phase 2 (588, 133)"], 1],
    #bridge voidwoken
    ["S_RC_DU_HeroicRescue_GiantInsect_Wings_01_899212c1-3ba7-438d-981f-51ecf75c01a9", ["Stonegarden: Venom-Wing Voidwoken (503, 52)"], 1],
    ["S_RC_DU_HeroicRescue_GiantInsect_NoWings_03_e131e879-68fb-43f2-ae69-5110bea54905", ["Stonegarden: Noxious Voidwoken (497, 52)"], 1],
    ["S_RC_DU_HeroicRescue_GiantInsect_NoWings_01_9f5cc975-fbca-4383-aff8-837f527dd950", ["Stonegarden: Noxious Voidwoken (499, 58)"], 1],
    ["S_RC_DU_HeroicRescue_GiantInsect_Wings_02_00166785-b066-4b72-adae-4fb97dc9795e", ["Stonegarden: Venom-Wing Voidwoken (511, 48)"], 1],
    #andras
    ["S_RC_GY_LoyalDog_46e022c5-f2d4-465c-a5f0-db0e9760fcce", ["Stonegarden: Andras (554, 137)"], 1],
    #ancestor tree ads go away after ghalann is dead, missable
    ["S_RC_GY_VoidwokenAncestorTree_Boss_e3e5e53f-e167-4b35-bd53-d11b4332db76", ["Stonegarden: Ghalann, Scion of the Elves (106, 540)"], 1], #kill list candidate
    #clay army
    ["S_RC_GY_VengefulSpirits_ClayArmy_W1_Melee_01_84782e40-4f83-4707-80e3-e890a49182af", ["Stonegarden: Clay Sentinel (154, 597)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W1_Melee_02_40548524-2067-4604-808c-a3cb4436bf99", ["Stonegarden: Clay Sentinel (154, 595)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W1_Melee_03_276921b9-5a17-4255-8e10-0525737493c3", ["Stonegarden: Clay Sentinel (152, 595)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W1_Melee_04_99607d38-0445-4442-a919-3077578b27f3", ["Stonegarden: Clay Sentinel (152, 597)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W1_Ranged_01_b602e50f-d4c7-48fc-b086-a70d31a1266b", ["Stonegarden: Clay Sentinel (150, 597)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W1_Ranged_02_3ec5ef99-1383-4fac-a1e3-96f26953cc3a", ["Stonegarden: Clay Sentinel (150, 595)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W2_Melee_01_23f1101e-76b7-44ae-8e9e-646889c20a72", ["Stonegarden: Clay Sentinel (154, 610)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W2_Melee_02_f79ee5a2-8b76-4774-ad04-f9a895325074", ["Stonegarden: Clay Sentinel (154, 609)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W2_Melee_03_1ebcc164-4479-4558-a9df-ef130b54b089", ["Stonegarden: Clay Sentinel (152, 609)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W2_Melee_04_3cc448db-13a3-4a97-96f8-25e9318b4de4", ["Stonegarden: Clay Sentinel (152, 610)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W2_Ranged_01_199eda77-0ec0-420f-bc43-27b53ab2eb2f", ["Stonegarden: Clay Sentinel (150, 610)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W2_Ranged_02_1bc4e3c7-a2aa-4f82-9e27-45586548819f", ["Stonegarden: Clay Sentinel (150, 609)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W2_Special_01_1ec42474-63ac-4107-86d7-07fba7d3b8e8", ["Stonegarden: Clay Sentinel (147, 610)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W3_Melee_01_a61aff31-5de5-4f94-93a2-063bcf764f15", ["Stonegarden: Clay Sentinel (154, 594)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W3_Melee_02_a6757c10-d163-4816-a98c-60519874d4a9", ["Stonegarden: Clay Sentinel (152, 594)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W3_Melee_03_d8d9de92-bba6-432c-b097-b94cf6bfe575", ["Stonegarden: Clay Sentinel (152, 592)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W3_Melee_04_a6223497-ddfe-4858-a78b-7f17d1824e0b", ["Stonegarden: Clay Sentinel (154, 592)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W3_Ranged_01_a6965245-1edb-4dd5-865a-9a65b006bea3", ["Stonegarden: Clay Sentinel (150, 594)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W3_Ranged_02_b3425c1c-41f1-4e5f-818a-5dc0fb58f24e", ["Stonegarden: Clay Sentinel (150, 592)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W3_Special_01_4a1278e8-a7ce-418c-9797-d964b36658a9", ["Stonegarden: Clay Sentinel (147, 595)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W4_Melee_01_0269ecd6-4d32-489b-9e7f-854c0d82aa20", ["Stonegarden: Clay Sentinel (154, 612)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W4_Melee_02_b77cabb0-2c8a-4cd7-adc5-de3e8a1021ce", ["Stonegarden: Clay Sentinel (154, 614)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W4_Melee_03_2842ce7b-3fc0-4ab5-8131-2c2a22278813", ["Stonegarden: Clay Sentinel (152, 612)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W4_Melee_04_9b20b5b8-ddf3-42aa-b679-5f8aa7c989a2", ["Stonegarden: Clay Sentinel (152, 614)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W4_Ranged_01_efd0d875-118b-4b6e-b97b-c55be6300f61", ["Stonegarden: Clay Sentinel (150, 612)"], 1],
    ["S_RC_GY_VengefulSpirits_ClayArmy_W4_Ranged_02_bebe490d-c1e8-44c3-9280-1157656f00d0", ["Stonegarden: Clay Sentinel (150, 614)"], 1],
    #rykers spider
    ["S_RC_GY_RykersSpider_bdc57d81-43fb-4592-8387-efd757a9b3be", ["Stonegarden: The Weaver (196, 647)"], 1],
    #ryker if you already have the tablet before first talking to ryker and give it to him there, you will fight upstairs instead of downstairs,
    #not to mention killing ryker first makes the ads dissapear making the ads from both arenas missable
    ["S_RC_GY_Ryker_522b8095-b539-4a82-84f3-bf8e5a74dfe4", ["Stonegarden: Ryker (516, 181)"], 1], #kill list candidate
    #bloodmoon island The advocate and gang are not hostile and the voidwoken ambush upon making the advocate say god king is missable, not included
    #advocate is a kill list canidate for the same reason mordus is
    #["S_GLO_Advocate_bfa3e903-78ab-46aa-9a95-54fb956eb2b3", ["Bloodmoon Island: The Advocate (274, 351)"], 1], #kill list exclusive
    ["S_RC_BI_DemonSpot2_Demon_1_9a9e4795-2612-4190-8976-478c6a80240f", ["Bloodmoon Island: Gryst Bloodspawn (207, 415)"], 1],
    ["S_RC_BI_DemonSpot2_Demon_2_80b8fc46-b0a3-44a2-8519-2371ea962b2b", ["Bloodmoon Island: Puxk Bloodspawn (224, 428)"], 1],
    ["S_RC_BI_DemonSpot2_Demon_3_f759d7b1-2e66-4bab-8842-91cdba94ee7b", ["Bloodmoon Island: Lrm the Accursed (207, 429)"], 1],
    ["S_RC_BI_DemonSpot2_Demon_4_fb670465-9ad0-4e1a-971a-e148b19f65c7", ["Bloodmoon Island: Myrvl the Accursed (214, 429)"], 1],
    ["S_RC_BI_DemonSpot2_Demon_5_1998386f-d638-4d4b-96dc-7bc6e9aff661", ["Bloodmoon Island: Virkdn Spellbinder (204, 436)"], 1],
    ["S_RC_BI_DemonSpot2_Demon_6_3bfacaa9-c9a8-4e5e-868c-d1115c0b47e7", ["Bloodmoon Island: Feygr Bloodspawn (219, 435)"], 1],
    ["S_RC_BI_AncestorTree_Blackring_001_5c413561-15bf-4cd7-8db6-f69df9bf978d", ["Bloodmoon Island: Black Ring Painweaver (270, 438)"], 1],
    ["S_RC_BI_AncestorTree_Blackring_002_ce4b11ce-0f4b-487b-a67c-4123134e1b8b", ["Bloodmoon Island: Black Ring Fearmaiden (278, 429)"], 1],
    ["S_RC_BI_AncestorTree_Blackring_003_ec71afef-c81f-4c56-b81d-7bc73958478d", ["Bloodmoon Island: Black Ring Painweaver (287, 438)"], 1],
    ["S_RC_BI_AncestorTree_Blackring_004_f1ca4587-d0e9-415c-a0c9-c0dd0a992748", ["Bloodmoon Island: Black Ring Fearmaiden (278, 447)"], 1],
    ["S_RC_BI_AncestorTree_Blackring_005_ffaeae79-c8c7-422b-be80-c0190836b531", ["Bloodmoon Island: Dead Black Ring Destroyer (266, 437)"], 1],
    ["S_RC_BI_DemonSpot1_Demon_001_839d90c0-9457-4d9d-a263-dd1c0cd71c8a", ["Bloodmoon Island: Zerachial the Accursed (390, 418)"], 1],
    ["S_RC_BI_DemonSpot1_Demon_002_615510ae-efbf-4e09-94f5-83791d4767d2", ["Bloodmoon Island: Kortan the Stalker (390, 425)"], 1],
    ["S_RC_BI_DemonSpot1_Demon_003_0d40d6c6-09f6-44af-aba1-195bae750ff6", ["Bloodmoon Island: Enelrahc the Baleful (388, 418)"], 1],
    ["S_RC_BI_DemonSpot1_Demon_004_0de0d830-725f-473e-ab10-3355774d52fa", ["Bloodmoon Island: Huld the Stalker (395, 421)"], 1],
    ["S_RC_BI_DemonSpot1_Demon_005_2492c275-d6fa-47f3-8af4-74db7fee295a", ["Bloodmoon Island: Quisvilius the Malevolent (393, 424)"], 1],
    #vaults
    ["S_RC_BI_Vault_PosessedPerson_001_f0d1f343-fc73-4c09-8d13-ed37bf51ae25", ["Bloodmoon Island: Possessed Dwarf (674, 851)"], 1],
    ["S_RC_BI_Vault_Demon_001_01c5d4d3-425f-42fd-8200-528b14aafec8", ["Bloodmoon Island: Mor the Trenchmouthed (673, 852)"], 1],
    ["S_RC_BI_Vault_PossessedPerson_003_019e266d-2d45-4818-a778-2cebffdcd743", ["Bloodmoon Island: Rajjarima (674, 775)"], 1],
    #-- act 3 --
    #vrogir
    ["S_CoS_Temples_OrcEntranceBR_001_d1734204-2ddf-47f1-aee8-1b6ce55a1a1a", ["The Nameless Isle: Black Ring Defiler (136, 897)"], 2],
    ["S_CoS_Temples_OrcEntranceBR_002_ab370701-5c09-4f99-b7fe-7ab32818c356", ["The Nameless Isle: Black Ring Reaver (137, 902)"], 2],
    ["S_CoS_Temples_Orc_CampBlackRing_001_7b438b65-1122-4fb5-bb5f-fc3a2cf460ea", ["The Nameless Isle: Black Ring Painweaver (157, 943)"], 2],
    ["S_CoS_Temples_Orc_CampBlackRing_002_5f1f25ab-9e95-4602-bcf9-2b488c63d2a6", ["The Nameless Isle: Black Ring Defiler (166, 950)"], 2],
    ["S_CoS_Temples_Orc_PortalMaster_74f2fccd-a0a6-408e-98ff-19ac07418ff2", ["The Nameless Isle: Black Ring Portalmaster (158, 963)"], 2],
    ["S_CoS_Temples_Orc_CampBlackRing_Captain_1eceaf90-79a6-4d36-9360-975f1464b0e3", ["The Nameless Isle: Black Ring Captain (167, 942)"], 2],
    #rhalic, you can side with the order or the black ring if your undead, the order force only has 3 combatants so this is my best compromise
    ["S_CoS_Temples_Human_Magister_001_5b6cb39b-2e8a-4a8c-8447-8538f6b47313", ["The Nameless Isle: Magister Inquisitor/Black Ring Defiler (191, 828)"], 2],
    ["S_CoS_Temples_Human_BlackRing_001_25888479-67b5-4380-9cd4-163a004883db", ["The Nameless Isle: Magister Inquisitor/Black Ring Defiler (191, 828)"], 2],
    ["S_CoS_Temples_Human_Magister_002_3c5a4458-a17c-43c7-9827-4eb3fd028559", ["The Nameless Isle: Paladin Archer/Black Ring Defiler (203, 823)"], 2],
    ["S_CoS_Temples_Human_BlackRing_002_29c6711c-adce-4e8f-b402-8b6239a7c7e3", ["The Nameless Isle: Paladin Archer/Black Ring Defiler (203, 823)"], 2],
    ["S_CoS_Temples_Human_Magister_003_318befa0-49d4-4ada-9196-90d8bd4d89ca", ["The Nameless Isle: Magister Priestess/Black Ring Painweaver (202, 833)"], 2],
    ["S_CoS_Temples_Human_BlackRing_003_93f7c630-eece-420c-b519-6caa057ecff6", ["The Nameless Isle: Magister Priestess/Black Ring Painweaver (202, 833)"], 2],
    #forktongue
    ["S_CoS_Temples_Elf_BlackRing_001_78df2cf8-b492-461b-a34d-2116b29a294d", ["The Nameless Isle: Black Ring Reaver (251, 884)"], 2],
    ["S_CoS_Temples_Elf_BlackRing_002_4078d759-ed9d-4971-9f68-415cb9a71704", ["The Nameless Isle: Forktongue (243, 878)"], 2],
    ["S_CoS_Temples_Elf_BlackRing_003_b31439fd-3d0f-4a85-aedd-a59ad856842b", ["The Nameless Isle: Black Ring Painweaver (235, 888)"], 2],
    ["S_CoS_Temples_Elf_BlackRing_004_c1631c6e-e570-49ed-9987-d699da96059c", ["The Nameless Isle: Black Ring Fearmaiden (238, 883)"], 2],
    ["S_CoS_Temples_Elf_BlackRing_005_8f340801-5f6e-4b7e-9f34-c734f22e3b53", ["The Nameless Isle: Black Ring Defiler (247, 876)"], 2],
    ["S_CoS_Temples_Elf_BlackRingWarg_001_d13b4a32-5c70-4585-aef2-1e858c920c8b", ["The Nameless Isle: Black Ring Warg (246, 884)"], 2],
    #stormblade cave
    ["S_CoS_Temples_ElfCave_Automaton_001_3242ab1a-db0d-4c3b-a7f1-68c8d62bc651", ["The Nameless Isle: Eternal Protector (617, 254)"], 2],
    ["S_CoS_Temples_ElfCave_Automaton_002_444c20b4-8f62-4903-a0ff-de55707496e0", ["The Nameless Isle: Eternal Sentinel (626, 247)"], 2],
    ["S_CoS_Temples_ElfCave_Automaton_003_88f85544-1280-4b00-8beb-d05c6747afa4", ["The Nameless Isle: Eternal Protector (617, 236)"], 2],
    ["S_CoS_Temples_ElfCave_Automaton_004_c35234bc-6172-4661-a766-7542b6df79e5", ["The Nameless Isle: Eternal Sentinel (607, 246)"], 2],
    #opting to exclude sallow and alexander for there are paths you can take that leave one of them alive, still kill list canidates
    #also exluding windego, funnily enough its the exact same one so the check is already sent in act 1
    #black ring hub
    ["S_CoS_Temples_BlackRingHub_Grunt_001_22e17bb5-887b-49b9-a435-fa3565a2fb43", ["The Nameless Isle: Black Ring Reaver (236, 765)"], 2],
    ["S_CoS_Temples_BlackRingHub_Grunt_002_bd6234b0-7ecc-4c2d-a07c-4d196f1a0958", ["The Nameless Isle: Black Ring Fearmaiden (228, 765)"], 2],
    ["S_CoS_Temples_BlackRingHub_Alchemist_9ba43a01-adb5-418f-8f66-da36657bc402", ["The Nameless Isle: Black Ring Alchemist (226, 770)"], 2],
    ["S_CoS_Temples_BlackRingHub_Quartermaster_a652a830-6202-4589-a5c5-a49154d2a87e", ["The Nameless Isle: Black Ring Quartermaster (238, 771)"], 2],
    ["S_CoS_Temples_BlackRingHub_Captain_7d32e545-6c6c-4a95-90dd-3ed14d3a20de", ["The Nameless Isle: Wordless (231, 773)"], 2],
    ["S_CoS_Temples_BlackRingHub_Dreamer_001_3307d7f7-b2fe-448e-828d-3cd3cde1cb8c", ["The Nameless Isle: Lizard Dreamer (242, 751)"], 2],
    ["S_CoS_Temples_BlackRingHub_Dreamer_002_25bf2b1b-0d49-4be1-946d-837dfd1ccf54", ["The Nameless Isle: Lizard Dreamer (237, 750)"], 2],
    #arena ads die when boss does, so theyre missable
    ["S_CoS_MonolithBoss_Char_c963ad5d-72f7-4c0e-8f08-910ffe11a0a3", ["The Nameless Isle: The Great Guardian (549, 923)"], 2], #kill list candidate
    #finale prob should double check this one
    ["S_CoS_AotO_SourceTitan_d230a9d9-e44d-493e-8c69-9570f2fa065f", ["The Nameless Isle: Source Titan (-211, 1027)"], 2], #kill list canidate
    #-- act 4 --
    #hermits
    ["DeathfogZone_Voidwoken_Explosive_01_2a65a44f-ac78-4402-88b2-d595cb05475d", ["Arx Outskirts: Volatile Voidling (377, 1)"], 3],
    ["DeathfogZone_Voidwoken_Explosive_02_4a5eb175-49d2-457d-b3db-25b1b5ba36cd", ["Arx Outskirts: Volatile Voidling (371, 3)"], 3],
    ["DeathfogZone_Voidwoken_Explosive_03_0d9fa4d7-ab72-4586-84f3-065d1325d011", ["Arx Outskirts: Volatile Voidling (367, 1)"], 3],
    ["DeathfogZone_Voidwoken_Explosive_04_6688b678-f05c-4d39-8383-ebe1a5968fea", ["Arx Outskirts: Volatile Voidling (373, -1)"], 3],
    ["DeathfogZone_Voidwoken_Ranged_01_e4642ce2-fb01-41bc-b2b9-9aec5aa29fea", ["Arx Outskirts: Necro-Wing Voidwoken (377, -6)"], 3],
    ["DeathfogZone_Voidwoken_Ranged_02_6157ab98-4971-4ef2-a562-59895f7a5e8c", ["Arx Outskirts: Necro-Wing Voidwoken (374, -15)"], 3],
    ["DeathfogZone_Voidwoken_Ranged_03_a96fd67a-9acf-4fad-b6ba-9fa1475ef663", ["Arx Outskirts: Necro-Wing Voidwoken (360, -5)"], 3],
    ["DeathfogZone_Troll_Undead_01_c7feba75-58ef-446b-8a90-779db62e5128", ["Arx Outskirts: Awakened Construct (381, -18)"], 3],
    ["DeathfogZone_Champion_Undead_01_192521f2-0889-4e29-aa49-705c943aa024", ["Arx Outskirts: Loic the Immaculate (356, -7)"], 3], #hit list canidate
    #harbor kraken leaves at half health unfortunatly
    ["S_ARX_Outskirts_Harbour_Voidwoken_01_e0a7f25e-7aaf-428f-8725-3f8dadc643d4", ["Arx Outskirts: Abyssal Void Flayer (450, 136)"], 3],
    ["S_ARX_Outskirts_Harbour_Voidwoken_02_6428cbe6-5356-408b-8607-b9effa0d5355", ["Arx Outskirts: Abyssal Void Flayer (463, 99)"], 3],
    ["S_ARX_Outskirts_Harbour_Voidwoken_03_997a816c-2018-484b-81bd-c49621ac2cc7", ["Arx Outskirts: Abyssal Void Devourer (450, 100)"], 3],
    #bottom left corner
    ["S_ARX_JahansDemons_Fallback_Warrior_01_adeb719d-86a5-46c2-b7a9-1b82b5f24544", ["Arx Outskirts: Outcast Berserker (240, 74)"], 3],
    ["S_ARX_JahansDemons_Fallback_Warrior_01_Animal_441c0c36-39bb-4563-a885-b06d6374af02", ["Arx Outskirts: Cuddles (242, 74)"], 3],
    ["S_ARX_JahansDemons_Fallback_Ranger_01_185efcd7-4aa8-4091-b65e-2c62ff4199a3", ["Arx Outskirts: Outcast Hunter (236, 80)"], 3],
    ["S_ARX_JahansDemons_Fallback_Ranger_01_Animal_126a13cd-5931-4a25-b568-db5c609082b0", ["Arx Outskirts: Featherfang (240, 81)"], 3],
    ["S_ARX_JahansDemons_Fallback_Mage_01_cfef563e-2391-43a3-b291-acc6ba6a6692", ["Arx Outskirts: Outcast Spellweaver (236, 62)"], 3],
    ["S_ARX_JahansDemons_Fallback_Mage_01_Animal_7f8d502d-cc64-475e-a0aa-18a4a0a98814", ["Arx Outskirts: Emberwing (236, 75)"], 3],
    #entrance
    ["S_ARX_ClanWar_OffStageVoidwoken_Boss_df50b95d-807b-47e5-8854-c2f01ae4f74b", ["Arx Outskirts: Voidwoken Bloodfury (302, 172)"], 3], #hit list canidate
    ["S_ARX_ClanWar_Voidwoken_01_e3603964-4654-44a0-9556-61ac9cde82af", ["Arx Outskirts: Vampiric Voidwoken (291, 171)"], 3],
    ["S_ARX_ClanWar_Voidwoken_02_ff762c81-0473-490c-b4f5-742aac4637ea", ["Arx Outskirts: Vampiric Voidwoken (291, 164)"], 3],
    ["S_ARX_ClanWar_Voidwoken_03_41813ffd-4b91-408d-b4c9-538b6280b844", ["Arx Outskirts: Vampiric Voidwoken (295, 163)"], 3],
    ["S_ARX_ClanWar_OffStageVoidwoken_01_0fde4292-1148-4bdb-b923-1165e93b0452", ["Arx Outskirts: Necro-Wing Voidwoken (282, 149)"], 3],
    ["S_ARX_ClanWar_OffStageVoidwoken_02_89bd87d9-018d-4d8b-8c01-64bfdb9550d8", ["Arx Outskirts: Necro-Wing Voidwoken (302, 165)"], 3],
    ["S_ARX_ClanWar_OffstageVoidwoken_06_295919a7-a232-4e6f-8ed3-869808c21052", ["Arx Outskirts: Necro-Wing Voidwoken (283, 162)"], 3],
    #magister vault
    ["S_ARX_Barracks_WhiteMagisterVault_Gheist1_bf45ee01-e395-4169-9013-4dd96e422e07", ["Arx: Gheist (145, 43)"], 3],
    ["S_ARX_Barracks_WhiteMagisterVault_Gheist2_99366040-3f84-4fbb-ac32-b26fe0378ae8", ["Arx: Gheist (145, 50)"], 3],
    ["S_ARX_Barracks_WhiteMagisterVault_Gheist3_1a3dd9ea-1c4c-440e-82bf-0e9ca9ac6e30", ["Arx: Gheist (143, 46)"], 3],
    #blood dowry
    ["S_ARX_MerchantEstate_Groom_50b47558-7485-4f84-b530-f04fcf3018d1", ["Arx: Dorian Gall (318, 336)"], 3],
    ["S_ARX_Neighborhood_HouseAlchemist_Ooze_01_1673d4c0-937d-4cb3-ac2a-1ef40f3fb806", ["Arx: Failed Experiment (124, -39)"], 3],
    ["S_ARX_Neighborhood_HouseAlchemist_Ooze_02_eeab1cbf-a852-416b-8133-9ee03ceed54d", ["Arx: Failed Experiment (112, -39)"], 3],
    ["S_ARX_Neighborhood_HouseAlchemist_Ooze_03_6a6325cf-7949-48a4-9432-34ed19090ab9", ["Arx: Failed Experiment (124, -17)"], 3],
    ["S_ARX_Neighborhood_HouseAlchemist_Ooze_04_96c029cb-adda-48eb-a086-89110dae6499", ["Arx: Failed Experiment (108, -22)"], 3],
    #school
    # ["S_ARX_DemonAmbush1_Spotter_cfd1a537-df32-46fc-9878-2c4181fd3c14", ["Arx: Nemesis Devourer (394, 259)"], 3], these run and are missable
    # ["S_ARX_DemonAmbush2_Spotter_3dad22a2-0c6f-4f34-bfeb-b83c64e23832", ["Arx: Nemesis Soulhunter (218, 322)"], 3],
    # ["S_ARX_DemonAmbush3_Spotter_a9cdf6c2-43f1-48eb-a976-9337f6bd36d2", ["Arx: Nemesis Heartpiercer (167, 238)"], 3],
    # ["S_ARX_DemonAmbush4_55da9d21-9eaf-445b-82b0-aae2c85aac96", ["Arx: Nemesis Stargazer (109, 280)"], 3],
    #old lady house
    ["S_ARX_Neighborhood_TheFence_Demon_01_f7a9e3e9-1d24-41e2-9c7b-86feae69b012", ["Arx: Debt Collector (379, 735)"], 3],
    ["S_ARX_Neighborhood_TheFence_Demon_02_3d0566de-786e-4ff9-ab1a-5c7a279c1580", ["Arx: Debt Collector (385, 741)"], 3],
    ["S_ARX_Neighborhood_TheFence_Demon_03_0fc21242-8f25-4091-a42b-e7614199a243", ["Arx: Debt Collector (376, 733)"], 3],
    ["S_ARX_Neighborhood_TheFence_973d85be-5756-4bf1-aae3-a2b06fcb2b31", ["Arx: Sanguinia Tell (419, 298)"], 3], #kill list canidate
    #mistake
    ["S_ARX_Prison_Mistake_BlackRing1_6144fe66-7ac8-4034-9f0d-8335efa4ac91", ["Arx: Saeva the Many-faced (148, 763)"], 3],
    ["S_ARX_Prison_Mistake_BlackRing2_fb59309d-5167-4ad7-97fd-f43122040124", ["Arx: Sahun Woundbinder (148, 735)"], 3],
    ["S_ARX_Prison_Mistake_BlackRing3_0419d25a-af6e-4ad2-9394-710803f4af0f", ["Arx: Urrha the Snake Charmer (177, 753)"], 3],
    ["S_ARX_Prison_Mistake_BlackRing4_026049be-0529-4c39-82dd-245cb2c6b4cc", ["Arx: Kajun Frozenheart (177, 736)"], 3],
    ["S_ARX_Prison_TheMistake_5136657b-5d75-409f-814c-0eee4ff3913d", ["Arx: Karon (163, 750)"], 3], #hit list candidate
    #spider ambush
    ["S_ARX_Sewers_CombatRoom_Spider_01_be2ee8d1-1e2c-4d49-9006-b13511d88efb", ["Arx: Fog-Swollen Crawler (444, 578)"], 3],
    ["S_ARX_Sewers_CombatRoom_Spider_02_6aa78db3-f828-44ef-af25-702302a84506", ["Arx: Void-touched Crawler (427, 594)"], 3],
    ["S_ARX_Sewers_CombatRoom_Spider_03_1dba6ede-5303-4a87-9e35-31a0e7da2fa1", ["Arx: Void-touched Crawler (458, 607)"], 3],
    ["S_ARX_Sewers_CombatRoom_Spider_04_fda1a4b2-3477-4704-bafd-039698b80937", ["Arx: Fog-Swollen Crawler (443, 607)"], 3],
    #isbel
    ["S_ARX_Sewers_Q_52f20922-7b22-4d47-90f7-83172f21fe3b", ["Arx: Isbeil (280, 672)"], 3], #hit list canidate
    ["S_ARX_Sewers_ImperialGuard_01_Unmasked_2a5e722e-0123-48ae-9d51-027bd9079b5c", ["Arx: Black Ring Witherknight (296, 617)"], 3],
    ["S_ARX_Sewers_ImperialGuard_02_Unmasked_4d847c4b-3eb9-4ccf-8d94-f1d2b5de9f01", ["Arx: Black Rang Flamebringer (291, 618)"], 3],
    ["S_ARX_Sewers_EliteImperialGuard_01_Unmasked_125b1265-cef0-4782-b7e6-a551210a2a8c", ["Arx: Black Ring Skullcrusher (308, 617)"], 3],
    ["S_ARX_Sewers_EliteImperialGuard_04_Unmasked_e9293a04-303a-45b4-9226-1fbef76cc131", ["Arx: Black Ring Limbchopper (303, 617)"], 3],
    #kemm garden
    ["S_RC_ARX_KemmMansion_Garden_Shambl_Tank_01_0b0b9920-64e4-4b29-b465-0c578916a099", ["Arx: Thorny Suncaller (101, 286)"], 3], #hit lst candidate
    ["S_RC_ARX_KemmMansion_Garden_Shambl_Ranger_01_cb26f904-3b70-4d1b-b36d-aee47955f8f3", ["Arx: Malignant Oak (100, 271)"], 3],
    ["S_RC_ARX_KemmMansion_Garden_Shambl_Ranger_02_cddc80f7-32dd-4cd4-bdf4-0cf29b531ece", ["Arx: Malignant Oak (99, 301)"], 3],
    ["S_RC_ARX_KemmMansion_Garden_Shambl_Caster_01_f971c19e-4fbb-45fb-a57e-2d7991aade88", ["Arx: Hungry Flower (97, 294)"], 3],
    ["S_RC_ARX_KemmMansion_Garden_Shambl_Caster_02_67ea8705-133f-42d6-b8fe-32065f6c45c2", ["Arx: Hungry Flower (97, 277)"], 3],
    #kemm vault
    ["S_ARX_KemmVault_ArhusPrison_Horror_01_e5da66e9-a385-48ef-a488-df463dfc7de5", ["Arx: Black Ring Fearmaiden (279, 764)"], 3],
    ["S_ARX_KemmVault_ArhusPrison_Horror_02_9abc5e99-9ebe-4107-b561-691bad0c6cd7", ["Arx: Black Ring Painweaver (267, 764)"], 3],
    ["S_ARX_KemmVault_ArhusPrison_Horror_03_8604e931-2d21-4f2e-b5f4-b27a9c12eff3", ["Arx: Black Ring Defiler (282, 751)"], 3],
    ["S_ARX_KemmVault_ArhusPrison_Horror_04_b5d345ea-7a93-4b3a-9f9b-9c6d666b6c01", ["Arx: Black Ring Defiler (264, 751)"], 3],
    ["S_ARX_Kemm_3e6ead7d-dd35-4f9d-985e-af2de0d76d28", ["Arx: Lord Linder Kemm (325, 263)"], 3], #hit list canidate
    #lizard consulate
    ["S_ARX_LizardConsualte_InfernalLizard_01_ade1bfee-f057-4b1f-8390-33ae025e9ea8", ["Arx: Cursed Revenant (174, 332)"], 3],
    ["S_ARX_LizardConsualte_InfernalLizard_02_c0f3c58e-8d05-4d64-9098-d2f7bb8669d0", ["Arx: Cursed Revenant (193, 333)"], 3],
    ["S_ARX_LizardConsualte_InfernalLizard_03_85bf82a9-de63-4982-8806-bbd1cee3ab37", ["Arx: Cursed Revenant (182, 384)"], 3],
    ["S_ARX_LizardConsualte_InfernalLizard_04_7161c772-d04d-4c6a-b5e4-46568fcbd612", ["Arx: Cursed Revenant (170, 375)"], 3],
    ["S_ARX_LizardConsualte_InfernalLizard_05_7c94819e-89d2-46cf-8ea4-0d0d7e317a75", ["Arx: Cursed Revenant (190, 373)"], 3],
    #lizard dream (nvm none of these figths happen if you have red prince in your party and the shadow prince fight afterwards dosent happen if you dont have red prince)
    #there are two more hunter-dreamers, but you can leave without aggroing them and you cannot return to this area
    # ["S_GLO_Brahmos_d4064352-33f9-49df-b208-09fd822d2270", ["Arx: Brahmos the Wanderer (633, 758)"], 3],
    # ["S_ARX_HorrorSleep_WarZone_LizardDreamer_2_cb0fd13b-6719-47ea-b660-8b858940eb1b", ["Arx: Earth-dreamer (342, 1086)"], 3],
    # ["S_ARX_HorrorSleep_WarZone_LizardDreamer_3_cf0cf358-d803-44e0-a742-922152950472", ["Arx: Wave-dreamer (346, 1091)"], 3],
    # ["S_ARX_HorrorSleep_WarZone_LizardDreamer_4_d1aa71d7-4d75-4c47-baec-b7077426b627", ["Arx: Flame-dreamer (346, 1086)"], 3],
    # ["S_ARX_HorrorSleep_WarZone_LizardDreamer_5_90e70559-d9de-465c-9a07-86009e6f6a21", ["Arx: Storm-dreamer (341, 1092)"], 3],
    # ["S_ARX_HorrorSleep_Sunset_Newt_1f46750f-1d62-4676-aaa7-9ec226c96428", ["Arx: Dragonchild (281, 937)"], 3],
    # ["S_ARX_HorrorSleep_Sunset_HunterDreamer_01_68e15ffc-7fb1-4ea0-8d91-ede24744ea06", ["Arx: Hunter-dreamer (292, 923)"], 3],
    # ["S_ARX_HorrorSleep_Sunset_HunterDreamer_02_356d752f-03e4-48ee-88f3-3b72a8db6e2a", ["Arx: Hunter-dreamer (273, 929)"], 3],
    # ["S_ARX_HorrorSleep_Sunset_LizardDreamer_01_f60aae58-94f5-4668-8e1f-173970b68a60", ["Arx: Earth-dreamer (299, 936)"], 3],
    # ["S_ARX_HorrorSleep_Sunset_LizardDreamer_02_9b8741fb-ee59-41e3-b68f-82c3bea760fe", ["Arx: Flame-dreamer (277, 944)"], 3],
    # ["S_GLO_RedPrincess_050fbbf9-3fc9-40cd-9cbb-43b4b3754a5e", ["Arx: Sadha (577, 445)"], 3],
    #toys
    ["S_ARX_CreepyShop_2ndFloor_SourcePuppet1_480f3e01-426b-4d07-b001-892b8aa7b7f7", ["Arx: Bewitched Moppet (100, -82)"], 3],
    ["S_ARX_CreepyShop_2ndFloor_SourcePuppet2_aa35f60d-d12f-4021-b714-5207f138434b", ["Arx: Bewitched Moppet (119, -100)"], 3],
    ["S_ARX_CreepyShop_2ndFloor_SourcePuppet3_ccce45e6-566c-4d59-88a0-f2721c2a692e", ["Arx: Bewitched Moppet (106, -93)"], 3],
    ["S_ARX_CreepyShop_2ndFloor_SourcePuppet4_69cf2e83-1b5a-4831-b214-352cadceba96", ["Arx: Bewitched Moppet (105, -81)"], 3],
    ["S_ARX_CreepyShop_2ndFloor_SourcePuppet5_72df0b99-e10f-4c8c-81de-c3967f31d94d", ["Arx: Bewitched Moppet (101, -96)"], 3],
    #doctor
    #["Creatures_Demon_Caster_A_ONLYUSE_THEDOCTOR_83083470-c543-45b3-ac8a-108df0daca8d", ["Arx: Adramahlihk (387, 418)"], 3], #the demon form, hit list canidate (shouldnt be needed anymore since it has the same id as normal doctor)
    ["S_ARX_DoctorsHouse_TheDoctor_83083470-c543-45b3-ac8a-108df0daca8d", ["Arx: Adramahlihk (387, 418)"], 3], #the human form
    #["S_ARX_DoctorsHouse_DoctorsDemon_01_4ac45868-d71a-4756-8e39-cf7550544c95", ["Arx: Nemesis Stargazer (386, 417)"], 3], #these only spawn if you do not snuff the candles
    #["S_ARX_DoctorsHouse_DoctorsDemon_02_ba9b8596-ddfa-4199-b4bb-273d010046eb", ["Arx: Nemesis Devourer (386, 412)"], 3],
    #["S_ARX_DoctorsHouse_DoctorsDemon_03_f12c9cc0-0219-46de-9746-3ea5b802cee6", ["Arx: Nemesis Heartpiercer (393, 427)"], 3],
    #["S_ARX_DoctorsHouse_DoctorsDemon_04_7f2515b5-1482-41d5-8f3d-20304eda0e9e", ["Arx: Nemesis Soulhunter (386, 422)"], 3],
    ["S_ARX_DoctorsHouse_Nurse_01_649673eb-79f4-417f-9703-2a640a284f12", ["Arx: Nurse Do (392, 417)"], 3],
    ["S_ARX_DoctorsHouse_Nurse_02_e8cc0255-7d6e-4f52-81ca-2551e8b445a1", ["Arx: Nurse Fa (408, 382)"], 3],
    ["S_ARX_DoctorsHouse_Nurse_03_0933d507-2e69-4d6d-9631-dff702e03744", ["Arx: Nurse Si (407, 434)"], 3],
    ["S_ARX_DoctorsHouse_Nurse_04_6831724d-d355-42ef-be25-5bcc1e9baa52", ["Arx: Nurse Mi (426, 409)"], 3],
    ["S_ARX_DoctorsHouse_Nurse_05_708e03a9-50c3-40de-90ed-c5f58a45df84", ["Arx: Nurse La (419, 421)"], 3],
    ["S_ARX_DoctorsHouse_Nurse_06_88d45ba2-a4ec-45b8-bdcd-92951dbd06ca", ["Arx: Nurse Re (417, 397)"], 3],
    #seed of power 
    ["CON03_Ranger_01ae9dbb-2f5e-4000-b707-26667910d2ad", ["Arx: Spiked Trunk (169, 132)"], 3],
    ["CON03_PoisonousPlant_000_21c39d23-1eb6-41ba-bd24-217d57e0a0b0", ["Arx: Corrosive Flower (165, 124)"], 3],
    ["CON03_PoisonousPlant_c470733f-3a3b-412c-9892-d767974ec0aa", ["Arx: Corrosive Flower (158, 140)"], 3],
    ["CON03_HeartOfMight_7d513fa3-a897-4351-aa50-0dbe501dca9c", ["Arx: Bloom of Might (152, 144)"], 3],
    ["CON03_HeartOfNimbleness_4bab9a2d-7730-49fb-aae9-eae654afe843", ["Arx: Bloom of Momentum (159, 136)"], 3],
    ["CON03_HeartOfEndurance_cc7fe0bd-abe4-4da3-8ee4-f253d864aba9", ["Arx: Bloom of Mettle (172, 117)"], 3],
    ["CON03_ContaminationGuardian_93b0ac12-4884-4902-9b03-cedcb4f8a179", ["Arx: Contaminated Horror (172, 136)"], 3], #hit list candidate
    #["CON00_ElvenScion_ARX_e13fde00-fca4-494e-973b-7812c56a08d1", ["Arx: Daeyena (172, 140)"], 3], #can die earlier than here
    #end, braccus is the only one you kill with both choices for the ending
    ["S_GLO_Braccus_358ba541-0710-43be-8263-87afe1a8d9b5", ["Tomb of Lucian: Braccus Rex (581, 284)"], 3], #hit list candidate
]

for loc in DOS2_KILL_LIST:
    loc[0] = loc[0].rsplit("_", 1)[-1]

#All of the FTJ ones came from @chaotic and @JeyKey09, thank you!
DOS2_LOCATION_LIST = [
    ["Quest-TUT_ShipInvestigation", ["Merryweather: Death Belowdecks - Complete"], 0],
    ["Quest-TUT_ShipMurder", ["Merryweather: Troubled Waters - Complete"], 0],
    ["Quest-FTJ_Escape", ["Fort Joy: Escape From Fort Joy - Complete"], 0],
    ["Quest-FTJ_Escape_Island", ["North-east Reaper's Eye: Escape From Reaper's Eye - Complete", "Victory_Escape_Reapers_Eye"], 0],
    ["Quest-FTJ_Escape_Island_SUBA", ["North-east Reaper's Eye: Seek and You Shall Find - Complete"], 0], #Seek and You Shall Find
    #["Quest-FTJ_Escape_Island_SUBB", ["placeholder4"], 0], #The Dragon's Way, mutually exclusive
    #["Quest-FTJ_Escape_Island_SUBC", ["placeholder5"], 0], #Silence the Shrieking
    ["Quest-FTJ_Voice", ["East Reaper's Eye: The Voices - Complete"], 0],
    #["Quest-FTJ_Godwoken", ["placeholder7"], 0], #Champion of the Gods - {character}
    #["Quest-FTJ_Hunted", ["placeholder8"], 0], #A Rare Prey
    #["Quest-FTJ_Seeker", ["placeholder9"], 0], #Signs of Resistance
    ["Quest-RC_FTJ_OlgoSaheila", ["Fort Joy: The Imprisioned Elf - Complete"], 0],
    ["Quest-RC_FTJ_MurderousGheist", ["Fort Joy: The Murderous Gheist - Complete"], 0],
    ["Quest-FTJ_SourceHounds", ["Fort Joy: Finding Emmie - Complete"], 0],
    ["Quest-FTJ_Arena", ["Fort Joy: The Arena of Fort Joy - Complete"], 0],
    ["Quest-RC_FTJ_SoulJar", ["Fort Joy: Withermoore's Soul Jar - Complete"], 0],
    #["Quest-RC_FTJ_SaheilaSignet", ["placeholder16"], 0], #this doesnt seem to be used
    ["Quest-FTJ_Teleporter", ["Fort Joy: The Teleporter - Complete"], 0],
    ["Quest-FTJ_Elodi", ["Fort Joy: The Shakedown - Complete"], 0],
    ["Quest-FTJ_SW_Illusionist", ["East Reaper's Eye: The Vault of Braccus Rex - Complete"], 0],
    ["Quest-FTJ_SW_HurtSeekers", ["East Reaper's Eye: Healing Touch - Complete"], 0], #correctly seperated from Most Dangerous When Cornered now
    ["Quest-FTJ_SW_StuckHaunting", ["East Reaper's Eye: The Eternal Worshipper - Complete"], 0], #patched the same way Most Dangerous When Cornered was
    ["Quest-FTJ_SW_Necromancers", ["East Reaper's Eye: A Fate Worse Than Death - Complete"], 0],
    ["Quest-FTJ_SW_BraccusArmory", ["East Reaper's Eye: The Armoury - Complete"], 0],
    ["Quest-FTJ_SW_CursedRing", ["East Reaper's Eye: The Cursed Ring - Complete"], 0],
    ["Quest-FTJ_SW_UndeadTowerMaze", ["East Reaper's Eye: The Gargoyle's Maze - Complete"], 0],
    ["Quest-FTJ_SW_CursedPig", ["East Reaper's Eye: The Burning Pigs - Complete"], 0],
    ["Quest-FTJ_SW_PurgedDragon", ["East Reaper's Eye: The Purged Dragon - Complete"], 0],
    ["Quest-FTJ_SW_CallToArms", ["East Reaper's Eye: Call to Arms - Complete"], 0],
    ["Quest-FTJ_SW_Shriekers", ["East Reaper's Eye: The Shreikers - Complete"], 0],
    ["Quest-FTJ_SW_Tyrant", ["North-east Reaper's Eye: Artefacts of the Tyrant - Complete"], 0],
    ["Quest-FTJ_SW_BatteredAndCornered", ["East Reaper's Eye: Most Dangerous When Cornered - Complete"], 0], #patched, all flags besides murder gareth did not have a QuestUpdate prefix
    ["Quest-CaptainArmour", ["North-east Reaper's Eye: Threads of a Curse - Complete"], 0],
    ["Quest-RC_FTJ_SourceCollar", ["East Reaper's Eye: Hot Under the Collar - Complete"], 0], #patched in GLO_SourceCollars, might have unintended consequences
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
    #["Quest-RC_ThreeAltars", ["The Meadows: The Three Altars - Complete"], 1], #according to the wiki, this quest doesnt actually close and is just recorded in The Eternal Proimse, so this probably doesnt work (wiki was right, closes on act leave)
    ["Quest-RC_DW_GarvanSupplies", ["Driftwood: Red Ink in the Ledger - Complete"], 1],
    #["Quest-RC_DW_GrandmasterArrest", ["placeholder11"], 1], idk, none fired on act exit
    #["Quest-RC_DW_Looter", ["placeholder12"], 1],
    #["Quest-RC_DW_TrappedHusband", ["placeholder13"], 1],
    #["Quest-RC_DW_BridgeDog", ["placeholder14"], 1],
    ["Quest-RC_DW_FunnyMeat", ["Driftwood: The Missing Magisters - Complete"], 1],
    #["Quest-RC_DW_FunnyMeat_SUBA", ["placeholder16"], 1], these are different routes the quest can take, ie annoying missabled, the main fire on all of them anyway #Stewart's Investigation
    #["Quest-RC_DW_FunnyMeat_SUBB", ["placeholder17"], 1], #Carver's Investigation
    #["Quest-RC_DW_FunnyMeat_SUBC", ["placeholder18"], 1], #Investigation Over
    ["Quest-RC_DW_HidingTinkerer", ["Driftwood: Strange Cargo - Complete"], 1],
    ["Quest-RC_DW_Dock_Kids", ["Driftwood: Hide & Seek - Complete"], 1],
    #["Quest-RC_DW_FishScholar", ["Driftwood: Grebb the Scholar - Complete"], 1], #no longer a quest in DE
    #["Quest-RC_DW_CaptiansGhost", ["placeholder22"], 1], notably not Drowning Her Sorrows, dosnt fire on act exit
    ["Quest-RC_DW_FishermanRing", ["Reaper's Bluffs: Lost and Found - Complete"], 1],
    #["Quest-RC_DW_Harmon", ["placeholder24"], 1], no idea, doest fire on act exit
    ["Quest-RC_DW_SpidersKiss", ["Driftwood - A Web of Desire - Complete"], 1],
    ["Quest-RC_DW_TheDrunkenSailor", ["Driftwood: Drowning Her Sorrows - Complete"], 1],
    ["Quest-RC_DW_Arena", ["Driftwood: The Driftwood Arena - Complete"], 1],
    ["Quest-RC_DW_SurpriseDate", ["Driftwood: Love Has a Price - Complete"], 1],
    #["Quest-RC_DW_MissingEquipment", ["placeholder29"], 1], no idea, doesnt fire on act exit #Getting Your Own Back (I think this is added when you get your stuff stolen in Love Has a Price idk)
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
    ["Quest-RC_DF_PolyLovers", ["The Meadows: Treated Like Cattle - Complete"], 1],
    ["Quest-RC_DF_UndeadTrader", ["Cloisterwood: Eithne the Trader - Complete"], 1],
    ["Quest-RC_DF_TrollBridge", ["Cloisterwood: Business Rivals - Complete"], 1], #cant get both paths in one save, keeping the main and nothnig else
    #["Quest-RC_DF_TrollBridge_SUBA", ["placeholder45"], 1], #Grog's Monopoly
    #["Quest-RC_DF_TrollBridge_SUBB", ["placeholder46"], 1], #Marg's Monopoly
    ["Quest-RC_GY_RykersContract", ["Stonegarden: A Generous Offer - Complete"], 1],
    ["Quest-RC_GY_RykersSpider", ["Stonegarden: The Weaver - Complete"], 1],
    ["Quest-RC_GY_PurgedDaughter", ["Stonegarden: A Danger to Herself and Others - Complete"], 1],
    ["Quest-RC_GY_LizardSpeakingLizard", ["Stonegarden: Speaking In Forked Tongues - Complete"], 1],
    ["Quest-RC_GY_FavoritePet", ["Stonegarden: Popularity Contest - Complete"], 1],
    ["Quest-RC_GY_TurtleLove", ["Stonegarden: Opposites Attract - Complete"], 1],
    ["Quest-RC_GY_BuriedLizard", ["Stonegarden: Stranger in a Strange Land - Complete"], 1],
    ["Quest-RC_GY_MemorialOfHeroes", ["Stonegarden: Heroes' Rest - Complete"], 1],
    ["Quest-RC_GY_UglyBird", ["The Meadows: The Ugly Little Bird - Complete"], 1],
    ["Quest-RC_GY_DeerGhost", ["Stonegarden: A Prize Kill - Complete"], 1],
    ["Quest-RC_GY_Godslayer", ["Stonegarden: All In The Family - Complete"], 1],
    ["Quest-RC_GY_WronglyBuried", ["Stonegarden: An Existential Crisis - Complete"], 1],
    ["Quest-RC_GY_KillRyker", ["Stonegarden: The Reluctant Servants - Complete"], 1],
    ["Quest-RC_DF_PaladinCheckpoint", ["The Meadows: Dark Dealings in the Blackpits - Complete"], 1],
    ["Quest-RC_OIL_FourthHouse", ["The Blackpits: No Way Out - Complete"], 1],
    ["Quest-RC_FL_BrokenPromises", ["Paradise Downs: Unlikely Lovers - Complete"], 1],
    ["Quest-RC_FL_TabletForAlmira", ["Paradise Downs: Almira's Request - Complete"], 1],
    ["Quest-RC_BF_ThePresence", ["Cloisterwood: A Hunter of Wicked Things - Complete"], 1],
    #["Quest-RC_BI_TheTruth", ["placeholder65"], 1], #The Secrets of Bloodmoon Island? cant be completed till act 4 if so (nvm fires on act exit i have no idea what this is) -it is secrets of bloodmoon (it also fire exactly where youd think too in act 4)
    ["Quest-RC_BI_TheVaults", ["Bloodmoon Island: The Forgotten and the Damned - Complete"], 1],
    ["Quest-RC_BI_TheVaults_SUBA", ["Bloodmoon Island: Delusions of Gradeur - Comeplete"], 1],
    ["Quest-RC_BI_TheVaults_SUBB", ["Bloodmoon Island: Silent as the Grave - Complete"], 1],
    ["Quest-RC_BI_TheVaults_SUBC", ["Bloodmoon Island: The Sweet Shackles of Pain - Complete"], 1], 
    ["Quest-RC_BI_TheVaults_SUBD", ["Bloodmoon Island: Metalwork - Complete"], 1], #fixed same way Most Cornered When Dangerous was
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
    ["Quest-VultureArmour", ["Reaper's Bluffs: Keep Calm and Carrion - Complete"], 1],
    ["Quest-RC_DW_SnoozingAdventurer", ["Driftwood: The Snoozing Adventurer - Complete"], 1],
    ["Quest-RC_DW_RichMerchant", ["Driftwood: The Merchant - Complete"], 1],
    ["Quest-RC_DW_Beggar", ["Driftwood: A Man and His Dog - Complete"], 1],
    #["Quest-RC_FL_GarethFarm", ["placeholder93"], 1], #fires when killing jonathan in the first encounter with gareth, no where else in Burying the Past. Every other path doesnt fire until act exit, opting to omit this one (can fix it, missable anyway)
    #["Quest-RC_FL_GarethParents", ["placeholder94"], 1], #This is whatever the one is for killing voidwoken at gareths parents behest, obnoixously missable, probably wont include, doesn't fire on act exit either #Infestation
    ["Quest-RC_MIL_ElvenBurial", ["The Cullwoods: Burial Rites - Complete"], 1], #fixed the same as Most Dangerous When Cornered
    ["Quest-RC_MIL_ElfTest", ["The Cullwoods: A Trial for All Seasons - Complete"], 1], #fixed the same as Most Dangerous When Cornered
    ["Quest-RC_MIL_AvengingSaheila", ["The Cullwoods: The Elven Seer/Vengeance for the Fallen - Complete"], 1],
    ["Quest-RC_OIL_ThirdHouse", ["The Blackpits: On the Ropes - Complete"], 1],
    ["Quest-RC_DW_Meistr_SUBI", ["Driftwood: The Gift of the Blackroot - Complete"], 1],
    #-- act 3 --
    #["Quest-CoS_BreakerForAlmira", ["The Nameless Isle: The Key to Freedom - Complete"], 2], #probably missable
    ["Quest-CoS_Temples", ["The Nameless Isle: The Nameless Isle - Complete"], 2], #
    #["Quest-CoS_Temples_SUBA", ["The Nameless Isle: Helping Alexander - Complete"], 2], #missable (pops at aoto)
    #["Quest-CoS_Temples_SUBB", ["The Nameless Isle: Helping Sallow - Complete"], 2], (pops at aoto)
    #["Quest-CoS_Temples_SUBC", ["The Nameless Isle: To the Belly of the Mountain - Complete"], 2],
    ["Quest-CoS_ImpTemple", ["The Nameless Isle: Running like Clockwork - Complete"], 2],
    ["Quest-CoS_OrcTemple", ["The Nameless Isle: The Drowned Temple - Complete"], 2], #good (pops at aoto)
    ["Quest-CoS_WizardTemple", ["The Nameless Isle: Up in the Clouds - Complete"], 2], #(pops at aoto)
    ["Quest-CoS_HelpingTheSallowMan", ["The Nameless Isle: The Sallow Man - Complete"], 2], #probably mutually exclusive with unlikley patron (pops at aoto) pops on sallows death so actually keeping this as an either you do it, or you fail it
    #["Quest-CoS_CompanionCulling", ["The Nameless Isle: Thinning the Herd - Complete"], 2], #thinning the herd - {character} gonna be missable
    #["Quest-CoS_HelpingAlexandar", ["The Nameless Isle: An Unlikely Patron - Complete"], 2], #(pops at aoto) this doesnt pop for anything, completing or failing the quest
    #["Quest-CoS_Delorus", ["The Nameless Isle: A Familiar Face - Complete"], 2], #missable
    #["Quest-CoS_GarethsRevenge", ["The Nameless Isle: Seeking Revenge - Complete"], 2], #also probably super missable, correct
    ["Quest-CoS_BlackRing", ["The Nameless Isle: Invaders - Complete"], 2], #(pops at aoto)
    ["Quest-CoS_TheWatcher", ["The Nameless Isle: The Watcher's Mercy - Complete"], 2], #(pops at aoto)
    ["Quest-CoS_SpyMaster", ["The Nameless Isle: The Mother Tree - Complete"], 2], #(pops at aoto)
    ["Quest-CoS_MissingStudent", ["The Nameless Isle: Unscholarly Pursuits - Complete"], 2], #(pops at aoto)
    ["Quest-CoS_ForbiddenLibrary", ["The Nameless Isle: Proving Ground - Complete"], 2], #(pops at aoto)
    ["Quest-CoS_Academy", ["The Nameless Isle: The Academy - Complete"], 2],
    ["Quest-CoS_ArenaOfTheOne", ["The Nameless Isle: The Arena of the One - Complete", "Victory_Escape_The_Nameless_Isle"], 2], #probably the goal locaion
    #-- act 4 --
    #["Quest-DevourerArmour", ["A Hunger From Beyond - Complete"], 1], very missable
    ["Quest-ContaminationArmour", ["Arx: Seed of Power - Complete"], 3], #not actually missable, all piece can be found in arx if you missed some earlier, although if you get a piece and lose it the quest becomes incompleteable
    ["Quest-ARX_HuntingForDallis", ["Arx Outskirts: Hammerfall - Complete"], 3], #probably hammerfall
    ["Quest-ARX_HuntingForDallis_SUBA", ["Arx: Wisdom of the Keeper/The Righteous - Complete"], 3],
    ["Quest-ARX_HuntingForDallis_SUBB", ["Arx: Wisdom of the Keeper/The Righteous - Complete"], 3], #techinacally mutually exclusive
    ["Quest-ARX_KemmVault", ["Arx: The Vault of Linder Kemm - Complete"], 3],
    ["Quest-ARX_KemmVault_SUBA", ["Arx: The Second Passion of Lucian - Complete"], 3], #it does work not really sure its a quest
    ["Quest-ARX_DisappearanceOfArhu", ["Arx: Finding Lord Arhu - Complete"], 3],
    #["Quest-ARX_CreepyCraftsman", [" - Complete"], 3], #fires when giving sanders the fully charged amulet, not really a quest though. missable if you do The Righteous
    ["Quest-ARX_Barracks", ["Arx: The Last Stand of the Magisters - Complete"], 3],
    ["Quest-ARX_LV_Godslayer", ["Arx: A King Reborn - Complete"], 3],
    ["Quest-ARX_MerchantEstate_Wetwork", ["Arx: Blood Dowry - Complete"], 3],
    ["Quest-ARX_MerchantEstate_Wetwork_SUBA", ["Arx: A Son's Contract - Complete"], 3], #surpiringly fine, pops on eithers death which is required to complete the other
    ["Quest-ARX_MerchantEstate_Wetwork_SUBB", ["Arx: A Family Affair - Complete"], 3],
    ["Quest-ARX_Cathedral_Dog", ["Arx: A Most Urgent Matter - Complete"], 3],
    ["Quest-ARX_AntiqueTraders", ["Arx: Old means Gold - Complete"], 3],
    ["Quest-ARX_Neighborhood_HouseSchool", ["Arx: School's Out - Complete"], 3],
    #["Quest-ARX_Outskirts_PossessedKid", ["Arx Outskirts: Silence Broken - Complete"], 3], #missable, follows Silent as the Grave
    #["Quest-ARX_Outskirts_PossessedKid_SUBA", ["Arx Outskirts: The Purity of Divinity - Complete"], 3], #hell no
    #["Quest-ARX_Outskirts_PossessedKid_SUBB", ["Arx Outskirts: Who Am I? - Complete"], 3], #missable
    #["Quest-ARX_Outskirts_PossessedKid_SUBC", ["Arx Outskirts: A Girl and Her Demon - Complete"], 3], #missable
    ["Quest-RC_ARX_TheImperialDwarves", ["Arx: Deathfog Rising - Complete"], 3],
    ["Quest-RC_ARX_TheImperialDwarves_SUBA", ["Arx: Dwarven Politics - Complete"], 3],
    ["Quest-ARX_Prison_Windego", ["Arx: Mercy is Power - Complete"], 3],
    ["Quest-ARX_Prison_TheMistake", ["Arx: Past Mistakes - Complete"], 3],
    ["Quest-ARX_TheDoctor", ["Arx: Doctor's Orders - Complete"], 3],
    ["Quest-ARX_TheWeakening", ["Arx: Crippling a Demon - Complete"], 3],
    ["Quest-ARX_LizardConsulate", ["Arx: A Lizard Nightmare - Complete"], 3],
    ["Quest-EG", ["Tomb of Lucian: End Times - Complete", "Victory_Defeat_Braccus_Rex"], 3],
    #["Quest-ARX_DemonAmbush", [" - Complete"], 3], #probably unused
    ["Quest-ARX_Neighborhood_TheFence", ["Arx: What a Fuss to have Wrought - Complete"], 3],
    ["Quest-ARX_MissingPrisoners", ["Arx: The Missing Prisoners - Complete"], 3],
] + DOS2_KILL_LIST

LOCATION_NAME_ID_REGION = [
    ["Merryweather: Death Belowdecks - Complete", 1, "Merryweather"],
    ["Merryweather: Troubled Waters - Complete", 2, "Merryweather"],
    ["Merryweather: Voidling (27, 16)", 3, "Merryweather"],
    ["Merryweather: Voidling (28, 18)", 4, "Merryweather"],
    ["Fort Joy: Voidling (158, 325)", 5, "Fort Joy"],
    ["Fort Joy: Voidling (157, 330)", 6, "Fort Joy"],
    ["Fort Joy: Freshly Buried Corpse (225, 287)", 7, "Fort Joy"],
    ["Fort Joy: Turtle (258, 363)", 8, "Fort Joy"],
    ["Fort Joy: Ancient Turtle (271, 365)", 9, "Fort Joy"],
    ["Fort Joy: Turtle (283, 349)", 10, "Fort Joy"],
    ["Fort Joy: Saltwater Crocodile (113, 217)", 11, "Fort Joy"],
    ["Fort Joy: Saltwater Crocodile (124, 224)", 12, "Fort Joy"],
    ["Fort Joy: Saltwater Crocodile (116, 231)", 13, "Fort Joy"],
    ["Fort Joy: Charged Amphibian (528, 489)", 14, "Fort Joy"],
    ["Fort Joy: Venomous Amphibian (503, 491)", 15, "Fort Joy"],
    ["Fort Joy: Venomous Amphibian (518, 504)", 16, "Fort Joy"],
    ["Fort Joy: Gedeon, the Tenacious One (69, 562)", 17, "Fort Joy"],
    ["Fort Joy: Veerle, the Avid One (64, 566)", 18, "Fort Joy"],
    ["Fort Joy: Ailsa, the Cultured One (64, 559)", 19, "Fort Joy"],
    ["Fort Joy: Rex (72, 566)", 20, "Fort Joy"],
    ["Fort Joy: Magister Houndmaster (276, 654)", 21, "Fort Joy"],
    ["Fort Joy: Magister Swordsman (276, 651)", 22, "Fort Joy"],
    ["Fort Joy: Magister Ranger (280, 651)", 23, "Fort Joy"],
    ["Fort Joy: Magister Ranger (279, 663)", 24, "Fort Joy"],
    ["Fort Joy: Kniles the Flenser (384, 630)", 27, "Fort Joy"],
    ["Fort Joy: Meat Golem (389, 641)", 28, "Fort Joy"],
    ["Fort Joy: Meat Golem (370, 639)", 29, "Fort Joy"],
    ["Fort Joy: Meat Golem (389, 620)", 30, "Fort Joy"],
    ["Fort Joy: Agitated Silent Monk (386, 651)", 31, "Fort Joy"],
    ["Fort Joy: Agitated Silent Monk (389, 635)", 32, "Fort Joy"],
    ["Fort Joy: Agitated Silent Monk (379, 614)", 33, "Fort Joy"],
    ["Fort Joy: Magister Ranger (293, 197)", 34, "Fort Joy"],
    ["Fort Joy: Magister Swordsman (258, 164)", 35, "Fort Joy"],
    ["Fort Joy: Magister Ranger (302, 173)", 36, "Fort Joy"],
    ["Fort Joy: Magister Ranger (262, 196)", 37, "Fort Joy"],
    ["Fort Joy: Magister Swordsman (260, 198)", 38, "Fort Joy"],
    ["Fort Joy: Magister Captian Trippel (279, 196)", 40, "Fort Joy"],
    ["Fort Joy: Silent Monk (328, 224)", 41, "Fort Joy"],
    ["Fort Joy: Silent Monk (326, 224)", 42, "Fort Joy"],
    ["Fort Joy: Silent Monk (323, 224)", 43, "Fort Joy"],
    ["Fort Joy: Silent Monk (321, 224)", 44, "Fort Joy"],
    ["Fort Joy: Silent Monk (331, 224)", 45, "Fort Joy"],
    ["Fort Joy: Magister Ranger (324, 244)", 46, "Fort Joy"],
    ["Fort Joy: Magister Inquisitor (323 246)", 47, "Fort Joy"],
    ["Fort Joy: Magister Ranger (322, 244)", 48, "Fort Joy"],
    ["Fort Joy: Magister Knight (333, 235)", 49, "Fort Joy"],
    ["Fort Joy: Magister Dayve (321, 225)", 50, "Fort Joy"],
    ["Fort Joy: Magister Courtroom Swordsman (276, 139)", 51, "Fort Joy"],
    ["Fort Joy: Magister Courtroom Swordsman (289, 139)", 52, "Fort Joy"],
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
    ["Fort Joy: Magister Ellwin (337, 359)", 1000, "Fort Joy"],
    ["Fort Joy: Magister Krendt (340, 361)", 1001, "Fort Joy"],
    ["Fort Joy: Magister Swentin (340, 365)", 1002, "Fort Joy"],
    ["Fort Joy: Source Hound Phyllip (332, 367)", 1003, "Fort Joy"],
    ["East Reaper's Eye: Windego (357, 192)", 63, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Assassin (379, 152)", 64, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Swashbuckler (386, 155)", 65, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Terramancer (389, 151)", 66, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Swashbuckler (391, 206)", 67, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Markswoman (401, 213)", 68, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Marksman (396, 216)", 69, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Swashbuckler (395, 210)", 70, "East Reaper's Eye"],
    ["East Reaper's Eye: Viscous Voidling (461, 105)", 71, "East Reaper's Eye"],
    ["East Reaper's Eye: Viscous Voidling (443, 118)", 72, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling (441, 98)", 73, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling (464, 109)", 74, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling (466, 115)", 75, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling (451, 114)", 76, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling (453, 92)", 77, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling (447, 95)", 78, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling (447, 120)", 79, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling (454, 96)", 80, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling (460, 114)", 81, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling (440, 102)", 82, "East Reaper's Eye"], 
    ["East Reaper's Eye: Viscous Voidling (464, 106)", 83, "East Reaper's Eye"],
    ["East Reaper's Eye: Void Salamander (492, 94)", 84, "East Reaper's Eye"],
    ["East Reaper's Eye: Noxious Void Salamander (494, 86)", 85, "East Reaper's Eye"],
    ["East Reaper's Eye: Void Salamander (485, 82)", 86, "East Reaper's Eye"],
    ["East Reaper's Eye: Magister Inquisitor (471, 254)", 87, "East Reaper's Eye"],
    ["East Reaper's Eye: Magister Ranger (469, 253)", 88, "East Reaper's Eye"],
    ["East Reaper's Eye: Magister Ranger (464, 254)", 89, "East Reaper's Eye"],
    ["East Reaper's Eye: Magister Swordsman (462, 254)", 90, "East Reaper's Eye"],
    ["East Reaper's Eye: Magister Knight (469, 230)", 91, "East Reaper's Eye"],
    ["East Reaper's Eye: Magister Ranger (469, 228)", 92, "East Reaper's Eye"],
    ["East Reaper's Eye: Magister Swordsman (460, 231)", 93, "East Reaper's Eye"],
    ["East Reaper's Eye: Magister Ranger (460, 229)", 94, "East Reaper's Eye"],
    ["East Reaper's Eye: Incandescent Decapitator (529, 93)", 95, "East Reaper's Eye"],
    ["East Reaper's Eye: Incandescent Scorcher (539, 94)", 96, "East Reaper's Eye"],
    ["East Reaper's Eye: Incandescent Marksman (529, 100)", 97, "East Reaper's Eye"],
    ["East Reaper's Eye: Trompdoy (629, 496)", 98, "East Reaper's Eye"],
    ["East Reaper's Eye: Trompdoy (631, 482)", 99, "East Reaper's Eye"],
    ["East Reaper's Eye: Trompdoy (643, 496)", 1005, "East Reaper's Eye"],
    ["East Reaper's Eye: Trompdoy (669, 538)", 1006, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Aeromancer (494, 170)", 100, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Cryomancer (480, 159)", 101, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Swashbuckler (481, 164)", 102, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Swashbuckler (502, 167)", 103, "East Reaper's Eye"],
    ["East Reaper's Eye: Decomposing Marksman (482, 175)", 104, "East Reaper's Eye"],
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
    ["North-east Reaper's Eye: Seek and You Shall Find - Complete", 122, "North-east Reaper's Eye"],
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
    #["placeholder16", 135, "Fort Joy"],
    ["Fort Joy: The Teleporter - Complete", 136, "Fort Joy"],
    ["Fort Joy: The Shakedown - Complete", 137, "Fort Joy"],
    ["East Reaper's Eye: The Vault of Braccus Rex - Complete", 138, "East Reaper's Eye"],
    ["East Reaper's Eye: Healing Touch - Complete", 139, "East Reaper's Eye"],
    ["East Reaper's Eye: The Eternal Worshipper - Complete", 140, "East Reaper's Eye"],
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
    ["East Reaper's Eye: Most Dangerous When Cornered - Complete", 151, "East Reaper's Eye"],
    ["North-east Reaper's Eye: Threads of a Curse - Complete", 152, "North-east Reaper's Eye"],
    ["North-east Reaper's Eye: Bishop Alexander (564, 306)", 153, "North-east Reaper's Eye"],
    ["East Reaper's Eye: Hot Under the Collar - Complete", 1004, "East Reaper's Eye"],
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
    #["The Meadows: The Three Altars - Complete", 164, "The Meadows"],
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
    #["Driftwood: Grebb the Scholar - Complete", 176, "Driftwood"],
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
    ["Lady Vengence: Powerful Awakening - Complete", 188, "End Act 2"],
    ["Reaper's Bluffs: Mordus Awakens - Complete", 189, "Reaper's Bluffs"],
    ["Stonegarden: Waking Ryker - Complete", 190, "Stonegarden"],
    ["Cloisterwood: Jahan's Lesson - Complete", 191, "Cloisterwood"],
    ["Cloisterwood: Hannag's Bargin - Complete", 192, "Cloisterwood"],
    ["Bloodmoon Island: The Demon's Advocate - Complete", 193, "Bloodmoon Island"],
    ["The Cullwoods: Saheila's Reward - Complete", 194, "The Cullwoods"],
    ["Paradise Downs: Almira's Dowry - Complete", 195, "Paradise Downs"],
    ["The Blackpits: The Midnight Oil - Complete", 196, "The Blackpits"],
    ["The Meadows: Treated Like Cattle - Complete", 197, "The Meadows"],
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
    ["The Meadows: The Ugly Little Bird - Complete", 210, "The Meadows"],
    ["Stonegarden: A Prize Kill - Complete", 211, "Stonegarden"],
    ["Stonegarden: All In The Family - Complete", 212, "Stonegarden"],
    ["Stonegarden: An Existential Crisis - Complete", 213, "Stonegarden"],
    ["Stonegarden: The Reluctant Servants - Complete", 214, "Stonegarden"],
    ["The Meadows: Dark Dealings in the Blackpits - Complete", 215, "The Meadows"],
    ["The Blackpits: No Way Out - Complete", 216, "The Blackpits"],
    ["Paradise Downs: Unlikely Lovers - Complete", 217, "Paradise Downs"],
    ["Paradise Downs: Almira's Request - Complete", 218, "Paradise Downs"],
    ["Cloisterwood: A Hunter of Wicked Things - Complete", 219, "Cloisterwood"],
    #["placeholder65", 220, "Reaper's Coast"],
    ["Bloodmoon Island: The Forgotten and the Damned - Complete", 221, "Bloodmoon Island"],
    ["Bloodmoon Island: Delusions of Gradeur - Comeplete", 222, "Bloodmoon Island"],
    ["Bloodmoon Island: Silent as the Grave - Complete", 223, "Bloodmoon Island"],
    ["Bloodmoon Island: The Sweet Shackles of Pain - Complete", 224, "Bloodmoon Island"],
    ["Bloodmoon Island: Metalwork - Complete", 225, "Bloodmoon Island"],
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
    ["The Cullwoods: Burial Rites - Complete", 251, "The Cullwoods"],
    ["The Cullwoods: A Trial for All Seasons - Complete", 252, "The Cullwoods"],
    ["The Blackpits: On the Ropes - Complete", 254, "The Blackpits"],
    ["Driftwood: The Gift of the Blackroot - Complete", 255, "Driftwood"],
    ["Reaper's Coast: Viscous Voidling (423, -4)", 256, "Reaper's Coast"],
    ["Reaper's Coast: Viscous Voidling (407, 1)", 257, "Reaper's Coast"],
    ["Reaper's Coast: Viscous Voidling (408, -2)", 258, "Reaper's Coast"],
    ["Reaper's Coast: Viscous Voidling (423, -8)", 259, "Reaper's Coast"],
    ["Reaper's Coast: Volatile Voidling (425, -6)", 260, "Reaper's Coast"],
    ["Reaper's Coast: Volatile Voidling (408, 0)", 261, "Reaper's Coast"],
    ["Reaper's Coast: Silent Watcher (442, 151)", 262, "Reaper's Coast"],
    ["Reaper's Coast: Executioner Ninyan (438, 148)", 263, "Reaper's Coast"],
    ["Reaper's Coast: Venom-Wing Voidwoken (461, 157)", 264, "Reaper's Coast"],
    ["Driftwood: Viscous Voidling (222, 611)", 265, "Driftwood"],
    ["Driftwood: Viscous Voidling (226, 612)", 266, "Driftwood"],
    ["Driftwood: Viscous Voidling (221, 614)", 267, "Driftwood"],
    ["Driftwood: Volatile Voidling (227, 616)", 268, "Driftwood"],
    ["Driftwood: Volatile Voidling (230, 614)", 269, "Driftwood"],
    ["Driftwood: Volatile Voidling (223, 618)", 270, "Driftwood"],
    ["Driftwood: Volatile Voidling (227, 609)", 271, "Driftwood"],
    ["Driftwood: Volatile Voidling (211, 609)", 272, "Driftwood"],
    ["Driftwood: Volatile Voidling (212, 617)", 273, "Driftwood"],
    ["Driftwood: Volatile Voidling (217, 598)", 274, "Driftwood"],
    ["Driftwood: Volatile Voidling (235, 608)", 275, "Driftwood"],
    ["Driftwood: Volatile Voidling (236, 614)", 276, "Driftwood"],
    ["Driftwood: Volatile Voidling (235, 603)", 277, "Driftwood"],
    ["Driftwood: Jeroen, the Mindful One (414, 861)", 278, "Driftwood"],
    ["Driftwood: Kenna, the Persistent One (417, 863)", 279, "Driftwood"],
    ["Driftwood: Jada, the Rash One (415, 862)", 280, "Driftwood"],
    ["Driftwood: Layali, the Wily One (412, 861)", 281, "Driftwood"],
    ["Driftwood: Amr, the Veiled One (411, 861)", 282, "Driftwood"],
    ["Driftwood: Murga (420, 862)", 283, "Driftwood"],
    ["Driftwood: Captive Deep-Dweller (413, 855)", 284, "Driftwood"],
    ["Driftwood: Dessicated Undead (490, 828)", 285, "Driftwood"],
    ["Driftwood: Skeletal Hailcaster (496, 812)", 286, "Driftwood"],
    ["Driftwood: Skeletal Flameweaver (499, 842)", 287, "Driftwood"],
    ["Driftwood: Skeletal Graverobber (483, 826)", 288, "Driftwood"],
    ["Driftwood: Skeletal Stormbinder (513, 831)", 289, "Driftwood"],
    ["Driftwood: Skeletal Skullcrusher (496, 835)", 290, "Driftwood"],
    ["Reaper's Bluffs: Slippery Voidling (245, 50)", 291, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Slippery Voidling (246, 67)", 292, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Slippery Voidling (243, 48)", 293, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Slippery Voidling (248, 69)", 294, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Slippery Voidling (247, 62)", 295, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Voidwoken Deep-Dweller (249, 57)", 296, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Possessed Marksman (186, 108)", 297, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Possessed Elementalist (207, 95)", 298, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Possessed Summoner (161, 72)", 299, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Possessed Elementalist (171, 77)", 300, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Possessed Markswoman (165, 50)", 301, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Possessed Summoner (162, 47)", 302, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Possessed Warmaiden (111, 107)", 303, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Possessed Cleric (118, 121)", 304, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Possessed Battlemage (109, 118)", 305, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Possessed Arbalist (113, 132)", 306, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Possessed Arbalist (119, 125)", 307, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Venom-Wing Voidwoken (113, 112)", 308, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Vampiric Voidwoken (722, 671)", 309, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Vampiric Voidwoken (743, 655)", 310, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Storm-Wing Voidwoken (724, 685)", 311, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Vampiric Voidwoken (702, 676)", 312, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Cold-crawler Voidwoken (647, 607)", 313, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Cold-crawler Voidwoken (659, 656)", 314, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Possessed Rogue (672, 687)", 315, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Possessed Elementalist (674, 684)", 316, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Cold-crawler Voidwoken (717, 597)", 317, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Possessed Markswoman (738, 553)", 318, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Possessed Elementalist (725, 552)", 319, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Cold-crawler Voidwoken (656, 533)", 320, "Reaper's Bluffs"],
    ["Reaper's Bluffs: Shark (77, 782)", 321, "Reaper's Bluffs"],
    ["Cloisterwood: Old Gray Wolf (127, 273)", 322, "Cloisterwood"],
    ["Cloisterwood: Black Wolf (110, 273)", 323, "Cloisterwood"],
    ["Cloisterwood: Black Wolf (129, 267)", 324, "Cloisterwood"],
    ["Cloisterwood: Black Wolf (116, 276)", 325, "Cloisterwood"],
    ["Cloisterwood: Black Wolf (122, 262)", 326, "Cloisterwood"],
    ["Cloisterwood: Lamenting Abomination (112, 267)", 327, "Cloisterwood"],
    ["Cloisterwood: Alice Alisceon (221, 316)", 328, "Cloisterwood"],
    ["The Meadows: Enchanted Scarecrow (394, 211)", 329, "The Meadows"],
    ["The Meadows: Enchanted Scarecrow (399, 217)", 330, "The Meadows"],
    ["The Meadows: Enchanted Scarecrow (418, 194)", 331, "The Meadows"],
    ["The Meadows: Enchanted Scarecrow (416, 206)", 332, "The Meadows"],
    ["The Meadows: Restless Scarecrow (413, 199)", 333, "The Meadows"],
    ["The Meadows: Shadowcloak Skullcrusher (468, 233)", 334, "The Meadows"],
    ["The Meadows: Shadowcloak Heartpiercer (484, 227)", 335, "The Meadows"],
    ["The Meadows: Shadowcloak Deadeye (490, 230)", 336, "The Meadows"],
    ["The Meadows: Shadowcloak Deadeye (464, 216)", 337, "The Meadows"],
    ["The Meadows: Shadowcloak Spellweaver (475, 238)", 338, "The Meadows"],
    ["The Meadows: Shadowcloak Spellweaver (492, 216)", 339, "The Meadows"],
    ["The Cullwoods: Void-touched Deer (489, 261)", 340, "The Cullwoods"],
    ["The Cullwoods: Challenger of Summer (448, 346)", 341, "The Cullwoods"],
    ["The Cullwoods: Challenger of Spring (454, 340)", 342, "The Cullwoods"],
    ["The Cullwoods: Challenger of Winter (447, 335)", 343, "The Cullwoods"],
    ["The Cullwoods: Challenger of Autumn (441, 340)", 344, "The Cullwoods"],
    ["The Cullwoods: Lady (139, 751)", 345, "The Cullwoods"],
    ["The Cullwoods: Lord (145, 751)", 346, "The Cullwoods"],
    ["The Cullwoods: Roost Anlon (141, 748)", 347, "The Cullwoods"],
    ["The Cullwoods: Bodyguard (139, 743)", 348, "The Cullwoods"],
    ["The Cullwoods: Shadow (145, 743)", 349, "The Cullwoods"],
    ["The Cullwoods: Deadeye (517, 415)", 350, "The Cullwoods"],
    ["The Cullwoods: Pigsbane (507, 412)", 351, "The Cullwoods"],
    ["The Cullwoods: Naptooth (511, 412)", 352, "The Cullwoods"],
    ["The Cullwoods: Firewater (503, 415)", 353, "The Cullwoods"],
    ["The Cullwoods: Honeyhook (508, 447)", 354, "The Cullwoods"],
    ["The Cullwoods: Slumberjack (478, 442)", 355, "The Cullwoods"],
    ["The Cullwoods: Snakeroot (504, 447)", 356, "The Cullwoods"],
    ["The Cullwoods: Elixir Mixer (486, 463)", 357, "The Cullwoods"],
    ["The Cullwoods: Mummie Dearest (478, 427)", 358, "The Cullwoods"],
    ["Paradise Downs: Alchemist Looter (604, 375)", 359, "Paradise Downs"],
    ["Paradise Downs: Assassin Looter (600, 379)", 360, "Paradise Downs"],
    ["Paradise Downs: Crossbowman Looter (599, 396)", 361, "Paradise Downs"],
    ["Paradise Downs: Chief Looter (604, 396)", 362, "Paradise Downs"],
    ["Paradise Downs: Harbinger of Doom (679, 437)", 363, "Paradise Downs"],
    ["Paradise Downs: Dead Magister Knight (675, 437)", 364, "Paradise Downs"],
    ["Paradise Downs: Dead Magister Swordsman (678, 439)", 365, "Paradise Downs"],
    ["Paradise Downs: Dead Magister Knight (676, 432)", 366, "Paradise Downs"],
    ["Paradise Downs: Dead Magister Inquisitor (674, 434)", 367, "Paradise Downs"],
    ["Paradise Downs: Elder of Passing (608, 289)", 368, "Paradise Downs"],
    ["Paradise Downs: Elder of Enkindling (624, 305)", 369, "Paradise Downs"],
    ["Paradise Downs: Elder of Mending (616, 302)", 370, "Paradise Downs"],
    ["The Blackpits: Magister Knight (714, 88)", 371, "The Blackpits"],
    ["The Blackpits: Magister Ranger (711, 110)", 372, "The Blackpits"],
    ["The Blackpits: Oil Voidling (719, 72)", 373, "The Blackpits"],
    ["The Blackpits: Oil Voidling (729, 113)", 374, "The Blackpits"],
    ["The Blackpits: Oil Voidling (710, 122)", 375, "The Blackpits"],
    ["The Blackpits: Oil Voidling (705, 82)", 376, "The Blackpits"],
    ["The Blackpits: Oil Voidling (692, 86)", 377, "The Blackpits"],
    ["The Blackpits: Oil Voidling (694, 109)", 378, "The Blackpits"],
    ["The Blackpits: Primordial Oil Voidling (731, 115)", 379, "The Blackpits"],
    ["The Blackpits: Primordial Oil Voidling (693, 113)", 380, "The Blackpits"],
    ["The Blackpits: Oil Voidling (699, 80)", 381, "The Blackpits"],
    ["The Blackpits: Oil Voidling (731, 110)", 382, "The Blackpits"],
    ["The Blackpits: Oil Voidling (729, 117)", 383, "The Blackpits"],
    ["The Blackpits: Oil Voidling (692, 110)", 384, "The Blackpits"],
    ["The Blackpits: Oil Voidling (694, 85)", 385, "The Blackpits"],
    ["The Blackpits: Oil Voidling (717, 72)", 386, "The Blackpits"],
    ["The Blackpits: Primordial Fire Voidling (731, 112)", 387, "The Blackpits"],
    ["The Blackpits: Primordial Fire Voidling (695, 106)", 388, "The Blackpits"],
    ["The Blackpits: Fire Voidling (692, 107)", 389, "The Blackpits"],
    ["The Blackpits: Fire Voidling (702, 79)", 390, "The Blackpits"],
    ["The Blackpits: Fire Voidling (695, 111)", 391, "The Blackpits"],
    ["The Blackpits: Fire Voidling (718, 73)", 392, "The Blackpits"],
    ["The Blackpits: Fire Voidling (733, 111)", 393, "The Blackpits"],
    ["The Blackpits: Fire Voidling (729, 111)", 394, "The Blackpits"],
    ["The Blackpits: Magister Ranger (724, 229)", 395, "The Blackpits"],
    ["The Blackpits: Magister Axeman (731, 238)", 396, "The Blackpits"],
    ["The Blackpits: Void-touched Boar (725, 233)", 397, "The Blackpits"],
    ["The Blackpits: Venom-Wing-Voidwoken (717, 236)", 398, "The Blackpits"],
    ["The Blackpits: Void-touched Boar (729, 235)", 399, "The Blackpits"],
    ["The Blackpits: Venom-Wing-Voidwoken (725, 244)", 400, "The Blackpits"],
    ["The Blackpits: Magister Executioner (679, 173)", 401, "The Blackpits"],
    ["The Blackpits: Magister Inquisitor (679, 176)", 402, "The Blackpits"],
    ["The Blackpits: Silent Watcher (685, 176)", 403, "The Blackpits"],
    ["The Blackpits: Silent Watcher (683, 169)", 404, "The Blackpits"],
    ["The Blackpits: Magister Assassin (653, 142)", 405, "The Blackpits"],
    ["The Blackpits: Magister Inquisitor (653, 146)", 406, "The Blackpits"],
    ["The Blackpits: Magister Ranger (653, 144)", 407, "The Blackpits"],
    ["The Blackpits: Magister Grimes (679, 126)", 408, "The Blackpits"],
    ["The Blackpits: Magister Markswoman (683, 129)", 409, "The Blackpits"],
    ["The Blackpits: Magister Marksman (672, 123)", 410, "The Blackpits"],
    ["The Blackpits: Silent Watcher (351, 76)", 411, "The Blackpits"],
    ["The Blackpits: Silent Watcher (351, 82)", 412, "The Blackpits"],
    ["The Blackpits: Source Hound (623, 62)", 413, "The Blackpits"],
    ["The Blackpits: Source Hound (638, 58)", 414, "The Blackpits"],
    ["The Blackpits: Magister Vorrh (629, 60)", 415, "The Blackpits"],
    ["The Blackpits: Magister Reimond (355, 77)", 416, "The Blackpits"],
    ["The Blackpits: Armoured Voidling (290, 598)", 417, "The Blackpits"],
    #["The Blackpits: Fluorescent Voidling (309, 601)", 418, "The Blackpits"],
    #["The Blackpits: Fluorescent Voidling (295, 591)", 419, "The Blackpits"],
    ["The Blackpits: Armoured Voidling (320, 599)", 420, "The Blackpits"],
    ["The Blackpits: Armoured Voidling (313, 604)", 421, "The Blackpits"],
    ["The Blackpits: Armoured Voidling (423, 561)", 422, "The Blackpits"],
    #["The Blackpits: Fluorescent Voidling (415, 566)", 423, "The Blackpits"],
    #["The Blackpits: Fluorescent Voidling (432, 549)", 424, "The Blackpits"],
    ["The Blackpits: Armoured Voidling (409, 555)", 425, "The Blackpits"],
    ["The Blackpits: Vampiric Voidwoken (409, 550)", 426, "The Blackpits"],
    ["The Blackpits: Vampiric Voidwoken (429, 558)", 427, "The Blackpits"],
    ["The Blackpits: Magister Gremory (413, 557)", 428, "The Blackpits"],
    ["The Blackpits: Silent Watcher (416, 561)", 429, "The Blackpits"],
    ["The Blackpits: Silent Watcher (420, 547)", 430, "The Blackpits"],
    ["The Blackpits: Silent Watcher (410, 547)", 431, "The Blackpits"],
    ["The Blackpits: Weaponised Monk (472, 614)", 432, "The Blackpits"],
    ["The Blackpits: Weaponised Monk (467, 599)", 433, "The Blackpits"],
    ["The Blackpits: Magister Knight (473, 599)", 434, "The Blackpits"],
    ["The Blackpits: Silent Watcher (468, 588)", 435, "The Blackpits"],
    ["The Blackpits: Possessed Black Ring Reaver (475, 603)", 436, "The Blackpits"],
    ["The Blackpits: Possessed Black Ring Reaver (471, 604)", 437, "The Blackpits"],
    ["The Blackpits: White Magister (472, 601)", 438, "The Blackpits"],
    ["The Blackpits: Eternal Stalker (419, 673)", 439, "The Blackpits"],
    ["The Blackpits: Eternal Stalker (420, 665)", 440, "The Blackpits"],
    ["The Blackpits: Eternal Stalker (408, 673)", 441, "The Blackpits"],
    ["The Blackpits: Eternal Stalker (408, 665)", 442, "The Blackpits"],
    ["The Blackpits: The Eternal Aetera (411, 671)", 443, "The Blackpits"],
    ["Stonegarden: Vydia (584, 137)", 444, "Stonegarden"],
    ["Stonegarden: Garrick (592, 146)", 445, "Stonegarden"],
    ["Stonegarden: Halla (597, 142)", 446, "Stonegarden"],
    ["Stonegarden: Bromley (588, 133)", 447, "Stonegarden"],
    ["Stonegarden: Vydia Phase 2 (584, 137)", 448, "Stonegarden"],
    ["Stonegarden: Garrick Phase 2 (592, 146)", 449, "Stonegarden"],
    ["Stonegarden: Halla Phase 2 (597, 142)", 450, "Stonegarden"],
    ["Stonegarden: Bromley Phase 2 (588, 133)", 451, "Stonegarden"],
    ["Stonegarden: Venom-Wing Voidwoken (503, 52)", 452, "Stonegarden"],
    ["Stonegarden: Noxious Voidwoken (497, 52)", 453, "Stonegarden"],
    ["Stonegarden: Noxious Voidwoken (499, 58)", 454, "Stonegarden"],
    ["Stonegarden: Venom-Wing Voidwoken (511, 48)", 455, "Stonegarden"],
    ["Stonegarden: Andras (554, 137)", 456, "Stonegarden"],
    ["Stonegarden: Ghalann, Scion of the Elves (106, 540)", 457, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (154, 597)", 458, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (154, 595)", 459, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (152, 595)", 460, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (152, 597)", 461, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (150, 597)", 462, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (150, 595)", 463, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (154, 610)", 464, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (154, 609)", 465, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (152, 609)", 466, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (152, 610)", 467, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (150, 610)", 468, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (150, 609)", 469, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (147, 610)", 470, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (154, 594)", 471, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (152, 594)", 472, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (152, 592)", 473, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (154, 592)", 474, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (150, 594)", 475, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (150, 592)", 476, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (147, 595)", 477, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (154, 612)", 478, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (154, 614)", 479, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (152, 612)", 480, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (152, 614)", 481, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (150, 612)", 482, "Stonegarden"],
    ["Stonegarden: Clay Sentinel (150, 614)", 483, "Stonegarden"],
    ["Stonegarden: The Weaver (196, 647)", 484, "Stonegarden"],
    ["Stonegarden: Ryker (516, 181)", 485, "Stonegarden"],
    ["Bloodmoon Island: Gryst Bloodspawn (207, 415)", 486, "Bloodmoon Island"],
    ["Bloodmoon Island: Puxk Bloodspawn (224, 428)", 487, "Bloodmoon Island"],
    ["Bloodmoon Island: Lrm the Accursed (207, 429)", 488, "Bloodmoon Island"],
    ["Bloodmoon Island: Myrvl the Accursed (214, 429)", 489, "Bloodmoon Island"],
    ["Bloodmoon Island: Virkdn Spellbinder (204, 436)", 490, "Bloodmoon Island"],
    ["Bloodmoon Island: Feygr Bloodspawn (219, 435)", 491, "Bloodmoon Island"],
    ["Bloodmoon Island: Black Ring Painweaver (270, 438)", 492, "Bloodmoon Island"],
    ["Bloodmoon Island: Black Ring Fearmaiden (278, 429)", 493, "Bloodmoon Island"],
    ["Bloodmoon Island: Black Ring Painweaver (287, 438)", 494, "Bloodmoon Island"],
    ["Bloodmoon Island: Black Ring Fearmaiden (278, 447)", 495, "Bloodmoon Island"],
    ["Bloodmoon Island: Dead Black Ring Destroyer (266, 437)", 496, "Bloodmoon Island"],
    ["Bloodmoon Island: Zerachial the Accursed (390, 418)", 497, "Bloodmoon Island"],
    ["Bloodmoon Island: Kortan the Stalker (390, 425)", 498, "Bloodmoon Island"],
    ["Bloodmoon Island: Enelrahc the Baleful (388, 418)", 499, "Bloodmoon Island"],
    ["Bloodmoon Island: Huld the Stalker (395, 421)", 500, "Bloodmoon Island"],
    ["Bloodmoon Island: Quisvilius the Malevolent (393, 424)", 501, "Bloodmoon Island"],
    ["Bloodmoon Island: Possessed Dwarf (674, 851)", 502, "Bloodmoon Island"],
    ["Bloodmoon Island: Mor the Trenchmouthed (673, 852)", 503, "Bloodmoon Island"],
    ["Bloodmoon Island: Rajjarima (674, 775)", 504, "Bloodmoon Island"],
    #-- act 3 --
    #["The Nameless Isle: The Key to Freedom - Complete", 505, "The Nameless Isle"],
    ["The Nameless Isle: The Nameless Isle - Complete", 506, "The Nameless Isle"],
    #["The Nameless Isle: Helping Alexander - Complete", 507, "The Nameless Isle"],
    #["The Nameless Isle: Helping Sallow - Complete", 508, "The Nameless Isle"],
    #["The Nameless Isle: To the Belly of the Mountain - Complete", 509, "The Nameless Isle"],
    ["The Nameless Isle: Running like Clockwork - Complete", 510, "The Nameless Isle"],
    ["The Nameless Isle: The Drowned Temple - Complete", 511, "The Nameless Isle"],
    ["The Nameless Isle: Up in the Clouds - Complete", 512, "The Nameless Isle"],
    ["The Nameless Isle: The Sallow Man - Complete", 513, "The Nameless Isle"],
    #["The Nameless Isle: Thinning the Herd - Complete", 514, "The Nameless Isle"],
    #["The Nameless Isle: An Unlikely Patron - Complete", 515, "The Nameless Isle"],
    #["The Nameless Isle: A Familiar Face - Complete", 516, "The Nameless Isle"],
    #["The Nameless Isle: Seeking Revenge - Complete", 517, "The Nameless Isle"],
    ["The Nameless Isle: Invaders - Complete", 518, "The Nameless Isle"],
    ["The Nameless Isle: The Watcher's Mercy - Complete", 519, "The Nameless Isle"],
    ["The Nameless Isle: The Mother Tree - Complete", 520, "The Nameless Isle"],
    ["The Nameless Isle: Unscholarly Pursuits - Complete", 521, "The Nameless Isle"],
    ["The Nameless Isle: Proving Ground - Complete", 522, "The Nameless Isle"],
    ["The Nameless Isle: The Academy - Complete", 523, "The Nameless Isle"],
    ["The Nameless Isle: The Arena of the One - Complete", 524, "The Nameless Isle"],
    ["The Nameless Isle: Black Ring Defiler (136, 897)", 525, "The Nameless Isle"],
    ["The Nameless Isle: Black Ring Reaver (137, 902)", 526, "The Nameless Isle"],
    ["The Nameless Isle: Black Ring Painweaver (157, 943)", 527, "The Nameless Isle"],
    ["The Nameless Isle: Black Ring Defiler (166, 950)", 528, "The Nameless Isle"],
    ["The Nameless Isle: Black Ring Portalmaster (158, 963)", 529, "The Nameless Isle"],
    ["The Nameless Isle: Black Ring Captain (167, 942)", 530, "The Nameless Isle"],
    ["The Nameless Isle: Magister Inquisitor/Black Ring Defiler (191, 828)", 531, "The Nameless Isle"],
    ["The Nameless Isle: Paladin Archer/Black Ring Defiler (203, 823)", 532, "The Nameless Isle"],
    ["The Nameless Isle: Magister Priestess/Black Ring Painweaver (202, 833)", 533, "The Nameless Isle"],
    ["The Nameless Isle: Black Ring Reaver (251, 884)", 534, "The Nameless Isle"],
    ["The Nameless Isle: Forktongue (243, 878)", 535, "The Nameless Isle"],
    ["The Nameless Isle: Black Ring Painweaver (235, 888)", 536, "The Nameless Isle"],
    ["The Nameless Isle: Black Ring Fearmaiden (238, 883)", 537, "The Nameless Isle"],
    ["The Nameless Isle: Black Ring Defiler (247, 876)", 538, "The Nameless Isle"],
    ["The Nameless Isle: Black Ring Warg (246, 884)", 539, "The Nameless Isle"],
    ["The Nameless Isle: Eternal Protector (617, 254)", 540, "The Nameless Isle"],
    ["The Nameless Isle: Eternal Sentinel (626, 247)", 541, "The Nameless Isle"],
    ["The Nameless Isle: Eternal Protector (617, 236)", 542, "The Nameless Isle"],
    ["The Nameless Isle: Eternal Sentinel (607, 246)", 543, "The Nameless Isle"],
    ["The Nameless Isle: Black Ring Reaver (236, 765)", 544, "The Nameless Isle"],
    ["The Nameless Isle: Black Ring Fearmaiden (228, 765)", 545, "The Nameless Isle"],
    ["The Nameless Isle: Black Ring Alchemist (226, 770)", 546, "The Nameless Isle"],
    ["The Nameless Isle: Black Ring Quartermaster (238, 771)", 547, "The Nameless Isle"],
    ["The Nameless Isle: Wordless (231, 773)", 548, "The Nameless Isle"],
    ["The Nameless Isle: Lizard Dreamer (242, 751)", 549, "The Nameless Isle"],
    ["The Nameless Isle: Lizard Dreamer (237, 750)", 550, "The Nameless Isle"],
    ["The Nameless Isle: The Great Guardian (549, 923)", 551, "The Nameless Isle"],
    ["The Nameless Isle: Source Titan (-211, 1027)", 552, "The Nameless Isle"],
    #-- act 4 --
    ["Arx: Seed of Power - Complete", 553, "Arx"],
    ["Arx Outskirts: Hammerfall - Complete", 554, "Arx Outskirts"],
    ["Arx: Wisdom of the Keeper/The Righteous - Complete", 555, "Arx"],
    ["Arx: The Vault of Linder Kemm - Complete", 557, "Arx"],
    ["Arx: The Second Passion of Lucian - Complete", 558, "Arx"],
    ["Arx: Finding Lord Arhu - Complete", 559, "Arx"],
    ["Arx: The Last Stand of the Magisters - Complete", 560, "Arx"],
    ["Arx: A King Reborn - Complete", 561, "Arx"],
    ["Arx: Blood Dowry - Complete", 562, "Arx"],
    ["Arx: A Son's Contract - Complete", 563, "Arx"],
    ["Arx: A Family Affair - Complete", 564, "Arx"],
    ["Arx: A Most Urgent Matter - Complete", 565, "Arx"],
    ["Arx: Old means Gold - Complete", 566, "Arx"],
    ["Arx: School's Out - Complete", 567, "Arx"],
    #["Arx Outskirts: Silence Broken - Complete", 568, "Arx Outskirts"],
    #["Arx Outskirts: The Purity of Divinity - Complete", 569, "Arx Outskirts"],
    #["Arx Outskirts: Who Am I? - Complete", 570, "Arx Outskirts"],
    #["Arx Outskirts: A Girl and Her Demon - Complete", 571, "Arx Outskirts"],
    ["Arx: Deathfog Rising - Complete", 572, "Arx"],
    ["Arx: Dwarven Politics - Complete", 573, "Arx"],
    ["Arx: Mercy is Power - Complete", 574, "Arx"],
    ["Arx: Past Mistakes - Complete", 575, "Arx"],
    ["Arx: Doctor's Orders - Complete", 576, "Arx"],
    ["Arx: Crippling a Demon - Complete", 577, "Arx"],
    ["Arx: A Lizard Nightmare - Complete", 578, "Arx"],
    ["Tomb of Lucian: End Times - Complete", 579, "Tomb of Lucian"],
    ["Arx: What a Fuss to have Wrought - Complete", 580, "Arx"],
    ["Arx: The Missing Prisoners - Complete", 581, "Arx"],
    ["Arx Outskirts: Volatile Voidling (377, 1)", 582, "Arx Outskirts"],
    ["Arx Outskirts: Volatile Voidling (371, 3)", 583, "Arx Outskirts"],
    ["Arx Outskirts: Volatile Voidling (367, 1)", 584, "Arx Outskirts"],
    ["Arx Outskirts: Volatile Voidling (373, -1)", 585, "Arx Outskirts"],
    ["Arx Outskirts: Necro-Wing Voidwoken (377, -6)", 586, "Arx Outskirts"],
    ["Arx Outskirts: Necro-Wing Voidwoken (374, -15)", 587, "Arx Outskirts"],
    ["Arx Outskirts: Necro-Wing Voidwoken (360, -5)", 588, "Arx Outskirts"],
    ["Arx Outskirts: Awakened Construct (381, -18)", 589, "Arx Outskirts"],
    ["Arx Outskirts: Loic the Immaculate (356, -7)", 590, "Arx Outskirts"],
    ["Arx Outskirts: Abyssal Void Flayer (450, 136)", 591, "Arx Outskirts"],
    ["Arx Outskirts: Abyssal Void Flayer (463, 99)", 592, "Arx Outskirts"],
    ["Arx Outskirts: Abyssal Void Devourer (450, 100)", 593, "Arx Outskirts"],
    ["Arx Outskirts: Outcast Berserker (240, 74)", 594, "Arx Outskirts"],
    ["Arx Outskirts: Cuddles (242, 74)", 595, "Arx Outskirts"],
    ["Arx Outskirts: Outcast Hunter (236, 80)", 596, "Arx Outskirts"],
    ["Arx Outskirts: Featherfang (240, 81)", 597, "Arx Outskirts"],
    ["Arx Outskirts: Outcast Spellweaver (236, 62)", 598, "Arx Outskirts"],
    ["Arx Outskirts: Emberwing (236, 75)", 599, "Arx Outskirts"],
    ["Arx Outskirts: Voidwoken Bloodfury (302, 172)", 600, "Arx Outskirts"],
    ["Arx Outskirts: Vampiric Voidwoken (291, 171)", 601, "Arx Outskirts"],
    ["Arx Outskirts: Vampiric Voidwoken (291, 164)", 602, "Arx Outskirts"],
    ["Arx Outskirts: Vampiric Voidwoken (295, 163)", 603, "Arx Outskirts"],
    ["Arx Outskirts: Necro-Wing Voidwoken (282, 149)", 604, "Arx Outskirts"],
    ["Arx Outskirts: Necro-Wing Voidwoken (302, 165)", 605, "Arx Outskirts"],
    ["Arx Outskirts: Necro-Wing Voidwoken (283, 162)", 606, "Arx Outskirts"],
    ["Arx: Gheist (145, 43)", 607, "Arx"],
    ["Arx: Gheist (145, 50)", 608, "Arx"],
    ["Arx: Gheist (143, 46)", 609, "Arx"],
    ["Arx: Dorian Gall (318, 336)", 610, "Arx"],
    ["Arx: Failed Experiment (124, -39)", 611, "Arx"],
    ["Arx: Failed Experiment (112, -39)", 612, "Arx"],
    ["Arx: Failed Experiment (124, -17)", 613, "Arx"],
    ["Arx: Failed Experiment (108, -22)", 614, "Arx"],
    ["Arx: Debt Collector (379, 735)", 615, "Arx"],
    ["Arx: Debt Collector (385, 741)", 616, "Arx"],
    ["Arx: Debt Collector (376, 733)", 617, "Arx"],
    ["Arx: Sanguinia Tell (419, 298)", 618, "Arx"],
    ["Arx: Saeva the Many-faced (148, 763)", 619, "Arx"],
    ["Arx: Sahun Woundbinder (148, 735)", 620, "Arx"],
    ["Arx: Urrha the Snake Charmer (177, 753)", 621, "Arx"],
    ["Arx: Kajun Frozenheart (177, 736)", 622, "Arx"],
    ["Arx: Karon (163, 750)", 623, "Arx"],
    ["Arx: Fog-Swollen Crawler (444, 578)", 634, "Arx"],
    ["Arx: Void-touched Crawler (427, 594)", 635, "Arx"],
    ["Arx: Void-touched Crawler (458, 607)", 636, "Arx"],
    ["Arx: Fog-Swollen Crawler (443, 607)", 637, "Arx"],
    ["Arx: Isbeil (280, 672)", 638, "Arx"],
    ["Arx: Black Ring Witherknight (296, 617)", 639, "Arx"],
    ["Arx: Black Rang Flamebringer (291, 618)", 640, "Arx"],
    ["Arx: Black Ring Skullcrusher (308, 617)", 641, "Arx"],
    ["Arx: Black Ring Limbchopper (303, 617)", 642, "Arx"],
    ["Arx: Thorny Suncaller (101, 286)", 643, "Arx"],
    ["Arx: Malignant Oak (100, 271)", 644, "Arx"],
    ["Arx: Malignant Oak (99, 301)", 645, "Arx"],
    ["Arx: Hungry Flower (97, 294)", 646, "Arx"],
    ["Arx: Hungry Flower (97, 277)", 647, "Arx"],
    ["Arx: Black Ring Fearmaiden (279, 764)", 648, "Arx"],
    ["Arx: Black Ring Painweaver (267, 764)", 649, "Arx"],
    ["Arx: Black Ring Defiler (282, 751)", 650, "Arx"],
    ["Arx: Black Ring Defiler (264, 751)", 651, "Arx"],
    ["Arx: Lord Linder Kemm (325, 263)", 652, "Arx"],
    ["Arx: Cursed Revenant (174, 332)", 653, "Arx"],
    ["Arx: Cursed Revenant (193, 333)", 654, "Arx"],
    ["Arx: Cursed Revenant (182, 384)", 655, "Arx"],
    ["Arx: Cursed Revenant (170, 375)", 656, "Arx"],
    ["Arx: Cursed Revenant (190, 373)", 657, "Arx"],
    ["Arx: Bewitched Moppet (100, -82)", 658, "Arx"],
    ["Arx: Bewitched Moppet (119, -100)", 659, "Arx"],
    ["Arx: Bewitched Moppet (106, -93)", 660, "Arx"],
    ["Arx: Bewitched Moppet (105, -81)", 661, "Arx"],
    ["Arx: Bewitched Moppet (101, -96)", 662, "Arx"],
    ["Arx: Adramahlihk (387, 418)", 663, "Arx"],
    ["Arx: Nurse Do (392, 417)", 664, "Arx"],
    ["Arx: Nurse Fa (408, 382)", 665, "Arx"],
    ["Arx: Nurse Si (407, 434)", 666, "Arx"],
    ["Arx: Nurse Mi (426, 409)", 667, "Arx"],
    ["Arx: Nurse La (419, 421)", 668, "Arx"],
    ["Arx: Nurse Re (417, 397)", 669, "Arx"],
    ["Arx: Spiked Trunk (169, 132)", 670, "Arx"],
    ["Arx: Corrosive Flower (165, 124)", 671, "Arx"],
    ["Arx: Corrosive Flower (158, 140)", 672, "Arx"],
    ["Arx: Bloom of Might (152, 144)", 673, "Arx"],
    ["Arx: Bloom of Momentum (159, 136)", 674, "Arx"],
    ["Arx: Bloom of Mettle (172, 117)", 675, "Arx"],
    ["Arx: Contaminated Horror (172, 136)", 676, "Arx"],
    ["Tomb of Lucian: Braccus Rex (581, 284)", 677, "Tomb of Lucian"],
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
    theMeadows = world.get_region("The Meadows")
    theCullwoods = world.get_region("The Cullwoods")
    paradiseDowns = world.get_region("Paradise Downs")
    bloodmoonIsland = world.get_region("Bloodmoon Island")
    endAct2 = world.get_region("End Act 2")

    namelessIsle = world.get_region("The Nameless Isle")

    arxOutskirts = world.get_region("Arx Outskirts")
    arx = world.get_region("Arx")
    tombOfLucian = world.get_region("Tomb of Lucian")

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

    if(world.options.goal != world.options.goal.option_escape_reapers_eye and world.options.goal != world.options.goal.option_reapers_eye_hit_list):
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

        theMeadowsLocationNames = []
        for loc in LOCATION_NAME_ID_REGION:
            if(loc[2] == "The Meadows"):
                theMeadowsLocationNames.append(loc[0])
        theMeadowsLocations = get_location_names_with_ids(theMeadowsLocationNames)
        theMeadows.add_locations(theMeadowsLocations, DOS2Location)

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

        endAct2LocationNames = []
        for loc in LOCATION_NAME_ID_REGION:
            if(loc[2] == "End Act 2"):
                endAct2LocationNames.append(loc[0])
        endAct2Locations = get_location_names_with_ids(endAct2LocationNames)
        endAct2.add_locations(endAct2Locations, DOS2Location)

        if(world.options.goal != world.options.goal.option_leave_reapers_coast and world.options.goal != world.options.goal.option_reapers_coast_hit_list):
            namelessIsleLocationNames = []
            for loc in LOCATION_NAME_ID_REGION:
                if(loc[2] == "The Nameless Isle"):
                    namelessIsleLocationNames.append(loc[0])
            namelessIsleLocations = get_location_names_with_ids(namelessIsleLocationNames)
            namelessIsle.add_locations(namelessIsleLocations, DOS2Location)

            if(world.options.goal != world.options.goal.option_escape_the_nameless_isle and world.options.goal != world.options.goal.option_the_nameless_isle_hit_list):
                arxOutskirtsLocationNames = []
                for loc in LOCATION_NAME_ID_REGION:
                    if(loc[2] == "Arx Outskirts"):
                        arxOutskirtsLocationNames.append(loc[0])
                arxOutskirtsLocations = get_location_names_with_ids(arxOutskirtsLocationNames)
                arxOutskirts.add_locations(arxOutskirtsLocations, DOS2Location)

                arxLocationNames = []
                for loc in LOCATION_NAME_ID_REGION:
                    if(loc[2] == "Arx"):
                        arxLocationNames.append(loc[0])
                arxLocations = get_location_names_with_ids(arxLocationNames)
                arx.add_locations(arxLocations, DOS2Location)

                tombOfLucianLocationNames = []
                for loc in LOCATION_NAME_ID_REGION:
                    if(loc[2] == "Tomb of Lucian"):
                        tombOfLucianLocationNames.append(loc[0])
                tombOfLucianLocations = get_location_names_with_ids(tombOfLucianLocationNames)
                tombOfLucian.add_locations(tombOfLucianLocations, DOS2Location)



    if(world.options.goal == world.options.goal.option_escape_reapers_eye):
        finalReapersEye.add_event("Victory_Escape_Reapers_Eye", "Victory", location_type = DOS2Location, item_type = Items.DOS2Item)
    elif(world.options.goal == world.options.goal.option_leave_reapers_coast):
        ladyVengence.add_event("Victory_Leave_Reapers_Coast", "Victory", location_type = DOS2Location, item_type = Items.DOS2Item)
    elif(world.options.goal == world.options.goal.option_escape_the_nameless_isle):
        namelessIsle.add_event("Victory_Escape_The_Nameless_Isle", "Victory", location_type = DOS2Location, item_type = Items.DOS2Item)
    elif(world.options.goal == world.options.goal.option_defeat_braccus_rex):
        tombOfLucian.add_event("Victory_Defeat_Braccus_Rex", "Victory", location_type = DOS2Location, item_type = Items.DOS2Item)
    elif(world.options.goal == world.options.goal.option_reapers_eye_hit_list or world.options.goal == world.options.goal.option_reapers_coast_hit_list or world.options.goal == world.options.goal.option_the_nameless_isle_hit_list or world.options.goal == world.options.goal.option_arx_hit_list):
        fortJoy.add_event("Victory_All_Hits", "Victory", location_type = DOS2Location, item_type = Items.DOS2Item)