import pygame
from audio_mixer import *
from background import *
from grid import *
from base import *
from tower import *
from projectile import *
from impact import * 
from ennemy import *
from dead_body import *
from mouse import *
from menu import *
from gold import *
from spawning_mode import *
from utilitaries import *

############################# 
## Main functions
#############################

class Game():
      def __init__(self):
            self.timestep = CLOCK.get_time()
            self.timer = 0.0

            self.has_started = False

            self.mixer = Mixer()

            self.background = Background()

            self.grid = Grid(self)

            self.menu = Menu(self)

            self.gold = Gold()

            self.mouse = Mouse()

            self.spawning_mode = Spawning_mode(self)

            self.base = Base(self)

            self.all_towers = All_towers()

            self.all_projectiles = All_projectiles()

            self.all_impacts = All_impacts()

            self.all_ennemies = All_ennemies()

            self.all_dead_bodies = All_dead_bodies()

      def deal_with_mouse(self):
            self.mouse.doing_stuff(self)

      def spawning_ennemies(self):
            self.spawning_mode.spawning_ennemies(self)

      def fight(self):
            for tower in self.all_towers:
                  tower.check_ennemies(self)
                  tower.attack_and_reload(self)
            for ennemy in self.all_ennemies:
                  ennemy.attack(self)

      def move_objects(self):
            for ennemy in self.all_ennemies:
                  ennemy.move(self)
                  
            for projectile in self.all_projectiles:
                  projectile.move(self)
                  projectile.check_impact(self)

            for impact in self.all_impacts:
                  impact.explode(self)
                  impact.check_impact(self)

      def die(self):
            for ennemy in self.all_ennemies:
                  ennemy.die(self)
            for dead_body in self.all_dead_bodies:
                  dead_body.fall(self)            
            for tower in self.all_towers:
                  tower.die()
            for gate in self.base.all_gates:
                  gate.destroy()

      def render(self):
            self.background.render(0)
            self.menu.render(0)

            for rendering_layer in range(TOTAL_NUMBER_RENDERING_LAYER):
                  for asset_background in self.background.all_assets:
                        asset_background.render(rendering_layer)

                  for tower in self.all_towers:
                        tower.render(rendering_layer)

                  for projectile in self.all_projectiles:
                        projectile.render(rendering_layer)

                  for ennemy in self.all_ennemies:
                        ennemy.render(rendering_layer)

                  for dead_body in self.all_dead_bodies:
                        dead_body.render(rendering_layer)

                  for impact in self.all_impacts:
                        impact.render(rendering_layer)

            self.gold.render(rendering_layer)

            self.mouse.render(rendering_layer)

            pygame.display.update()

      def advance_time(self):
            CLOCK.tick(FPS)
            self.timestep = CLOCK.get_time()
            self.timer += self.timestep
            #print(CLOCK.get_fps())
                  
            


 

