# coding: utf-8
# Copyright 2016 Thomas Schatz, Xuan-Nga Cao, Mathieu Bernard
#
# This file is part of abkhazia: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abkhazia is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with abkhazia. If not, see <http://www.gnu.org/licenses/>.

"""Japanese specific preprocessing for the GlobalPhone corpus

    This does not apply directly to the raw corpus. Instead
    a cleaned-up version is needed (see perceptual-tuning
    notes in Thomas's Ulysses).
    The cleaning steps should be integrated with this file. Probably
    to be done for spock/scorpus though as it should make it more
    convenient to associate several files, including some
    light data files, to a single recipe than with
    present abkhazia.
"""

import abkhazia.utils as utils
from abkhazia.corpus.prepare.globalphone_abstract_preparator import (
    AbstractGlobalPhonePreparator)


class JapanesePreparator(AbstractGlobalPhonePreparator):
    """Japanese specific preprocessing for the GlobalPhone corpus"""
    language = 'Japanese'

    name = '-'.join([AbstractGlobalPhonePreparator.name, language]).lower()

    transcription_key = 'rmn'

    exclude_wavs = ['JA001_13', 'JA001_15', 'JA001_16', 'JA001_20', 'JA001_26',
                    'JA001_29', 'JA001_32', 'JA001_33', 'JA001_34', 'JA001_41',
                    'JA001_50', 'JA001_54', 'JA001_56', 'JA001_6', 'JA001_62',
                    'JA001_67', 'JA001_68', 'JA001_72', 'JA001_74', 'JA001_78',
                    'JA001_8', 'JA001_80', 'JA001_85', 'JA001_91', 'JA002_101',
                    'JA002_103', 'JA002_104', 'JA002_107', 'JA002_110',
                    'JA002_18', 'JA002_19', 'JA002_23', 'JA002_27', 'JA002_28',
                    'JA002_30', 'JA002_34', 'JA002_38', 'JA002_47', 'JA002_54',
                    'JA002_56', 'JA002_58', 'JA002_59', 'JA002_6', 'JA002_7',
                    'JA002_70', 'JA002_71', 'JA002_72', 'JA002_73', 'JA002_74',
                    'JA002_83', 'JA002_84', 'JA002_86', 'JA002_87', 'JA002_88',
                    'JA002_89', 'JA002_90', 'JA002_93', 'JA002_96', 'JA002_97',
                    'JA002_99', 'JA003_15', 'JA003_17', 'JA003_21', 'JA003_24',
                    'JA003_31', 'JA003_34', 'JA003_5', 'JA003_53', 'JA003_55',
                    'JA003_61', 'JA004_13', 'JA004_14', 'JA004_19', 'JA004_47',
                    'JA004_51', 'JA004_53', 'JA004_54', 'JA004_55', 'JA004_64',
                    'JA004_67', 'JA004_72', 'JA004_85', 'JA004_86', 'JA004_9',
                    'JA005_101', 'JA005_102', 'JA005_105', 'JA005_109',
                    'JA005_11', 'JA005_110', 'JA005_113', 'JA005_114',
                    'JA005_115', 'JA005_129', 'JA005_132', 'JA005_138',
                    'JA005_142', 'JA005_143', 'JA005_15', 'JA005_16',
                    'JA005_2', 'JA005_23', 'JA005_24', 'JA005_25', 'JA005_26',
                    'JA005_27', 'JA005_28', 'JA005_29', 'JA005_3', 'JA005_30',
                    'JA005_35', 'JA005_40', 'JA005_42', 'JA005_45', 'JA005_46',
                    'JA005_5', 'JA005_53', 'JA005_55', 'JA005_62', 'JA005_63',
                    'JA005_64', 'JA005_65', 'JA005_69', 'JA005_7', 'JA005_70',
                    'JA005_74', 'JA005_76', 'JA005_79', 'JA005_99', 'JA006_10',
                    'JA006_23', 'JA006_37', 'JA006_44', 'JA006_45', 'JA006_46',
                    'JA006_5', 'JA006_55', 'JA006_9', 'JA007_15', 'JA007_19',
                    'JA007_21', 'JA007_27', 'JA007_29', 'JA007_33', 'JA007_48',
                    'JA007_56', 'JA007_61', 'JA007_64', 'JA007_65', 'JA007_68',
                    'JA008_14', 'JA008_25', 'JA008_29', 'JA009_10', 'JA009_12',
                    'JA009_21', 'JA009_23', 'JA009_24', 'JA009_26', 'JA009_44',
                    'JA009_48', 'JA009_50', 'JA009_51', 'JA009_52', 'JA009_53',
                    'JA009_54', 'JA009_62', 'JA009_67', 'JA009_68', 'JA009_69',
                    'JA009_71', 'JA009_72', 'JA009_97', 'JA009_98', 'JA009_99',
                    'JA010_15', 'JA010_16', 'JA010_23', 'JA010_25', 'JA010_28',
                    'JA010_32', 'JA010_35', 'JA010_40', 'JA010_48', 'JA010_56',
                    'JA010_57', 'JA010_58', 'JA010_62', 'JA010_64', 'JA010_71',
                    'JA010_74', 'JA010_76', 'JA010_77', 'JA011_20', 'JA011_38',
                    'JA011_54', 'JA011_55', 'JA012_29', 'JA012_3', 'JA012_32',
                    'JA012_42', 'JA012_45', 'JA012_48', 'JA012_49', 'JA012_51',
                    'JA012_6', 'JA012_62', 'JA012_63', 'JA012_7', 'JA013_15',
                    'JA013_16', 'JA013_2', 'JA013_3', 'JA013_36', 'JA013_37',
                    'JA013_4', 'JA013_40', 'JA013_41', 'JA013_48', 'JA013_53',
                    'JA013_56', 'JA013_60', 'JA013_67', 'JA013_79', 'JA013_83',
                    'JA013_92', 'JA015_19', 'JA015_23', 'JA015_26', 'JA015_33',
                    'JA015_42', 'JA015_45', 'JA015_58', 'JA015_61', 'JA015_66',
                    'JA015_69', 'JA015_73', 'JA015_81', 'JA016_28', 'JA016_29',
                    'JA016_32', 'JA016_4', 'JA016_42', 'JA016_43', 'JA016_53',
                    'JA016_54', 'JA016_8', 'JA017_3', 'JA017_53', 'JA017_57',
                    'JA017_62', 'JA017_64', 'JA018_22', 'JA018_40', 'JA018_49',
                    'JA018_50', 'JA018_52', 'JA018_7', 'JA018_8', 'JA019_4',
                    'JA019_59', 'JA019_69', 'JA019_71', 'JA019_76', 'JA019_77',
                    'JA020_26', 'JA020_31', 'JA020_38', 'JA020_47', 'JA020_50',
                    'JA020_56', 'JA020_58', 'JA020_66', 'JA020_77', 'JA020_8',
                    'JA020_81', 'JA021_13', 'JA022_20', 'JA023_70', 'JA023_8',
                    'JA024_1', 'JA024_3', 'JA024_30', 'JA024_34', 'JA024_37',
                    'JA024_39', 'JA024_46', 'JA024_49', 'JA024_56', 'JA025_21',
                    'JA026_105', 'JA026_17', 'JA026_21', 'JA026_24',
                    'JA026_27', 'JA026_30', 'JA026_41', 'JA026_45', 'JA026_53',
                    'JA026_56', 'JA026_58', 'JA026_68', 'JA026_78', 'JA026_8',
                    'JA026_84', 'JA026_86', 'JA027_10', 'JA027_24', 'JA027_25',
                    'JA027_31', 'JA027_33', 'JA027_58', 'JA027_8', 'JA028_10',
                    'JA028_11', 'JA028_20', 'JA028_22', 'JA028_26', 'JA028_31',
                    'JA028_33', 'JA028_34', 'JA028_37', 'JA028_4', 'JA028_45',
                    'JA028_47', 'JA028_48', 'JA028_51', 'JA028_52', 'JA028_56',
                    'JA028_61', 'JA029_14', 'JA029_20', 'JA029_24', 'JA029_25',
                    'JA029_27', 'JA029_35', 'JA029_36', 'JA029_49', 'JA029_6',
                    'JA029_61', 'JA029_7', 'JA030_103', 'JA030_105',
                    'JA030_11', 'JA030_111', 'JA030_112', 'JA030_116',
                    'JA030_19', 'JA030_20', 'JA030_24', 'JA030_25', 'JA030_28',
                    'JA030_3', 'JA030_31', 'JA030_32', 'JA030_36', 'JA030_46',
                    'JA030_58', 'JA030_66', 'JA030_67', 'JA030_68', 'JA030_77',
                    'JA030_80', 'JA030_86', 'JA030_87', 'JA030_90', 'JA030_92',
                    'JA030_94', 'JA030_95', 'JA030_98', 'JA031_13', 'JA031_2',
                    'JA031_32', 'JA031_37', 'JA031_42', 'JA031_44', 'JA032_10',
                    'JA032_25', 'JA032_52', 'JA032_57', 'JA032_65', 'JA032_67',
                    'JA032_68', 'JA033_1', 'JA033_15', 'JA033_19', 'JA033_24',
                    'JA033_28', 'JA033_30', 'JA033_31', 'JA033_4', 'JA033_40',
                    'JA033_43', 'JA033_51', 'JA033_56', 'JA033_58', 'JA033_6',
                    'JA033_61', 'JA033_66', 'JA034_18', 'JA034_3', 'JA034_47',
                    'JA034_5', 'JA034_55', 'JA034_57', 'JA034_80', 'JA035_36',
                    'JA035_54', 'JA035_59', 'JA035_83', 'JA036_101',
                    'JA036_19', 'JA036_3', 'JA036_31', 'JA036_34', 'JA036_4',
                    'JA036_41', 'JA036_44', 'JA036_45', 'JA036_5', 'JA036_51',
                    'JA036_52', 'JA036_54', 'JA036_60', 'JA036_62', 'JA036_67',
                    'JA036_72', 'JA036_73', 'JA036_77', 'JA036_78', 'JA036_80',
                    'JA036_83', 'JA036_85', 'JA036_88', 'JA036_92', 'JA036_95',
                    'JA037_11', 'JA037_12', 'JA037_13', 'JA037_15', 'JA037_17',
                    'JA037_25', 'JA037_4', 'JA037_44', 'JA037_45', 'JA037_46',
                    'JA037_47', 'JA037_49', 'JA037_55', 'JA037_56', 'JA037_59',
                    'JA037_6', 'JA037_60', 'JA037_61', 'JA037_72', 'JA037_75',
                    'JA037_76', 'JA037_77', 'JA038_22', 'JA038_25', 'JA038_5',
                    'JA039_1', 'JA039_11', 'JA039_12', 'JA039_15', 'JA039_18',
                    'JA039_25', 'JA039_47', 'JA039_49', 'JA039_51', 'JA039_62',
                    'JA039_70', 'JA039_71', 'JA039_73', 'JA039_74', 'JA039_80',
                    'JA039_83', 'JA040_4', 'JA040_42', 'JA040_43', 'JA040_48',
                    'JA040_5', 'JA040_53', 'JA040_55', 'JA040_56', 'JA040_58',
                    'JA040_68', 'JA040_73', 'JA040_77', 'JA040_78',
                    'JA041_100', 'JA041_103', 'JA041_104', 'JA041_105',
                    'JA041_12', 'JA041_14', 'JA041_19', 'JA041_24', 'JA041_30',
                    'JA041_34', 'JA041_37', 'JA041_40', 'JA041_45', 'JA041_51',
                    'JA041_57', 'JA041_67', 'JA041_69', 'JA041_71', 'JA041_77',
                    'JA041_78', 'JA041_81', 'JA041_86', 'JA041_87', 'JA041_88',
                    'JA041_90', 'JA041_95', 'JA042_17', 'JA042_21', 'JA042_24',
                    'JA042_35', 'JA042_39', 'JA042_40', 'JA042_59', 'JA042_65',
                    'JA043_31', 'JA043_69', 'JA043_82', 'JA044_113',
                    'JA044_114', 'JA044_120', 'JA044_24', 'JA044_25',
                    'JA044_26', 'JA044_27', 'JA044_28', 'JA044_29', 'JA044_30',
                    'JA044_38', 'JA044_39', 'JA044_42', 'JA044_43', 'JA044_51',
                    'JA044_52', 'JA044_68', 'JA044_69', 'JA044_70', 'JA044_71',
                    'JA044_82', 'JA044_83', 'JA044_88', 'JA044_89', 'JA044_90',
                    'JA044_93', 'JA044_94', 'JA045_3', 'JA045_4', 'JA046_1',
                    'JA046_3', 'JA046_6', 'JA046_7', 'JA048_14', 'JA048_35',
                    'JA048_5', 'JA049_103', 'JA049_113', 'JA049_2', 'JA049_26',
                    'JA049_27', 'JA049_30', 'JA049_33', 'JA049_35', 'JA049_38',
                    'JA049_48', 'JA049_51', 'JA049_57', 'JA049_62', 'JA049_7',
                    'JA049_73', 'JA049_75', 'JA049_8', 'JA049_95', 'JA049_96',
                    'JA049_98', 'JA049_99', 'JA050_19', 'JA050_40', 'JA050_74',
                    'JA050_80', 'JA051_1', 'JA051_15', 'JA051_17', 'JA051_21',
                    'JA051_22', 'JA051_24', 'JA051_26', 'JA051_33', 'JA051_35',
                    'JA051_40', 'JA051_42', 'JA051_43', 'JA051_45', 'JA051_48',
                    'JA051_50', 'JA051_53', 'JA051_54', 'JA051_59', 'JA051_6',
                    'JA051_61', 'JA051_65', 'JA051_66', 'JA051_68', 'JA051_74',
                    'JA051_78', 'JA051_80', 'JA051_87', 'JA051_9', 'JA052_50',
                    'JA052_69', 'JA053_10', 'JA053_15', 'JA053_23', 'JA053_26',
                    'JA053_29', 'JA053_3', 'JA053_30', 'JA053_31', 'JA053_33',
                    'JA053_34', 'JA053_36', 'JA053_39', 'JA053_40', 'JA053_45',
                    'JA053_46', 'JA053_47', 'JA053_49', 'JA053_57', 'JA053_62',
                    'JA053_68', 'JA053_71', 'JA053_75', 'JA053_8', 'JA053_80',
                    'JA053_82', 'JA053_83', 'JA054_22', 'JA054_25', 'JA054_30',
                    'JA054_31', 'JA054_37', 'JA054_45', 'JA054_53', 'JA054_6',
                    'JA054_65', 'JA054_67', 'JA055_17', 'JA055_2', 'JA055_21',
                    'JA055_25', 'JA055_26', 'JA055_40', 'JA055_42', 'JA055_44',
                    'JA055_45', 'JA055_47', 'JA055_52', 'JA055_53', 'JA055_58',
                    'JA055_63', 'JA055_64', 'JA055_66', 'JA055_7', 'JA055_70',
                    'JA055_71', 'JA055_72', 'JA055_73', 'JA055_76', 'JA055_77',
                    'JA055_8', 'JA055_80', 'JA055_81', 'JA055_82', 'JA055_85',
                    'JA055_89', 'JA055_9', 'JA055_92', 'JA056_11', 'JA056_21',
                    'JA056_26', 'JA056_29', 'JA056_33', 'JA056_4', 'JA056_45',
                    'JA056_53', 'JA056_57', 'JA056_58', 'JA056_61', 'JA056_62',
                    'JA056_74', 'JA056_76', 'JA057_10', 'JA057_13', 'JA057_16',
                    'JA057_2', 'JA057_21', 'JA057_24', 'JA057_25', 'JA057_28',
                    'JA057_3', 'JA057_30', 'JA057_33', 'JA057_34', 'JA057_39',
                    'JA057_4', 'JA057_41', 'JA057_43', 'JA057_46', 'JA057_48',
                    'JA057_51', 'JA057_52', 'JA057_53', 'JA057_57', 'JA057_6',
                    'JA057_61', 'JA057_63', 'JA057_68', 'JA057_8', 'JA057_9',
                    'JA059_14', 'JA059_15', 'JA059_16', 'JA059_23', 'JA059_26',
                    'JA059_3', 'JA059_39', 'JA059_41', 'JA059_43', 'JA059_45',
                    'JA059_49', 'JA059_56', 'JA059_60', 'JA059_63', 'JA059_7',
                    'JA059_72', 'JA060_107', 'JA060_43', 'JA060_52',
                    'JA060_75', 'JA060_76', 'JA060_81', 'JA060_82', 'JA060_85',
                    'JA060_94', 'JA061_11', 'JA061_17', 'JA061_2', 'JA061_20',
                    'JA061_4', 'JA061_57', 'JA061_61', 'JA061_7', 'JA061_84',
                    'JA061_89', 'JA062_11', 'JA062_20', 'JA062_49', 'JA062_50',
                    'JA062_7', 'JA062_9', 'JA063_24', 'JA063_84', 'JA063_87',
                    'JA066_17', 'JA066_44', 'JA066_59', 'JA066_6', 'JA067_13',
                    'JA067_15', 'JA067_16', 'JA067_20', 'JA067_22', 'JA067_29',
                    'JA067_33', 'JA067_35', 'JA067_36', 'JA067_38', 'JA067_43',
                    'JA067_44', 'JA067_45', 'JA067_47', 'JA067_5', 'JA067_50',
                    'JA067_52', 'JA067_54', 'JA067_55', 'JA067_56', 'JA067_59',
                    'JA067_61', 'JA067_62', 'JA067_63', 'JA067_64', 'JA067_67',
                    'JA067_68', 'JA067_69', 'JA067_70', 'JA067_8', 'JA068_49',
                    'JA069_21', 'JA069_45', 'JA069_7', 'JA069_8', 'JA070_14',
                    'JA070_15', 'JA070_21', 'JA070_22', 'JA070_3', 'JA070_33',
                    'JA070_38', 'JA070_39', 'JA070_4', 'JA070_47', 'JA070_53',
                    'JA070_57', 'JA070_58', 'JA070_59', 'JA070_64', 'JA070_67',
                    'JA070_68', 'JA070_7', 'JA070_71', 'JA070_77', 'JA070_8',
                    'JA070_81', 'JA070_88', 'JA070_90', 'JA071_31', 'JA071_55',
                    'JA071_57', 'JA071_62', 'JA071_70', 'JA073_13', 'JA073_15',
                    'JA073_16', 'JA073_24', 'JA073_27', 'JA073_3', 'JA073_38',
                    'JA073_40', 'JA073_51', 'JA073_52', 'JA073_53', 'JA073_7',
                    'JA073_9', 'JA074_16', 'JA074_20', 'JA074_24', 'JA074_25',
                    'JA074_28', 'JA074_37', 'JA074_42', 'JA074_43', 'JA074_45',
                    'JA074_47', 'JA074_5', 'JA074_50', 'JA074_51', 'JA074_52',
                    'JA074_56', 'JA074_57', 'JA074_59', 'JA074_6', 'JA074_7',
                    'JA075_1', 'JA075_2', 'JA075_3', 'JA076_103', 'JA076_13',
                    'JA076_14', 'JA076_25', 'JA076_27', 'JA076_3', 'JA076_55',
                    'JA076_83', 'JA076_87', 'JA077_10', 'JA077_16', 'JA077_28',
                    'JA077_31', 'JA077_51', 'JA077_59', 'JA077_64', 'JA077_65',
                    'JA077_8', 'JA078_1', 'JA078_103', 'JA078_107',
                    'JA078_110', 'JA078_112', 'JA078_116', 'JA078_120',
                    'JA078_121', 'JA078_123', 'JA078_16', 'JA078_17',
                    'JA078_19', 'JA078_2', 'JA078_20', 'JA078_22', 'JA078_23',
                    'JA078_24', 'JA078_27', 'JA078_28', 'JA078_3', 'JA078_39',
                    'JA078_4', 'JA078_43', 'JA078_44', 'JA078_6', 'JA078_60',
                    'JA078_62', 'JA078_66', 'JA078_7', 'JA078_73', 'JA078_83',
                    'JA078_90', 'JA078_93', 'JA078_95', 'JA078_98', 'JA079_13',
                    'JA079_22', 'JA079_33', 'JA079_36', 'JA079_74',
                    'JA080_101', 'JA080_12', 'JA080_16', 'JA080_18',
                    'JA080_19', 'JA080_20', 'JA080_26', 'JA080_27', 'JA080_3',
                    'JA080_30', 'JA080_32', 'JA080_33', 'JA080_37', 'JA080_38',
                    'JA080_39', 'JA080_4', 'JA080_40', 'JA080_41', 'JA080_47',
                    'JA080_48', 'JA080_49', 'JA080_50', 'JA080_51', 'JA080_59',
                    'JA080_6', 'JA080_60', 'JA080_61', 'JA080_62', 'JA080_63',
                    'JA080_64', 'JA080_65', 'JA080_66', 'JA080_67', 'JA080_69',
                    'JA080_7', 'JA080_71', 'JA080_72', 'JA080_74', 'JA080_79',
                    'JA080_8', 'JA080_82', 'JA080_84', 'JA080_85', 'JA080_89',
                    'JA080_90', 'JA080_94', 'JA080_95', 'JA080_98', 'JA080_99',
                    'JA081_17', 'JA081_21', 'JA081_26', 'JA081_3', 'JA081_30',
                    'JA081_32', 'JA081_34', 'JA081_37', 'JA081_38', 'JA081_58',
                    'JA081_66', 'JA081_7', 'JA081_74', 'JA081_76', 'JA081_80',
                    'JA083_16', 'JA083_17', 'JA083_66', 'JA084_1', 'JA085_15',
                    'JA085_16', 'JA085_4', 'JA085_53', 'JA085_80', 'JA086_17',
                    'JA086_18', 'JA086_58', 'JA086_59', 'JA086_6', 'JA087_101',
                    'JA087_12', 'JA087_4', 'JA087_40', 'JA087_53', 'JA087_63',
                    'JA088_13', 'JA088_15', 'JA088_62', 'JA089_1', 'JA089_2',
                    'JA089_3', 'JA089_38', 'JA089_39', 'JA089_44', 'JA089_45',
                    'JA089_46', 'JA089_47', 'JA089_67', 'JA089_7', 'JA089_77',
                    'JA089_78', 'JA089_88', 'JA089_89', 'JA089_90', 'JA089_91',
                    'JA091_20', 'JA091_53', 'JA091_62', 'JA091_63', 'JA091_64',
                    'JA091_69', 'JA092_22', 'JA092_62', 'JA094_1', 'JA094_2',
                    'JA094_3', 'JA094_58', 'JA094_72', 'JA095_8', 'JA096_12',
                    'JA096_62', 'JA097_19', 'JA097_59', 'JA098_25', 'JA099_11',
                    'JA099_33', 'JA099_40', 'JA099_6', 'JA100_103',
                    'JA100_113', 'JA100_119', 'JA100_14', 'JA100_18',
                    'JA100_69', 'JA100_72', 'JA100_79', 'JA100_83',
                    'JA102_102', 'JA102_110', 'JA102_17', 'JA102_20',
                    'JA102_21', 'JA102_24', 'JA102_60', 'JA102_63', 'JA102_69',
                    'JA102_77', 'JA103_19', 'JA103_4', 'JA104_19', 'JA104_26',
                    'JA104_33', 'JA104_6', 'JA106_43', 'JA107_10', 'JA107_22',
                    'JA107_25', 'JA108_38', 'JA108_4', 'JA108_41', 'JA108_48',
                    'JA108_58', 'JA109_14', 'JA109_22', 'JA109_35', 'JA109_36',
                    'JA109_40', 'JA109_43', 'JA109_51', 'JA109_54', 'JA109_68',
                    'JA109_69', 'JA109_73', 'JA109_76', 'JA109_82',
                    'JA110_100', 'JA110_12', 'JA110_30', 'JA110_31',
                    'JA110_45', 'JA110_52', 'JA110_68', 'JA110_74', 'JA110_76',
                    'JA110_82', 'JA110_88', 'JA110_90', 'JA111_16', 'JA111_23',
                    'JA111_25', 'JA111_38', 'JA111_39', 'JA111_49', 'JA111_50',
                    'JA111_53', 'JA111_56', 'JA111_57', 'JA111_8', 'JA111_89',
                    'JA112_11', 'JA112_14', 'JA112_22', 'JA112_25', 'JA112_36',
                    'JA112_40', 'JA112_57', 'JA112_60', 'JA112_69', 'JA112_73',
                    'JA113_18', 'JA113_19', 'JA113_22', 'JA113_25', 'JA113_26',
                    'JA113_39', 'JA113_4', 'JA113_42', 'JA113_44', 'JA113_46',
                    'JA113_48', 'JA113_52', 'JA113_54', 'JA113_56', 'JA113_62',
                    'JA113_65', 'JA113_67', 'JA113_68', 'JA113_71', 'JA113_9',
                    'JA114_3', 'JA114_43', 'JA114_45', 'JA114_51', 'JA114_52',
                    'JA114_54', 'JA114_55', 'JA115_14', 'JA115_15', 'JA115_17',
                    'JA115_20', 'JA115_21', 'JA115_24', 'JA115_26', 'JA115_27',
                    'JA115_29', 'JA115_3', 'JA115_31', 'JA115_32', 'JA115_34',
                    'JA115_35', 'JA115_37', 'JA115_38', 'JA115_39', 'JA115_51',
                    'JA115_52', 'JA115_55', 'JA115_59', 'JA115_6', 'JA115_60',
                    'JA115_62', 'JA115_63', 'JA115_68', 'JA115_70', 'JA115_73',
                    'JA115_79', 'JA115_8', 'JA116_20', 'JA116_3', 'JA116_52',
                    'JA116_7', 'JA117_11', 'JA117_16', 'JA117_32', 'JA117_40',
                    'JA117_52', 'JA117_56', 'JA117_57', 'JA117_61', 'JA117_62',
                    'JA118_18', 'JA118_23', 'JA118_24', 'JA118_28', 'JA118_29',
                    'JA118_38', 'JA118_4', 'JA118_8', 'JA201_10', 'JA201_100',
                    'JA201_103', 'JA201_105', 'JA201_111', 'JA201_112',
                    'JA201_113', 'JA201_114', 'JA201_115', 'JA201_121',
                    'JA201_122', 'JA201_124', 'JA201_126', 'JA201_127',
                    'JA201_130', 'JA201_134', 'JA201_135', 'JA201_136',
                    'JA201_137', 'JA201_138', 'JA201_14', 'JA201_140',
                    'JA201_141', 'JA201_142', 'JA201_144', 'JA201_146',
                    'JA201_149', 'JA201_15', 'JA201_150', 'JA201_152',
                    'JA201_153', 'JA201_155', 'JA201_156', 'JA201_158',
                    'JA201_159', 'JA201_16', 'JA201_160', 'JA201_19',
                    'JA201_2', 'JA201_23', 'JA201_27', 'JA201_29', 'JA201_34',
                    'JA201_36', 'JA201_39', 'JA201_41', 'JA201_42', 'JA201_44',
                    'JA201_45', 'JA201_47', 'JA201_49', 'JA201_5', 'JA201_52',
                    'JA201_53', 'JA201_55', 'JA201_56', 'JA201_58', 'JA201_59',
                    'JA201_6', 'JA201_63', 'JA201_65', 'JA201_66', 'JA201_67',
                    'JA201_68', 'JA201_71', 'JA201_72', 'JA201_73', 'JA201_74',
                    'JA201_76', 'JA201_8', 'JA201_80', 'JA201_82', 'JA201_83',
                    'JA201_88', 'JA201_89', 'JA201_9', 'JA201_92', 'JA201_94',
                    'JA201_97', 'JA202_106', 'JA202_107', 'JA202_110',
                    'JA202_111', 'JA202_113', 'JA202_120', 'JA202_126',
                    'JA202_127', 'JA202_132', 'JA202_133', 'JA202_135',
                    'JA202_136', 'JA202_138', 'JA202_14', 'JA202_140',
                    'JA202_141', 'JA202_142', 'JA202_145', 'JA202_17',
                    'JA202_18', 'JA202_19', 'JA202_2', 'JA202_20', 'JA202_21',
                    'JA202_26', 'JA202_28', 'JA202_29', 'JA202_35', 'JA202_45',
                    'JA202_46', 'JA202_51', 'JA202_52', 'JA202_53', 'JA202_54',
                    'JA202_6', 'JA202_62', 'JA202_63', 'JA202_64', 'JA202_65',
                    'JA202_66', 'JA202_67', 'JA202_7', 'JA202_70', 'JA202_72',
                    'JA202_73', 'JA202_76', 'JA202_79', 'JA202_80', 'JA202_83',
                    'JA202_85', 'JA202_86', 'JA202_88', 'JA202_89', 'JA202_9',
                    'JA202_91', 'JA202_94', 'JA202_95', 'JA202_96', 'JA202_98',
                    'JA202_99', 'JA203_10', 'JA203_103', 'JA203_104',
                    'JA203_11', 'JA203_114', 'JA203_117', 'JA203_12',
                    'JA203_121', 'JA203_124', 'JA203_126', 'JA203_13',
                    'JA203_14', 'JA203_15', 'JA203_16', 'JA203_2', 'JA203_54',
                    'JA203_55', 'JA203_57', 'JA203_58', 'JA203_62', 'JA203_66',
                    'JA203_67', 'JA203_69', 'JA203_70', 'JA203_71', 'JA203_73',
                    'JA203_77', 'JA203_78', 'JA203_80', 'JA203_82', 'JA203_83',
                    'JA203_90', 'JA203_97', 'JA203_98', 'JA203_99',
                    'JA204_102', 'JA204_103', 'JA204_104', 'JA204_105',
                    'JA204_11', 'JA204_114', 'JA204_115', 'JA204_14',
                    'JA204_2', 'JA204_25', 'JA204_47', 'JA204_8', 'JA204_88',
                    'JA204_9', 'JA204_90', 'JA204_97', 'JA205_1', 'JA205_100',
                    'JA205_103', 'JA205_108', 'JA205_111', 'JA205_113',
                    'JA205_114', 'JA205_119', 'JA205_120', 'JA205_121',
                    'JA205_130', 'JA205_131', 'JA205_133', 'JA205_136',
                    'JA205_139', 'JA205_150', 'JA205_151', 'JA205_152',
                    'JA205_155', 'JA205_162', 'JA205_166', 'JA205_17',
                    'JA205_19', 'JA205_2', 'JA205_24', 'JA205_29', 'JA205_30',
                    'JA205_4', 'JA205_41', 'JA205_42', 'JA205_45', 'JA205_47',
                    'JA205_50', 'JA205_51', 'JA205_55', 'JA205_58', 'JA205_60',
                    'JA205_63', 'JA205_67', 'JA205_70', 'JA205_71', 'JA205_75',
                    'JA205_76', 'JA205_79', 'JA205_8', 'JA205_80', 'JA205_96',
                    'JA205_97', 'JA205_99', 'JA206_1', 'JA206_2', 'JA206_3',
                    'JA206_4', 'JA207_1', 'JA207_100', 'JA207_105',
                    'JA207_106', 'JA207_116', 'JA207_125', 'JA207_138',
                    'JA207_139', 'JA207_14', 'JA207_141', 'JA207_143',
                    'JA207_148', 'JA207_153', 'JA207_160', 'JA207_20',
                    'JA207_22', 'JA207_23', 'JA207_27', 'JA207_31', 'JA207_37',
                    'JA207_38', 'JA207_4', 'JA207_43', 'JA207_49', 'JA207_5',
                    'JA207_56', 'JA207_59', 'JA207_60', 'JA207_9', 'JA207_90',
                    'JA207_92', 'JA207_93', 'JA207_96', 'JA209_1', 'JA209_100',
                    'JA209_103', 'JA209_108', 'JA209_111', 'JA209_113',
                    'JA209_115', 'JA209_116', 'JA209_124', 'JA209_133',
                    'JA209_15', 'JA209_20', 'JA209_27', 'JA209_30', 'JA209_33',
                    'JA209_36', 'JA209_38', 'JA209_39', 'JA209_41', 'JA209_43',
                    'JA209_49', 'JA209_51', 'JA209_57', 'JA209_60', 'JA209_64',
                    'JA209_75', 'JA209_80', 'JA209_88', 'JA209_91', 'JA209_92',
                    'JA209_94', 'JA209_98', 'JA210_100', 'JA210_109',
                    'JA210_112', 'JA210_114', 'JA210_118', 'JA210_12',
                    'JA210_14', 'JA210_20', 'JA210_22', 'JA210_26', 'JA210_27',
                    'JA210_29', 'JA210_3', 'JA210_31', 'JA210_34', 'JA210_36',
                    'JA210_40', 'JA210_45', 'JA210_56', 'JA210_59', 'JA210_71',
                    'JA210_73', 'JA210_79', 'JA210_81', 'JA210_83', 'JA210_84',
                    'JA210_86', 'JA210_87', 'JA210_89', 'JA210_92', 'JA210_93',
                    'JA210_98', 'JA210_99', 'JA211_104', 'JA211_106',
                    'JA211_109', 'JA211_118', 'JA211_125', 'JA211_128',
                    'JA211_16', 'JA211_17', 'JA211_18', 'JA211_31', 'JA211_32',
                    'JA211_33', 'JA211_35', 'JA211_37', 'JA211_45', 'JA211_46',
                    'JA211_48', 'JA211_5', 'JA211_57', 'JA211_8', 'JA211_82',
                    'JA211_89', 'JA211_9', 'JA211_91', 'JA211_99', 'JA212_15',
                    'JA212_30', 'JA212_41', 'JA212_44', 'JA212_51', 'JA212_52',
                    'JA212_55', 'JA212_59', 'JA212_6', 'JA212_63', 'JA212_64',
                    'JA212_72', 'JA212_74', 'JA212_8', 'JA212_80', 'JA212_82',
                    'JA212_86', 'JA212_94', 'JA213_1', 'JA213_10', 'JA213_101',
                    'JA213_102', 'JA213_104', 'JA213_105', 'JA213_113',
                    'JA213_118', 'JA213_13', 'JA213_17', 'JA213_18', 'JA213_2',
                    'JA213_21', 'JA213_23', 'JA213_25', 'JA213_27', 'JA213_35',
                    'JA213_36', 'JA213_37', 'JA213_39', 'JA213_4', 'JA213_40',
                    'JA213_42', 'JA213_44', 'JA213_53', 'JA213_56', 'JA213_57',
                    'JA213_60', 'JA213_61', 'JA213_64', 'JA213_67', 'JA213_69',
                    'JA213_71', 'JA213_76', 'JA213_77', 'JA213_8', 'JA213_81',
                    'JA213_82', 'JA213_84', 'JA213_88', 'JA213_9', 'JA213_93',
                    'JA213_95', 'JA213_99', 'JA214_1', 'JA214_10', 'JA214_100',
                    'JA214_102', 'JA214_104', 'JA214_120', 'JA214_121',
                    'JA214_124', 'JA214_127', 'JA214_13', 'JA214_130',
                    'JA214_134', 'JA214_136', 'JA214_138', 'JA214_139',
                    'JA214_140', 'JA214_22', 'JA214_25', 'JA214_26',
                    'JA214_29', 'JA214_30', 'JA214_31', 'JA214_36', 'JA214_39',
                    'JA214_42', 'JA214_44', 'JA214_45', 'JA214_54', 'JA214_57',
                    'JA214_60', 'JA214_63', 'JA214_67', 'JA214_75', 'JA214_76',
                    'JA214_87', 'JA214_94', 'JA214_95', 'JA214_97',
                    'JA215_101', 'JA215_102', 'JA215_105', 'JA215_106',
                    'JA215_111', 'JA215_113', 'JA215_120', 'JA215_125',
                    'JA215_128', 'JA215_131', 'JA215_133', 'JA215_134',
                    'JA215_135', 'JA215_138', 'JA215_17', 'JA215_34',
                    'JA215_39', 'JA215_4', 'JA215_40', 'JA215_45', 'JA215_46',
                    'JA215_55', 'JA215_57', 'JA215_58', 'JA215_64', 'JA215_66',
                    'JA215_7', 'JA215_72', 'JA215_73', 'JA215_74', 'JA215_79',
                    'JA215_81', 'JA215_83', 'JA215_84', 'JA215_86', 'JA215_98',
                    'JA216_104', 'JA216_106', 'JA216_112', 'JA216_114',
                    'JA216_116', 'JA216_120', 'JA216_123', 'JA216_127',
                    'JA216_133', 'JA216_136', 'JA216_138', 'JA216_144',
                    'JA216_145', 'JA216_22', 'JA216_26', 'JA216_28',
                    'JA216_30', 'JA216_33', 'JA216_37', 'JA216_39', 'JA216_47',
                    'JA216_5', 'JA216_50', 'JA216_56', 'JA216_61', 'JA216_65',
                    'JA216_69', 'JA216_72', 'JA216_85', 'JA216_91', 'JA216_92',
                    'JA216_99', 'JA217_10', 'JA217_100', 'JA217_101',
                    'JA217_102', 'JA217_104', 'JA217_105', 'JA217_11',
                    'JA217_117', 'JA217_118', 'JA217_119', 'JA217_120',
                    'JA217_123', 'JA217_125', 'JA217_132', 'JA217_134',
                    'JA217_137', 'JA217_138', 'JA217_14', 'JA217_141',
                    'JA217_143', 'JA217_144', 'JA217_146', 'JA217_157',
                    'JA217_159', 'JA217_160', 'JA217_18', 'JA217_19',
                    'JA217_20', 'JA217_21', 'JA217_23', 'JA217_24', 'JA217_25',
                    'JA217_27', 'JA217_28', 'JA217_31', 'JA217_32', 'JA217_36',
                    'JA217_46', 'JA217_5', 'JA217_51', 'JA217_59', 'JA217_6',
                    'JA217_61', 'JA217_62', 'JA217_63', 'JA217_65', 'JA217_72',
                    'JA217_8', 'JA217_82', 'JA217_84', 'JA217_86', 'JA217_88',
                    'JA217_89', 'JA217_90', 'JA217_91', 'JA217_92', 'JA217_93',
                    'JA217_99', 'JA218_107', 'JA218_11', 'JA218_110',
                    'JA218_117', 'JA218_125', 'JA218_132', 'JA218_141',
                    'JA218_22', 'JA218_23', 'JA218_26', 'JA218_27', 'JA218_29',
                    'JA218_31', 'JA218_34', 'JA218_38', 'JA218_42', 'JA218_43',
                    'JA218_51', 'JA218_56', 'JA218_60', 'JA218_65', 'JA218_67',
                    'JA218_73', 'JA218_77', 'JA218_8', 'JA218_90', 'JA219_105',
                    'JA219_109', 'JA219_11', 'JA219_112', 'JA219_113',
                    'JA219_114', 'JA219_115', 'JA219_119', 'JA219_121',
                    'JA219_122', 'JA219_127', 'JA219_133', 'JA219_142',
                    'JA219_143', 'JA219_148', 'JA219_149', 'JA219_151',
                    'JA219_154', 'JA219_17', 'JA219_19', 'JA219_20',
                    'JA219_21', 'JA219_24', 'JA219_28', 'JA219_32', 'JA219_34',
                    'JA219_35', 'JA219_36', 'JA219_39', 'JA219_4', 'JA219_47',
                    'JA219_48', 'JA219_49', 'JA219_50', 'JA219_56', 'JA219_6',
                    'JA219_69', 'JA219_73', 'JA219_79', 'JA219_8', 'JA219_89',
                    'JA219_93', 'JA219_96', 'JA219_98', 'JA220_115',
                    'JA220_119', 'JA220_39', 'JA220_45', 'JA220_47',
                    'JA220_55', 'JA221_101', 'JA221_108', 'JA221_113',
                    'JA221_27', 'JA221_3', 'JA221_52', 'JA221_54', 'JA221_58',
                    'JA221_63', 'JA221_66', 'JA221_67', 'JA221_80', 'JA221_9',
                    'JA222_100', 'JA222_103', 'JA222_105', 'JA222_106',
                    'JA222_112', 'JA222_33', 'JA222_54', 'JA222_55',
                    'JA222_57', 'JA222_68', 'JA222_69', 'JA222_82', 'JA222_89',
                    'JA222_91', 'JA222_96', 'JA222_99', 'JA223_100',
                    'JA223_101', 'JA223_102', 'JA223_103', 'JA223_32',
                    'JA223_92', 'JA223_93', 'JA223_94', 'JA223_95', 'JA223_96',
                    'JA223_97', 'JA223_98', 'JA223_99', 'JA224_101',
                    'JA224_103', 'JA224_19', 'JA224_21', 'JA224_22',
                    'JA224_23', 'JA224_26', 'JA224_29', 'JA224_35', 'JA224_37',
                    'JA224_41', 'JA224_42', 'JA224_46', 'JA224_48', 'JA224_67',
                    'JA224_7', 'JA224_70', 'JA224_80', 'JA224_82', 'JA224_85',
                    'JA224_87', 'JA224_9', 'JA224_92', 'JA224_94', 'JA224_99',
                    'JA225_100', 'JA225_107', 'JA225_108', 'JA225_114',
                    'JA225_27', 'JA225_3', 'JA225_30', 'JA225_33', 'JA225_43',
                    'JA225_45', 'JA225_60', 'JA225_68', 'JA225_70', 'JA225_82',
                    'JA225_87', 'JA226_114', 'JA226_119', 'JA226_21',
                    'JA226_29', 'JA226_54', 'JA226_61', 'JA226_76', 'JA226_83',
                    'JA226_84', 'JA226_87', 'JA226_89', 'JA226_97', 'JA228_11',
                    'JA228_12', 'JA228_13', 'JA228_17', 'JA228_18', 'JA228_2',
                    'JA228_20', 'JA228_25', 'JA228_26', 'JA228_27', 'JA228_28',
                    'JA228_3', 'JA228_30', 'JA228_32', 'JA228_33', 'JA228_34',
                    'JA228_35', 'JA228_36', 'JA228_37', 'JA228_40', 'JA228_43',
                    'JA228_6', 'JA228_7', 'JA228_9']

    # https://docs.google.com/spreadsheets/d/1a4ZWvuKfe2wMd_sVOid3KLY7PqKQkPe1uYNa_7zC5Gw/edit?pli=1#gid=0
    # with C+glide considered as two separate phonemes

    vowels = {
        'a': u'??',
        'e': u'e',
        'i': u'i',
        'o': u'o',
        'u': u'??',
        'a+H': u'??:',
        'e+H': u'e:',
        'i+H': u'i:',
        'o+H': u'o:',
        'u+H': u'??:'
    }

    consonants = {
        'w': u'w',
        'y': u'j',
        'm': u'm',
        'n': u'n',
        'N': u'??',
        'd': u'd',
        't': u't',
        'Q+t': u't:',
        'c': u't??s',
        'c+y': u't????',
        'Q+c+y': u't????:',
        's': u's',
        'Q+s': u's:',
        's+y': u'??',
        'Q+s+y': u'??:',
        'z': u'z',  # fricative or affricate
        'z+y': u'??',  # fricative or affricate
        'F': u'??',
        'h': u'h',
        'g': u'g',
        'k': u'k',
        'Q+k': u'k:',
        'p': u'p',
        'Q+p': u'p:',
        'r': u'r',
        'b': u'b',
        # infrequent phones
        'Q+c': u't??s:',
        'Q+g': u'g:',
        'Q+h': u'h:',
        'Q+d': u'd:',
        'Q+z': u'z:',  # fricative or affricate
        'Q+z+y': u'??:',  # fricative or affricate
        'Q+F': u'??:',
        'Q+b': u'b:'
    }

    """
    Frequencies of the various phones in the corpus
    produced by this recipe, before dropping infrequent
    phones:

        [('a', 1244643),
         ('o', 930707),
         ('i', 809173),
         ('e', 624466),
         ('k', 535058),
         ('n', 518087),
         ('u', 499639),
         ('t', 445306),
         ('m', 337715),
         ('r', 326103),
         ('s', 297367),
         ('d', 285754),
         ('N', 276768),
         ('o+H', 189680),
         ('s+y', 186292),
         ('y', 164743),
         ('g', 162616),
         ('Q+t', 108847),
         ('w', 108092),
         ('h', 92601),
         ('u+H', 82833),
         ('e+H', 81238),
         ('z+y', 76611),
         ('b', 72008),
         ('c+y', 60997),
         ('c', 54208),
         ('z', 36106),
         ('a+H', 31660),
         ('i+H', 23952),
         ('F', 20939),
         ('Q+k', 18819),
         ('p', 13239),
         ('Q+p', 10359),
         ('Q+s+y', 4791),
         ('Q+s', 4062),
         ('Q+c+y', 2851),
         ('Q+c', 1155),
         ('Q+d', 276),
         ('Q+g', 125),
         ('Q+F', 116),
         ('Q+h', 84),
         ('Q+z+y', 56),
         ('Q+z', 24),
         ('Q+b', 16)]

    Infrequent phones are removed from the corpus in a subsequent step.
    """

    # phones are vowels and consonants
    phones = utils.merge_dicts(vowels, consonants)

    silences = []

    variants = []
