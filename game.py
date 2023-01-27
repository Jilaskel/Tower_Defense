import pygame
from pygame.locals import *
from audio_mixer import *
from background import *
from grid import *
from base import *
from tower import *
from projectile import *
from impact import * 
from ennemy import *
from dead_body import *
from game_mouse import *
from menu import *
from selected_object import * 
from gold import *
from error_message import *
from spawning_mode import *
from utilitaries import *

############################# 
## Main functions
#############################

class Game():
      def __init__(self):

            self.timestep = 0.0
            self.timer = 0.0

            self.is_running = True

            self.all_mixers = All_mixers()

            self.background = Background()

            loading_progress.value += 10

            self.grid = Grid(self)

            self.show_grid = False

            self.menu = Menu(self)

            self.selected_object = Selected_object()

            loading_progress.value += 10

            self.gold = Gold()

            self.mouse = Game_mouse()

            loading_progress.value += 10

            self.spawning_mode = Spawning_mode(self)

            self.base = Base(self)

            loading_progress.value += 10

            self.all_towers = All_towers()

            self.all_projectiles = All_projectiles()

            loading_progress.value += 10

            self.all_impacts = All_impacts()

            loading_progress.value += 10

            self.all_ennemies = All_ennemies()

            loading_progress.value += 10

            self.all_dead_bodies = All_dead_bodies()

            loading_progress.value += 10

            self.all_gold_anim = All_gold_anim()

            loading_progress.value += 10

            self.all_error_messages = All_error_message_anim()

            self.object_to_render = []

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

            for gold_gain in self.all_gold_anim.list:
                  gold_gain.move(self)

            for error_message in self.all_error_messages.list:
                  error_message.move(self)

            self.check_game_over()

      def check_game_over(self):
            for ennemy in self.all_ennemies:
                  if (ennemy.posX>WINDOW_WIDTH):
                        global_status.status = "Game Over"
                        break

      def die(self):
            for ennemy in self.all_ennemies:
                  ennemy.die(self)
            for dead_body in self.all_dead_bodies:
                  dead_body.fall(self)            
            for tower in self.all_towers:
                  tower.die()
            for gate in self.base.all_gates:
                  gate.destroy()

      def render(self,update=True):
            self.object_to_render.append(self.background)
            self.object_to_render.append(self.menu)

            for button in self.menu.all_buttons:
                  self.object_to_render.append(button)

            for button in self.menu.all_options_buttons:
                  self.object_to_render.append(button)

            for asset_background in self.background.all_assets:
                  self.object_to_render.append(asset_background)

            for gate in self.base.all_gates:
                  self.object_to_render.append(gate)

            for tower in self.all_towers:
                  self.object_to_render.append(tower)

            for projectile in self.all_projectiles:
                  self.object_to_render.append(projectile)

            for ennemy in self.all_ennemies:
                  self.object_to_render.append(ennemy)

            for dead_body in self.all_dead_bodies:
                  self.object_to_render.append(dead_body)

            for impact in self.all_impacts:
                  self.object_to_render.append(impact)

            for gold_gain in self.all_gold_anim.list:
                  self.object_to_render.append(gold_gain)

            for error_message in self.all_error_messages.list:
                  self.object_to_render.append(error_message)

            self.object_to_render.append(self.gold)

            self.object_to_render.append(self.selected_object)

            if (self.show_grid):
                  for box in self.grid.all_boxes:
                        self.object_to_render.append(box)

            if (global_status.status == "In game"):
                  self.object_to_render.append(self.mouse)

            self.object_to_render.sort(key =lambda object : object.rendering_layer)

            for object in self.object_to_render:
                  object.render()

            if update:
                  pygame.display.update()

            self.object_to_render.clear()

      def advance_time(self):
            self.timer += self.timestep
            #print(CLOCK.get_fps())

      def reset(self):

            self.spawning_mode.reset()

            self.gold.reset()

            self.base.reset()

            self.all_towers.empty()

            self.all_projectiles.empty()

            self.all_impacts.empty()

            self.all_ennemies.empty()

            self.all_dead_bodies.empty()

            self.all_gold_anim.list.clear()

            self.all_error_messages.list.clear()

            for box in self.grid.all_boxes:
                  box.occupied = False

            self.timer = 0.0
                  
      def get_event(self):
            CLOCK.tick(FPS)
            self.timestep = CLOCK.get_time()

            self.all_events = pygame.event.get()
            for event in self.all_events:
                  if event.type == QUIT:
                        global_status.status = "Quitting"
                  if event.type == KEYDOWN:
                        if ((event.key == K_ESCAPE) or (event.key == K_p)):
                              if (global_status.status == "In game"):
                                    global_status.status = "In pause"
                              elif (global_status.status == "In pause"):
                                    global_status.status = "In game"
                        if (event.key == K_g):
                              global_status.status = "Game Over"
                        if (event.key == K_n):
                              self.gold.amount *= 2
            


 

