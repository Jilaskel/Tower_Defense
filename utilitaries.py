import pygame
from globals import * 

pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional

loading_progress = Loading_progress()
global_status = Global_status()

RUNNING = True

DEV_MODE = False  # activate shortcuts, see README
TURN_OFF_NATURAL_SPAWNING = False

############### RESOLUTION
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
# WINDOW_WIDTH = 1920*0.75
# WINDOW_HEIGHT = 1080*0.75

RESIZE_COEFF = WINDOW_WIDTH/1920

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

############### GAME
GAME_TITLE = "You Shall Not Pass"
GAME_ICON_PATH = "Assets/game_icon.png"

pygame.display.set_caption(GAME_TITLE)
pygame_icon = pygame.image.load(GAME_ICON_PATH)
pygame.display.set_icon(pygame_icon)

################## FPS
FPS = 60
CLOCK = pygame.time.Clock() 
TOTAL_NUMBER_RENDERING_LAYER = 25

##############################################################

############### BACKGROUND

##############################################################

BACKGROUND_IMAGE_PATH = "Assets/Background/BackgroundNoGrassAsset.png"
BACKGROUND_GRASS_ASSETS_PATH = "Assets/Background/GrassAsset/"
BACKGROUND_WALLS_ASSETS_PATH = "Assets/Background/Walls/"
BACKGROUND_SQUARE_SIDE = WINDOW_HEIGHT/8.0

##############################################################

############### FONT

##############################################################

FONT_PATH = "Font/Kingcastle-0W8Kr.ttf"
# LOADING_FONT_PATH = "Font/DragonFire-K7voy.ttf"
LOADING_FONT_PATH = "Font/misc/Balgruf-d256.woff"

##############################################################

############### GOLD

##############################################################

GOLD_STARTING_AMOUNT = 12
GOLD_EARNING_WITH_TIME = 0 # per seconds
GOLD_TOWER_REFUND_COEFF = 0.5

GOLD_GAIN_IMAGE_PATH = "Assets/Gold/GoldGain.png"    
GOLD_RESERVE_IMAGE_PATH = "Assets/Gold/GoldReserve.png"  ## useless atm
GOLD_GAIN_RESIZE_FACTOR = 0.125*RESIZE_COEFF
GOLD_GAIN_FONT_SIZE = 25*RESIZE_COEFF
GOLD_GAIN_POSITIVE_RGB = (0,0,153)
GOLD_GAIN_NEGATIVE_RGB = (153,0,0)
GOLD_GAIN_OFFSET = [0*RESIZE_COEFF, 0*RESIZE_COEFF]  ## offset with the center of the object
GOLD_GAIN_TIME = 2000  # in ms
GOLD_GAIN_TRAVEL_VECTOR = [0*RESIZE_COEFF, -100*RESIZE_COEFF] 

##############################################################

############### ERROR MESSAGE

##############################################################

ERROR_MESSAGE_IMAGE_PATH = "Assets/Error/error.png"
ERROR_MESSAGE_RGB = (153,0,0)
ERROR_MESSAGE_RESIZE_FACTOR = 0.1*RESIZE_COEFF
ERROR_MESSAGE_FONT_SIZE = 25*RESIZE_COEFF
ERROR_MESSAGE_OFFSET = [0*RESIZE_COEFF, 0*RESIZE_COEFF]
ERROR_MESSAGE_TIME = 2000
ERROR_MESSAGE_TRAVEL_VECTOR = [0*RESIZE_COEFF, -100*RESIZE_COEFF]

##############################################################

############### MOUSE

##############################################################

MOUSE_IMAGE_PATH = "Assets/Cursor/cursor6.png"
MOUSE_RESIZE_FACTOR = 0.4*RESIZE_COEFF
MOUSE_RATIO_FOR_HITBOX = 1.0

MOUSE_CARRIED_IMAGE_ALPHA = 100
MOUSE_OVER_ENLARGED_COEFF = 1.5

MOUSE_VALID_BOX_IMAGE_PATH = "Assets/Tower/Valid_boxes/valid.png"
MOUSE_VALID_BOX_IMAGE_ALPHA = 150
MOUSE_NOT_VALID_BOX_IMAGE_PATH = "Assets/Tower/Valid_boxes/not_valid.png"
MOUSE_NOT_VALID_BOX_IMAGE_ALPHA = 150
MOUSE_BOX_BORDER_IMAGE_PATH = "Assets/Tower/Valid_boxes/box_border_1.png"

##############################################################

############### STARTING MENU

##############################################################

STARTING_MENU_PANNEL_PATH = "Assets/Menu/Buttons/starting_menu_pannel.png"
STARTING_MENU_BUTTON_1_PATH = "Assets/Menu/Buttons/starting_menu_button.png"
STARTING_MENU_BUTTON_2_PATH = "Assets/Menu/Buttons/starting_menu_button_2.png"

STARTING_MOUSE_OVER_ENLARGED_COEFF = 1.25

##############################################################

############### PAUSE MENU

##############################################################

PAUSE_MENU_BACKGROUND = "Assets/Menu/pause_menu_background.png"

##############################################################

############### MENU

##############################################################

# MENU_BUTTON_SIZE = [BACKGROUND_SQUARE_SIDE,BACKGROUND_SQUARE_SIDE]
MENU_BUTTON_SIZE = [BACKGROUND_SQUARE_SIDE*0.75,BACKGROUND_SQUARE_SIDE*0.75]
MENU_ARCANE_TOWER_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/arcane_tower_button.png"
MENU_ARCANE_TOWER_LVL2_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/arcane_tower_lvl2_button.png"
MENU_ARCANE_TOWER_LVL3_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/arcane_tower_lvl3_button.png"
MENU_FIRE_TOWER_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/fire_tower_button.png"
MENU_FIRE_TOWER_LVL2_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/fire_tower_lvl2_button.png"
MENU_FIRE_TOWER_LVL3_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/fire_tower_lvl3_button.png"
MENU_LIGHTNING_TOWER_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/lightning_tower_button.png"
MENU_LIGHTNING_TOWER_LVL2_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/lightning_tower_lvl2_button.png"
MENU_LIGHTNING_TOWER_LVL3_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/lightning_tower_lvl3_button.png"
MENU_ICE_TOWER_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/ice_tower_button.png"
MENU_ICE_TOWER_LVL2_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/ice_tower_lvl2_button.png"
MENU_ICE_TOWER_LVL3_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/ice_tower_lvl3_button.png"
MENU_BALLISTA_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/ballista_button.png"
MENU_CATAPULT_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/catapult_button.png"

MENU_MENU_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/menu_button.png"

MENU_GOLD_RESERVE_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/gold_reserve_button.png"
MENU_GOLD_RESERVE_BUTTON_RESIZE_FACTOR = 0.33*RESIZE_COEFF
MENU_SCORE_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/score_button_empty.png"
MENU_SCORE_BUTTON_RESIZE_FACTOR = 0.30*RESIZE_COEFF
MENU_SELECTION_IMAGE_PATH = "Assets/Menu/Buttons/menu_selection.png"
# MENU_SELECTION_RESIZE_FACTOR = 0.15*RESIZE_COEFF
MENU_SELECTION_SIZE = [BACKGROUND_SQUARE_SIDE*2.8,BACKGROUND_SQUARE_SIDE*0.9]

MENU_DESTROY_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/menu_destroy.png"
MENU_UPGRADE_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/menu_bar_upgrade.png"
MENU_LVL_MAX_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/menu_bar.png"

##############################################################

############### ENNEMIES SPAWNING 

##############################################################

SPAWNING_MARGIN_SPACE = 0.1   ## *background.bush_width
INITIAL_SPAWNING_TIME = 10.0

TIME_BETWEEN_ROUNDS = 15.0 # in seconds
ROUND_DISPLAY_TIME = 4.0

LAST_ROUND_HP_COEFF_PER_SEC = 0.1  # after the end of last round duration, the coeff will increase of this amount each second
LAST_ROUND_DAMAGE_COEFF_PER_SEC = 0.1  # after the end of last round duration, the coeff will increase of this amount each second
LAST_ROUND_VELOCITY_COEFF_PER_SEC = 0.1  # after the end of last round duration, the coeff will increase of this amount each second

spawning_coeff = Spawning_coeff()

SPAWNING_DICT = {
    "R1"  : {

        "HP_COEFF" : 1.0,
        "DAMAGE_COEFF" : 1.0,
        "VELOCITY_COEFF" : 1.0,

        "PHASES": {
            "P1": {
                "DURATION" : 15,  ## in seconds
                "BLUE_SKEL_PERIOD" : 3.4,   ## in seconds
                "RED_SKEL_PERIOD" : 6.4   ## in seconds
                # "MIN_BLUE_SKEL_SIMULTANEOUSLY" : 3,
                # "MAX_RED_SKEL_SIMULTANEOUSLY" : 1

            },

            "P2" : {
                "DURATION" : 15,  ## in seconds
                "GOBLIN_PERIOD" : 5.0,   ## in seconds
                "RED_SKEL_PERIOD" : 3.4,   ## in seconds
                "GREEN_SKEL_PERIOD" : 6.4  ## in seconds
            },

            "P3" : {
                "DURATION" : 15,  ## in seconds
                "GOBLIN_PERIOD" : 3.0,   ## in seconds
                "BLUE_SKEL_PERIOD" : 5.6,   ## in seconds
                "GREEN_SKEL_PERIOD" : 4.4  ## in seconds
            },

            "P4" : {
                "DURATION" : 15,  ## in seconds
                "OGRE_PERIOD" : 5.0,   ## in seconds
                "GOBLIN_PERIOD" : 3.0,   ## in seconds
                "BLUE_SKEL_PERIOD" : 7.3,   ## in seconds
                "RED_SKEL_PERIOD" : 6.0,   ## in seconds
                "GREEN_SKEL_PERIOD" : 4.8,  ## in seconds
            }
        }
    },
    "R2"  : {
        "HP_COEFF" : 1.0,
        "DAMAGE_COEFF" : 1.0,
        "VELOCITY_COEFF" : 1.0,

        "PHASES": {
            "P1": {
                "DURATION" : 15,  ## in seconds
                "GOBLIN_PERIOD" : 1.9,   ## in seconds
                "OGRE_PERIOD" : 2.8,   ## in seconds
                "BLUE_NEC_PERIOD" : 3.8  ## in seconds
            },

            "P2" : {
                "DURATION" : 15,  ## in seconds
                "GOBLIN_PERIOD" : 1.9,   ## in seconds
                "OGRE_PERIOD" : 3.3,   ## in seconds
                "BLUE_NEC_PERIOD" : 3.2,   ## in seconds
                "RED_NEC_PERIOD" : 6.0   ## in seconds
            },

            "P3" : {
                "DURATION" : 15,  ## in seconds
                "GOBLIN_PERIOD" : 1.9,   ## in seconds
                "OGRE_PERIOD" : 3.3,   ## in seconds
                "RED_NEC_PERIOD" : 3.4,   ## in seconds
                "GREEN_NEC_PERIOD" : 4.6   ## in seconds
            },

            "P4" : {
                "DURATION" : 15,  ## in seconds
                "GOBLIN_PERIOD" : 1.9,   ## in seconds
                "OGRE_PERIOD" : 3.3,   ## in seconds
                "BLUE_NEC_PERIOD" : 3.4,   ## in seconds
                "RED_NEC_PERIOD" : 2.7,   ## in seconds
                "GREEN_NEC_PERIOD" : 4.6   ## in seconds
            }

        }
    },
    "R3"  : {
        "HP_COEFF" : 1.6,
        "DAMAGE_COEFF" : 1.0,
        "VELOCITY_COEFF" : 1.1,

        "PHASES": {
            "P1": {
                "DURATION" : 2,  ## in seconds
                "KAMIKAZE_PERIOD" : 1 ## in seconds
            },

            "P2": {
                "DURATION" : 15,  ## in seconds
                "GOBLIN_PERIOD" : 1.5,   ## in seconds
                "OGRE_PERIOD" : 3.0,   ## in seconds
                "KAMIKAZE_PERIOD" : 3.4, ## in seconds
                "RED_NEC_PERIOD" : 2.2   ## in seconds
            },

            "P3": {
                "DURATION" : 15,  ## in seconds
                "GOBLIN_PERIOD" : 2.0,   ## in seconds
                "OGRE_PERIOD" : 4.0,   ## in seconds
                "KAMIKAZE_PERIOD" : 2.7, ## in seconds
                "BLUE_NEC_PERIOD" : 2.3,   ## in seconds
                "RED_NEC_PERIOD" : 3.1   ## in seconds
                #"GREEN_NEC_PERIOD" : 4.6   ## in seconds
                #"DRAGON_PERIOD" : 7.0,  ## in seconds

            },

            "P4": {
                "DURATION" : 15,  ## in seconds
                "GOBLIN_PERIOD" : 2.0,   ## in seconds
                "OGRE_PERIOD" : 4.0,   ## in seconds
                "KAMIKAZE_PERIOD" : 4.0, ## in seconds
                "BLUE_NEC_PERIOD" : 4.4,   ## in seconds
                "RED_NEC_PERIOD" : 3.7,   ## in seconds
                "GREEN_NEC_PERIOD" : 2.6   ## in seconds
                #"DRAGON_PERIOD" : 7.0,  ## in seconds

            },

            "P5": {
                "DURATION" : 15,  ## in seconds
                "GOBLIN_PERIOD" : 2.0,   ## in seconds
                "OGRE_PERIOD" : 4.0,   ## in seconds
                "KAMIKAZE_PERIOD" : 3.7, ## in seconds
                "BLUE_NEC_PERIOD" : 3.4,   ## in seconds
                "RED_NEC_PERIOD" : 2.7,   ## in seconds
                "GREEN_NEC_PERIOD" : 4.6,   ## in seconds
                "DRAGON_PERIOD" : 7.5  ## in seconds
            },

            "P6": {
                "DURATION" : 2.0,  ## in seconds
                "BLUE_NEC_PERIOD" : 1.0,   ## in seconds
                "RED_NEC_PERIOD" : 1.0,   ## in seconds
                "GREEN_NEC_PERIOD" : 1.0,   ## in seconds
                "DRAGON_PERIOD" : 1.0  ## in seconds
            },

                        "P7": {
                "DURATION" : 10.0,  ## in seconds
                "DRAGON_PERIOD" : 1.4  ## in seconds
            }
        }
    },
    "R4"  : {
        "HP_COEFF" : 2.0,
        "DAMAGE_COEFF" : 1.2,
        "VELOCITY_COEFF" : 1.2,

        "PHASES": {
            "P1": {
                "DURATION" : 15,  ## in seconds
                "GOBLIN_PERIOD" : 2.0,   ## in seconds
                "OGRE_PERIOD" : 4.0,   ## in seconds
                "KAMIKAZE_PERIOD" : 3.7, ## in seconds
                "BLUE_NEC_PERIOD" : 3.4,   ## in seconds
                "RED_NEC_PERIOD" : 2.7,   ## in seconds
                "GREEN_NEC_PERIOD" : 4.6,   ## in seconds
                "DRAGON_PERIOD" : 5.0  ## in seconds

        }
     }
    }

}


##############################################################

###############     BASE     ###############

##############################################################

BASE_GATE_HP_MAX = 150

##############################################################

###############     ENNEMIES     ###############

##############################################################

#### GOBLIN
GOBLIN_DICT = {

"NAME" : "Goblin",
"HP_MAX" : 10.0,
"DAMAGE" : 3,
"VELOCITY" : 0.1 * RESIZE_COEFF, # pixel by ms
"GOLD_EARNING" : 4,

"HITBOX_FACTOR" : 1.0,
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF, #   pixel
"OFFSET" : [50* RESIZE_COEFF,-20* RESIZE_COEFF], 
"CENTER_VECTOR" : [0.26, 0.63],

"WALKING_IMAGE_PATH" : "Assets/Ennemies/Goblin/WalkAnim/",
"NUMBER_FRAME_WALKING" : 20,
"ANIMATION_WALKING_TOTAL_TIME" : 600, # in ms
"STOP_WALKING_FRAME" : 11,

"NUMBER_FRAME_TRANSITION" : 1,
"TRANSITION_IMAGE_PATH" : "Assets/Ennemies/Goblin/TransitionAnim/",
"ANIMATION_TRANSITION_TOTAL_TIME" : 300, # in ms

"NUMBER_FRAME_ATTACKING" : 10,
"ATTACKING_IMAGE_PATH" : "Assets/Ennemies/Goblin/AttackAnim/",
"ANIMATION_ATTACKING_TOTAL_TIME" : 300, # in ms
"HITTING_FRAME" : 5,

"NUMBER_FRAME_DEATH" : 20,
"DEATH_IMAGE_PATH" : "Assets/Ennemies/Goblin/DeathAnim/",
"ANIMATION_DEATH_TOTAL_TIME" : 1000, # in ms
"FADING_TIME" : 3000, # in ms

"STUN_NUMBER_FRAME" : 10,
"STUN_IMAGE_PATH" : "Assets/Ennemies/Goblin/StunAnim/",
"STUN_TIME_PER_FRAME" : 100, # in ms

"ICED_IMAGE_PATH" :  "Assets/Ennemies/Goblin/GoblinIced.png",
"ICED_HP_MAX" : 10.0,
"ICED_NAME" : "Iced Goblin",
"ICED_TIME_MAX" : 2.5 # in second

}

#### OGRE
OGRE_DICT = {

"NAME" : "Ogre",
"HP_MAX" : 30.0,
"DAMAGE" : 8,
"VELOCITY" : 0.10 * RESIZE_COEFF, # pixel by ms
"GOLD_EARNING" : 12,

"HITBOX_FACTOR" : 1.0,
"RESIZE_FACTOR" : 0.75*RESIZE_COEFF, #   pixel
"OFFSET" : [0* RESIZE_COEFF,-80* RESIZE_COEFF], 
"CENTER_VECTOR" : [0.37, 0.59],

"WALKING_IMAGE_PATH" : "Assets/Ennemies/Ogre/WalkAnim/",
"NUMBER_FRAME_WALKING" : 20,
"ANIMATION_WALKING_TOTAL_TIME" : 600*1.5, # in ms
"STOP_WALKING_FRAME" : 16,

"NUMBER_FRAME_TRANSITION" : 4,
"TRANSITION_IMAGE_PATH" : "Assets/Ennemies/Ogre/TransitionAnim/",
"ANIMATION_TRANSITION_TOTAL_TIME" : 300, # in ms

"NUMBER_FRAME_ATTACKING" : 15,
"ATTACKING_IMAGE_PATH" : "Assets/Ennemies/Ogre/AttackAnim/",
"ANIMATION_ATTACKING_TOTAL_TIME" : 300*3, # in ms
"HITTING_FRAME" : 13,

"NUMBER_FRAME_DEATH" : 20,
"DEATH_IMAGE_PATH" : "Assets/Ennemies/Ogre/DeathAnim/",
"ANIMATION_DEATH_TOTAL_TIME" : 600, # in ms
"FADING_TIME" : 3000, # in ms

"STUN_NUMBER_FRAME" : 10,
"STUN_IMAGE_PATH" : "Assets/Ennemies/Ogre/StunAnim/",
"STUN_TIME_PER_FRAME" : 50, # in ms

"ICED_IMAGE_PATH" :  "Assets/Ennemies/Ogre/OgreIced.png",
"ICED_HP_MAX" : 10.0,
"ICED_NAME" : "Iced Goblin",
"ICED_TIME_MAX" : 2.5 # in second

}

#### KAMIKAZE
KAMIKAZE_DICT = {

"NAME" : "Kamikaze Goblin",
"HP_MAX" : 20.0,
"DAMAGE" : 2.5,  #useless, see explosion damage 
"VELOCITY" : 0.15 * RESIZE_COEFF, # pixel by ms
"GOLD_EARNING" : 15,

"HITBOX_FACTOR" : 1.0,
"RESIZE_FACTOR" : 0.125*RESIZE_COEFF, #   pixel
"OFFSET" : [50* RESIZE_COEFF,-20* RESIZE_COEFF], 
"CENTER_VECTOR" : [0.26, 0.63],

"WALKING_IMAGE_PATH" : "Assets/Ennemies/KamikazeGoblin/RunAnim/0",
"NUMBER_FRAME_WALKING" : 28,
"ANIMATION_WALKING_TOTAL_TIME" : 300, # in ms

"NUMBER_FRAME_ATTACKING" : 1,
"ATTACKING_IMAGE_PATH" : "Assets/Ennemies/KamikazeGoblin/RunAnim/0",
"ANIMATION_ATTACKING_TOTAL_TIME" : 0, # in ms
"HITTING_FRAME" : 0,

"STUN_NUMBER_FRAME" : 10,
"STUN_IMAGE_PATH" : "Assets/Ennemies/KamikazeGoblin/StunAnim/",
"STUN_TIME_PER_FRAME" : 100, # in ms

"EXPLOSION_WHEN_KILLED" : True

# "ICED_IMAGE_PATH" :  "Assets/Ennemies/KamikazeGoblin/KamikazeGoblinIced.png",
# "ICED_HP_MAX" : 20.0,
# "ICED_NAME" : "Iced Kamikaze",
# "ICED_TIME_MAX" : 10.0 # in second

}

#### BLUE_NEC
BLUE_NEC_DICT = {

"NAME" : "Ice Necromancer",
"HP_MAX" : 15.0,
"DAMAGE" : 4,
"VELOCITY" : 0.1 * RESIZE_COEFF, # pixel by ms
"GOLD_EARNING" : 7,

"HITBOX_FACTOR" : 1.0,
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF, #   pixel
"OFFSET" : [0* RESIZE_COEFF,-20* RESIZE_COEFF], 
"CENTER_VECTOR" : [0.40, 0.56],

"WALKING_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Blue_Necromancer/WalkAnim/",
"NUMBER_FRAME_WALKING" : 5,
"ANIMATION_WALKING_TOTAL_TIME" : 900, # in ms

"NUMBER_FRAME_ATTACKING" : 5,
"ATTACKING_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Blue_Necromancer/AttackAnim/",
"ANIMATION_ATTACKING_TOTAL_TIME" : 1500, # in ms
"HITTING_FRAME" : 3,

"NUMBER_FRAME_DEATH" : 5,
"DEATH_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Blue_Necromancer/DeathAnim/",
"ANIMATION_DEATH_TOTAL_TIME" : 300, # in ms
"FADING_TIME" : 3000, # in ms

"STUN_NUMBER_FRAME" : 10,
"STUN_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Blue_Necromancer/StunAnim/",
"STUN_TIME_PER_FRAME" : 75, # in ms

"ICED_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Blue_Necromancer/BlueNecroIced.png",
"ICED_HP_MAX" : 10.0,
"ICED_NAME" : "Iced Ice Necro",
"ICED_TIME_MAX" : 2.5, # in second

"REZ_RADIUS" : 2.0,
"REZ_COOLDOWN" : 10.0, # in second

"NUMBER_FRAME_CASTING" : 5,
"CASTING_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Blue_Necromancer/SummonAnim/",
"ANIMATION_CASTING_TOTAL_TIME" : 1500, # in ms

"WAVE_COOLDOWN" : 10,   # in second
"FIRST_WAVE_TIME" : 2   # in second
}

#### RED_NEC
RED_NEC_DICT = {

"NAME" : "Fire Necromancer",
"HP_MAX" : 15.0,
"DAMAGE" : 4,
"VELOCITY" : 0.1 * RESIZE_COEFF, # pixel by ms
"GOLD_EARNING" : 7,

"HITBOX_FACTOR" : 1.0,
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF, #   pixel
"OFFSET" : [0* RESIZE_COEFF,-20* RESIZE_COEFF], 
"CENTER_VECTOR" : [0.40, 0.56],

"WALKING_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Red_Necromancer/WalkAnim/",
"NUMBER_FRAME_WALKING" : 5,
"ANIMATION_WALKING_TOTAL_TIME" : 900, # in ms

"NUMBER_FRAME_ATTACKING" : 5,
"ATTACKING_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Red_Necromancer/AttackAnim/",
"ANIMATION_ATTACKING_TOTAL_TIME" : 1500, # in ms
"HITTING_FRAME" : 3,

"NUMBER_FRAME_DEATH" : 5,
"DEATH_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Red_Necromancer/DeathAnim/",
"ANIMATION_DEATH_TOTAL_TIME" : 300, # in ms
"FADING_TIME" : 3000, # in ms

"STUN_NUMBER_FRAME" : 10,
"STUN_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Red_Necromancer/StunAnim/",
"STUN_TIME_PER_FRAME" : 75, # in ms

"ICED_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Red_Necromancer/RedNecroIced.png",
"ICED_HP_MAX" : 10.0,
"ICED_NAME" : "Iced Fire Necro",
"ICED_TIME_MAX" : 2.5, # in second

"REZ_RADIUS" : 2.0,  # also used for buffing
"REZ_COOLDOWN" : 10.0, # in second

"NUMBER_FRAME_CASTING" : 5,
"CASTING_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Red_Necromancer/SummonAnim/",
"ANIMATION_CASTING_TOTAL_TIME" : 1500, # in ms

"BUFF_COOLDOWN" : 5,   # in second
"FIRST_BUFF_TIME" : 2  # in second
}

#### GREEN_NEC
GREEN_NEC_DICT = {

"NAME" : "Plant Necromancer",
"HP_MAX" : 15.0,
"DAMAGE" : 4,
"VELOCITY" : 0.1 * RESIZE_COEFF, # pixel by ms
"GOLD_EARNING" : 7,

"HITBOX_FACTOR" : 1.0,
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF, #   pixel
"OFFSET" : [0* RESIZE_COEFF,-20* RESIZE_COEFF], 
"CENTER_VECTOR" : [0.40, 0.56],

"WALKING_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Green_Necromancer/WalkAnim/",
"NUMBER_FRAME_WALKING" : 5,
"ANIMATION_WALKING_TOTAL_TIME" : 900, # in ms

"NUMBER_FRAME_ATTACKING" : 5,
"ATTACKING_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Green_Necromancer/AttackAnim/",
"ANIMATION_ATTACKING_TOTAL_TIME" : 1500, # in ms
"HITTING_FRAME" : 3,

"NUMBER_FRAME_DEATH" : 5,
"DEATH_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Green_Necromancer/DeathAnim/",
"ANIMATION_DEATH_TOTAL_TIME" : 300, # in ms
"FADING_TIME" : 3000, # in ms

"STUN_NUMBER_FRAME" : 10,
"STUN_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Green_Necromancer/StunAnim/",
"STUN_TIME_PER_FRAME" : 75, # in ms

"ICED_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Green_Necromancer/GreenNecroIced.png",
"ICED_HP_MAX" : 10.0,
"ICED_NAME" : "Iced Plant Necro",
"ICED_TIME_MAX" : 2.5, # in second

"REZ_RADIUS" : 2.0,
"REZ_COOLDOWN" : 10.0, # in second

"NUMBER_FRAME_CASTING" : 5,
"CASTING_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Green_Necromancer/SummonAnim/",
"ANIMATION_CASTING_TOTAL_TIME" : 1500, # in ms

"ROOT_COOLDOWN" : 15,   # in second
"FIRST_ROOT_TIME" : 3,  # in second
"NUMBER_MAX_OF_TOWER_ROOT" : 1

}

#### BLUE_SKELETON
BLUE_SKEL_DICT = {

"NAME" : "Ice Skeleton",
"HP_MAX" : 5.0,
"DAMAGE" : 4,
"VELOCITY" : 0.09 * RESIZE_COEFF, # pixel by ms
"GOLD_EARNING" : 2,
"GOLD_EARNING_WHEN_SUMMONED" : 0,

"HITBOX_FACTOR" : 1.0,
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF, #   pixel
"OFFSET" : [0* RESIZE_COEFF,-30* RESIZE_COEFF], 
"CENTER_VECTOR" : [0.40, 0.56],

"WALKING_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonBlue/WalkAnim/",
"NUMBER_FRAME_WALKING" : 4,
"ANIMATION_WALKING_TOTAL_TIME" : 900, # in ms

"NUMBER_FRAME_ATTACKING" : 6,
"ATTACKING_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonBlue/AttackAnim/",
"ANIMATION_ATTACKING_TOTAL_TIME" : 1500, # in ms
"HITTING_FRAME" : 5,

"NUMBER_FRAME_DEATH" : 6,
"DEATH_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonBlue/DeathAnim/",
"ANIMATION_DEATH_TOTAL_TIME" : 300, # in ms
"FADING_TIME" : 3000, # in ms

"STUN_NUMBER_FRAME" : 10,
"STUN_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonBlue/StunAnim/",
"STUN_TIME_PER_FRAME" : 100, # in ms

"ICED_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonBlue/BlueSkeletonIced.png",
"ICED_HP_MAX" : 10.0,
"ICED_NAME" : "Iced Ice Skel",
"ICED_TIME_MAX" : 2.5, # in second

"NUMBER_FRAME_SPAWNING" : 5,
"SPAWNING_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonBlue/SummonAnim/",
"ANIMATION_SPAWNING_TOTAL_TIME" : 1500

}

#### RED_SKELETON
RED_SKEL_DICT = {

"NAME" : "Red Skeleton",
"HP_MAX" : 5.0,
"DAMAGE" : 4,
"VELOCITY" : 0.09 * RESIZE_COEFF, # pixel by ms
"GOLD_EARNING" : 2,
"GOLD_EARNING_WHEN_SUMMONED" : 0,

"HITBOX_FACTOR" : 1.0,
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF, #   pixel
"OFFSET" : [0* RESIZE_COEFF,-30* RESIZE_COEFF], 
"CENTER_VECTOR" : [0.40, 0.56],

"WALKING_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonRed/WalkAnim/",
"NUMBER_FRAME_WALKING" : 4,
"ANIMATION_WALKING_TOTAL_TIME" : 900, # in ms

"NUMBER_FRAME_ATTACKING" : 6,
"ATTACKING_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonRed/AttackAnim/",
"ANIMATION_ATTACKING_TOTAL_TIME" : 1500, # in ms
"HITTING_FRAME" : 5,

"NUMBER_FRAME_DEATH" : 6,
"DEATH_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonRed/DeathAnim/",
"ANIMATION_DEATH_TOTAL_TIME" : 300, # in ms
"FADING_TIME" : 3000, # in ms

"STUN_NUMBER_FRAME" : 10,
"STUN_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonRed/StunAnim/",
"STUN_TIME_PER_FRAME" : 100, # in ms

"ICED_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonRed/RedSkeletonIced.png",
"ICED_HP_MAX" : 10.0,
"ICED_NAME" : "Iced Red Skel",
"ICED_TIME_MAX" : 2.5, # in second

"NUMBER_FRAME_SPAWNING" : 5,
"SPAWNING_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonRed/SummonAnim/",
"ANIMATION_SPAWNING_TOTAL_TIME" : 1500

}

#### GREEN_SKELETON
GREEN_SKEL_DICT = {

"NAME" : "Green Skeleton",
"HP_MAX" : 5.0,
"DAMAGE" : 4,
"VELOCITY" : 0.09 * RESIZE_COEFF, # pixel by ms
"GOLD_EARNING" : 2,
"GOLD_EARNING_WHEN_SUMMONED" : 0,

"HITBOX_FACTOR" : 1.0,
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF, #   pixel
"OFFSET" : [0* RESIZE_COEFF,-30* RESIZE_COEFF], 
"CENTER_VECTOR" : [0.40, 0.56],

"WALKING_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonGreen/WalkAnim/",
"NUMBER_FRAME_WALKING" : 4,
"ANIMATION_WALKING_TOTAL_TIME" : 900, # in ms

"NUMBER_FRAME_ATTACKING" : 6,
"ATTACKING_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonGreen/AttackAnim/",
"ANIMATION_ATTACKING_TOTAL_TIME" : 1500, # in ms
"HITTING_FRAME" : 5,

"NUMBER_FRAME_DEATH" : 6,
"DEATH_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonGreen/DeathAnim/",
"ANIMATION_DEATH_TOTAL_TIME" : 300, # in ms
"FADING_TIME" : 3000, # in ms

"STUN_NUMBER_FRAME" : 10,
"STUN_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonGreen/StunAnim/",
"STUN_TIME_PER_FRAME" : 100, # in ms

"ICED_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonGreen/GreenSkeletonIced.png",
"ICED_HP_MAX" : 10.0,
"ICED_NAME" : "Iced Green Skel",
"ICED_TIME_MAX" : 2.5, # in second

"NUMBER_FRAME_SPAWNING" : 5,
"SPAWNING_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonGreen/SummonAnim/",
"ANIMATION_SPAWNING_TOTAL_TIME" : 1500

}

#### DRAGON
DRAGON_DICT = {

"NAME" : "Dragon",
"HP_MAX" : 100.0,
"VELOCITY" : 0.1 * RESIZE_COEFF, # pixel by ms
"GOLD_EARNING" : 35,

"HITBOX_FACTOR" : 1.0,
"RESIZE_FACTOR" : 0.15*RESIZE_COEFF, #   pixel
"OFFSET" : [50* RESIZE_COEFF,-60* RESIZE_COEFF], 
"CENTER_VECTOR" : [0.33, 0.55],

"WALKING_IMAGE_PATH" : "Assets/Ennemies/Dragon/FlightAnim/",
"NUMBER_FRAME_WALKING" : 39,
"ANIMATION_WALKING_TOTAL_TIME" : 1000 # in ms

}

##############################################################

###############     TOWERS     ###############

##############################################################


TOWER_RECT_RANGE_IMAGE_PATH = "Assets/Tower/Range_boxes/rect_range.png"
TOWER_RECT_RANGE_IMAGE_ALPHA = 100
TOWER_CIRCLE_RANGE_IMAGE_PATH = "Assets/Tower/Range_boxes/circle_range.png"
TOWER_CIRCLE_RANGE_IMAGE_ALPHA = 100

#### ARCANE_TOWER_LVL1
ARCANE_TOWER_LVL1_DICT = { 

"NAME" : "Arcane tower Lvl.1",
"HP_MAX" : 100.0,
"RANGE" : 2.0, # multiplied by the square side
"PRICE" : 60,
"DAMAGE" : 9.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/Niveau1/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : 800,  # in ms
"ANIMATION_RELOADING_TOTAL_TIME" : 600,  # in ms

"ROOT_IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/Niveau1/RootedAnim/",
"NUMBER_FRAME_ROOTING" : 10,
"ANIMATION_ROOTING_TOTAL_TIME" : 2500,  # in ms
"ANIMATION_ROOTING_TIME_PER_FRAME" : 250,  # in ms
"ROOT_DPS" : 2,

"OFFSET" : [0.1*BACKGROUND_SQUARE_SIDE,-0.7*BACKGROUND_SQUARE_SIDE],
"RESIZE_FACTOR" : 0.4*RESIZE_COEFF,
"FIRING_OFFSET" : [40* RESIZE_COEFF,50* RESIZE_COEFF],

"UPGRADE_COST" : 100

}

#### ARCANE_TOWER_LVL2
ARCANE_TOWER_LVL2_DICT = { 

"NAME" : "Arcane tower Lvl.2",
"HP_MAX" : 150.0,
"RANGE" : 2.0, # multiplied by the square side
"PRICE" : 75,
"DAMAGE" : 14.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/Niveau2/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : 600,
"ANIMATION_RELOADING_TOTAL_TIME" : 400,

"ROOT_IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/Niveau2/RootedAnim/",
"NUMBER_FRAME_ROOTING" : 10,
"ANIMATION_ROOTING_TOTAL_TIME" : 8000,  # in ms
"ANIMATION_ROOTING_TIME_PER_FRAME" : 500,  # in ms
"ROOT_DPS" : 2,

"OFFSET" : ARCANE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : ARCANE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : ARCANE_TOWER_LVL1_DICT["FIRING_OFFSET"],

"UPGRADE_COST" : 300

}

#### ARCANE_TOWER_LVL3
ARCANE_TOWER_LVL3_DICT = { 

"NAME" : "Arcane tower Lvl.3",
"HP_MAX" : 300.0,
"RANGE" : 3.5, # multiplied by the square side
"PRICE" : 90,
"DAMAGE" : 30.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/Niveau3/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : 300,
"ANIMATION_RELOADING_TOTAL_TIME" : 200,

"ROOT_IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/Niveau3/RootedAnim/",
"NUMBER_FRAME_ROOTING" : 10,
"ANIMATION_ROOTING_TOTAL_TIME" : 8000,  # in ms
"ANIMATION_ROOTING_TIME_PER_FRAME" : 500,  # in ms
"ROOT_DPS" : 2,

"OFFSET" : ARCANE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : ARCANE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : ARCANE_TOWER_LVL1_DICT["FIRING_OFFSET"],

"UPGRADE_COST" : None

}

#### FIRE_TOWER_LVL1
FIRE_TOWER_LVL1_DICT = { 

"NAME" : "Fire tower Lvl.1",
"HP_MAX" : 100.0,
"RANGE" : 3.5, # multiplied by the square side
"PRICE" : 60,
"DAMAGE" : 15.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/Niveau1/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : ARCANE_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"]*1.5,
"ANIMATION_RELOADING_TOTAL_TIME" : ARCANE_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"]*2,

"ROOT_IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/Niveau1/RootedAnim/",
"NUMBER_FRAME_ROOTING" : 10,
"ANIMATION_ROOTING_TOTAL_TIME" : 2500,  # in ms
"ANIMATION_ROOTING_TIME_PER_FRAME" : 250,  # in ms
"ROOT_DPS" : 2,

"OFFSET" : ARCANE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : ARCANE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : [40* RESIZE_COEFF,50* RESIZE_COEFF],

"UPGRADE_COST" : 100

}

#### FIRE_TOWER_LVL2
FIRE_TOWER_LVL2_DICT = { 

"NAME" : "Fire tower Lvl.2",
"HP_MAX" : 150.0,
"RANGE" : 4.0, # multiplied by the square side
"PRICE" : 75,
"DAMAGE" : 20.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/Niveau2/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : ARCANE_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"]*1.5,
"ANIMATION_RELOADING_TOTAL_TIME" : ARCANE_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"]*2,

"ROOT_IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/Niveau2/RootedAnim/",
"NUMBER_FRAME_ROOTING" : 10,
"ANIMATION_ROOTING_TOTAL_TIME" : 8000,  # in ms
"ANIMATION_ROOTING_TIME_PER_FRAME" : 500,  # in ms
"ROOT_DPS" : 2,

"OFFSET" : FIRE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : FIRE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : FIRE_TOWER_LVL1_DICT["FIRING_OFFSET"],

"UPGRADE_COST" : 300

}

#### FIRE_TOWER_LVL3
FIRE_TOWER_LVL3_DICT = { 

"NAME" : "Fire tower Lvl.3",
"HP_MAX" : 300.0,
"RANGE" : 4.5, # multiplied by the square side
"PRICE" : 90,
"DAMAGE" : 40.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/Niveau3/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : ARCANE_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"],
"ANIMATION_RELOADING_TOTAL_TIME" : ARCANE_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"],

"ROOT_IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/Niveau3/RootedAnim/",
"NUMBER_FRAME_ROOTING" : 10,
"ANIMATION_ROOTING_TOTAL_TIME" : 8000,  # in ms
"ANIMATION_ROOTING_TIME_PER_FRAME" : 500,  # in ms
"ROOT_DPS" : 2,

"OFFSET" : FIRE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : FIRE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : FIRE_TOWER_LVL1_DICT["FIRING_OFFSET"],

"UPGRADE_COST" : None

}

#### LIGHTNING_TOWER_LVL1
LIGHTNING_TOWER_LVL1_DICT = { 

"NAME" : "Lightning tower Lvl.1",
"HP_MAX" : 100.0,
"RANGE" : 2.5, # multiplied by the square side
"PRICE" : 60,
"DAMAGE" : 6.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Jaune/Niveau1/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : ARCANE_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"]*2,
"ANIMATION_RELOADING_TOTAL_TIME" : ARCANE_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"]*4,

"ROOT_IMAGE_PATH" : "Assets/Tower/ToursMagique/Jaune/Niveau1/RootedAnim/",
"NUMBER_FRAME_ROOTING" : 10,
"ANIMATION_ROOTING_TOTAL_TIME" : 2500,  # in ms
"ANIMATION_ROOTING_TIME_PER_FRAME" : 250,  # in ms
"ROOT_DPS" : 2,

"OFFSET" : ARCANE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : ARCANE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : [60* RESIZE_COEFF,60* RESIZE_COEFF],

"UPGRADE_COST" : 100

}

#### LIGHTNING_TOWER_LVL2
LIGHTNING_TOWER_LVL2_DICT = { 

"NAME" : "Lightning tower Lvl.2",
"HP_MAX" : 150.0,
"RANGE" : 2.8, # multiplied by the square side
"PRICE" : 75,
"DAMAGE" : 8.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Jaune/Niveau2/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : LIGHTNING_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"],
"ANIMATION_RELOADING_TOTAL_TIME" : LIGHTNING_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"],

"ROOT_IMAGE_PATH" : "Assets/Tower/ToursMagique/Jaune/Niveau2/RootedAnim/",
"NUMBER_FRAME_ROOTING" : 10,
"ANIMATION_ROOTING_TOTAL_TIME" : 8000,  # in ms
"ANIMATION_ROOTING_TIME_PER_FRAME" : 500,  # in ms
"ROOT_DPS" : 2,

"OFFSET" : LIGHTNING_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : LIGHTNING_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : LIGHTNING_TOWER_LVL1_DICT["FIRING_OFFSET"],

"UPGRADE_COST" : 300

}

#### LIGHTNING_TOWER_LVL3
LIGHTNING_TOWER_LVL3_DICT = { 

"NAME" : "Lightning tower Lvl.3",
"HP_MAX" : 300.0,
"RANGE" : 4.5, # multiplied by the square side
"PRICE" : 90,
"DAMAGE" : 15.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Jaune/Niveau3/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : LIGHTNING_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"],
"ANIMATION_RELOADING_TOTAL_TIME" : LIGHTNING_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"],

"ROOT_IMAGE_PATH" : "Assets/Tower/ToursMagique/Jaune/Niveau3/RootedAnim/",
"NUMBER_FRAME_ROOTING" : 10,
"ANIMATION_ROOTING_TOTAL_TIME" : 8000,  # in ms
"ANIMATION_ROOTING_TIME_PER_FRAME" : 500,  # in ms
"ROOT_DPS" : 2,

"OFFSET" : LIGHTNING_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : LIGHTNING_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : LIGHTNING_TOWER_LVL1_DICT["FIRING_OFFSET"],

"UPGRADE_COST" : None

}

#### ICE_TOWER_LVL1
ICE_TOWER_LVL1_DICT = { 

"NAME" : "Ice tower Lvl.1",
"HP_MAX" : 100.0,
"RANGE" : 2.5, # multiplied by the square side
"PRICE" : 60,
"DAMAGE" : 8.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Bleue/Niveau1/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : ARCANE_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"],
"ANIMATION_RELOADING_TOTAL_TIME" : ARCANE_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"],

"ROOT_IMAGE_PATH" : "Assets/Tower/ToursMagique/Bleue/Niveau1/RootedAnim/",
"NUMBER_FRAME_ROOTING" : 10,
"ANIMATION_ROOTING_TOTAL_TIME" : 2500,  # in ms
"ANIMATION_ROOTING_TIME_PER_FRAME" : 250,  # in ms
"ROOT_DPS" : 2,

"OFFSET" : ARCANE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : ARCANE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : [60* RESIZE_COEFF,70* RESIZE_COEFF],

"UPGRADE_COST" : 100

}

#### ICE_TOWER_LVL2
ICE_TOWER_LVL2_DICT = { 

"NAME" : "Ice tower Lvl.2",
"HP_MAX" : 150.0,
"RANGE" : 3.0, # multiplied by the square side
"PRICE" : 75,
"DAMAGE" : 10.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Bleue/Niveau2/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : ICE_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"],
"ANIMATION_RELOADING_TOTAL_TIME" : ICE_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"],

"ROOT_IMAGE_PATH" : "Assets/Tower/ToursMagique/Bleue/Niveau2/RootedAnim/",
"NUMBER_FRAME_ROOTING" : 10,
"ANIMATION_ROOTING_TOTAL_TIME" : 8000,  # in ms
"ANIMATION_ROOTING_TIME_PER_FRAME" : 500,  # in ms
"ROOT_DPS" : 2,

"OFFSET" : ICE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : ICE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : ICE_TOWER_LVL1_DICT["FIRING_OFFSET"],

"UPGRADE_COST" : 300

}

#### ICE_TOWER_LVL3
ICE_TOWER_LVL3_DICT = { 

"NAME" : "Ice tower Lvl.3",
"HP_MAX" : 300.0,
"RANGE" : 2.5, # multiplied by the square side
"PRICE" : 90,
"DAMAGE" : 20,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Bleue/Niveau3/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : ICE_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"],
"ANIMATION_RELOADING_TOTAL_TIME" : ICE_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"],

"ROOT_IMAGE_PATH" : "Assets/Tower/ToursMagique/Bleue/Niveau3/RootedAnim/",
"NUMBER_FRAME_ROOTING" : 10,
"ANIMATION_ROOTING_TOTAL_TIME" : 8000,  # in ms
"ANIMATION_ROOTING_TIME_PER_FRAME" : 500,  # in ms
"ROOT_DPS" : 2,

"OFFSET" : ICE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : ICE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : ICE_TOWER_LVL1_DICT["FIRING_OFFSET"],

"UPGRADE_COST" : None

}

#### BALLISTA
BALLISTA_DICT = { 

"NAME" : "Ballista",
"HP_MAX" : 18.0,
"RANGE" : 7.0, # multiplied by the square side
"PRICE" : 5,
"DAMAGE" : 2,

"ATTACK_IMAGE_PATH" : "Assets/Tower/Baliste/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 5,
"ANIMATION_ATTACKING_TOTAL_TIME" : 200,

"RELOAD_IMAGE_PATH" : "Assets/Tower/Baliste/ReloadAnim/",
"NUMBER_FRAME_RELOADING" : 40,
"ANIMATION_RELOADING_TOTAL_TIME" : 1400,

"OFFSET" : [0* RESIZE_COEFF,20* RESIZE_COEFF],
"RESIZE_FACTOR" : 0.4*RESIZE_COEFF,
"FIRING_OFFSET" : [0* RESIZE_COEFF,40* RESIZE_COEFF],

}

#### CATAPULT
CATAPULT_DICT = { 

"NAME" : "Catapult",
"HP_MAX" : 12.0,
"RANGE" : 9.0, # multiplied by the square side
"PRICE" : 10,
"DAMAGE" : 2,

"ATTACK_IMAGE_PATH" : "Assets/Tower/Catapult/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 5,
"ANIMATION_ATTACKING_TOTAL_TIME" : 200,

"RELOAD_IMAGE_PATH" : "Assets/Tower/Catapult/ReloadAnim/",
"NUMBER_FRAME_RELOADING" : 55,
"ANIMATION_RELOADING_TOTAL_TIME" : 2500,

"OFFSET" : [0* RESIZE_COEFF,-20* RESIZE_COEFF],
"RESIZE_FACTOR" : 1.0*RESIZE_COEFF,
"FIRING_OFFSET" : [40* RESIZE_COEFF,20* RESIZE_COEFF],

}

##############################################################

###############     PROJECTILES     ###############

##############################################################

#### ARCANE_BOLT_LVL1
ARCANE_BOLT_LVL1_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/projectile/arcane_proj.png",
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,
"CENTER_VECTOR" : [0.14,0.5],
"RATIO_FOR_IMPACT" : 0.5,

"DAMAGE" : ARCANE_TOWER_LVL1_DICT["DAMAGE"],
"VELOCITY" : 0.75 * RESIZE_COEFF # pixel by ms

}

#### ARCANE_BOLT_LVL2
ARCANE_BOLT_LVL2_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/projectile/arcane_proj.png",
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,
"CENTER_VECTOR" : [0.14,0.5],
"RATIO_FOR_IMPACT" : 0.5,

"DAMAGE" : ARCANE_TOWER_LVL2_DICT["DAMAGE"],
"VELOCITY" : 0.75 * RESIZE_COEFF # pixel by ms

}

#### ARCANE_BOLT_LVL3
ARCANE_BOLT_LVL3_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/projectile/arcane_proj.png",
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,
"CENTER_VECTOR" : [0.14,0.5],
"RATIO_FOR_IMPACT" : 0.5,

"DAMAGE" : ARCANE_TOWER_LVL2_DICT["DAMAGE"],
"VELOCITY" : 0.75 * RESIZE_COEFF # pixel by ms

}

#### FIRE_BOLT_LVL1
FIRE_BOLT_LVL1_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/ProjectileAnim/",
"NUMBER_FRAME" : 5,
"TOTAL_TIME" : 200,  # in ms

"RESIZE_FACTOR" : 0.25*RESIZE_COEFF,
"CENTER_VECTOR" : [0.14,0.5],
"RATIO_FOR_IMPACT" : 0.5,

"DAMAGE" : FIRE_TOWER_LVL1_DICT["DAMAGE"],
"VELOCITY" : 0.5 * RESIZE_COEFF # pixel by ms

}

#### FIRE_BOLT_LVL2
FIRE_BOLT_LVL2_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/ProjectileAnim/",
"NUMBER_FRAME" : 5,
"TOTAL_TIME" : 200,  # in ms

"RESIZE_FACTOR" : 0.25*RESIZE_COEFF,
"CENTER_VECTOR" : [0.14,0.5],
"RATIO_FOR_IMPACT" : 0.5,

"DAMAGE" : FIRE_TOWER_LVL2_DICT["DAMAGE"],
"VELOCITY" : 0.5 * RESIZE_COEFF # pixel by ms

}

#### FIRE_BOLT_LVL3
FIRE_BOLT_LVL3_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/ProjectileAnimLvl3/",
"NUMBER_FRAME" : 5,
"TOTAL_TIME" : 200,  # in ms

"RESIZE_FACTOR" : 0.25*RESIZE_COEFF,
"CENTER_VECTOR" : [0.14,0.5],
"RATIO_FOR_IMPACT" : 0.5,

"DAMAGE" : FIRE_TOWER_LVL3_DICT["DAMAGE"],
"VELOCITY" : 0.5 * RESIZE_COEFF # pixel by ms

}

#### LIGHTNING_BOLT_LVL1
LIGHTNING_BOLT_LVL1_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Jaune/ProjectileAnim/",
"NUMBER_FRAME" : 2,
"TIME_PER_FRAME" : 50,  # in ms
"TOTAL_TIME" : 500,  # in ms

"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,  ## only for width
"CENTER_VECTOR" : [0.5,0.0],

"DAMAGE" : LIGHTNING_TOWER_LVL1_DICT["DAMAGE"],
"STUN_TIME" : 0.5,
"NUMBER_BOUNCE_MAX" : 4,
"DECREASING_DISTANCE_BOUNCE_FACTOR" : 0.1,  # will decrease of X% at each bounce
"DECREASING_DAMAGE_BOUNCE_FACTOR" : 0.2, # will decrease of X% at each bounce
"RANGE" : LIGHTNING_TOWER_LVL1_DICT["RANGE"]

}

#### LIGHTNING_BOLT_LVL2
LIGHTNING_BOLT_LVL2_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Jaune/ProjectileAnim/",
"NUMBER_FRAME" : 2,
"TIME_PER_FRAME" : 50,  # in ms
"TOTAL_TIME" : 500,  # in ms

"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,  ## only for width
"CENTER_VECTOR" : [0.5,0.0],

"DAMAGE" : LIGHTNING_TOWER_LVL2_DICT["DAMAGE"],
"STUN_TIME" : 1.0,
"NUMBER_BOUNCE_MAX" : 8,
"DECREASING_DISTANCE_BOUNCE_FACTOR" : 0.1,  # will decrease of X% at each bounce
"DECREASING_DAMAGE_BOUNCE_FACTOR" : 0.2, # will decrease of X% at each bounce
"RANGE" : LIGHTNING_TOWER_LVL2_DICT["RANGE"]

}

#### LIGHTNING_BOLT_LVL3
LIGHTNING_BOLT_LVL3_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Jaune/ProjectileAnim3/",
"NUMBER_FRAME" : 2,
"TIME_PER_FRAME" : 50,  # in ms
"TOTAL_TIME" : 500,  # in ms

"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,  ## only for width
"CENTER_VECTOR" : [0.5,0.0],

"DAMAGE" : LIGHTNING_TOWER_LVL3_DICT["DAMAGE"],
"STUN_TIME" : 2.0,
"NUMBER_BOUNCE_MAX" : 15,
"DECREASING_DISTANCE_BOUNCE_FACTOR" : 0,  # will decrease of X% at each bounce
"DECREASING_DAMAGE_BOUNCE_FACTOR" : 0, # will decrease of X% at each bounce
"RANGE" : LIGHTNING_TOWER_LVL3_DICT["RANGE"]

}

#### ICE_BOLT_LVL1
ICE_BOLT_LVL1_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Bleue/ProjectileAnim/",
"NUMBER_FRAME" : 11,
"TIME_PER_FRAME" : 100,  # in ms
"NUMBER_FRAME_FADING" : 5,
"TOTAL_TIME_FADING" : 500,  # in ms

"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,  ## only for width
"CENTER_VECTOR" : [0.5,0.0],

"DAMAGE" : ICE_TOWER_LVL1_DICT["DAMAGE"],
"SLOWING_COEFF" : 0.5,
"FREEZING" : True, # Turn ennemie into ice block
"RANGE" : ICE_TOWER_LVL1_DICT["RANGE"]

}

#### ICE_BOLT_LVL2
ICE_BOLT_LVL2_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Bleue/ProjectileAnim/",
"NUMBER_FRAME" : 11,
"TIME_PER_FRAME" : 100,  # in ms
"NUMBER_FRAME_FADING" : 5,
"TOTAL_TIME_FADING" : 500,  # in ms

"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,  ## only for width
"CENTER_VECTOR" : [0.5,0.0],

"DAMAGE" : ICE_TOWER_LVL2_DICT["DAMAGE"],
"SLOWING_COEFF" : 0.7,
"FREEZING" : False, # Turn ennemie into ice block
"RANGE" : ICE_TOWER_LVL2_DICT["RANGE"]

}

#### ICE_BOLT_LVL3
ICE_BOLT_LVL3_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Bleue/ProjectileAnim/",
"NUMBER_FRAME" : 11,
"TIME_PER_FRAME" : 100,  # in ms
"NUMBER_FRAME_FADING" : 5,
"TOTAL_TIME_FADING" : 500,  # in ms

"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,  ## only for width
"CENTER_VECTOR" : [0.5,0.0],

"DAMAGE" : ICE_TOWER_LVL3_DICT["DAMAGE"],
"SLOWING_COEFF" : 0.9,
"FREEZING" : True, # Turn ennemie into ice block
"RANGE" : ICE_TOWER_LVL3_DICT["RANGE"]

}

#### BOLT
BOLT_DICT = {

"IMAGE_PATH" : "Assets/Tower/Baliste/CarreauBaliste_cropped.png",
"RESIZE_FACTOR" : 0.8*RESIZE_COEFF,
"CENTER_VECTOR" : [0.16,0.47],
"RATIO_FOR_IMPACT" : 0.5,

"DAMAGE" : BALLISTA_DICT["DAMAGE"],
"VELOCITY" : 2.0 * RESIZE_COEFF # pixel by ms

}

#### ROCK
ROCK_DICT = {

"IMAGE_PATH" : "Assets/Tower/Catapult/Rock_cropped.png",
"RESIZE_FACTOR" : 0.8*RESIZE_COEFF,
"CENTER_VECTOR" : [0.5,0.5],
"RATIO_FOR_IMPACT" : 0.5,  # not used

"DAMAGE" : CATAPULT_DICT["DAMAGE"],
"VELOCITY" : 0.60 * RESIZE_COEFF, # pixel by ms
"ROTATION_SPEED"  : 0.01, # rotation per second
"ORTHO_MOVEMENT" : 0.25   # multiplied by distance with the target

}

##############################################################

###############     IMPACTS     ###############

##############################################################


#### ARCANE_IMPACT_LVL1
ARCANE_IMPACT_LVL1_DICT = {

"DAMAGE" : 3.0,

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/ImpactAnim/",
"RESIZE_FACTOR" : 0.3*RESIZE_COEFF,
"CENTER_VECTOR" : [0.5,0.83],

"NUMBER_FRAME" : 17,
"TOTAL_TIME" : 500,
"DAMAGE_FRAME" : 4

}

#### ARCANE_IMPACT_LVL2
ARCANE_IMPACT_LVL2_DICT = {

"DAMAGE" : 6.0,

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/ImpactAnim/",
"RESIZE_FACTOR" : 0.3*RESIZE_COEFF,
"CENTER_VECTOR" : [0.5,0.83],

"NUMBER_FRAME" : 17,
"TOTAL_TIME" : 500,
"DAMAGE_FRAME" : 4

}

#### ARCANE_IMPACT_LVL3
ARCANE_IMPACT_LVL3_DICT = {

"DAMAGE" : 15.0,

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/ImpactAnim/",
"RESIZE_FACTOR" : 0.3*RESIZE_COEFF,
"CENTER_VECTOR" : [0.5,0.83],

"NUMBER_FRAME" : 17,
"TOTAL_TIME" : 500,
"DAMAGE_FRAME" : 4

}

#### FIRE_IMPACT_LVL1
FIRE_IMPACT_LVL1_DICT = {

"DAMAGE" : 0.0,

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/ImpactAnim/",
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,
"CENTER_VECTOR" : [1.0,1.5],

"NUMBER_FRAME" : 8,
"TOTAL_TIME" : 500,
"DAMAGE_FRAME" : 4

}

#### FIRE_IMPACT_LVL2
FIRE_IMPACT_LVL2_DICT = {

"DAMAGE" : 0.0,

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/ImpactAnim/",
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,
"CENTER_VECTOR" : [1.0,1.5],

"NUMBER_FRAME" : 8,
"TOTAL_TIME" : 500,
"DAMAGE_FRAME" : 4

}

#### FIRE_IMPACT_LVL3
FIRE_IMPACT_LVL3_DICT = {

"DAMAGE" : 0.0,

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/ImpactAnimLvl3/",
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,
"CENTER_VECTOR" : [1.0,1.5],

"NUMBER_FRAME" : 8,
"TOTAL_TIME" : 500,
"DAMAGE_FRAME" : 4

}

#### ROCK_IMPACT
ROCK_IMPACT_DICT = {

"DAMAGE" : 2.0,

"IMAGE_PATH" : "Assets/Tower/Catapult/ImpactAnim/",
"RESIZE_FACTOR" : 0.8*RESIZE_COEFF,
"CENTER_VECTOR" : [0.51,0.78],

"NUMBER_FRAME" : 10,
"TOTAL_TIME" : 600,
"DAMAGE_FRAME" : 4

}

##############################################################

###############     MAGICAL_EFFECTS     ###############

##############################################################

WAVE_DICT = {
    
"NUMBER_FRAME" : 25,
"IMAGE_PATH" : "Assets/Ennemies/Necromancers/Blue_Necromancer/WaveAnim/",
"OFFSET" : [0* RESIZE_COEFF,-40* RESIZE_COEFF],
"TIME_PER_FRAME" : 200, # in ms,
"VELOCITY" : 0.15, # in ms
"DAMAGE" : 0,
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF

}

HEAL_DICT = {

"NUMBER_FRAME" : 149,
"IMAGE_PATH" : "Assets/Effects/HealAnim/",
"OFFSET" : [-80* RESIZE_COEFF,30* RESIZE_COEFF],
"TIME_PER_FRAME" : 20, # in ms,
"TOTAL_TIME" : 5.0,
"AMOUNT" : 2.0, # heal by seconds
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF

}

BUFF_DICT = {

"NUMBER_FRAME" : 78,
"IMAGE_PATH" : "Assets/Effects/BuffAnim/",
"OFFSET" : [-90* RESIZE_COEFF,30* RESIZE_COEFF],
"TIME_PER_FRAME" : 20, # in ms,
"TOTAL_TIME" : 5.0,
"VELOCITY_COEFF" : 1.275,
"DAMAGE_COEFF" : 2,
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF

}

EXPLOSION_DICT = {
    
"NUMBER_FRAME" : 9,
"IMAGE_PATH" : "Assets/Ennemies/KamikazeGoblin/ExplosionAnim/",
"OFFSET" : [-50* RESIZE_COEFF,-80* RESIZE_COEFF],
"TIME_PER_FRAME" : 100, # in ms,
"DAMAGE_FRAME" : 4,
"HITBOX_FACTOR" : 1.0, 
"DAMAGE" : 40,
"RESIZE_FACTOR" : 0.75*RESIZE_COEFF

}

##############################################################

###############     AUDIO     ###############

##############################################################

### MUSIC
MUSIC_FILE_PATH = "Audio/Music/Age_of_War_Theme_Soundtrack.mp3"
FADE_UP_TIME = 3.0 # in seconds
MUSIC_VOLUME = 0.05 # 0.05

## SOUND
AUDIO_EFFECTS_COEFF = 1.0

SOUND_BUILDING_ROCK_PATH = "Audio/Other_effect/ES_Impact Wood Hit 6 - SFX Producer.mp3"
SOUND_BUILDING_ROCK_VOLUME = 0.1

SOUND_BUILDING_WOOD_PATH = "Audio/Other_effect/ES_Impact Wood 3.mp3"
SOUND_BUILDING_WOOD_VOLUME = 0.2

SOUND_GOLD_GAIN_PATH = "Audio/Other_effect/ES_Coin Bag Drop 1.mp3"
SOUND_BIG_GOLD_GAIN_PATH = "Audio/Other_effect/ES_Money Bag Drop Coins.mp3"
SOUND_BIG_GOLD_GAIN_TRESHOLD = 300
SOUND_GOLD_GAIN_VOLUME = 0.1

SOUND_FALLING_PATH = "Audio/Ennemy/ES_Body Fall Heavy Rustle 2 - SFX Producer.mp3"
SOUND_FALLING_VOLUME = 0.0

SOUND_OGRE_D_1_PATH = "Audio/Ennemy/ES_Monster Groan 14.mp3"
SOUND_OGRE_D_2_PATH = "Audio/Ennemy/ES_Monster Groan 19.mp3"
SOUND_OGRE_D_3_PATH = "Audio/Ennemy/ES_Monster Groan 32.mp3"
SOUND_OGRE_D_VOLUME = 0.2

SOUND_ROCK_PATH = "Audio/Impact/ES_Rock Impact - SFX Producer.mp3"
SOUND_ROCK_VOLUME = 0.05

SOUND_BOLT_PROJ_1_PATH = "Audio/Projectile/Bolt/ES_Arrow Out Whooshing Release 4-zone-002.mp3"
SOUND_BOLT_PROJ_2_PATH = "Audio/Projectile/Bolt/ES_Arrow Out Whooshing Release 5-zone-001.mp3"
SOUND_BOLT_PROJ_VOLUME = 0.1

SOUND_ARCANE_PROJ_PATH = "Audio/Projectile/Arcane_bolt/ES_Magic Transition 3_cropped.mp3"
SOUND_ARCANE_PROJ_VOLUME = 0.05
SOUND_ARCANE_PROJ_MAX_TIME = 0  # in ms

SOUND_FIRE_PROJ_PATH = "Audio/Projectile/Fire_bolt/ES_Fireball Burst 4_cropped.mp3"
SOUND_FIRE_PROJ_VOLUME = 0.1
SOUND_FIRE_PROJ_MAX_TIME = 1200  # in ms

SOUND_LIGHT_PROJ_1_PATH = "Audio/Projectile/Lightning_bolt/ES_Lightning Bolt 1-zone-003.mp3"
SOUND_LIGHT_PROJ_2_PATH = "Audio/Projectile/Lightning_bolt/ES_Lightning Bolt 2-zone-004.mp3"
SOUND_LIGHT_PROJ_3_PATH = "Audio/Projectile/Lightning_bolt/ES_Lightning Bolt 3-zone-005.mp3"
SOUND_LIGHT_PROJ_4_PATH = "Audio/Projectile/Lightning_bolt/ES_Lightning Bolt 4-zone-006.mp3"
SOUND_LIGHT_PROJ_VOLUME = 0.1

SOUND_ICE_BOLT_PROJ_1_PATH = "Audio/Projectile/ICE_BOLT/ES_Magic Spell Build 13-zone-007.mp3"
SOUND_ICE_BOLT_PROJ_2_PATH = "Audio/Projectile/ICE_BOLT/ES_Magic Spell Build 15.mp3"
SOUND_ICE_BOLT_PROJ_VOLUME = 0.05

SOUND_ARCANE_IMPACT_PATH = "Audio/Impact/ES_Energy Blasts 9-zone-000.mp3"
SOUND_ARCANE_IMPACT_VOLUME = 0.0
SOUND_ARCANE_IMPACT_MAX_TIME = 0 # in ms

SOUND_WAVE_PATH = "Audio/Magical_effect/ES_Ocean Waves Crash 3_cropped.mp3"
SOUND_WAVE_VOLUME = 0.1
SOUND_WAVE_MAX_TIME = 0 # in ms

SOUND_ROOT_PATH = "Audio/Magical_effect/plant-growing-sound-effect.mp3"
SOUND_ROOT_VOLUME = 0.5
SOUND_ROOT_MAX_TIME = 0 #2000 # in ms

SOUND_EXPLOSION_PATH = "Audio/Magical_effect/ES_Explosion Blast 6_cropped.mp3"
SOUND_EXPLOSION_VOLUME = 0.5
SOUND_EXPLOSION_MAX_TIME = 0 #2000 # in ms