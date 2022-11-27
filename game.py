import pygame
from background import *
from tower import *
from ennemy import *
from utilitaries import *

############################# 
## Main functions
#############################

class Game():
      def __init__(self):
            self.background = Background()
            self.tower = Tower(self)
            self.ennemy = Ennemy(self)

      def move_objects(self):
            self.ennemy.move()

      def render(self):
            self.background.render()
            self.tower.render()
            self.ennemy.render()
            pygame.display.update()      
            FPS_CLOCK.tick(FPS)


 

