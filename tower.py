import pygame
from utilitaries import *
from projectile import *
from functions import *

ARCANE_TOWER_BUTTON_TAG = 1
ARCANE_TOWER_LVL2_BUTTON_TAG = 2
ARCANE_TOWER_LVL3_BUTTON_TAG = 3
FIRE_TOWER_BUTTON_TAG = 4
FIRE_TOWER_LVL2_BUTTON_TAG = 5
FIRE_TOWER_LVL3_BUTTON_TAG = 6
LIGHTNING_TOWER_BUTTON_TAG = 7
LIGHTNING_TOWER_LVL2_BUTTON_TAG = 8
LIGHTNING_TOWER_LVL3_BUTTON_TAG = 9
ICE_TOWER_BUTTON_TAG = 10
ICE_TOWER_LVL2_BUTTON_TAG = 11
ICE_TOWER_LVL3_BUTTON_TAG = 12
BALLISTA_BUTTON_TAG = 13
CATAPULT_BUTTON_TAG = 14


class All_towers(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self)   

            self.all_siege_engines = All_siege_engines()

            self.arcane_tower_data = Arcane_tower_data()
            self.arcane_tower_lvl2_data = Arcane_tower_lvl2_data()
            self.arcane_tower_lvl3_data = Arcane_tower_lvl3_data()
            self.fire_tower_data = Fire_tower_data()
            self.fire_tower_lvl2_data = Fire_tower_lvl2_data()
            self.fire_tower_lvl3_data = Fire_tower_lvl3_data()
            self.lightning_tower_data = Lightning_tower_data()
            self.lightning_tower_lvl2_data = Lightning_tower_lvl2_data()
            self.lightning_tower_lvl3_data = Lightning_tower_lvl3_data()
            self.ice_tower_data = Ice_tower_data()
            self.ice_tower_lvl2_data = Ice_tower_lvl2_data()
            self.ice_tower_lvl3_data = Ice_tower_lvl3_data()
                        
            self.ballista_data = Ballista_data()
            self.catapult_data = Catapult_data()

      def add_tower(self,game,box,tag):
            if (tag==ARCANE_TOWER_BUTTON_TAG):
                  self.add_arcane_tower(game,box)
            elif (tag==ARCANE_TOWER_LVL2_BUTTON_TAG):
                  self.add_arcane_tower_lvl2(game,box)
            elif (tag==ARCANE_TOWER_LVL3_BUTTON_TAG):
                  self.add_arcane_tower_lvl3(game,box)
            elif (tag==FIRE_TOWER_BUTTON_TAG):
                  self.add_fire_tower(game,box)
            elif (tag==FIRE_TOWER_LVL2_BUTTON_TAG):
                  self.add_fire_tower_lvl2(game,box)
            elif (tag==FIRE_TOWER_LVL3_BUTTON_TAG):
                  self.add_fire_tower_lvl3(game,box)
            elif (tag==LIGHTNING_TOWER_BUTTON_TAG):
                  self.add_lightning_tower(game,box)
            elif (tag==LIGHTNING_TOWER_LVL2_BUTTON_TAG):
                  self.add_lightning_tower_lvl2(game,box)
            elif (tag==LIGHTNING_TOWER_LVL3_BUTTON_TAG):
                  self.add_lightning_tower_lvl3(game,box)
            elif (tag==ICE_TOWER_BUTTON_TAG):
                  self.add_ice_tower(game,box)
            elif (tag==ICE_TOWER_LVL2_BUTTON_TAG):
                  self.add_ice_tower_lvl2(game,box)
            elif (tag==ICE_TOWER_LVL3_BUTTON_TAG):
                  self.add_ice_tower_lvl3(game,box)
            elif (tag==BALLISTA_BUTTON_TAG):
                  self.add_ballista(game,box)
            elif (tag==CATAPULT_BUTTON_TAG):
                  self.add_catapult(game,box)      
          

      def add_arcane_tower(self,game,box):
            self.add(Arcane_tower(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()  

      def add_arcane_tower_lvl2(self,game,box):
            self.add(Arcane_tower_lvl2(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()  

      def add_arcane_tower_lvl3(self,game,box):
            self.add(Arcane_tower_lvl3(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()  

      def add_fire_tower(self,game,box):
            self.add(Fire_tower(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()

      def add_fire_tower_lvl2(self,game,box):
            self.add(Fire_tower_lvl2(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()

      def add_fire_tower_lvl3(self,game,box):
            self.add(Fire_tower_lvl3(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()
      
      def add_lightning_tower(self,game,box):
            self.add(Lightning_tower(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()

      def add_lightning_tower_lvl2(self,game,box):
            self.add(Lightning_tower_lvl2(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()

      def add_lightning_tower_lvl3(self,game,box):
            self.add(Lightning_tower_lvl3(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()

      def add_ice_tower(self,game,box):
            self.add(Ice_tower(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()

      def add_ice_tower_lvl2(self,game,box):
            self.add(Ice_tower_lvl2(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()

      def add_ice_tower_lvl3(self,game,box):
            self.add(Ice_tower_lvl3(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()

      def add_ballista(self,game,box):
            balliste = Ballista(game,self,box)
            self.add(balliste)
            if (box.rendering_layer!=23):       ## not on walls
                  self.all_siege_engines.add(balliste)
            game.all_mixers.mouse_mixer.building_wood_sound.play()

      def add_catapult(self,game,box):
            catapulte = Catapult(game,self,box)
            self.add(catapulte)
            if (box.rendering_layer!=23):       ## not on walls
                  self.all_siege_engines.add(catapulte)
            game.all_mixers.mouse_mixer.building_wood_sound.play()


class All_siege_engines(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self)  

class Arcane_tower_data():
      def __init__(self):
            self.name = "Arcane tower Lvl.1" 

            self.hp_max = ARCANE_TOWER_HP_MAX

            self.gold_cost = -ARCANE_TOWER_PRICE

            self.bolt_tag = ARCANE_TOWER_BOLT_TAG

            self.static_image = pygame.image.load(ARCANE_TOWER_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ARCANE_TOWER_RESIZE_FACTOR)        
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = ARCANE_TOWER_OFFSET
            self.firing_offset = ARCANE_TOWER_FIRING_OFFSET
            self.range = ARCANE_TOWER_RANGE

            self.image_attacking = []
            self.number_frame_attacking = ARCANE_TOWER_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(ARCANE_TOWER_ATTACK_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*ARCANE_TOWER_RESIZE_FACTOR)
            self.anim_total_time_a = ARCANE_TOWER_ANIMATION_ATTACKING_TOTAL_TIME
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            self.number_frame_reloading = ARCANE_TOWER_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(ARCANE_TOWER_ATTACK_IMAGE_PATH+str(self.number_frame_reloading-i+1).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*ARCANE_TOWER_RESIZE_FACTOR)
            self.anim_total_time_r = ARCANE_TOWER_ANIMATION_RELOADING_TOTAL_TIME
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms

class Arcane_tower_lvl2_data():
      def __init__(self):
            self.name = "Arcane tower Lvl.2" 

            self.hp_max = ARCANE_TOWER_LVL2_HP_MAX

            self.gold_cost = -ARCANE_TOWER_LVL2_PRICE

            self.bolt_tag = ARCANE_TOWER_LVL2_BOLT_TAG

            self.static_image = pygame.image.load(ARCANE_TOWER_LVL2_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ARCANE_TOWER_LVL2_RESIZE_FACTOR)        
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = ARCANE_TOWER_LVL2_OFFSET
            self.firing_offset = ARCANE_TOWER_LVL2_FIRING_OFFSET
            self.range = ARCANE_TOWER_LVL2_RANGE

            self.image_attacking = []
            self.number_frame_attacking = ARCANE_TOWER_LVL2_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(ARCANE_TOWER_LVL2_ATTACK_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*ARCANE_TOWER_LVL2_RESIZE_FACTOR)
            self.anim_total_time_a = ARCANE_TOWER_LVL2_ANIMATION_ATTACKING_TOTAL_TIME
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            self.number_frame_reloading = ARCANE_TOWER_LVL2_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(ARCANE_TOWER_LVL2_ATTACK_IMAGE_PATH+str(self.number_frame_reloading-i+1).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*ARCANE_TOWER_LVL2_RESIZE_FACTOR)
            self.anim_total_time_r = ARCANE_TOWER_LVL2_ANIMATION_RELOADING_TOTAL_TIME
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms

class Arcane_tower_lvl3_data():
      def __init__(self):
            self.name = "Arcane tower Lvl.3" 

            self.hp_max = ARCANE_TOWER_LVL3_HP_MAX

            self.gold_cost = -ARCANE_TOWER_LVL3_PRICE

            self.bolt_tag = ARCANE_TOWER_LVL3_BOLT_TAG

            self.static_image = pygame.image.load(ARCANE_TOWER_LVL3_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ARCANE_TOWER_LVL3_RESIZE_FACTOR)        
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = ARCANE_TOWER_LVL3_OFFSET
            self.firing_offset = ARCANE_TOWER_LVL3_FIRING_OFFSET
            self.range = ARCANE_TOWER_LVL3_RANGE

            self.image_attacking = []
            self.number_frame_attacking = ARCANE_TOWER_LVL3_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(ARCANE_TOWER_LVL3_ATTACK_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*ARCANE_TOWER_LVL3_RESIZE_FACTOR)
            self.anim_total_time_a = ARCANE_TOWER_LVL3_ANIMATION_ATTACKING_TOTAL_TIME
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            self.number_frame_reloading = ARCANE_TOWER_LVL3_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(ARCANE_TOWER_LVL3_ATTACK_IMAGE_PATH+str(self.number_frame_reloading-i+1).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*ARCANE_TOWER_LVL3_RESIZE_FACTOR)
            self.anim_total_time_r = ARCANE_TOWER_LVL3_ANIMATION_RELOADING_TOTAL_TIME
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms

class Fire_tower_data():
      def __init__(self):
            self.name = "Fire tower Lvl.1"
            
            self.hp_max = FIRE_TOWER_HP_MAX

            self.gold_cost = -FIRE_TOWER_PRICE

            self.bolt_tag = FIRE_TOWER_BOLT_TAG

            self.static_image = pygame.image.load(FIRE_TOWER_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*FIRE_TOWER_RESIZE_FACTOR)        
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = FIRE_TOWER_OFFSET
            self.firing_offset = FIRE_TOWER_FIRING_OFFSET
            self.range = FIRE_TOWER_RANGE

            self.image_attacking = []
            self.number_frame_attacking = FIRE_TOWER_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(FIRE_TOWER_ATTACK_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*FIRE_TOWER_RESIZE_FACTOR)
            self.anim_total_time_a = FIRE_TOWER_ANIMATION_ATTACKING_TOTAL_TIME
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            self.number_frame_reloading = FIRE_TOWER_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(FIRE_TOWER_ATTACK_IMAGE_PATH+str(self.number_frame_reloading-i+1).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*FIRE_TOWER_RESIZE_FACTOR)
            self.anim_total_time_r = FIRE_TOWER_ANIMATION_RELOADING_TOTAL_TIME
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms

class Fire_tower_lvl2_data():
      def __init__(self):
            self.name = "Fire tower Lvl.2"
            
            self.hp_max = FIRE_TOWER_LVL2_HP_MAX

            self.gold_cost = -FIRE_TOWER_LVL2_PRICE

            self.bolt_tag = FIRE_TOWER_LVL2_BOLT_TAG

            self.static_image = pygame.image.load(FIRE_TOWER_LVL2_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*FIRE_TOWER_LVL2_RESIZE_FACTOR)        
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = FIRE_TOWER_LVL2_OFFSET
            self.firing_offset = FIRE_TOWER_LVL2_FIRING_OFFSET
            self.range = FIRE_TOWER_LVL2_RANGE

            self.image_attacking = []
            self.number_frame_attacking = FIRE_TOWER_LVL2_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(FIRE_TOWER_LVL2_ATTACK_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*FIRE_TOWER_LVL2_RESIZE_FACTOR)
            self.anim_total_time_a = FIRE_TOWER_LVL2_ANIMATION_ATTACKING_TOTAL_TIME
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            self.number_frame_reloading = FIRE_TOWER_LVL2_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(FIRE_TOWER_LVL2_ATTACK_IMAGE_PATH+str(self.number_frame_reloading-i+1).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*FIRE_TOWER_LVL2_RESIZE_FACTOR)
            self.anim_total_time_r = FIRE_TOWER_LVL2_ANIMATION_RELOADING_TOTAL_TIME
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms


class Fire_tower_lvl3_data():
      def __init__(self):
            self.name = "Fire tower Lvl.3"
            
            self.hp_max = FIRE_TOWER_LVL3_HP_MAX

            self.gold_cost = -FIRE_TOWER_LVL3_PRICE

            self.bolt_tag = FIRE_TOWER_LVL3_BOLT_TAG

            self.static_image = pygame.image.load(FIRE_TOWER_LVL3_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*FIRE_TOWER_LVL3_RESIZE_FACTOR)        
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = FIRE_TOWER_LVL3_OFFSET
            self.firing_offset = FIRE_TOWER_LVL3_FIRING_OFFSET
            self.range = FIRE_TOWER_LVL3_RANGE

            self.image_attacking = []
            self.number_frame_attacking = FIRE_TOWER_LVL3_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(FIRE_TOWER_LVL3_ATTACK_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*FIRE_TOWER_LVL3_RESIZE_FACTOR)
            self.anim_total_time_a = FIRE_TOWER_LVL3_ANIMATION_ATTACKING_TOTAL_TIME
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            self.number_frame_reloading = FIRE_TOWER_LVL3_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(FIRE_TOWER_LVL3_ATTACK_IMAGE_PATH+str(self.number_frame_reloading-i+1).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*FIRE_TOWER_LVL3_RESIZE_FACTOR)
            self.anim_total_time_r = FIRE_TOWER_LVL3_ANIMATION_RELOADING_TOTAL_TIME
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms

class Lightning_tower_data():
      def __init__(self):
            self.name = "Lightning tower Lvl.1"

            self.hp_max = LIGHTNING_TOWER_HP_MAX

            self.gold_cost = -LIGHTNING_TOWER_PRICE

            self.bolt_tag = LIGHTNING_TOWER_BOLT_TAG

            self.static_image = pygame.image.load(LIGHTNING_TOWER_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*LIGHTNING_TOWER_RESIZE_FACTOR)        
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = LIGHTNING_TOWER_OFFSET
            self.firing_offset = LIGHTNING_TOWER_FIRING_OFFSET
            self.range = LIGHTNING_TOWER_RANGE

            self.image_attacking = []
            self.number_frame_attacking = LIGHTNING_TOWER_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(LIGHTNING_TOWER_ATTACK_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*LIGHTNING_TOWER_RESIZE_FACTOR)
            self.anim_total_time_a = LIGHTNING_TOWER_ANIMATION_ATTACKING_TOTAL_TIME
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            self.number_frame_reloading = LIGHTNING_TOWER_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(LIGHTNING_TOWER_ATTACK_IMAGE_PATH+str(self.number_frame_reloading-i+1).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*LIGHTNING_TOWER_RESIZE_FACTOR)
            self.anim_total_time_r = LIGHTNING_TOWER_ANIMATION_RELOADING_TOTAL_TIME
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms

class Lightning_tower_lvl2_data():
      def __init__(self):
            self.name = "Lightning tower Lvl.2"

            self.hp_max = LIGHTNING_TOWER_LVL2_HP_MAX

            self.gold_cost = -LIGHTNING_TOWER_LVL2_PRICE

            self.bolt_tag = LIGHTNING_TOWER_LVL2_BOLT_TAG

            self.static_image = pygame.image.load(LIGHTNING_TOWER_LVL2_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*LIGHTNING_TOWER_LVL2_RESIZE_FACTOR)        
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = LIGHTNING_TOWER_LVL2_OFFSET
            self.firing_offset = LIGHTNING_TOWER_LVL2_FIRING_OFFSET
            self.range = LIGHTNING_TOWER_LVL2_RANGE

            self.image_attacking = []
            self.number_frame_attacking = LIGHTNING_TOWER_LVL2_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(LIGHTNING_TOWER_LVL2_ATTACK_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*LIGHTNING_TOWER_LVL2_RESIZE_FACTOR)
            self.anim_total_time_a = LIGHTNING_TOWER_LVL2_ANIMATION_ATTACKING_TOTAL_TIME
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            self.number_frame_reloading = LIGHTNING_TOWER_LVL2_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(LIGHTNING_TOWER_LVL2_ATTACK_IMAGE_PATH+str(self.number_frame_reloading-i+1).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*LIGHTNING_TOWER_LVL2_RESIZE_FACTOR)
            self.anim_total_time_r = LIGHTNING_TOWER_LVL2_ANIMATION_RELOADING_TOTAL_TIME
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms

class Lightning_tower_lvl3_data():
      def __init__(self):
            self.name = "Lightning tower Lvl.3"

            self.hp_max = LIGHTNING_TOWER_LVL3_HP_MAX

            self.gold_cost = -LIGHTNING_TOWER_LVL3_PRICE

            self.bolt_tag = LIGHTNING_TOWER_LVL3_BOLT_TAG

            self.static_image = pygame.image.load(LIGHTNING_TOWER_LVL3_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*LIGHTNING_TOWER_LVL3_RESIZE_FACTOR)        
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = LIGHTNING_TOWER_LVL3_OFFSET
            self.firing_offset = LIGHTNING_TOWER_LVL3_FIRING_OFFSET
            self.range = LIGHTNING_TOWER_LVL3_RANGE

            self.image_attacking = []
            self.number_frame_attacking = LIGHTNING_TOWER_LVL3_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(LIGHTNING_TOWER_LVL3_ATTACK_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*LIGHTNING_TOWER_LVL3_RESIZE_FACTOR)
            self.anim_total_time_a = LIGHTNING_TOWER_LVL3_ANIMATION_ATTACKING_TOTAL_TIME
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            self.number_frame_reloading = LIGHTNING_TOWER_LVL3_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(LIGHTNING_TOWER_LVL3_ATTACK_IMAGE_PATH+str(self.number_frame_reloading-i+1).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*LIGHTNING_TOWER_LVL3_RESIZE_FACTOR)
            self.anim_total_time_r = LIGHTNING_TOWER_LVL3_ANIMATION_RELOADING_TOTAL_TIME
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms

class Ice_tower_data():
      def __init__(self):
            self.name = "Ice tower Lvl.1"

            self.hp_max = ICE_TOWER_HP_MAX

            self.gold_cost = -ICE_TOWER_PRICE

            self.bolt_tag = ICE_TOWER_BOLT_TAG

            self.static_image = pygame.image.load(ICE_TOWER_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ICE_TOWER_RESIZE_FACTOR)        
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = ICE_TOWER_OFFSET
            self.firing_offset = ICE_TOWER_FIRING_OFFSET
            self.range = ICE_TOWER_RANGE

            self.image_attacking = []
            self.number_frame_attacking = ICE_TOWER_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(ICE_TOWER_ATTACK_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*ICE_TOWER_RESIZE_FACTOR)
            self.anim_total_time_a = ICE_TOWER_ANIMATION_ATTACKING_TOTAL_TIME
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            self.number_frame_reloading = ICE_TOWER_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(ICE_TOWER_ATTACK_IMAGE_PATH+str(self.number_frame_reloading-i+1).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*ICE_TOWER_RESIZE_FACTOR)
            self.anim_total_time_r = ICE_TOWER_ANIMATION_RELOADING_TOTAL_TIME
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms

class Ice_tower_lvl2_data():
      def __init__(self):
            self.name = "Ice tower Lvl.2"

            self.hp_max = ICE_TOWER_LVL2_HP_MAX

            self.gold_cost = -ICE_TOWER_LVL2_PRICE

            self.bolt_tag = ICE_TOWER_LVL2_BOLT_TAG

            self.static_image = pygame.image.load(ICE_TOWER_LVL2_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ICE_TOWER_LVL2_RESIZE_FACTOR)        
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = ICE_TOWER_LVL2_OFFSET
            self.firing_offset = ICE_TOWER_LVL2_FIRING_OFFSET
            self.range = ICE_TOWER_LVL2_RANGE

            self.image_attacking = []
            self.number_frame_attacking = ICE_TOWER_LVL2_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(ICE_TOWER_LVL2_ATTACK_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*ICE_TOWER_LVL2_RESIZE_FACTOR)
            self.anim_total_time_a = ICE_TOWER_LVL2_ANIMATION_ATTACKING_TOTAL_TIME
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            self.number_frame_reloading = ICE_TOWER_LVL2_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(ICE_TOWER_LVL2_ATTACK_IMAGE_PATH+str(self.number_frame_reloading-i+1).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*ICE_TOWER_LVL2_RESIZE_FACTOR)
            self.anim_total_time_r = ICE_TOWER_LVL2_ANIMATION_RELOADING_TOTAL_TIME
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms

class Ice_tower_lvl3_data():
      def __init__(self):
            self.name = "Ice tower Lvl.2"

            self.hp_max = ICE_TOWER_LVL3_HP_MAX

            self.gold_cost = -ICE_TOWER_LVL3_PRICE

            self.bolt_tag = ICE_TOWER_LVL3_BOLT_TAG

            self.static_image = pygame.image.load(ICE_TOWER_LVL3_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ICE_TOWER_LVL3_RESIZE_FACTOR)        
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = ICE_TOWER_LVL3_OFFSET
            self.firing_offset = ICE_TOWER_LVL3_FIRING_OFFSET
            self.range = ICE_TOWER_LVL3_RANGE

            self.image_attacking = []
            self.number_frame_attacking = ICE_TOWER_LVL3_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(ICE_TOWER_LVL3_ATTACK_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*ICE_TOWER_LVL3_RESIZE_FACTOR)
            self.anim_total_time_a = ICE_TOWER_LVL3_ANIMATION_ATTACKING_TOTAL_TIME
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            self.number_frame_reloading = ICE_TOWER_LVL3_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(ICE_TOWER_LVL3_ATTACK_IMAGE_PATH+str(self.number_frame_reloading-i+1).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*ICE_TOWER_LVL3_RESIZE_FACTOR)
            self.anim_total_time_r = ICE_TOWER_LVL3_ANIMATION_RELOADING_TOTAL_TIME
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms

class Ballista_data():
      def __init__(self):
            self.name = "Ballista"

            self.hp_max = BALLISTA_HP_MAX

            self.gold_cost = -BALLISTA_PRICE

            self.bolt_tag = BALLISTA_BOLT_TAG

            self.static_image = pygame.image.load(BALLISTA_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*BALLISTA_RESIZE_FACTOR)  
            self.image_size = vec(self.static_image.get_size())

            self.firing_offset = BALLISTA_FIRING_OFFSET

            self.image_attacking = []
            self.number_frame_attacking = BALLISTA_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(BALLISTA_ATTACK_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*BALLISTA_RESIZE_FACTOR)
            self.anim_total_time_a = BALLISTA_ANIMATION_ATTACKING_TOTAL_TIME
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            offset_degeu = 5
            self.number_frame_reloading = BALLISTA_NUMBER_FRAME_RELOADING
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(BALLISTA_RELOAD_IMAGE_PATH+str(i+offset_degeu).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*BALLISTA_RESIZE_FACTOR)
            self.anim_total_time_r = BALLISTA_ANIMATION_RELOADING_TOTAL_TIME
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms

class Catapult_data():
      def __init__(self):
            self.name = "Catapult"

            self.hp_max = CATAPULT_HP_MAX

            self.gold_cost = -CATAPULT_PRICE

            self.bolt_tag = CATAPULT_BOLT_TAG

            self.static_image = pygame.image.load(CATAPULT_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*CATAPULT_RESIZE_FACTOR)  
            self.image_size = vec(self.static_image.get_size())

            self.firing_offset = CATAPULT_FIRING_OFFSET

            self.image_attacking = []
            self.number_frame_attacking = CATAPULT_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(CATAPULT_ATTACK_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*CATAPULT_RESIZE_FACTOR)
            self.anim_total_time_a = CATAPULT_ANIMATION_ATTACKING_TOTAL_TIME
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            offset_degeu = 5
            self.number_frame_reloading = CATAPULT_NUMBER_FRAME_RELOADING
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(CATAPULT_RELOAD_IMAGE_PATH+str(i+offset_degeu).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*CATAPULT_RESIZE_FACTOR)
            self.anim_total_time_r = CATAPULT_ANIMATION_RELOADING_TOTAL_TIME
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms

class Tower(pygame.sprite.Sprite):
      def __init__(self,game,box):
            
            x = box.posX
            y = box.posY
            self.box = box

            self.hp = self.my_data.hp_max
      
            self.current_image = self.my_data.static_image  
            self.posX = x + self.my_data.image_offset[0]
            self.posY = y + self.my_data.image_offset[1]
            self.image_size = self.my_data.image_size
            self.center = vec(self.posX+self.image_size[0]*0.5,self.posY+self.image_size[1]*0.5)

            if (box.rendering_layer==23):       ## on walls
                  self.rendering_layer = 23
            else:
                  self.rendering_layer = compute_rendering_layer_number(self)

            self.my_timer = 0

            self.attacking = True
            self.reloading = False

            self.anim_frame_r = 0
            self.anim_frame_a = 0

            self.detected_ennemies = False
            self.my_target = []
            
            self.hitbox_left = x
            self.hitbox_top = y
            self.hitbox_width = BACKGROUND_SQUARE_SIDE
            self.hitbox_height = BACKGROUND_SQUARE_SIDE
            self.rect = pygame.Rect(self.hitbox_left,self.hitbox_top,self.hitbox_width,self.hitbox_height)

            self.range = self.my_data.range * (self.rect.width+self.rect.height)/2.0
            self.range_hitbox = Range_Hitbox(self,self.rect.w,self.rect.h,self.range,circular=True)

            game.gold.gold_gain(game,self,self.my_data.gold_cost)

      def check_ennemies(self,game):
            if self.range_hitbox.circular:
                  self.detected_ennemies = pygame.sprite.spritecollide(self.range_hitbox, game.all_ennemies, False, pygame.sprite.collide_circle)
            else:
                  self.detected_ennemies = pygame.sprite.spritecollide(self.range_hitbox, game.all_ennemies, False)

            if (self.detected_ennemies):
                  self.attacking = True
                  if not(self.my_target in self.detected_ennemies):
                        self.my_target = self.detected_ennemies[0]
            else:
                  self.attacking = False

      def attack_and_reload(self,game):
            if (self.attacking):
                  self.my_timer += game.timestep
                  if self.reloading:
                        if self.my_timer>self.my_data.time_per_frame_r:
                              self.anim_frame_r += 1
                              self.my_timer = 0.0
                              if (self.anim_frame_r==self.my_data.number_frame_reloading):
                                    self.anim_frame_r = 0
                                    self.reloading = False
                                    self.current_image= self.my_data.image_attacking[self.anim_frame_a]
                              else:
                                    self.current_image= self.my_data.image_reloading[self.anim_frame_r]
                  else:
                        if self.my_timer>self.my_data.time_per_frame_a:
                              self.anim_frame_a += 1
                              self.my_timer = 0.0
                              if (self.anim_frame_a==self.my_data.number_frame_attacking):
                                    game.all_projectiles.add_bolt(game,self.posX+self.my_data.firing_offset[0],self.posY+self.my_data.firing_offset[1],self.my_target,self.my_data.bolt_tag)
                                    self.anim_frame_a = 0
                                    self.reloading = True
                                    self.current_image= self.my_data.image_reloading[self.anim_frame_r]
                              else:
                                    self.current_image= self.my_data.image_attacking[self.anim_frame_a]
            else:
                  if self.reloading:
                        self.my_timer += game.timestep
                        if self.my_timer>self.my_data.time_per_frame_r:
                              self.anim_frame_r += 1
                              self.my_timer = 0.0
                              if (self.anim_frame_r==self.my_data.number_frame_reloading):
                                    self.reloading = False   
                                    self.anim_frame_r = 0
                                    self.current_image= self.my_data.image_attacking[self.anim_frame_a]
                              else:
                                    self.current_image= self.my_data.image_reloading[self.anim_frame_r]
                  else:
                        self.anim_frame_a = 0
                        self.current_image= self.my_data.image_attacking[self.anim_frame_a]

      # def attack_and_reload(self,game):
      #       if (self.attacking):
      #             self.attack_finished = False
      #             self.my_timer += game.timestep
      #             if self.my_timer>self.my_data.firing_period:
      #                   self.my_timer = 0.0
      #                   game.all_projectiles.add_bolt(self.posX+ARCANE_TOWER_FIRING_OFFSET[0],self.posY+ARCANE_TOWER_FIRING_OFFSET[1],self.my_target)
      #       else:
      #             if not(self.attack_finished):
      #                   self.my_timer += game.timestep
      #                   if self.my_timer>self.my_data.firing_period:
      #                         self.my_timer = 2*self.my_data.firing_period
      #                         self.attack_finished = True 

      def die(self):
            if (self.hp<=0):
                  self.box.occupied = False
                  pygame.sprite.Sprite.kill(self)

      def destroy(self,game):
            self.box.occupied = False
            game.gold.gold_gain(game,self,-int(self.my_data.gold_cost*GOLD_TOWER_REFUND_COEFF))
            pygame.sprite.Sprite.kill(self)                 

      def render(self):
            window.blit(self.current_image, (self.posX, self.posY))  


class Arcane_tower(Tower,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.arcane_tower_data

            Tower.__init__(self,game,box)

class Arcane_tower_lvl2(Tower,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.arcane_tower_lvl2_data

            Tower.__init__(self,game,box)

class Arcane_tower_lvl3(Tower,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.arcane_tower_lvl3_data

            Tower.__init__(self,game,box)

class Fire_tower(Tower,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.fire_tower_data

            Tower.__init__(self,game,box)

class Fire_tower_lvl2(Tower,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.fire_tower_lvl2_data

            Tower.__init__(self,game,box)

      def check_ennemies(self,game):
            if self.range_hitbox.circular:
                  self.detected_ennemies = pygame.sprite.spritecollide(self.range_hitbox, game.all_ennemies, False, pygame.sprite.collide_circle)
            else:
                  self.detected_ennemies = pygame.sprite.spritecollide(self.range_hitbox, game.all_ennemies, False)

            if (self.detected_ennemies):
                  self.attacking = True
                  if not(self.my_target in self.detected_ennemies):
                        self.my_target = self.detected_ennemies[0]
                  if (len(self.detected_ennemies)>1):
                        self.second_target = self.detected_ennemies[1]
                  else:
                        self.second_target = None
            else:
                  self.attacking = False
                  self.second_target = None

      def attack_and_reload(self,game):
            if (self.attacking):
                  self.my_timer += game.timestep
                  if self.reloading:
                        if self.my_timer>self.my_data.time_per_frame_r:
                              self.anim_frame_r += 1
                              self.my_timer = 0.0
                              if (self.anim_frame_r==self.my_data.number_frame_reloading):
                                    self.anim_frame_r = 0
                                    self.reloading = False
                                    self.current_image= self.my_data.image_attacking[self.anim_frame_a]
                              else:
                                    self.current_image= self.my_data.image_reloading[self.anim_frame_r]
                  else:
                        if self.my_timer>self.my_data.time_per_frame_a:
                              self.anim_frame_a += 1
                              self.my_timer = 0.0
                              if (self.anim_frame_a==self.my_data.number_frame_attacking):
                                    game.all_projectiles.add_bolt(game,self.posX+self.my_data.firing_offset[0],self.posY+self.my_data.firing_offset[1],self.my_target,self.my_data.bolt_tag)
                                    if self.second_target:
                                          game.all_projectiles.add_bolt(game,self.posX+self.my_data.firing_offset[0],self.posY+self.my_data.firing_offset[1],self.second_target,self.my_data.bolt_tag)
                                    self.anim_frame_a = 0
                                    self.reloading = True
                                    self.current_image= self.my_data.image_reloading[self.anim_frame_r]
                              else:
                                    self.current_image= self.my_data.image_attacking[self.anim_frame_a]
            else:
                  if self.reloading:
                        self.my_timer += game.timestep
                        if self.my_timer>self.my_data.time_per_frame_r:
                              self.anim_frame_r += 1
                              self.my_timer = 0.0
                              if (self.anim_frame_r==self.my_data.number_frame_reloading):
                                    self.reloading = False   
                                    self.anim_frame_r = 0
                                    self.current_image= self.my_data.image_attacking[self.anim_frame_a]
                              else:
                                    self.current_image= self.my_data.image_reloading[self.anim_frame_r]
                  else:
                        self.anim_frame_a = 0
                        self.current_image= self.my_data.image_attacking[self.anim_frame_a]


class Fire_tower_lvl3(Fire_tower_lvl2,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.fire_tower_lvl3_data

            Tower.__init__(self,game,box)

class Lightning_tower(Tower,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.lightning_tower_data

            Tower.__init__(self,game,box)

class Lightning_tower_lvl2(Tower,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.lightning_tower_lvl2_data

            Tower.__init__(self,game,box)

class Lightning_tower_lvl3(Tower,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.lightning_tower_lvl3_data

            Tower.__init__(self,game,box)

class Ice_tower(Tower,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.ice_tower_data

            self.firing = False

            Tower.__init__(self,game,box)

      def attack_and_reload(self,game):
            if not(self.firing):
                  if (self.attacking):
                        self.my_timer += game.timestep
                        if self.reloading:
                              if self.my_timer>self.my_data.time_per_frame_r:
                                    self.anim_frame_r += 1
                                    self.my_timer = 0.0
                                    if (self.anim_frame_r==self.my_data.number_frame_reloading):
                                          self.anim_frame_r = 0
                                          self.reloading = False
                                          self.current_image= self.my_data.image_attacking[self.anim_frame_a]
                                    else:
                                          self.current_image= self.my_data.image_reloading[self.anim_frame_r]
                        else:
                              if self.my_timer>self.my_data.time_per_frame_a:
                                    self.anim_frame_a += 1
                                    self.my_timer = 0.0
                                    if (self.anim_frame_a==self.my_data.number_frame_attacking):
                                          game.all_projectiles.add_bolt(game,self.posX+self.my_data.firing_offset[0],self.posY+self.my_data.firing_offset[1],self.my_target,self.my_data.bolt_tag,self)
                                          self.anim_frame_a = 0
                                          self.reloading = True
                                          self.current_image= self.my_data.image_reloading[self.anim_frame_r]
                                    else:
                                          self.current_image= self.my_data.image_attacking[self.anim_frame_a]
                  else:
                        if self.reloading:
                              self.my_timer += game.timestep
                              if self.my_timer>self.my_data.time_per_frame_r:
                                    self.anim_frame_r += 1
                                    self.my_timer = 0.0
                                    if (self.anim_frame_r==self.my_data.number_frame_reloading):
                                          self.reloading = False   
                                          self.anim_frame_r = 0
                                          self.current_image= self.my_data.image_attacking[self.anim_frame_a]
                                    else:
                                          self.current_image= self.my_data.image_reloading[self.anim_frame_r]
                        else:
                              self.anim_frame_a = 0
                              self.current_image= self.my_data.image_attacking[self.anim_frame_a]

class Ice_tower_lvl2(Ice_tower,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.ice_tower_lvl2_data

            self.firing = False

            Tower.__init__(self,game,box)

class Ice_tower_lvl3(Ice_tower,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.ice_tower_lvl3_data

            self.firing = False

            Tower.__init__(self,game,box)

class Ballista(Tower,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            x = box.posX
            y = box.posY
            self.box = box

            self.my_data = all_t.ballista_data

            self.hp = self.my_data.hp_max

            self.current_image = self.my_data.static_image    
            self.posX = x + BALLISTA_OFFSET[0]
            self.posY = y + BALLISTA_OFFSET[1]
            self.image_size = self.my_data.image_size
            self.center = vec(self.posX+self.image_size[0]*0.5,self.posY+self.image_size[1]*0.5)

            if (box.rendering_layer==23):       ## on walls
                  self.rendering_layer = 23
            else:
                  self.rendering_layer = compute_rendering_layer_number(self)

            self.my_timer = 0

            self.attacking = True
            self.reloading = False

            self.anim_frame_a = 0
            self.anim_frame_r = 0

            self.detected_ennemies = False
            self.my_target = []

            self.hitbox_left = x
            self.hitbox_top = y
            self.hitbox_width = BACKGROUND_SQUARE_SIDE
            self.hitbox_height = BACKGROUND_SQUARE_SIDE
            self.rect = pygame.Rect(self.hitbox_left,self.hitbox_top,self.hitbox_width,self.hitbox_height)

            self.range = BALLISTA_RANGE*(self.rect.width+self.rect.height)/2.0
            self.range_hitbox = Range_Hitbox(self,self.rect.w,self.rect.h,self.range,circular=False,tag="Ballista")

            game.gold.gold_gain(game,self,self.my_data.gold_cost)

class Catapult(Tower,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            x = box.posX
            y = box.posY
            self.box = box

            self.my_data = all_t.catapult_data

            self.hp = self.my_data.hp_max

            self.current_image = self.my_data.static_image    
            self.posX = x + CATAPULT_OFFSET[0]
            self.posY = y + CATAPULT_OFFSET[1]
            self.image_size = self.my_data.image_size
            self.center = vec(self.posX+self.image_size[0]*0.5,self.posY+self.image_size[1]*0.5)

            if (box.rendering_layer==23):       ## on walls
                  self.rendering_layer = 23
            else:
                  self.rendering_layer = compute_rendering_layer_number(self)

            self.my_timer = 0

            self.attacking = True
            self.reloading = False

            self.anim_frame_a = 0
            self.anim_frame_r = 0

            self.detected_ennemies = False
            self.my_target = []

            self.hitbox_left = x
            self.hitbox_top = y
            self.hitbox_width = BACKGROUND_SQUARE_SIDE
            self.hitbox_height = BACKGROUND_SQUARE_SIDE
            self.rect = pygame.Rect(self.hitbox_left,self.hitbox_top,self.hitbox_width,self.hitbox_height)

            self.range = CATAPULT_RANGE*(self.rect.width+self.rect.height)/2.0
            self.range_hitbox = Range_Hitbox(self,self.rect.w,self.rect.h,self.range,circular=False,tag="Catapult")

            game.gold.gold_gain(game,self,self.my_data.gold_cost)

            
class Range_Hitbox(pygame.sprite.Sprite):
      def __init__(self,tower,width,height,range,circular,tag="Ballista"):
            super().__init__()
            self.range = range
            if circular:
                  self.circular = True
                  self.rect = pygame.Rect(tower.posX-ARCANE_TOWER_OFFSET[0],tower.posY-ARCANE_TOWER_OFFSET[1],tower.rect.width,tower.rect.height)
                  self.radius = self.range
                  self.posX = tower.posX-ARCANE_TOWER_OFFSET[0]+width*0.5 - self.radius
                  self.posY = tower.posY-ARCANE_TOWER_OFFSET[1]+height*0.5 - self.radius    

                  self.image = pygame.image.load(TOWER_CIRCLE_RANGE_IMAGE_PATH).convert_alpha()
                  self.image.set_alpha(TOWER_CIRCLE_RANGE_IMAGE_ALPHA)
                  self.image = pygame.transform.scale(self.image,(self.range*2,self.range*2))                                
            else:
                  if tag=="Ballista":
                        self.circular = False
                        self.rect = pygame.Rect(tower.posX,tower.posY,width,height)   
                        self.rect.x = tower.posX - self.range
                        self.posX = self.rect.x
                        self.rect.w = self.range              
                        self.posY = tower.posY    

                        self.image = pygame.image.load(TOWER_RECT_RANGE_IMAGE_PATH).convert_alpha()
                        self.image.set_alpha(TOWER_RECT_RANGE_IMAGE_ALPHA) 
                        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.h))      
                  elif tag=="Catapult":
                        self.circular = False
                        self.rect = pygame.Rect(tower.posX,tower.posY,width,height)   
                        self.rect.x = tower.posX - self.range
                        self.posX = self.rect.x
                        self.rect.w = self.range - 2*BACKGROUND_SQUARE_SIDE              
                        self.posY = tower.posY    

                        self.image = pygame.image.load(TOWER_RECT_RANGE_IMAGE_PATH).convert_alpha()
                        self.image.set_alpha(TOWER_RECT_RANGE_IMAGE_ALPHA) 
                        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.h))                          


            self.offset = vec(self.posX-tower.posX,self.posY-tower.posY)

