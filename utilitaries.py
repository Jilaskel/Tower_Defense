import pygame
 

pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional

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

#### GOLD
GOLD_RESERVE_IMAGE_PATH = "Assets/Gold/GoldReserve.png"  ## useless atm
GOLD_STARTING_AMOUNT = 20

GOLD_GAIN_IMAGE_PATH = "Assets/Gold/GoldGain.png"    
GOLD_GAIN_RESIZE_FACTOR = 0.25
GOLD_GAIN_FONT_SIZE = 50
GOLD_GAIN_OFFSET = [0*RESIZE_COEFF, 0*RESIZE_COEFF]
GOLD_GAIN_TIME = 1000  # in ms
GOLD_GAIN_TRAVEL_VECTOR = [0*RESIZE_COEFF, 200*RESIZE_COEFF] 

#### MOUSE
MOUSE_IMAGE_PATH = "Assets/Cursor/cursor6.png"
MOUSE_RESIZE_FACTOR = 0.4*RESIZE_COEFF
MOUSE_RATIO_FOR_HITBOX = 1.0

MOUSE_CARRIED_IMAGE_ALPHA = 100

MOUSE_VALID_BOX_IMAGE_PATH = "Assets/Tower/Valid_boxes/valid.png"
MOUSE_VALID_BOX_IMAGE_ALPHA = 150
MOUSE_NOT_VALID_BOX_IMAGE_PATH = "Assets/Tower/Valid_boxes/not_valid.png"
MOUSE_NOT_VALID_BOX_IMAGE_ALPHA = 150

#### MENU
MENU_BUTTON_SIZE = [BACKGROUND_SQUARE_SIDE,BACKGROUND_SQUARE_SIDE]
MENU_ARCANE_TOWER_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/arcane_tower_button_2.png"
MENU_BALLISTA_BUTTON_IMAGE_PATH = "Assets/Menu/Buttons/ballista_button_2.png"

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
GOBELIN_OFFSET = [50* RESIZE_COEFF,-25* RESIZE_COEFF] 
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
ARCANE_TOWER_PRICE = 5

ARCANE_TOWER_ATTACK_IMAGE_PATH = "Assets/Tower/ToursMagique/Blanche/AttackAnim/"
ARCANE_TOWER_NUMBER_FRAME_ATTACKING = 10
ARCANE_TOWER_ANIMATION_ATTACKING_TOTAL_TIME = 800
ARCANE_TOWER_RELOAD_IMAGE_PATH = "Assets/Tower/ToursMagique/Blanche/ReloadAnim/"
ARCANE_TOWER_NUMBER_FRAME_RELOADING = 10
ARCANE_TOWER_ANIMATION_RELOADING_TOTAL_TIME = 400

ARCANE_TOWER_OFFSET = [-0.0*BACKGROUND_SQUARE_SIDE,-1.2*BACKGROUND_SQUARE_SIDE] 
ARCANE_TOWER_RESIZE_FACTOR = 0.5*RESIZE_COEFF
ARCANE_TOWER_FIRING_OFFSET = [50* RESIZE_COEFF,0* RESIZE_COEFF]

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


###############     PROJECTILES     ###############

#### BOLT
BOLT_IMAGE_PATH = "Assets/Tower/Baliste/CarreauBaliste_cropped.png"
BOLT_RESIZE_FACTOR = 0.8*RESIZE_COEFF
BOLT_CENTOR_VECTOR = [0.16,0.47]
BOLT_RATIO_FOR_IMPACT = 0.5

BOLT_DAMAGE = 10.0
BOLT_VELOCITY = 2.0 * RESIZE_COEFF # pixel by ms


#### ARCANE_BOLT
ARCANE_BOLT_IMAGE_PATH = "Assets/Tower/ToursMagique/Blanche/projectile/arcane_proj.png"
ARCANE_BOLT_RESIZE_FACTOR = 0.5*RESIZE_COEFF
ARCANE_BOLT_CENTOR_VECTOR = [0.14,0.5]
ARCANE_BOLT_RATIO_FOR_IMPACT = 0.5

ARCANE_BOLT_DAMAGE = 20.0
ARCANE_BOLT_VELOCITY = 1.5 * RESIZE_COEFF # pixel by ms


###############     IMPACTS     ###############

#### ARCANE_IMPACT
ARCANE_IMPACT_IMAGE_PATH = "Assets/Tower/ToursMagique/Blanche/impact/"
ARCANE_IMPACT_RESIZE_FACTOR = 0.3*RESIZE_COEFF
ARCANE_IMPACT_CENTOR_VECTOR = [0.5,0.83]

ARCANE_IMPACT_NUMBER_FRAME = 17
ARCANE_IMPACT_TOTAL_TIME = 500
ARCANE_IMPACT_DAMAGE_FRAME = 4

