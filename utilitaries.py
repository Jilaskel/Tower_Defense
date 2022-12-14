import pygame
 

pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional

RUNNING = True
START_WITH_SPACE_BAR = False

### RESOLUTION
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("You Shall Not Pass")

### FPS
FPS = 120
CLOCK = pygame.time.Clock() 

### MUSIC
MUSIC_FILE_PATH = "Audio/Music/Age_of_War_Theme Soundtrack.mp3"
FADE_UP_TIME = 3.0 # in seconds
MUSIC_VOLUME = 0.1

#### BACKGROUND
BACKGROUND_IMAGE_PATH = "Assets/Background/background1.png"
BACKGROUND_SQUARE_SIDE = WINDOW_HEIGHT/8.0

#### MOUSE
MOUSE_IMAGE_PATH = "Assets/Cursor/cursor4.png"
MOUSE_SIZE = [40.8,50]  #   pixel
MOUSE_RATIO_FOR_HITBOX = 1.0

MOUSE_CARRIED_IMAGE_ALPHA = 100

MOUSE_VALID_BOX_IMAGE_PATH = "Assets/Tower/Valid_boxes/valid.png"
MOUSE_VALID_BOX_IMAGE_ALPHA = 150
MOUSE_NOT_VALID_BOX_IMAGE_PATH = "Assets/Tower/Valid_boxes/not_valid.png"
MOUSE_NOT_VALID_BOX_IMAGE_ALPHA = 150

#### MENU
MENU_BUTTON_SIZE = [BACKGROUND_SQUARE_SIDE,BACKGROUND_SQUARE_SIDE]
MENU_BASIC_TOWER_BUTTON_IMAGE_PATH = "Assets/Tower/Frame1.png"
MENU_BALLISTA_BUTTON_IMAGE_PATH = "Assets/Tower/Baliste/AnimAttack/0001.png"

#### ENNEMIES SPAWNING 
SPAWNING_WITH_SCRIPT = False
SPAWNING_MARGIN_SPACE = 0.1   ## *background.bush_width
SPAWNING_INITIAL_TIME = 4.0 # in seconds

TIME_P1 = 1000000   ## time phase n1 in seconds
P1_GOBELIN_SPAWNING_PERIOD = 2.0   ## in seconds


###############     ENNEMIES     ###############

#### GOBELIN
GOBELIN_HP_MAX = 20.0
GOBELIN_DAMAGE = 2.5
GOBELIN_VELOCITY = 0.2 # pixel by ms
GOBELIN_HITBOX_FACTOR = 0.8

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


###############     TOWERS     ###############
TOWER_RECT_RANGE_IMAGE_PATH = "Assets/Tower/Range_boxes/rect_range.png"
TOWER_RECT_RANGE_IMAGE_ALPHA = 100
TOWER_CIRCLE_RANGE_IMAGE_PATH = "Assets/Tower/Range_boxes/circle_range.png"
TOWER_CIRCLE_RANGE_IMAGE_ALPHA = 100

#### BASIC_TOWER
BASIC_TOWER_HP_MAX = 20.0
BASIC_TOWER_IMAGE_PATH = "Assets/Tower/Frame1.png"
BASIC_TOWER_SIZE = [BACKGROUND_SQUARE_SIDE,BACKGROUND_SQUARE_SIDE] #   pixel

BASIC_TOWER_FIRING_PERIOD = 900 # in ms
BASIC_TOWER_RANGE = 2.5 # multiplied by the image size

#### BALLISTA
BALLISTA_HP_MAX = 20.0
BALLISTA_ATTACK_IMAGE_PATH = "Assets/Tower/Baliste/AnimAttack/"
BALLISTA_SIZE = [BACKGROUND_SQUARE_SIDE,BACKGROUND_SQUARE_SIDE] #   pixel
BALLISTA_NUMBER_FRAME_ATTACKING = 45
BALLISTA_FIRING_FRAME = 5

BALLISTA_FIRING_PERIOD = 1800 # in ms
BALLISTA_RANGE = 6.0 # multiplied by the image size


###############     PROJECTILES     ###############

#### BOLT
BOLT_IMAGE_PATH = "Assets/Tower/Baliste/CarreauBaliste.png"
BOLT_RATIO_FOR_IMPACT = 0.25

BOLT_DAMAGE = 5.0
BOLT_VELOCITY = 2.0 # pixel by ms