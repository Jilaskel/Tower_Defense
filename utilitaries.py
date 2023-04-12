import pygame
from globals import * 

pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional

loading_progress = Loading_progress()
global_status = Global_status()

RUNNING = True

############### RESOLUTION
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
# WINDOW_WIDTH = 1920*0.50
# WINDOW_HEIGHT = 1080*0.50

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

GOLD_RESERVE_IMAGE_PATH = "Assets/Gold/GoldReserve.png"  ## useless atm
GOLD_STARTING_AMOUNT = 2000
GOLD_TOWER_REFUND_COEFF = 0.5

GOLD_GAIN_IMAGE_PATH = "Assets/Gold/GoldGain.png"    
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

SPAWNING_WITH_SCRIPT = False

SPAWNING_MARGIN_SPACE = 0.1   ## *background.bush_width
SPAWNING_INITIAL_TIME = 4.0 # in seconds

TIME_P1 = 1000000   ## time phase n1 in seconds
P1_GOBLIN_SPAWNING_PERIOD = 2.0   ## in seconds
P1_OGRE_SPAWNING_PERIOD = 4.0   ## in seconds
P1_BLUE_NEC_SPAWNING_PERIOD = 2.0   ## in seconds
P1_DRAGON_SPAWNING_PERIOD = 10.0   ## in seconds
## MULTIP HP, DAMAGE, VELOCITY
## DEGAT TOUR DIFF IMPACT
## NB MAX SPAWN

##############################################################

###############     BASE     ###############

##############################################################

BASE_GATE_HP_MAX = 100

##############################################################

###############     ENNEMIES     ###############

##############################################################

#### GOBLIN
GOBLIN_DICT = {

"NAME" : "Goblin",
"HP_MAX" : 20.0,
"DAMAGE" : 2.5,
"VELOCITY" : 0.15 * RESIZE_COEFF, # pixel by ms
"GOLD_EARNING" : 2,

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
"ICED_HP_MAX" : 20.0,
"ICED_NAME" : "Iced Goblin",
"ICED_TIME_MAX" : 10.0 # in second

}

#### OGRE
OGRE_DICT = {

"NAME" : "Ogre",
"HP_MAX" : 60.0,
"DAMAGE" : 10,
"VELOCITY" : 0.1 * RESIZE_COEFF, # pixel by ms
"GOLD_EARNING" : 4,

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
"STUN_TIME_PER_FRAME" : 100, # in ms

"ICED_IMAGE_PATH" :  "Assets/Ennemies/Ogre/OgreIced.png",
"ICED_HP_MAX" : 20.0,
"ICED_NAME" : "Iced Goblin",
"ICED_TIME_MAX" : 10.0 # in second

}

#### BLUE_NEC
BLUE_NEC_DICT = {

"NAME" : "Ice Necromancer",
"HP_MAX" : 60.0,
"DAMAGE" : 10,
"VELOCITY" : 0.1 * RESIZE_COEFF, # pixel by ms
"GOLD_EARNING" : 10,

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
"STUN_TIME_PER_FRAME" : 100, # in ms

"ICED_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Blue_Necromancer/BlueNecroIced.png",
"ICED_HP_MAX" : 20.0,
"ICED_NAME" : "Iced Ice Necro",
"ICED_TIME_MAX" : 10.0, # in second

"REZ_RADIUS" : 3.5,
"REZ_COOLDOWN" : 5.0, # in second

"NUMBER_FRAME_CASTING" : 5,
"CASTING_IMAGE_PATH" : "Assets/Ennemies/Necromancers/Blue_Necromancer/SummonAnim/",
"ANIMATION_CASTING_TOTAL_TIME" : 1500 # in ms

}

#### BLUE_SKELETON
BLUE_SKEL_DICT = {

"NAME" : "Ice Skeleton",
"HP_MAX" : 60.0,
"DAMAGE" : 10,
"VELOCITY" : 0.1 * RESIZE_COEFF, # pixel by ms
"GOLD_EARNING" : 4,

"HITBOX_FACTOR" : 1.0,
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF, #   pixel
"OFFSET" : [0* RESIZE_COEFF,-20* RESIZE_COEFF], 
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
"ICED_HP_MAX" : 20.0,
"ICED_NAME" : "Iced Ice Skel",
"ICED_TIME_MAX" : 10.0, # in second

"NUMBER_FRAME_SPAWNING" : 5,
"SPAWNING_IMAGE_PATH" : "Assets/Ennemies/Skeletons/FramesSkeletonBlue/SummonAnim/",
"ANIMATION_SPAWNING_TOTAL_TIME" : 1500

}

#### DRAGON
DRAGON_DICT = {

"NAME" : "Dragon",
"HP_MAX" : 60.0,
"VELOCITY" : 0.1 * RESIZE_COEFF, # pixel by ms
"GOLD_EARNING" : 100,

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

#### ARCANE_TOWER
ARCANE_TOWER_LVL1_DICT = { 

"NAME" : "Arcane tower Lvl.1",
"HP_MAX" : 20.0,
"RANGE" : 2.5, # multiplied by the square side
"PRICE" : 10,
"DAMAGE" : 10.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/Niveau1/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : 800,
"ANIMATION_RELOADING_TOTAL_TIME" : 400,

"OFFSET" : [0.1*BACKGROUND_SQUARE_SIDE,-0.7*BACKGROUND_SQUARE_SIDE],
"RESIZE_FACTOR" : 0.4*RESIZE_COEFF,
"FIRING_OFFSET" : [40* RESIZE_COEFF,50* RESIZE_COEFF],

"UPGRADE_COST" : 200

}

#### ARCANE_TOWER_LVL2
ARCANE_TOWER_LVL2_DICT = { 

"NAME" : "Arcane tower Lvl.2",
"HP_MAX" : 20.0,
"RANGE" : 3.5, # multiplied by the square side
"PRICE" : 200,
"DAMAGE" : 10.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/Niveau2/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : 400,
"ANIMATION_RELOADING_TOTAL_TIME" : 200,

"OFFSET" : ARCANE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : ARCANE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : ARCANE_TOWER_LVL1_DICT["FIRING_OFFSET"],

"UPGRADE_COST" : 600

}

#### ARCANE_TOWER_LVL3
ARCANE_TOWER_LVL3_DICT = { 

"NAME" : "Arcane tower Lvl.3",
"HP_MAX" : 20.0,
"RANGE" : 3.5, # multiplied by the square side
"PRICE" : 400,
"DAMAGE" : 10.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/Niveau3/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : 200,
"ANIMATION_RELOADING_TOTAL_TIME" : 100,

"OFFSET" : ARCANE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : ARCANE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : ARCANE_TOWER_LVL1_DICT["FIRING_OFFSET"],

"UPGRADE_COST" : None

}

#### FIRE_TOWER
FIRE_TOWER_LVL1_DICT = { 

"NAME" : "Fire tower Lvl.1",
"HP_MAX" : 20.0,
"RANGE" : 3.5, # multiplied by the square side
"PRICE" : 10,
"DAMAGE" : 20.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/Niveau1/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : ARCANE_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"],
"ANIMATION_RELOADING_TOTAL_TIME" : ARCANE_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"],

"OFFSET" : ARCANE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : ARCANE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : [40* RESIZE_COEFF,50* RESIZE_COEFF],

"UPGRADE_COST" : 200

}

#### FIRE_TOWER_LVL2
FIRE_TOWER_LVL2_DICT = { 

"NAME" : "Fire tower Lvl.2",
"HP_MAX" : 20.0,
"RANGE" : 4.5, # multiplied by the square side
"PRICE" : 200,
"DAMAGE" : 20.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/Niveau2/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : FIRE_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"],
"ANIMATION_RELOADING_TOTAL_TIME" : FIRE_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"],

"OFFSET" : FIRE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : FIRE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : FIRE_TOWER_LVL1_DICT["FIRING_OFFSET"],

"UPGRADE_COST" : 600

}

#### FIRE_TOWER_LVL3
FIRE_TOWER_LVL3_DICT = { 

"NAME" : "Fire tower Lvl.3",
"HP_MAX" : 20.0,
"RANGE" : 4.5, # multiplied by the square side
"PRICE" : 400,
"DAMAGE" : 20.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/Niveau3/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : FIRE_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"],
"ANIMATION_RELOADING_TOTAL_TIME" : FIRE_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"],

"OFFSET" : FIRE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : FIRE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : FIRE_TOWER_LVL1_DICT["FIRING_OFFSET"],

"UPGRADE_COST" : None

}

#### LIGHTNING_TOWER
LIGHTNING_TOWER_LVL1_DICT = { 

"NAME" : "Lightning tower Lvl.1",
"HP_MAX" : 20.0,
"RANGE" : 3.0, # multiplied by the square side
"PRICE" : 10,
"DAMAGE" : 20.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Jaune/Niveau1/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : ARCANE_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"],
"ANIMATION_RELOADING_TOTAL_TIME" : ARCANE_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"],

"OFFSET" : ARCANE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : ARCANE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : [60* RESIZE_COEFF,60* RESIZE_COEFF],

"UPGRADE_COST" : 200

}

#### LIGHTNING_TOWER_LVL2
LIGHTNING_TOWER_LVL2_DICT = { 

"NAME" : "Lightning tower Lvl.2",
"HP_MAX" : 20.0,
"RANGE" : 4.0, # multiplied by the square side
"PRICE" : 200,
"DAMAGE" : 10.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Jaune/Niveau2/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : LIGHTNING_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"],
"ANIMATION_RELOADING_TOTAL_TIME" : LIGHTNING_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"],

"OFFSET" : LIGHTNING_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : LIGHTNING_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : LIGHTNING_TOWER_LVL1_DICT["FIRING_OFFSET"],

"UPGRADE_COST" : 600

}

#### LIGHTNING_TOWER_LVL3
LIGHTNING_TOWER_LVL3_DICT = { 

"NAME" : "Lightning tower Lvl.3",
"HP_MAX" : 20.0,
"RANGE" : 4.5, # multiplied by the square side
"PRICE" : 400,
"DAMAGE" : 10.0,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Jaune/Niveau3/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : LIGHTNING_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"],
"ANIMATION_RELOADING_TOTAL_TIME" : LIGHTNING_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"],

"OFFSET" : LIGHTNING_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : LIGHTNING_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : LIGHTNING_TOWER_LVL1_DICT["FIRING_OFFSET"],

"UPGRADE_COST" : None

}

#### ICE_TOWER
ICE_TOWER_LVL1_DICT = { 

"NAME" : "Ice tower Lvl.1",
"HP_MAX" : 20.0,
"RANGE" : 2.5, # multiplied by the square side
"PRICE" : 10,
"DAMAGE" : 10,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Bleue/Niveau1/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : ARCANE_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"],
"ANIMATION_RELOADING_TOTAL_TIME" : ARCANE_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"],

"OFFSET" : ARCANE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : ARCANE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : [60* RESIZE_COEFF,70* RESIZE_COEFF],

"UPGRADE_COST" : 200

}

#### ICE_TOWER_LVL2
ICE_TOWER_LVL2_DICT = { 

"NAME" : "Ice tower Lvl.2",
"HP_MAX" : 20.0,
"RANGE" : 2.5, # multiplied by the square side
"PRICE" : 200,
"DAMAGE" : 10,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Bleue/Niveau2/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : ICE_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"],
"ANIMATION_RELOADING_TOTAL_TIME" : ICE_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"],

"OFFSET" : ICE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : ICE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : ICE_TOWER_LVL1_DICT["FIRING_OFFSET"],

"UPGRADE_COST" : 600

}

#### ICE_TOWER_LVL3
ICE_TOWER_LVL3_DICT = { 

"NAME" : "Ice tower Lvl.3",
"HP_MAX" : 20.0,
"RANGE" : 2.5, # multiplied by the square side
"PRICE" : 400,
"DAMAGE" : 10,

"ATTACK_IMAGE_PATH" : "Assets/Tower/ToursMagique/Bleue/Niveau3/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 10,
"ANIMATION_ATTACKING_TOTAL_TIME" : ICE_TOWER_LVL1_DICT["ANIMATION_ATTACKING_TOTAL_TIME"],
"ANIMATION_RELOADING_TOTAL_TIME" : ICE_TOWER_LVL1_DICT["ANIMATION_RELOADING_TOTAL_TIME"],

"OFFSET" : ICE_TOWER_LVL1_DICT["OFFSET"],
"RESIZE_FACTOR" : ICE_TOWER_LVL1_DICT["RESIZE_FACTOR"],
"FIRING_OFFSET" : ICE_TOWER_LVL1_DICT["FIRING_OFFSET"],

"UPGRADE_COST" : None

}

#### BALLISTA
BALLISTA_DICT = { 

"NAME" : "Ballista",
"HP_MAX" : 20.0,
"RANGE" : 6.0, # multiplied by the square side
"PRICE" : 5,
"DAMAGE" : 10,

"ATTACK_IMAGE_PATH" : "Assets/Tower/Baliste/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 5,
"ANIMATION_ATTACKING_TOTAL_TIME" : 200,

"RELOAD_IMAGE_PATH" : "Assets/Tower/Baliste/ReloadAnim/",
"NUMBER_FRAME_RELOADING" : 40,
"ANIMATION_RELOADING_TOTAL_TIME" : 1600,

"OFFSET" : [0* RESIZE_COEFF,20* RESIZE_COEFF],
"RESIZE_FACTOR" : 0.4*RESIZE_COEFF,
"FIRING_OFFSET" : [0* RESIZE_COEFF,40* RESIZE_COEFF],

}

#### CATAPULT
CATAPULT_DICT = { 

"NAME" : "Catapult",
"HP_MAX" : 20.0,
"RANGE" : 8.0, # multiplied by the square side
"PRICE" : 5,
"DAMAGE" : 20,

"ATTACK_IMAGE_PATH" : "Assets/Tower/Catapult/AttackAnim/",
"NUMBER_FRAME_ATTACKING" : 5,
"ANIMATION_ATTACKING_TOTAL_TIME" : 200,

"RELOAD_IMAGE_PATH" : "Assets/Tower/Catapult/ReloadAnim/",
"NUMBER_FRAME_RELOADING" : 55,
"ANIMATION_RELOADING_TOTAL_TIME" : 1600,

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
"CENTOR_VECTOR" : [0.14,0.5],
"RATIO_FOR_IMPACT" : 0.5,

"DAMAGE" : ARCANE_TOWER_LVL1_DICT["DAMAGE"],
"VELOCITY" : 0.75 * RESIZE_COEFF # pixel by ms

}

# ARCANE_BOLT_IMAGE_PATH = "Assets/Tower/ToursMagique/Blanche/projectile/arcane_proj.png"
# ARCANE_BOLT_RESIZE_FACTOR = 0.5*RESIZE_COEFF
# ARCANE_BOLT_CENTOR_VECTOR = [0.14,0.5]
# ARCANE_BOLT_RATIO_FOR_IMPACT = 0.5

# ARCANE_BOLT_DAMAGE = ARCANE_TOWER_LVL1_DICT["DAMAGE"]
# ARCANE_BOLT_VELOCITY = 0.75 * RESIZE_COEFF # pixel by ms

#### ARCANE_BOLT_LVL2
ARCANE_BOLT_LVL2_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/projectile/arcane_proj.png",
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,
"CENTOR_VECTOR" : [0.14,0.5],
"RATIO_FOR_IMPACT" : 0.5,

"DAMAGE" : ARCANE_TOWER_LVL2_DICT["DAMAGE"],
"VELOCITY" : 0.75 * RESIZE_COEFF # pixel by ms

}

# ARCANE_BOLT_LVL2_IMAGE_PATH = "Assets/Tower/ToursMagique/Blanche/projectile/arcane_proj.png"
# ARCANE_BOLT_LVL2_RESIZE_FACTOR = 0.5*RESIZE_COEFF
# ARCANE_BOLT_LVL2_CENTOR_VECTOR = [0.14,0.5]
# ARCANE_BOLT_LVL2_RATIO_FOR_IMPACT = 0.5

# ARCANE_BOLT_LVL2_DAMAGE = ARCANE_TOWER_LVL2_DICT["DAMAGE"]
# ARCANE_BOLT_LVL2_VELOCITY = 0.75 * RESIZE_COEFF # pixel by ms

#### ARCANE_BOLT_LVL3
ARCANE_BOLT_LVL3_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Blanche/projectile/arcane_proj.png",
"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,
"CENTOR_VECTOR" : [0.14,0.5],
"RATIO_FOR_IMPACT" : 0.5,

"DAMAGE" : ARCANE_TOWER_LVL2_DICT["DAMAGE"],
"VELOCITY" : 0.75 * RESIZE_COEFF # pixel by ms

}

# ARCANE_BOLT_LVL3_IMAGE_PATH = "Assets/Tower/ToursMagique/Blanche/projectile/arcane_proj.png"
# ARCANE_BOLT_LVL3_RESIZE_FACTOR = 0.5*RESIZE_COEFF
# ARCANE_BOLT_LVL3_CENTOR_VECTOR = [0.14,0.5]
# ARCANE_BOLT_LVL3_RATIO_FOR_IMPACT = 0.5

# ARCANE_BOLT_LVL3_DAMAGE = ARCANE_TOWER_LVL3_DICT["DAMAGE"]
# ARCANE_BOLT_LVL3_VELOCITY = 0.75 * RESIZE_COEFF # pixel by ms

#### FIRE_BOLT_LVL1
FIRE_BOLT_LVL1_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/ProjectileAnim/",
"NUMBER_FRAME" : 5,
"TOTAL_TIME" : 200,  # in ms

"RESIZE_FACTOR" : 0.25*RESIZE_COEFF,
"CENTOR_VECTOR" : [0.14,0.5],
"RATIO_FOR_IMPACT" : 0.5,

"DAMAGE" : FIRE_TOWER_LVL1_DICT["DAMAGE"],
"VELOCITY" : 0.75 * RESIZE_COEFF # pixel by ms

}

# FIRE_BOLT_IMAGE_PATH = "Assets/Tower/ToursMagique/Rouge/ProjectileAnim/"
# FIRE_BOLT_RESIZE_FACTOR = 0.25*RESIZE_COEFF
# FIRE_BOLT_CENTOR_VECTOR = [0.14,0.5]
# FIRE_BOLT_RATIO_FOR_IMPACT = 0.5

# FIRE_BOLT_DAMAGE = FIRE_TOWER_LVL1_DICT["DAMAGE"]
# FIRE_BOLT_VELOCITY = 0.25 * RESIZE_COEFF # pixel by ms

# FIRE_BOLT_NUMBER_FRAME = 5
# FIRE_BOLT_TOTAL_TIME = 200  # in ms

#### FIRE_BOLT_LVL2
FIRE_BOLT_LVL2_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/ProjectileAnim/",
"NUMBER_FRAME" : 5,
"TOTAL_TIME" : 200,  # in ms

"RESIZE_FACTOR" : 0.25*RESIZE_COEFF,
"CENTOR_VECTOR" : [0.14,0.5],
"RATIO_FOR_IMPACT" : 0.5,

"DAMAGE" : FIRE_TOWER_LVL2_DICT["DAMAGE"],
"VELOCITY" : 0.75 * RESIZE_COEFF # pixel by ms

}

# FIRE_BOLT_LVL2_IMAGE_PATH = "Assets/Tower/ToursMagique/Rouge/ProjectileAnim/"
# FIRE_BOLT_LVL2_RESIZE_FACTOR = 0.25*RESIZE_COEFF
# FIRE_BOLT_LVL2_CENTOR_VECTOR = [0.14,0.5]
# FIRE_BOLT_LVL2_RATIO_FOR_IMPACT = 0.5

# FIRE_BOLT_LVL2_DAMAGE = FIRE_TOWER_LVL2_DICT["DAMAGE"]
# FIRE_BOLT_LVL2_VELOCITY = 0.25 * RESIZE_COEFF # pixel by ms

# FIRE_BOLT_LVL2_NUMBER_FRAME = 5
# FIRE_BOLT_LVL2_TOTAL_TIME = 200  # in ms

#### FIRE_BOLT_LVL3
FIRE_BOLT_LVL3_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Rouge/ProjectileAnimLvl3/",
"NUMBER_FRAME" : 5,
"TOTAL_TIME" : 200,  # in ms

"RESIZE_FACTOR" : 0.25*RESIZE_COEFF,
"CENTOR_VECTOR" : [0.14,0.5],
"RATIO_FOR_IMPACT" : 0.5,

"DAMAGE" : FIRE_TOWER_LVL3_DICT["DAMAGE"],
"VELOCITY" : 0.25 * RESIZE_COEFF # pixel by ms

}

# FIRE_BOLT_LVL3_IMAGE_PATH = "Assets/Tower/ToursMagique/Rouge/ProjectileAnimLvl3/"
# FIRE_BOLT_LVL3_RESIZE_FACTOR = 0.25*RESIZE_COEFF
# FIRE_BOLT_LVL3_CENTOR_VECTOR = [0.14,0.5]
# FIRE_BOLT_LVL3_RATIO_FOR_IMPACT = 0.5

# FIRE_BOLT_LVL3_DAMAGE = FIRE_TOWER_LVL3_DICT["DAMAGE"]
# FIRE_BOLT_LVL3_VELOCITY = 0.25 * RESIZE_COEFF # pixel by ms

# FIRE_BOLT_LVL3_NUMBER_FRAME = 5
# FIRE_BOLT_LVL3_TOTAL_TIME = 200  # in ms

#### LIGHTNING_BOLT_LVL1
LIGHTNING_BOLT_LVL1_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Jaune/ProjectileAnim/",
"NUMBER_FRAME" : 5,
"TIME_PER_FRAME" : 50,  # in ms
"TOTAL_TIME" : 500,  # in ms

"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,  ## only for width
"CENTOR_VECTOR" : [0.5,0.0],

"DAMAGE" : LIGHTNING_TOWER_LVL1_DICT["DAMAGE"],
"STUN_TIME" : 0.0,
"NUMBER_BOUNCE_MAX" : 3,
"DECREASING_DISTANCE_BOUNCE_FACTOR" : 0.2,  # will decrease of X% at each bounce
"DECREASING_DAMAGE_BOUNCE_FACTOR" : 0.25, # will decrease of X% at each bounce
"RANGE" : LIGHTNING_TOWER_LVL1_DICT["RANGE"]

}

# LIGHTNING_BOLT_IMAGE_PATH = "Assets/Tower/ToursMagique/Jaune/ProjectileAnim/"
# LIGHTNING_BOLT_RESIZE_FACTOR = 0.5*RESIZE_COEFF  ## only for width
# LIGHTNING_BOLT_CENTOR_VECTOR = [0.5,0.0]

# LIGHTNING_BOLT_DAMAGE = LIGHTNING_TOWER_LVL1_DICT["DAMAGE"]
# LIGHTNING_BOLT_STUN_TIME = 0.0
# LIGHTNING_BOLT_NUMBER_BOUNCE_MAX = 3
# LIGHTNING_BOLT_DECREASING_DISTANCE_BOUNCE_FACTOR = 0.2  # will decrease of X% at each bounce
# LIGHTNING_BOLT_DECREASING_DAMAGE_BOUNCE_FACTOR = 0.25 # will decrease of X% at each bounce
# LIGHTNING_BOLT_RANGE = LIGHTNING_TOWER_LVL1_DICT["RANGE"]

# LIGHTNING_BOLT_NUMBER_FRAME = 2
# LIGHTNING_BOLT_TIME_PER_FRAME = 50  # in ms
# LIGHTNING_BOLT_TOTAL_TIME = 500  # in ms

#### LIGHTNING_BOLT_LVL2
LIGHTNING_BOLT_LVL2_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Jaune/ProjectileAnim/",
"NUMBER_FRAME" : 5,
"TIME_PER_FRAME" : 50,  # in ms
"TOTAL_TIME" : 500,  # in ms

"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,  ## only for width
"CENTOR_VECTOR" : [0.5,0.0],

"DAMAGE" : LIGHTNING_TOWER_LVL2_DICT["DAMAGE"],
"STUN_TIME" : 0.0,
"NUMBER_BOUNCE_MAX" : 3,
"DECREASING_DISTANCE_BOUNCE_FACTOR" : 0.2,  # will decrease of X% at each bounce
"DECREASING_DAMAGE_BOUNCE_FACTOR" : 0.25, # will decrease of X% at each bounce
"RANGE" : LIGHTNING_TOWER_LVL2_DICT["RANGE"]

}

# LIGHTNING_BOLT_LVL2_IMAGE_PATH = "Assets/Tower/ToursMagique/Jaune/ProjectileAnim/"
# LIGHTNING_BOLT_LVL2_RESIZE_FACTOR = 0.5*RESIZE_COEFF  ## only for width
# LIGHTNING_BOLT_LVL2_CENTOR_VECTOR = [0.5,0.0]

# LIGHTNING_BOLT_LVL2_DAMAGE = LIGHTNING_TOWER_LVL2_DICT["DAMAGE"]
# LIGHTNING_BOLT_LVL2_STUN_TIME = 0.0
# LIGHTNING_BOLT_LVL2_NUMBER_BOUNCE_MAX = 3
# LIGHTNING_BOLT_LVL2_DECREASING_DISTANCE_BOUNCE_FACTOR = 0.2  # will decrease of X% at each bounce
# LIGHTNING_BOLT_LVL2_DECREASING_DAMAGE_BOUNCE_FACTOR = 0.25 # will decrease of X% at each bounce
# LIGHTNING_BOLT_LVL2_RANGE = LIGHTNING_TOWER_LVL2_DICT["RANGE"]

# LIGHTNING_BOLT_LVL2_NUMBER_FRAME = 2
# LIGHTNING_BOLT_LVL2_TIME_PER_FRAME = 50  # in ms
# LIGHTNING_BOLT_LVL2_TOTAL_TIME = 500  # in ms

#### LIGHTNING_BOLT_LVL3
LIGHTNING_BOLT_LVL3_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Jaune/ProjectileAnim3/",
"NUMBER_FRAME" : 5,
"TIME_PER_FRAME" : 50,  # in ms
"TOTAL_TIME" : 500,  # in ms

"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,  ## only for width
"CENTOR_VECTOR" : [0.5,0.0],

"DAMAGE" : LIGHTNING_TOWER_LVL3_DICT["DAMAGE"],
"STUN_TIME" : 2.0,
"NUMBER_BOUNCE_MAX" : 3,
"DECREASING_DISTANCE_BOUNCE_FACTOR" : 0.2,  # will decrease of X% at each bounce
"DECREASING_DAMAGE_BOUNCE_FACTOR" : 0.25, # will decrease of X% at each bounce
"RANGE" : LIGHTNING_TOWER_LVL3_DICT["RANGE"]

}

# LIGHTNING_BOLT_LVL3_IMAGE_PATH = "Assets/Tower/ToursMagique/Jaune/ProjectileAnim3/"
# LIGHTNING_BOLT_LVL3_RESIZE_FACTOR = 0.5*RESIZE_COEFF  ## only for width
# LIGHTNING_BOLT_LVL3_CENTOR_VECTOR = [0.5,0.0]

# LIGHTNING_BOLT_LVL3_DAMAGE = LIGHTNING_TOWER_LVL3_DICT["DAMAGE"]
# LIGHTNING_BOLT_LVL3_STUN_TIME = 2.0
# LIGHTNING_BOLT_LVL3_NUMBER_BOUNCE_MAX = 3
# LIGHTNING_BOLT_LVL3_DECREASING_DISTANCE_BOUNCE_FACTOR = 0.2  # will decrease of X% at each bounce
# LIGHTNING_BOLT_LVL3_DECREASING_DAMAGE_BOUNCE_FACTOR = 0.25 # will decrease of X% at each bounce
# LIGHTNING_BOLT_LVL3_RANGE = LIGHTNING_TOWER_LVL3_DICT["RANGE"]

# LIGHTNING_BOLT_LVL3_NUMBER_FRAME = 2
# LIGHTNING_BOLT_LVL3_TIME_PER_FRAME = 50  # in ms
# LIGHTNING_BOLT_LVL3_TOTAL_TIME = 500  # in ms

#### ICE_BOLT
ICE_BOLT_LVL1_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Bleue/ProjectileAnim/",
"NUMBER_FRAME" : 11,
"TIME_PER_FRAME" : 100,  # in ms
"NUMBER_FRAME_FADING" : 5,
"TOTAL_TIME_FADING" : 500,  # in ms

"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,  ## only for width
"CENTOR_VECTOR" : [0.5,0.0],

"DAMAGE" : ICE_TOWER_LVL1_DICT["DAMAGE"],
"ICE_BOLT_SLOWING_COEFF" : 0.5,
"ICE_BOLT_FREEZING" : False, # Turn ennemie into ice block
"RANGE" : ICE_TOWER_LVL1_DICT["RANGE"]

}

# ICE_BOLT_IMAGE_PATH = "Assets/Tower/ToursMagique/Bleue/ProjectileAnim/"
# ICE_BOLT_RESIZE_FACTOR = 0.5*RESIZE_COEFF  ## only for width
# ICE_BOLT_CENTOR_VECTOR = [0.5,0.0]

# ICE_BOLT_DAMAGE = ICE_TOWER_LVL1_DICT["DAMAGE"] # per second
# ICE_BOLT_SLOWING_COEFF = 0.5
# ICE_BOLT_FREEZING = False # Turn ennemie into ice block
# ICE_BOLT_RANGE = ICE_TOWER_LVL1_DICT["RANGE"]

# ICE_BOLT_NUMBER_FRAME = 11
# ICE_BOLT_TIME_PER_FRAME = 100  # in ms
# ICE_BOLT_NUMBER_FRAME_FADING = 5
# ICE_BOLT_TOTAL_TIME_FADING = 500  # in ms

#### ICE_BOLT_LVL2
ICE_BOLT_LVL2_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Bleue/ProjectileAnim/",
"NUMBER_FRAME" : 11,
"TIME_PER_FRAME" : 100,  # in ms
"NUMBER_FRAME_FADING" : 5,
"TOTAL_TIME_FADING" : 500,  # in ms

"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,  ## only for width
"CENTOR_VECTOR" : [0.5,0.0],

"DAMAGE" : ICE_TOWER_LVL2_DICT["DAMAGE"],
"ICE_BOLT_SLOWING_COEFF" : 0.5,
"ICE_BOLT_FREEZING" : False, # Turn ennemie into ice block
"RANGE" : ICE_TOWER_LVL2_DICT["RANGE"]

}

# ICE_BOLT_LVL2_IMAGE_PATH = "Assets/Tower/ToursMagique/Bleue/ProjectileAnim/"
# ICE_BOLT_LVL2_RESIZE_FACTOR = 0.5*RESIZE_COEFF  ## only for width
# ICE_BOLT_LVL2_CENTOR_VECTOR = [0.5,0.0]

# ICE_BOLT_LVL2_DAMAGE = ICE_TOWER_LVL2_DICT["DAMAGE"] # per second
# ICE_BOLT_LVL2_SLOWING_COEFF = 0.5
# ICE_BOLT_LVL2_FREEZING = False # Turn ennemie into ice block
# ICE_BOLT_LVL2_RANGE = ICE_TOWER_LVL2_DICT["RANGE"]

# ICE_BOLT_LVL2_NUMBER_FRAME = 11
# ICE_BOLT_LVL2_TIME_PER_FRAME = 100  # in ms
# ICE_BOLT_LVL2_NUMBER_FRAME_FADING = 5
# ICE_BOLT_LVL2_TOTAL_TIME_FADING = 500  # in ms

#### ICE_BOLT_LVL3
ICE_BOLT_LVL3_DICT = {

"IMAGE_PATH" : "Assets/Tower/ToursMagique/Bleue/ProjectileAnim/",
"NUMBER_FRAME" : 11,
"TIME_PER_FRAME" : 100,  # in ms
"NUMBER_FRAME_FADING" : 5,
"TOTAL_TIME_FADING" : 500,  # in ms

"RESIZE_FACTOR" : 0.5*RESIZE_COEFF,  ## only for width
"CENTOR_VECTOR" : [0.5,0.0],

"DAMAGE" : ICE_TOWER_LVL3_DICT["DAMAGE"],
"ICE_BOLT_SLOWING_COEFF" : 0.5,
"ICE_BOLT_FREEZING" : True, # Turn ennemie into ice block
"RANGE" : ICE_TOWER_LVL3_DICT["RANGE"]

}

# ICE_BOLT_LVL3_IMAGE_PATH = "Assets/Tower/ToursMagique/Bleue/ProjectileAnim/"
# ICE_BOLT_LVL3_RESIZE_FACTOR = 0.5*RESIZE_COEFF  ## only for width
# ICE_BOLT_LVL3_CENTOR_VECTOR = [0.5,0.0]

# ICE_BOLT_LVL3_DAMAGE = ICE_TOWER_LVL3_DICT["DAMAGE"] # per second
# ICE_BOLT_LVL3_SLOWING_COEFF = 0.5
# ICE_BOLT_LVL3_FREEZING = True # Turn ennemie into ice block
# ICE_BOLT_LVL3_RANGE = ICE_TOWER_LVL3_DICT["RANGE"]

# ICE_BOLT_LVL3_NUMBER_FRAME = 11
# ICE_BOLT_LVL3_TIME_PER_FRAME = 100  # in ms
# ICE_BOLT_LVL3_NUMBER_FRAME_FADING = 5
# ICE_BOLT_LVL3_TOTAL_TIME_FADING = 500  # in ms

#### BOLT
BOLT_DICT = {

"IMAGE_PATH" : "Assets/Tower/Baliste/CarreauBaliste_cropped.png",
"RESIZE_FACTOR" : 0.8*RESIZE_COEFF,
"CENTOR_VECTOR" : [0.16,0.47],
"RATIO_FOR_IMPACT" : 0.5,

"DAMAGE" : BALLISTA_DICT["DAMAGE"],
"VELOCITY" : 2.0 * RESIZE_COEFF # pixel by ms

}

# BOLT_IMAGE_PATH = "Assets/Tower/Baliste/CarreauBaliste_cropped.png"
# BOLT_RESIZE_FACTOR = 0.8*RESIZE_COEFF
# BOLT_CENTOR_VECTOR = [0.16,0.47]
# BOLT_RATIO_FOR_IMPACT = 0.5

# BOLT_DAMAGE = BALLISTA_DICT["DAMAGE"]
# BOLT_VELOCITY = 2.0 * RESIZE_COEFF # pixel by ms

#### ROCK
ROCK_DICT = {

"IMAGE_PATH" : "Assets/Tower/Catapult/Rock_cropped.png",
"RESIZE_FACTOR" : 0.8*RESIZE_COEFF,
"CENTOR_VECTOR" : [0.51,0.78],

"DAMAGE" : BALLISTA_DICT["DAMAGE"],
"VELOCITY" : 2.0 * RESIZE_COEFF, # pixel by ms
"ROTATION_SPEED"  : 0.5 # rotation per second

}

# ROCK_IMAGE_PATH = "Assets/Tower/Catapult/Rock_cropped.png"
# ROCK_RESIZE_FACTOR = 0.8*RESIZE_COEFF
# ROCK_CENTOR_VECTOR = [0.51,0.78]

# ROCK_DAMAGE = CATAPULT_DICT["DAMAGE"]
# ROCK_VELOCITY = 0.60 * RESIZE_COEFF # pixel by ms
# ROCK_ROTATION_SPEED  = 0.5 # rotation per second

##############################################################

###############     IMPACTS     ###############

##############################################################


#### ARCANE_IMPACT
ARCANE_IMPACT_IMAGE_PATH = "Assets/Tower/ToursMagique/Blanche/impact/"
ARCANE_IMPACT_RESIZE_FACTOR = 0.3*RESIZE_COEFF
ARCANE_IMPACT_CENTOR_VECTOR = [0.5,0.83]

ARCANE_IMPACT_NUMBER_FRAME = 17
ARCANE_IMPACT_TOTAL_TIME = 500
ARCANE_IMPACT_DAMAGE_FRAME = 4

#### FIRE_IMPACT
FIRE_IMPACT_IMAGE_PATH = "Assets/Tower/ToursMagique/Rouge/ImpactAnim/"
FIRE_IMPACT_RESIZE_FACTOR = 0.5*RESIZE_COEFF
FIRE_IMPACT_CENTOR_VECTOR = [1.0,1.5]

FIRE_IMPACT_NUMBER_FRAME = 8
FIRE_IMPACT_TOTAL_TIME = 500
FIRE_IMPACT_DAMAGE_FRAME = 4

#### ROCK_IMPACT
ROCK_IMPACT_IMAGE_PATH = "Assets/Tower/Catapult/ImpactAnim/"
ROCK_IMPACT_RESIZE_FACTOR = 0.8*RESIZE_COEFF
ROCK_IMPACT_CENTOR_VECTOR = [0.51,0.78]

ROCK_IMPACT_NUMBER_FRAME = 10
ROCK_IMPACT_TOTAL_TIME = 600
ROCK_IMPACT_DAMAGE_FRAME = 4


##############################################################

###############     AUDIO     ###############

##############################################################

### MUSIC
MUSIC_FILE_PATH = "Audio/Music/Age_of_War_Theme_Soundtrack.mp3"
FADE_UP_TIME = 3.0 # in seconds
MUSIC_VOLUME = 0.00 # 0.05

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

SOUND_ARCANE_PROJ_PATH = "Audio/Projectile/ES_Magic Transition 3.mp3"
SOUND_ARCANE_PROJ_VOLUME = 0.05
SOUND_ARCANE_PROJ_MAX_TIME = 1000  # in ms

SOUND_FIRE_PROJ_PATH = "Audio/Projectile/ES_Fireball Burst 4.mp3"
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

