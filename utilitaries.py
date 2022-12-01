import pygame
 

pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional

RUNNING = True

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

FPS = 120
CLOCK = pygame.time.Clock()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("You Shall Not Pass")
 

SPAWNING_WITH_SCRIPT = False
SPAWNING_MARGIN_SPACE = 0.1

TIME_P1 = 1000000
P1_GOBELIN_SPAWNING_PERIOD = 2.0
    
 

