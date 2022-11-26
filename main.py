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
 
############################# 
## Classes (will move in other files in futur)
#############################
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
            self.vel = vec(0,0)
            self.vel.x = 20

      def move(self):
            # Will set running to False if the player has slowed down to a certain extent
            self.bgX += self.vel.x


      def render(self):
            window.blit(self.bgimage, (self.bgX, self.bgY))  

############################# 
## Main functions
#############################


background = Background()
tower = Tower()
ennemy = Ennemy()

def game_move_objects():
      ennemy.move()

def game_render():
      background.render()
      tower.render()
      ennemy.render()
      pygame.display.update()      
      FPS_CLOCK.tick(FPS)


############################# 
## MAIN LOOP
#############################
game_has_started = False
while True:
      for event in pygame.event.get():
            if event.type == QUIT:
                  pygame.quit()
                  sys.exit()
      # Event handling for a range of different key presses    
            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_SPACE:
                        game_has_started = True


      if game_has_started:
            game_move_objects()
      game_render()
    
 

