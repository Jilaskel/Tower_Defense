import pygame
from pygame.locals import *
import sys
import random
import time
 
pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional

WIDTH = 1920
HEIGHT = 1080

FPS = 60
FPS_CLOCK = pygame.time.Clock()
 
FramePerSec = pygame.time.Clock()
 
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("You Shall Not Pass")

 ## background size = 80% of window ==> 1536x864
 
class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load("Assets/Background/background.png").convert()    
            self.bgX = 170
            self.bgY = 100

      def render(self):
            window.blit(self.bgimage, (self.bgX, self.bgY))    

class Tower(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load("Assets/Tower/tower1.png").convert()    
            self.bgX = 800
            self.bgY = 500


      def render(self):
            window.blit(self.bgimage, (self.bgX, self.bgY))  


class Ennemy(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load("Assets/Ennemies/ennemy1.png").convert()    
            self.bgX = 400
            self.bgY = 500


      def render(self):
            window.blit(self.bgimage, (self.bgX, self.bgY))  


background = Background()
tower = Tower()
ennemy = Ennemy()

def game_render():
    background.render()
    tower.render()
    ennemy.render()
    pygame.display.update()      
    FPS_CLOCK.tick(FPS)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    game_render()
    
 

