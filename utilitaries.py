import pygame
from globals import * 

pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional

loading_progress = Loading_progress()

RUNNING = True
START_WITH_SPACE_BAR = False

### RESOLUTION
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
# WINDOW_WIDTH = 1920*0.50
# WINDOW_HEIGHT = 1080*0.50

RESIZE_COEFF = WINDOW_WIDTH/1920

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

### GAME
GAME_TITLE = "You Shall Not Pass"
GAME_ICON_PATH = "Assets/game_icon.png"

pygame.display.set_caption(GAME_TITLE)
pygame_icon = pygame.image.load(GAME_ICON_PATH)
pygame.display.set_icon(pygame_icon)

### FPS
FPS = 60
CLOCK = pygame.time.Clock() 
TOTAL_NUMBER_RENDERING_LAYER = 25

### MUSIC
MUSIC_FILE_PATH = "Audio/Music/Age_of_War_Theme_Soundtrack.mp3"
FADE_UP_TIME = 3.0 # in seconds
MUSIC_VOLUME = 0.1

#### BACKGROUND
BACKGROUND_IMAGE_PATH = "Assets/Background/BackgroundNoGrassAsset_menu_2.png"
BACKGROUND_GRASS_ASSETS_PATH = "Assets/Background/GrassAsset/"
BACKGROUND_SQUARE_SIDE = WINDOW_HEIGHT/8.0

#### FONT
FONT_PATH = "Font/Kingcastle-0W8Kr.ttf"
# LOADING_FONT_PATH = "Font/DragonFire-K7voy.ttf"
LOADING_FONT_PATH = "Font/misc/Balgruf-d256.woff"

#### GOLD
GOLD_RESERVE_IMAGE_PATH = "Assets/Gold/GoldReserve.png"  ## useless atm
GOLD_STARTING_AMOUNT = 20

GOLD_GAIN_IMAGE_PATH = "Assets/Gold/GoldGain.png"    
GOLD_GAIN_RESIZE_FACTOR = 0.125*RESIZE_COEFF
GOLD_GAIN_FONT_SIZE = 25*RESIZE_COEFF
GOLD_GAIN_POSITIVE_RGB = (0,0,153)
GOLD_GAIN_NEGATIVE_RGB = (153,0,0)
GOLD_GAIN_OFFSET = [0*RESIZE_COEFF, 0*RESIZE_COEFF]  ## offset with the center of the object
GOLD_GAIN_TIME = 2000  # in ms
GOLD_GAIN_TRAVEL_VECTOR = [0*RESIZE_COEFF, -100*RESIZE_COEFF] 

#### ERROR MESSAGE
ERROR_MESSAGE_IMAGE_PATH = "Assets/Error/error.png"
ERROR_MESSAGE_RGB = (153,0,0)
ERROR_MESSAGE_RESIZE_FACTOR = 0.1*RESIZE_COEFF
ERROR_MESSAGE_FONT_SIZE = 25*RESIZE_COEFF
ERROR_MESSAGE_OFFSET = [0*RESIZE_COEFF, 0*RESIZE_COEFF]
ERROR_MESSAGE_TIME = 2000
ERROR_MESSAGE_TRAVEL_VECTOR = [0*RESIZE_COEFF, -100*RESIZE_COEFF]

#### MOUSE
MOUSE_IMAGE_PATH = "Assets/Cursor/cursor6.png"
MOUSE_RESIZE_FACTOR = 0.4*RESIZE_COEFF
MOUSE_RATIO_FOR_HITBOX = 1.0

MOUSE_CARRIED_IMAGE_ALPHA = 100
MOUSE_OVER_ENLARGED_COEFF = 1.5

MOUSE_VALID_BOX_IMAGE_PATH = "Assets/Tower/Valid_boxes/valid.png"
MOUSE_VALID_BOX_IMAGE_ALPHA = 150
MOUSE_NOT_VALID_BOX_IMAGE_PATH = "Assets/Tower/Valid_boxes/not_valid.png"
MOUSE_NOT_VALID_BOX_IMAGE_ALPHA = 150

#### MENU
MENU_BUTTON_SIZE = [BACKGROUND_SQUARE_SIDE,BACKGROUND_SQUARE_SIDE]
MENU_ARCANE_TOWER_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/arcane_tower_button.png"
MENU_FIRE_TOWER_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/fire_tower_button.png"
MENU_ICE_TOWER_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/ice_tower_button.png"
MENU_LIGHTNING_TOWER_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/lightning_tower_button.png"
MENU_BALLISTA_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/ballista_button.png"
MENU_CATAPULT_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/catapult_button.png"

MENU_GOLD_RESERVE_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/gold_reserve_button.png"
MENU_GOLD_RESERVE_BUTTON_RESIZE_FACTOR = 0.33*RESIZE_COEFF

#### ENNEMIES SPAWNING 
SPAWNING_WITH_SCRIPT = False

SPAWNING_MARGIN_SPACE = 0.1   ## *background.bush_width
SPAWNING_INITIAL_TIME = 4.0 # in seconds

TIME_P1 = 1000000   ## time phase n1 in seconds
P1_GOBELIN_SPAWNING_PERIOD = 2.0   ## in seconds
P1_OGRE_SPAWNING_PERIOD = 4.0   ## in seconds

###############     BASE     ###############
BASE_GATE_HP_MAX = 10000


###############     ENNEMIES     ###############

#### GOBELIN
GOBELIN_HP_MAX = 20.0
GOBELIN_DAMAGE = 2.5
GOBELIN_VELOCITY = 0.15 * RESIZE_COEFF # pixel by ms
GOBELIN_GOLD_EARNING = 2

GOBELIN_HITBOX_FACTOR = 1.0
GOBELIN_RESIZE_FACTOR = 0.5*RESIZE_COEFF #   pixel
GOBELIN_OFFSET = [50* RESIZE_COEFF,-20* RESIZE_COEFF] 
GOBELIN_CENTER_VECTOR = [0.26, 0.63] 

GOBELIN_WALKING_IMAGE_PATH = "Assets/Ennemies/Gobelin/WalkAnim/"
GOBELIN_NUMBER_FRAME_WALKING = 20
GOBELIN_ANIMATION_WALKING_TOTAL_TIME = 600 # in ms
GOBELIN_STOP_WALKING_FRAME = 11
 
GOBELIN_NUMBER_FRAME_TRANSITION  = 1
GOBELIN_TRANSITION_IMAGE_PATH = "Assets/Ennemies/Gobelin/TransitionAnim/"
GOBELIN_ANIMATION_TRANSITION_TOTAL_TIME = 300 # in ms

GOBELIN_NUMBER_FRAME_ATTACKING  = 10
GOBELIN_ATTACKING_IMAGE_PATH = "Assets/Ennemies/Gobelin/AttackAnim/"
GOBELIN_ANIMATION_ATTACKING_TOTAL_TIME = 300 # in ms
GOBELIN_HITTING_FRAME = 5

GOBELIN_NUMBER_FRAME_DEATH  = 20
GOBELIN_DEATH_IMAGE_PATH = "Assets/Ennemies/Gobelin/DeathAnim/"
GOBELIN_ANIMATION_DEATH_TOTAL_TIME = 1000 # in ms
GOBELIN_FADING_TIME = 3000 # in ms

#### OGRE
OGRE_HP_MAX = 60.0
OGRE_DAMAGE = 10
OGRE_VELOCITY = 0.1 * RESIZE_COEFF # pixel by ms
OGRE_GOLD_EARNING = 4

OGRE_HITBOX_FACTOR = 1.0
OGRE_RESIZE_FACTOR = 0.75*RESIZE_COEFF
OGRE_OFFSET = [0* RESIZE_COEFF,-80* RESIZE_COEFF] 
OGRE_CENTER_VECTOR = [0.37, 0.59]

OGRE_WALKING_IMAGE_PATH = "Assets/Ennemies/Ogre/WalkAnim/"
OGRE_NUMBER_FRAME_WALKING = 20
OGRE_ANIMATION_WALKING_TOTAL_TIME = 600*1.5 # in ms
OGRE_STOP_WALKING_FRAME = 16
 
OGRE_NUMBER_FRAME_TRANSITION  = 4
OGRE_TRANSITION_IMAGE_PATH = "Assets/Ennemies/Ogre/TransitionAnim/"
OGRE_ANIMATION_TRANSITION_TOTAL_TIME = 300 # in ms

OGRE_NUMBER_FRAME_ATTACKING  = 15
OGRE_ATTACKING_IMAGE_PATH = "Assets/Ennemies/Ogre/AttackAnim/"
OGRE_ANIMATION_ATTACKING_TOTAL_TIME = 300*3 # in ms
OGRE_HITTING_FRAME = 13

OGRE_NUMBER_FRAME_DEATH  = 20
OGRE_DEATH_IMAGE_PATH = "Assets/Ennemies/Ogre/DeathAnim/"
OGRE_ANIMATION_DEATH_TOTAL_TIME = 600 # in ms
OGRE_FADING_TIME = 3000 # in ms

###############     TOWERS     ###############
TOWER_RECT_RANGE_IMAGE_PATH = "Assets/Tower/Range_boxes/rect_range.png"
TOWER_RECT_RANGE_IMAGE_ALPHA = 100
TOWER_CIRCLE_RANGE_IMAGE_PATH = "Assets/Tower/Range_boxes/circle_range.png"
TOWER_CIRCLE_RANGE_IMAGE_ALPHA = 100

#### ARCANE_TOWER
ARCANE_TOWER_HP_MAX = 20.0
ARCANE_TOWER_RANGE = 2.5 # multiplied by the square side
ARCANE_TOWER_PRICE = 10

ARCANE_TOWER_ATTACK_IMAGE_PATH = "Assets/Tower/ToursMagique/Blanche/AttackAnim/"
ARCANE_TOWER_NUMBER_FRAME_ATTACKING = 10
ARCANE_TOWER_ANIMATION_ATTACKING_TOTAL_TIME = 800
ARCANE_TOWER_RELOAD_IMAGE_PATH = "Assets/Tower/ToursMagique/Blanche/ReloadAnim/"
ARCANE_TOWER_NUMBER_FRAME_RELOADING = 10
ARCANE_TOWER_ANIMATION_RELOADING_TOTAL_TIME = 400

ARCANE_TOWER_OFFSET = [0.1*BACKGROUND_SQUARE_SIDE,-0.7*BACKGROUND_SQUARE_SIDE] 
ARCANE_TOWER_RESIZE_FACTOR = 0.4*RESIZE_COEFF
ARCANE_TOWER_FIRING_OFFSET = [40* RESIZE_COEFF,50* RESIZE_COEFF]


#### FIRE_TOWER
FIRE_TOWER_HP_MAX = 20.0
FIRE_TOWER_RANGE = 4.5 # multiplied by the square side
FIRE_TOWER_PRICE = 10

FIRE_TOWER_ATTACK_IMAGE_PATH = "Assets/Tower/ToursMagique/Rouge/AttackAnim/"
FIRE_TOWER_NUMBER_FRAME_ATTACKING = ARCANE_TOWER_NUMBER_FRAME_ATTACKING
FIRE_TOWER_ANIMATION_ATTACKING_TOTAL_TIME = ARCANE_TOWER_ANIMATION_ATTACKING_TOTAL_TIME
FIRE_TOWER_RELOAD_IMAGE_PATH = "Assets/Tower/ToursMagique/Rouge/ReloadAnim/"
FIRE_TOWER_NUMBER_FRAME_RELOADING = ARCANE_TOWER_NUMBER_FRAME_RELOADING
FIRE_TOWER_ANIMATION_RELOADING_TOTAL_TIME = ARCANE_TOWER_ANIMATION_RELOADING_TOTAL_TIME

FIRE_TOWER_OFFSET = ARCANE_TOWER_OFFSET 
FIRE_TOWER_RESIZE_FACTOR = ARCANE_TOWER_RESIZE_FACTOR
FIRE_TOWER_FIRING_OFFSET = [40* RESIZE_COEFF,50* RESIZE_COEFF]


#### LIGHTNING_TOWER
LIGHTNING_TOWER_HP_MAX = 20.0
LIGHTNING_TOWER_RANGE = 2.5 # multiplied by the square side
LIGHTNING_TOWER_PRICE = 10

LIGHTNING_TOWER_ATTACK_IMAGE_PATH = "Assets/Tower/ToursMagique/Jaune/AttackAnim/"
LIGHTNING_TOWER_NUMBER_FRAME_ATTACKING = ARCANE_TOWER_NUMBER_FRAME_ATTACKING
LIGHTNING_TOWER_ANIMATION_ATTACKING_TOTAL_TIME = ARCANE_TOWER_ANIMATION_ATTACKING_TOTAL_TIME
LIGHTNING_TOWER_RELOAD_IMAGE_PATH = "Assets/Tower/ToursMagique/Jaune/ReloadAnim/"
LIGHTNING_TOWER_NUMBER_FRAME_RELOADING = ARCANE_TOWER_NUMBER_FRAME_RELOADING
LIGHTNING_TOWER_ANIMATION_RELOADING_TOTAL_TIME = ARCANE_TOWER_ANIMATION_RELOADING_TOTAL_TIME

LIGHTNING_TOWER_OFFSET = ARCANE_TOWER_OFFSET 
LIGHTNING_TOWER_RESIZE_FACTOR = ARCANE_TOWER_RESIZE_FACTOR
LIGHTNING_TOWER_FIRING_OFFSET = [40* RESIZE_COEFF,50* RESIZE_COEFF]

#### ICE_TOWER
ICE_TOWER_HP_MAX = 20.0
ICE_TOWER_RANGE = 2.5 # multiplied by the square side
ICE_TOWER_PRICE = 10

ICE_TOWER_ATTACK_IMAGE_PATH = "Assets/Tower/ToursMagique/Bleue/AttackAnim/"
ICE_TOWER_NUMBER_FRAME_ATTACKING = ARCANE_TOWER_NUMBER_FRAME_ATTACKING
ICE_TOWER_ANIMATION_ATTACKING_TOTAL_TIME = ARCANE_TOWER_ANIMATION_ATTACKING_TOTAL_TIME
ICE_TOWER_RELOAD_IMAGE_PATH = "Assets/Tower/ToursMagique/Bleue/ReloadAnim/"
ICE_TOWER_NUMBER_FRAME_RELOADING = ARCANE_TOWER_NUMBER_FRAME_RELOADING
ICE_TOWER_ANIMATION_RELOADING_TOTAL_TIME = ARCANE_TOWER_ANIMATION_RELOADING_TOTAL_TIME

ICE_TOWER_OFFSET = ARCANE_TOWER_OFFSET 
ICE_TOWER_RESIZE_FACTOR = ARCANE_TOWER_RESIZE_FACTOR
ICE_TOWER_FIRING_OFFSET = [40* RESIZE_COEFF,50* RESIZE_COEFF]


#### BALLISTA
BALLISTA_HP_MAX = 20.0
BALLISTA_RANGE = 6.0 # multiplied by the square side
BALLISTA_PRICE = 5

BALLISTA_ATTACK_IMAGE_PATH = "Assets/Tower/Baliste/AttackAnim/"
BALLISTA_NUMBER_FRAME_ATTACKING = 5
BALLISTA_ANIMATION_ATTACKING_TOTAL_TIME = 200
BALLISTA_RELOAD_IMAGE_PATH = "Assets/Tower/Baliste/ReloadAnim/"
BALLISTA_NUMBER_FRAME_RELOADING = 40
BALLISTA_ANIMATION_RELOADING_TOTAL_TIME = 1600

BALLISTA_OFFSET = [0* RESIZE_COEFF,20* RESIZE_COEFF] 
BALLISTA_RESIZE_FACTOR = 0.4*RESIZE_COEFF
BALLISTA_FIRING_OFFSET = [0* RESIZE_COEFF,40* RESIZE_COEFF] 

#### CATAPULT
CATAPULT_HP_MAX = 20.0
CATAPULT_RANGE = 8.0 # multiplied by the square side
CATAPULT_PRICE = 5

CATAPULT_ATTACK_IMAGE_PATH = "Assets/Tower/Catapult/AttackAnim/"
CATAPULT_NUMBER_FRAME_ATTACKING = 5
CATAPULT_ANIMATION_ATTACKING_TOTAL_TIME = 200
CATAPULT_RELOAD_IMAGE_PATH = "Assets/Tower/Catapult/ReloadAnim/"
CATAPULT_NUMBER_FRAME_RELOADING = 55
CATAPULT_ANIMATION_RELOADING_TOTAL_TIME = 1600

CATAPULT_OFFSET = [0* RESIZE_COEFF,-20* RESIZE_COEFF] 
CATAPULT_RESIZE_FACTOR = 1.0*RESIZE_COEFF
CATAPULT_FIRING_OFFSET = [40* RESIZE_COEFF,20* RESIZE_COEFF] 

###############     PROJECTILES     ###############

#### BOLT
BOLT_IMAGE_PATH = "Assets/Tower/Baliste/CarreauBaliste_cropped.png"
BOLT_RESIZE_FACTOR = 0.8*RESIZE_COEFF
BOLT_CENTOR_VECTOR = [0.16,0.47]
BOLT_RATIO_FOR_IMPACT = 0.5

BOLT_DAMAGE = 10.0
BOLT_VELOCITY = 2.0 * RESIZE_COEFF # pixel by ms

#### ROCK
ROCK_IMAGE_PATH = "Assets/Tower/Catapult/Rock_cropped.png"
ROCK_RESIZE_FACTOR = 0.8*RESIZE_COEFF
ROCK_CENTOR_VECTOR = [0.51,0.78]

ROCK_DAMAGE = 20.0
ROCK_VELOCITY = 0.60 * RESIZE_COEFF # pixel by ms
ROCK_ROTATION_SPEED  = 0.5 # rotation per second

#### ARCANE_BOLT
ARCANE_BOLT_IMAGE_PATH = "Assets/Tower/ToursMagique/Blanche/projectile/arcane_proj.png"
ARCANE_BOLT_RESIZE_FACTOR = 0.5*RESIZE_COEFF
ARCANE_BOLT_CENTOR_VECTOR = [0.14,0.5]
ARCANE_BOLT_RATIO_FOR_IMPACT = 0.5

ARCANE_BOLT_DAMAGE = 10.0
ARCANE_BOLT_VELOCITY = 0.75 * RESIZE_COEFF # pixel by ms

#### FIRE_BOLT
FIRE_BOLT_IMAGE_PATH = "Assets/Tower/ToursMagique/Rouge/ProjectileAnim/"
FIRE_BOLT_RESIZE_FACTOR = 0.25*RESIZE_COEFF
FIRE_BOLT_CENTOR_VECTOR = [0.14,0.5]
FIRE_BOLT_RATIO_FOR_IMPACT = 0.5

FIRE_BOLT_DAMAGE = 20.0
FIRE_BOLT_VELOCITY = 0.25 * RESIZE_COEFF # pixel by ms

FIRE_BOLT_NUMBER_FRAME = 5
FIRE_BOLT_TOTAL_TIME = 200  # in ms


###############     IMPACTS     ###############

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



###############     AUDIO     ###############
AUDIO_EFFECTS_COEF = 1.0

SOUND_BUILDING_PATH = "Audio/Other_effect/ES_Impact Wood Hit 6 - SFX Producer.mp3"
SOUND_BUILDING_VOLUME = 0.1

SOUND_FALLING_PATH = "Audio/Ennemy/ES_Body Fall Heavy Rustle 2 - SFX Producer.mp3"
SOUND_FALLING_VOLUME = 0.1

SOUND_ROCK_PATH = "Audio/Impact/ES_Rock Impact - SFX Producer.mp3"
SOUND_ROCK_VOLUME = 0.05