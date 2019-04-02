# Created by: Shijin (Kevin) Yang

# setting for the map of university of waterloo

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# color code
GREEN = (0, 204, 0)
DARK_YELLOW = (204, 204, 0)
ORANGE = (230, 114, 12)
RED = (255, 0, 0)


WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "University of Waterloo Disease Modelling"
BGCOLOR = DARKGREY

TILESIZE = 8
GRIDWIDTH = WIDTH/TILESIZE
GRIDHEIGHT = HEIGHT/TILESIZE


# faculty
faculty = {"SCI 1": 0.06,
           "SCI 2": 0.02,
           "SCI 3": 0.09,
           "MATH 1": 0.04,
           "MATH 2": 0.09,
           "MATH 3": 0.04,
           "ENV 1": 0.02,
           "ENV 2": 0.02,
           "ENV 3": 0.02,
           "ARTS 1": 0.1,
           "ARTS 2": 0.02,
           "ARTS 3": 0.1,
           "AHS 1": 0.04,
           "AHS 2": 0.01,
           "AHS 3": 0.04,
           "ENG 1": 0.11,
           "ENG 2": 0.13,
           "ENG 3": 0.06}

schedule = {"SCI 1": ["CHEM 120", "ENGL 123", "PHYS 111", "CHEM 100", "MATH 127"],
            "SCI 2": ["CHEM 120", "EARTH 121", "EARTH 123", "MATH 127", "PHYS 111"],
            "SCI 3": ["CHEM 120", "MATH 136", "MATH 137", "PHYS 121", "ENGL 193"],
            "MATH 1": ["MATH 135", "MATH 137", "CS 135", "PHYS 121", "ECON 101"],
            "MATH 2": ["MATH 135", "MATH 137", "CS 115", "SPCOM 223", "AFM 101"],
            "MATH 3": ["MATH 127", "MATH 128", "ENGL 109", "CS 135", "BIOL 130"],
            "ENV 1": ["ERS 100", "ENVS 178", "ENVS 195", "INTEG 120", "ENGL 109"],
            "ENV 2": ["AFM 131", "ENBUS 102", "ECON 101", "INDEV 100", "ENVS 105"],
            "ENV 3": ["GEOG 100", "GEOG 101", "GEOG 181", "ENVS 178", "CS 115"],
            "ARTS 1": ["ARBUS 101", "ECON 101", "ARTS 130", "ARTS 140", "CLAS 104"],
            "ARTS 2": ["GBDA 101", "ARTS 130", "ARTS 140", "CS 105", "ECON 101"],
            "ARTS 3": ["AFM 101", "BET 100", "ECON 101", "SPCOM 111", "AFM 131"],
            "AHS 1": ["HLTH 101", "AHS 107", "BIOL 130", "CHEM 120", "PSYCH 101"],
            "AHS 2": ["REC 100", "AHS 107", "REC 120", "REC 101", "PSYCH 101"],
            "AHS 3": ["KIN 104", "AHS 107", "BIOL 130", "CHEM 120", "MATH 124"],
            "ENG 1": ["CHE 100", "CHE 102", "SPCOM 111", "CHE 180", "MATH 115"],
            "ENG 2": ["MATH 135", "MATH 115", "CS 137", "MATH 117", "ECE 105"],
            "ENG 3": ["CHE 102", "MATH 116", "CIVE 104", "ENVE 100", "ENGL 191"]}

faculty_to_building = {"SCI 1": ["M3", "B1", "AHS", "DWE", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "SCI 2": ["M3", "DWE", "MC", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "SCI 3": ["M3", "MC", "B1", "RCH", "HH", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "MATH 1": ["MC", "B1", "RCH", "E2", "STP", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "MATH 2": ["MC", "B1", "PHY", "RCH", "HH", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "MATH 3": ["DWE", "E2", "MC", "EV3", "STC", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "ENV 1": ["RCH", "EV3", "EV2", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "ENV 2": ["M3", "STP", "DC", "EV3", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "ENV 3": ["DC", "PHY", "RCH", "EV2", "M3", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "ARTS 1": ["STP", "AL", "ML", "QNC", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "ARTS 2": ["STP", "ML", "QNC", "PAC", "MC", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "ARTS 3": ["STP", "HH", "DC", "RCH", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "AHS 1": ["M3", "STC", "BMH", "AHS", "PAS", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "AHS 2": ["AHS", "PAS", "STC", "OPT", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "AHS 3": ["M3", "STC", "AHS", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "ENG 1": ["RCH", "E7", "DWE", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "ENG 2": ["MC", "RCH", "E7", "MKV", "REN", "STJ", "UWP", "V1", "REV"],
                       "ENG 3": ["E7", "EIT", "CPH", "ML", "MKV", "REN", "STJ", "UWP", "V1", "REV"]} 

building_to_faculty = {"HH": ["MATH 2", "ARTS 3", "SCI 3"],
                       "DC": ["ENV 2", "ARTS 3", "ENV 3"],
                       "AHS": ["AHS 1", "AHS 2", "AHS 3", "SCI 1"],
                       "AL": ["ARTS 1"],
                       "ML": ["ARTS 1", "ARTS 2", "ENG 3"],
                       "QNC": ["ARTS 1", "ARTS 2"],
                       "PAC": ["ARTS 2", "ARTS 3"],
                       "STC": ["MATH 3", "AHS 1", "AHS 2", "AHS 3"],
                       "RCH": ["ENG 1", "ENV 1", "ENV 3", "ENG 2", "SCI 3", "MATH 1", "ARTS 3", "MATH 2"],
                       "E7": ["ENG 1", "ENG 2", "ENG 3"],
                       "DWE": ["ENG 1", "SCI 1", "SCI 2", "MATH 3"],
                       "M3": ["SCI 1", "SCI 2", "SCI 3", "AHS 1", "AHS 3", "ENV 3"],
                       "EIT": ["ENG 3"],
                       "MC": ["ARTS 2", "ENG 2", "SCI 2", "SCI 3", "MATH 1", "MATH 2", "MATH 3"],
                       "PHY": ["MATH 2", "ENV 3"],
                       "E2": ["MATH 1", "MATH 3"],
                       "STP": ["MATH 1", "ENV 2", "ARTS 1", "ARTS 2", "ARTS 3"],
                       "EV3": ["ENV 2", "MATH 3", "ENV 1"],
                       "CPH": ["ENG 3"],
                       "EV2": ["ENV 3", "ENV 1"],
                       "BMH": ["AHS 1"],
                       "B1": ["SCI 1", "SCI 2", "SCI 3", "MATH 1", "MATH 2"],
                       "PAS": ["AHS 1", "AHS 2"],
                       "OPT": ["AHS 2"],
                       
                       "MKV": ["SCI 1", "SCI 2", "SCI 3",
                               "MATH 1", "MATH 2", "MATH 3",
                               "AHS 1", "AHS 2", "AHS 3",
                               "ARTS 1", "ARTS 2", "ARTS 3",
                               "ENG 1", "ENG 2", "ENG 3",
                               "ENV 1", "ENV 2", "ENV 3"],
                       "REN": ["SCI 1", "SCI 2", "SCI 3",
                               "MATH 1", "MATH 2", "MATH 3",
                               "AHS 1", "AHS 2", "AHS 3",
                               "ARTS 1", "ARTS 2", "ARTS 3",
                               "ENG 1", "ENG 2", "ENG 3",
                               "ENV 1", "ENV 2", "ENV 3"],
                       "STJ": ["SCI 1", "SCI 2", "SCI 3",
                               "MATH 1", "MATH 2", "MATH 3",
                               "AHS 1", "AHS 2", "AHS 3",
                               "ARTS 1", "ARTS 2", "ARTS 3",
                               "ENG 1", "ENG 2", "ENG 3",
                               "ENV 1", "ENV 2", "ENV 3"],
                       "UWP": ["SCI 1", "SCI 2", "SCI 3",
                               "MATH 1", "MATH 2", "MATH 3",
                               "AHS 1", "AHS 2", "AHS 3",
                               "ARTS 1", "ARTS 2", "ARTS 3",
                               "ENG 1", "ENG 2", "ENG 3",
                               "ENV 1", "ENV 2", "ENV 3"],
                       "V1": ["SCI 1", "SCI 2", "SCI 3",
                               "MATH 1", "MATH 2", "MATH 3",
                               "AHS 1", "AHS 2", "AHS 3",
                               "ARTS 1", "ARTS 2", "ARTS 3",
                               "ENG 1", "ENG 2", "ENG 3",
                               "ENV 1", "ENV 2", "ENV 3"],
                       "REV": ["SCI 1", "SCI 2", "SCI 3",
                               "MATH 1", "MATH 2", "MATH 3",
                               "AHS 1", "AHS 2", "AHS 3",
                               "ARTS 1", "ARTS 2", "ARTS 3",
                               "ENG 1", "ENG 2", "ENG 3",
                               "ENV 1", "ENV 2", "ENV 3"]}
