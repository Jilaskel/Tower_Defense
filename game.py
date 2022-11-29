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
            self.timestep = CLOCK.get_time()
            self.background = Background()

            x_middle = self.background.bush_width + 6*self.background.square_side
            y_middle = self.background.menu_height + 2*self.background.square_side

            self.all_towers = pygame.sprite.Group()
            self.all_towers.add(Ballista(self,x_middle,y_middle))
            self.all_towers.add(Basic_tower(self,x_middle,y_middle+2*self.background.square_side))

            self.all_projectiles = pygame.sprite.Group()

            self.all_ennemies = pygame.sprite.Group()
            self.all_ennemies.add(Gobelin(self.background.bush_width*0.1,y_middle))

      def fight(self):
            for tower in self.all_towers:
                  tower.check_ennemies(self)
                  tower.attack_and_reload(self)

      def move_objects(self):
            for ennemy in self.all_ennemies:
                  ennemy.move(self)
                  
            for projectile in self.all_projectiles:
                  projectile.move(self)
                  projectile.check_impact(self)

      def render(self):
            self.background.render()

            for tower in self.all_towers:
                  tower.render(self)

            for projectile in self.all_projectiles:
                  projectile.render(self)

            for ennemy in self.all_ennemies:
                  ennemy.render(self)

            pygame.display.update()
            CLOCK.tick(FPS)
            self.timestep = CLOCK.get_time()
                  
            


 

