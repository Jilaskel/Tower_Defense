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
            self.all_ennemies = pygame.sprite.Group()
            self.all_ennemies.add(Ennemy(self,self.background.bush_width,135))
            y_milieu = self.background.menu_height + 2*self.background.square_side
            self.all_ennemies.add(Gobelin(self,self.background.bush_width,y_milieu))
            #self.ennemy = Ennemy(self,self.background.bush_width,135)

      def move_objects(self):
            for ennemy in self.all_ennemies:
                  ennemy.move()

      def render(self):
            self.background.render()
            self.tower.render()
            for ennemy in self.all_ennemies:
                  ennemy.render()
            pygame.display.update()      
            FPS_CLOCK.tick(FPS)


 

