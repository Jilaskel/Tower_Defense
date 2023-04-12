import pygame
from utilitaries import *
from impact import * 
from functions import *
from numpy import sqrt
import numpy as np
import math
import random

ARCANE_TOWER_LVL1_BOLT_TAG = 1
ARCANE_TOWER_LVL2_BOLT_TAG = 2
ARCANE_TOWER_LVL3_BOLT_TAG = 3
FIRE_TOWER_LVL1_BOLT_TAG = 4
FIRE_TOWER_LVL2_BOLT_TAG = 5
FIRE_TOWER_LVL3_BOLT_TAG = 6
LIGHTNING_TOWER_LVL1_BOLT_TAG = 7
LIGHTNING_TOWER_LVL2_BOLT_TAG = 8
LIGHTNING_TOWER_LVL3_BOLT_TAG = 9
ICE_TOWER_LVL1_BOLT_TAG = 10
ICE_TOWER_LVL2_BOLT_TAG = 11
ICE_TOWER_LVL3_BOLT_TAG = 12
BALLISTA_BOLT_TAG = 13
CATAPULT_BOLT_TAG = 14

class All_projectiles(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self)  

            self.arcane_bolt_data = Arcane_bolt_lvl1_data()
            self.arcane_bolt_lvl2_data = Arcane_bolt_lvl2_data()
            self.arcane_bolt_lvl3_data = Arcane_bolt_lvl3_data()
            self.fire_bolt_data = Fire_bolt_lvl1_data()
            self.fire_bolt_lvl2_data = Fire_bolt_lvl2_data()
            self.fire_bolt_lvl3_data = Fire_bolt_lvl3_data()
            self.light_bolt_data = Light_bolt_lvl1_data()
            self.light_bolt_lvl2_data = Light_bolt_lvl2_data()
            self.light_bolt_lvl3_data = Light_bolt_lvl3_data()
            self.ice_bolt_data = Ice_bolt_lvl1_data()
            self.ice_bolt_lvl2_data = Ice_bolt_lvl2_data()
            self.ice_bolt_lvl3_data = Ice_bolt_lvl3_data()
            
            self.bolt_data = Bolt_data()
            self.rock_data = Rock_data()

      def add_bolt(self,game,x,y,target,tag,tower=None):
            if (tag==ARCANE_TOWER_LVL1_BOLT_TAG):
                  self.add_arcane_bolt_lvl1(game,x,y,target)
            if (tag==ARCANE_TOWER_LVL2_BOLT_TAG):
                  self.add_arcane_bolt_lvl2(game,x,y,target)
            if (tag==ARCANE_TOWER_LVL3_BOLT_TAG):
                  self.add_arcane_bolt_lvl3(game,x,y,target)
            elif (tag==FIRE_TOWER_LVL1_BOLT_TAG):
                  self.add_fire_bolt_lvl1(game,x,y,target)
            elif (tag==FIRE_TOWER_LVL2_BOLT_TAG):
                  self.add_fire_bolt_lvl2(game,x,y,target)
            elif (tag==FIRE_TOWER_LVL3_BOLT_TAG):
                  self.add_fire_bolt_lvl3(game,x,y,target)
            elif (tag==LIGHTNING_TOWER_LVL1_BOLT_TAG):
                  self.add_lightning_bolt_lvl1(game,x,y,target)
            elif (tag==LIGHTNING_TOWER_LVL2_BOLT_TAG):
                  self.add_lightning_bolt_lvl2(game,x,y,target)
            elif (tag==LIGHTNING_TOWER_LVL3_BOLT_TAG):
                  self.add_lightning_bolt_lvl3(game,x,y,target)
            elif (tag==ICE_TOWER_LVL1_BOLT_TAG):
                  self.add_ice_bolt_lvl1(game,x,y,target,tower)
            elif (tag==ICE_TOWER_LVL2_BOLT_TAG):
                  self.add_ice_bolt_lvl2(game,x,y,target,tower)
            elif (tag==ICE_TOWER_LVL3_BOLT_TAG):
                  self.add_ice_bolt_lvl3(game,x,y,target,tower)
            elif (tag==BALLISTA_BOLT_TAG):
                  self.add_ballista_bolt(game,x,y,target)
            elif (tag==CATAPULT_BOLT_TAG):
                  self.add_catapult_rock(game,x,y,target)

      def add_arcane_bolt_lvl1(self,game,x,y,target):
            self.add(Arcane_bolt_lvl1(self,x,y,target))
            game.all_mixers.projectile_mixer.arcane_proj_sound.play(maxtime=SOUND_ARCANE_PROJ_MAX_TIME)

      def add_arcane_bolt_lvl2(self,game,x,y,target):
            self.add(Arcane_bolt_lvl2(self,x,y,target))
            game.all_mixers.projectile_mixer.arcane_proj_sound.play(maxtime=SOUND_ARCANE_PROJ_MAX_TIME)

      def add_arcane_bolt_lvl3(self,game,x,y,target):
            self.add(Arcane_bolt_lvl3(self,x,y,target))
            game.all_mixers.projectile_mixer.arcane_proj_sound.play(maxtime=SOUND_ARCANE_PROJ_MAX_TIME)

      def add_fire_bolt_lvl1(self,game,x,y,target):
            self.add(Fire_bolt_lvl1(self,x,y,target))
            game.all_mixers.projectile_mixer.fire_proj_sound.play(maxtime=SOUND_FIRE_PROJ_MAX_TIME)

      def add_fire_bolt_lvl2(self,game,x,y,target):
            self.add(Fire_bolt_lvl2(self,x,y,target))
            game.all_mixers.projectile_mixer.fire_proj_sound.play(maxtime=SOUND_FIRE_PROJ_MAX_TIME)

      def add_fire_bolt_lvl3(self,game,x,y,target):
            self.add(Fire_bolt_lvl3(self,x,y,target))
            game.all_mixers.projectile_mixer.fire_proj_sound.play(maxtime=SOUND_FIRE_PROJ_MAX_TIME)

      def add_fire_bolt_no_target(self,game,x,y,impact_target,direction):
            self.add(Fire_bolt_no_target(self,x,y,impact_target,direction))
            # game.all_mixers.projectile_mixer.fire_proj_sound.play(maxtime=SOUND_FIRE_PROJ_MAX_TIME)

      def add_lightning_bolt_lvl1(self,game,x,y,target):
            damage = LIGHTNING_BOLT_LVL1_DICT["DAMAGE"]
            self.add(Light_bolt_lvl1(self,x,y,target,damage))
            old_x = target.center[0]
            old_y = target.center[1]
            old_target = []
            old_target.append(target)
            distance_lim = LIGHTNING_BOLT_LVL1_DICT["RANGE"]*BACKGROUND_SQUARE_SIDE
            for number_of_bounce in range(LIGHTNING_BOLT_LVL1_DICT["NUMBER_BOUNCE_MAX"]):
                  distance_lim = distance_lim*(1-LIGHTNING_BOLT_LVL1_DICT["DECREASING_DISTANCE_BOUNCE_FACTOR"])
                  damage = damage*(1-LIGHTNING_BOLT_LVL1_DICT["DECREASING_DAMAGE_BOUNCE_FACTOR"])
                  for new_target in game.all_ennemies:
                        if not(new_target in old_target):
                              new_x = new_target.center[0]
                              new_y = new_target.center[1]
                              distance = np.sqrt((old_x - new_x)**2 + (old_y - new_y)**2)
                              if (distance<(distance_lim)and(distance>0.1*BACKGROUND_SQUARE_SIDE)):
                                    self.add(Light_bolt(self,old_x,old_y,new_target,damage)) 
                                    old_x = new_x  
                                    old_y = new_y
                                    old_target.append(new_target)  
                                    break

            random.choice(game.all_mixers.projectile_mixer.light_proj_list).play()

      def add_lightning_bolt_lvl2(self,game,x,y,target):
            damage = LIGHTNING_BOLT_LVL2_DICT["DAMAGE"]
            self.add(Light_bolt_lvl2(self,x,y,target,damage))
            old_x = target.center[0]
            old_y = target.center[1]
            old_target = []
            old_target.append(target)
            distance_lim = LIGHTNING_BOLT_LVL2_DICT["RANGE"]*BACKGROUND_SQUARE_SIDE
            for number_of_bounce in range(LIGHTNING_BOLT_LVL2_DICT["NUMBER_BOUNCE_MAX"]):
                  distance_lim = distance_lim*(1-LIGHTNING_BOLT_LVL2_DICT["DECREASING_DISTANCE_BOUNCE_FACTOR"])
                  damage = damage*(1-LIGHTNING_BOLT_LVL2_DICT["DECREASING_DAMAGE_BOUNCE_FACTOR"])
                  for new_target in game.all_ennemies:
                        if not(new_target in old_target):
                              new_x = new_target.center[0]
                              new_y = new_target.center[1]
                              distance = np.sqrt((old_x - new_x)**2 + (old_y - new_y)**2)
                              if (distance<(distance_lim)and(distance>0.1*BACKGROUND_SQUARE_SIDE)):
                                    self.add(Light_bolt(self,old_x,old_y,new_target,damage)) 
                                    old_x = new_x  
                                    old_y = new_y
                                    old_target.append(new_target)  
                                    break

            random.choice(game.all_mixers.projectile_mixer.light_proj_list).play()

      def add_lightning_bolt_lvl3(self,game,x,y,target):
            damage = LIGHTNING_BOLT_LVL3_DICT["DAMAGE"]
            self.add(Light_bolt_lvl3(self,x,y,target,damage))
            old_x = target.center[0]
            old_y = target.center[1]
            old_target = []
            old_target.append(target)
            distance_lim = LIGHTNING_BOLT_LVL3_DICT["RANGE"]*BACKGROUND_SQUARE_SIDE
            for number_of_bounce in range(LIGHTNING_BOLT_LVL3_DICT["NUMBER_BOUNCE_MAX"]):
                  distance_lim = distance_lim*(1-LIGHTNING_BOLT_LVL3_DICT["DECREASING_DISTANCE_BOUNCE_FACTOR"])
                  damage = damage*(1-LIGHTNING_BOLT_LVL3_DICT["DECREASING_DAMAGE_BOUNCE_FACTOR"])
                  for new_target in game.all_ennemies:
                        if not(new_target in old_target):
                              new_x = new_target.center[0]
                              new_y = new_target.center[1]
                              distance = np.sqrt((old_x - new_x)**2 + (old_y - new_y)**2)
                              if (distance<(distance_lim)and(distance>0.1*BACKGROUND_SQUARE_SIDE)):
                                    self.add(Light_bolt(self,old_x,old_y,new_target,damage)) 
                                    old_x = new_x  
                                    old_y = new_y
                                    old_target.append(new_target)  
                                    break

            random.choice(game.all_mixers.projectile_mixer.light_proj_list).play()

      def add_ice_bolt_lvl1(self,game,x,y,target,tower):
            self.add(Ice_bolt_lvl1(self,x,y,target,tower))
            random.choice(game.all_mixers.projectile_mixer.ice_bolt_proj_list).play()

      def add_ice_bolt_lvl2(self,game,x,y,target,tower):
            self.add(Ice_bolt_lvl2(self,x,y,target,tower))
            random.choice(game.all_mixers.projectile_mixer.ice_bolt_proj_list).play()

      def add_ice_bolt_lvl3(self,game,x,y,target,tower):
            self.add(Ice_bolt_lvl3(self,x,y,target,tower))
            random.choice(game.all_mixers.projectile_mixer.ice_bolt_proj_list).play()

      def add_ballista_bolt(self,game,x,y,target):
            self.add(Bolt(self,x,y,target))
            random.choice(game.all_mixers.projectile_mixer.bolt_proj_list).play()

      def add_catapult_rock(self,game,x,y,target):
            self.add(Rock(self,x,y,target))

class Arcane_bolt_data():
      def __init__(self):

            self.damage = self.my_dict["DAMAGE"]
            self.velocity = self.my_dict["VELOCITY"]  # pixel by ms
            self.ratio_for_impact = self.my_dict["RATIO_FOR_IMPACT"]

            self.static_image = pygame.image.load(self.my_dict["IMAGE_PATH"]).convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*self.my_dict["RESIZE_FACTOR"])  
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(-1,0)
            self.offset = vec(self.my_dict["CENTOR_VECTOR"][0]*self.image_size[0],self.my_dict["CENTOR_VECTOR"][1]*self.image_size[1])

            self.centor_vector = self.my_dict["CENTOR_VECTOR"]

class Arcane_bolt_lvl1_data(Arcane_bolt_data):
      def __init__(self):
            self.my_dict = ARCANE_BOLT_LVL1_DICT

            Arcane_bolt_data.__init__(self)

            # self.damage = ARCANE_BOLT_DAMAGE
            # self.velocity = ARCANE_BOLT_VELOCITY  # pixel by ms
            # self.ratio_for_impact = ARCANE_BOLT_RATIO_FOR_IMPACT

            # self.static_image = pygame.image.load(ARCANE_BOLT_IMAGE_PATH).convert_alpha()
            # self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ARCANE_BOLT_RESIZE_FACTOR)  
            # self.image_size = vec(self.static_image.get_size())
            # self.initial_direction = vec(-1,0)
            # self.offset = vec(ARCANE_BOLT_CENTOR_VECTOR[0]*self.image_size[0],ARCANE_BOLT_CENTOR_VECTOR[1]*self.image_size[1])

            # self.centor_vector = ARCANE_BOLT_CENTOR_VECTOR

            self.impact_tag = ARCANE_TOWER_IMPACT_TAG

class Arcane_bolt_lvl2_data(Arcane_bolt_data):
      def __init__(self):
            self.my_dict = ARCANE_BOLT_LVL2_DICT

            Arcane_bolt_data.__init__(self)

            # self.damage = ARCANE_BOLT_LVL2_DAMAGE
            # self.velocity = ARCANE_BOLT_LVL2_VELOCITY  # pixel by ms
            # self.ratio_for_impact = ARCANE_BOLT_LVL2_RATIO_FOR_IMPACT

            # self.static_image = pygame.image.load(ARCANE_BOLT_LVL2_IMAGE_PATH).convert_alpha()
            # self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ARCANE_BOLT_LVL2_RESIZE_FACTOR)  
            # self.image_size = vec(self.static_image.get_size())
            # self.initial_direction = vec(-1,0)
            # self.offset = vec(ARCANE_BOLT_LVL2_CENTOR_VECTOR[0]*self.image_size[0],ARCANE_BOLT_LVL2_CENTOR_VECTOR[1]*self.image_size[1])

            # self.centor_vector = ARCANE_BOLT_LVL2_CENTOR_VECTOR

            self.impact_tag = ARCANE_TOWER_IMPACT_TAG

class Arcane_bolt_lvl3_data(Arcane_bolt_data):
      def __init__(self):
            self.my_dict = ARCANE_BOLT_LVL3_DICT

            Arcane_bolt_data.__init__(self)

            # self.damage = ARCANE_BOLT_LVL3_DAMAGE
            # self.velocity = ARCANE_BOLT_LVL3_VELOCITY  # pixel by ms
            # self.ratio_for_impact = ARCANE_BOLT_LVL3_RATIO_FOR_IMPACT

            # self.static_image = pygame.image.load(ARCANE_BOLT_LVL3_IMAGE_PATH).convert_alpha()
            # self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ARCANE_BOLT_LVL3_RESIZE_FACTOR)  
            # self.image_size = vec(self.static_image.get_size())
            # self.initial_direction = vec(-1,0)
            # self.offset = vec(ARCANE_BOLT_LVL3_CENTOR_VECTOR[0]*self.image_size[0],ARCANE_BOLT_LVL3_CENTOR_VECTOR[1]*self.image_size[1])

            # self.centor_vector = ARCANE_BOLT_LVL3_CENTOR_VECTOR

            self.impact_tag = ARCANE_TOWER_IMPACT_TAG

class Fire_bolt_data():
      def __init__(self):

            self.damage = self.my_dict["DAMAGE"]
            self.velocity = self.my_dict["VELOCITY"]  # pixel by ms
            self.ratio_for_impact = self.my_dict["RATIO_FOR_IMPACT"]

            self.static_image = pygame.image.load(self.my_dict["IMAGE_PATH"]+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*self.my_dict["RESIZE_FACTOR"])  
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(-1,0)
            self.offset = vec(self.my_dict["CENTOR_VECTOR"][0]*self.image_size[0],self.my_dict["CENTOR_VECTOR"][1]*self.image_size[1])

            self.number_frame = self.my_dict["NUMBER_FRAME"]
            self.images = []
            for i in range(1,self.number_frame+1):
                  self.images.append(pygame.image.load(self.my_dict["IMAGE_PATH"]+str(i).zfill(4)+".png").convert_alpha())  
                  self.images[i-1] = pygame.transform.scale(self.images[i-1],vec(self.images[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
            self.anim_total_time = self.my_dict["TOTAL_TIME"]  # in ms
            self.time_per_frame = self.anim_total_time/self.number_frame # in ms

            self.centor_vector = self.my_dict["CENTOR_VECTOR"]

class Fire_bolt_lvl1_data(Fire_bolt_data):
      def __init__(self):
            self.my_dict = FIRE_BOLT_LVL1_DICT

            Fire_bolt_data.__init__(self)

            # self.damage = FIRE_BOLT_DAMAGE
            # self.velocity = FIRE_BOLT_VELOCITY  # pixel by ms
            # self.ratio_for_impact = FIRE_BOLT_RATIO_FOR_IMPACT

            # self.static_image = pygame.image.load(FIRE_BOLT_IMAGE_PATH+"0001.png").convert_alpha()
            # self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*FIRE_BOLT_RESIZE_FACTOR)  
            # self.image_size = vec(self.static_image.get_size())
            # self.initial_direction = vec(-1,0)
            # self.offset = vec(FIRE_BOLT_CENTOR_VECTOR[0]*self.image_size[0],FIRE_BOLT_CENTOR_VECTOR[1]*self.image_size[1])

            # self.number_frame = FIRE_BOLT_NUMBER_FRAME
            # self.images = []
            # for i in range(1,self.number_frame+1):
            #       self.images.append(pygame.image.load(FIRE_BOLT_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())  
            #       self.images[i-1] = pygame.transform.scale(self.images[i-1],vec(self.images[i-1].get_size())*FIRE_BOLT_RESIZE_FACTOR)
            # self.anim_total_time = FIRE_BOLT_TOTAL_TIME  # in ms
            # self.time_per_frame = self.anim_total_time/self.number_frame # in ms

            # self.centor_vector = FIRE_BOLT_CENTOR_VECTOR

            self.impact_tag = FIRE_TOWER_IMPACT_TAG

class Fire_bolt_lvl2_data(Fire_bolt_data):
      def __init__(self):
            self.my_dict = FIRE_BOLT_LVL2_DICT

            Fire_bolt_data.__init__(self)

            # self.damage = FIRE_BOLT_LVL2_DAMAGE
            # self.velocity = FIRE_BOLT_LVL2_VELOCITY  # pixel by ms
            # self.ratio_for_impact = FIRE_BOLT_LVL2_RATIO_FOR_IMPACT

            # self.static_image = pygame.image.load(FIRE_BOLT_LVL2_IMAGE_PATH+"0001.png").convert_alpha()
            # self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*FIRE_BOLT_LVL2_RESIZE_FACTOR)  
            # self.image_size = vec(self.static_image.get_size())
            # self.initial_direction = vec(-1,0)
            # self.offset = vec(FIRE_BOLT_LVL2_CENTOR_VECTOR[0]*self.image_size[0],FIRE_BOLT_LVL2_CENTOR_VECTOR[1]*self.image_size[1])

            # self.number_frame = FIRE_BOLT_LVL2_NUMBER_FRAME
            # self.images = []
            # for i in range(1,self.number_frame+1):
            #       self.images.append(pygame.image.load(FIRE_BOLT_LVL2_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())  
            #       self.images[i-1] = pygame.transform.scale(self.images[i-1],vec(self.images[i-1].get_size())*FIRE_BOLT_LVL2_RESIZE_FACTOR)
            # self.anim_total_time = FIRE_BOLT_LVL2_TOTAL_TIME  # in ms
            # self.time_per_frame = self.anim_total_time/self.number_frame # in ms

            # self.centor_vector = FIRE_BOLT_LVL2_CENTOR_VECTOR

            self.impact_tag = FIRE_TOWER_IMPACT_TAG

class Fire_bolt_lvl3_data(Fire_bolt_data):
      def __init__(self):
            self.my_dict = FIRE_BOLT_LVL3_DICT

            Fire_bolt_data.__init__(self)

            # self.damage = FIRE_BOLT_LVL3_DAMAGE
            # self.velocity = FIRE_BOLT_LVL3_VELOCITY  # pixel by ms
            # self.ratio_for_impact = FIRE_BOLT_LVL3_RATIO_FOR_IMPACT

            # self.static_image = pygame.image.load(FIRE_BOLT_LVL3_IMAGE_PATH+"0001.png").convert_alpha()
            # self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*FIRE_BOLT_LVL3_RESIZE_FACTOR)  
            # self.image_size = vec(self.static_image.get_size())
            # self.initial_direction = vec(-1,0)
            # self.offset = vec(FIRE_BOLT_LVL3_CENTOR_VECTOR[0]*self.image_size[0],FIRE_BOLT_LVL3_CENTOR_VECTOR[1]*self.image_size[1])

            # self.number_frame = FIRE_BOLT_LVL3_NUMBER_FRAME
            # self.images = []
            # for i in range(1,self.number_frame+1):
            #       self.images.append(pygame.image.load(FIRE_BOLT_LVL3_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())  
            #       self.images[i-1] = pygame.transform.scale(self.images[i-1],vec(self.images[i-1].get_size())*FIRE_BOLT_LVL3_RESIZE_FACTOR)
            # self.anim_total_time = FIRE_BOLT_LVL3_TOTAL_TIME  # in ms
            # self.time_per_frame = self.anim_total_time/self.number_frame # in ms

            # self.centor_vector = FIRE_BOLT_LVL3_CENTOR_VECTOR

            self.impact_tag = FIRE_TOWER_IMPACT_TAG

            self.margin_spawn = vec(0.0,10.0)

class Light_bolt_data():
      def __init__(self):

            self.damage = self.my_dict["DAMAGE"]
            self.velocity = self.my_dict["VELOCITY"]  # pixel by ms
            self.ratio_for_impact = self.my_dict["RATIO_FOR_IMPACT"]

            self.static_image = pygame.image.load(self.my_dict["IMAGE_PATH"]+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*self.my_dict["RESIZE_FACTOR"])  
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(-1,0)
            self.offset = vec(self.my_dict["CENTOR_VECTOR"][0]*self.image_size[0],self.my_dict["CENTOR_VECTOR"][1]*self.image_size[1])

            self.number_frame = self.my_dict["NUMBER_FRAME"]
            self.images = []
            for i in range(1,self.number_frame+1):
                  self.images.append(pygame.image.load(self.my_dict["IMAGE_PATH"]+str(i).zfill(4)+".png").convert_alpha())  
                  self.images[i-1] = pygame.transform.scale(self.images[i-1],vec(self.images[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
            self.anim_total_time = self.my_dict["TOTAL_TIME"]  # in ms
            self.time_per_frame = self.anim_total_time/self.number_frame # in ms

            self.centor_vector = self.my_dict["CENTOR_VECTOR"]

class Light_bolt_lvl1_data():
      def __init__(self):

            self.damage = LIGHTNING_BOLT_DAMAGE

            self.static_image = pygame.image.load(LIGHTNING_BOLT_IMAGE_PATH+"light_2.png").convert_alpha()
            self.resize_factor = LIGHTNING_BOLT_RESIZE_FACTOR
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*LIGHTNING_BOLT_RESIZE_FACTOR)  
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(0,1)
            self.offset = vec(LIGHTNING_BOLT_CENTOR_VECTOR[0]*self.image_size[0],LIGHTNING_BOLT_CENTOR_VECTOR[1]*self.image_size[1])

            self.number_frame = LIGHTNING_BOLT_NUMBER_FRAME
            self.images = []
            for i in range(2,self.number_frame+2):
                  self.images.append(pygame.image.load(LIGHTNING_BOLT_IMAGE_PATH+"light_"+str(i)+".png").convert_alpha())  
            self.images_fading = []
            for i in range(4,self.number_frame+4):
                  self.images_fading.append(pygame.image.load(LIGHTNING_BOLT_IMAGE_PATH+"light_"+str(i)+".png").convert_alpha())  
            self.anim_total_time = LIGHTNING_BOLT_TOTAL_TIME  # in ms
            self.time_per_frame = LIGHTNING_BOLT_TIME_PER_FRAME # in ms

            self.centor_vector = LIGHTNING_BOLT_CENTOR_VECTOR

            self.short_images = []
            self.short_images.append(pygame.image.load(LIGHTNING_BOLT_IMAGE_PATH+"light_1.png").convert_alpha())
            self.short_images.append(pygame.transform.flip(self.short_images[0], True, False))

            self.stun_time = LIGHTNING_BOLT_STUN_TIME

class Light_bolt_lvl2_data():
      def __init__(self):

            self.damage = LIGHTNING_BOLT_LVL2_DAMAGE

            self.static_image = pygame.image.load(LIGHTNING_BOLT_LVL2_IMAGE_PATH+"light_2.png").convert_alpha()
            self.resize_factor = LIGHTNING_BOLT_LVL2_RESIZE_FACTOR
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*LIGHTNING_BOLT_LVL2_RESIZE_FACTOR)  
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(0,1)
            self.offset = vec(LIGHTNING_BOLT_LVL2_CENTOR_VECTOR[0]*self.image_size[0],LIGHTNING_BOLT_LVL2_CENTOR_VECTOR[1]*self.image_size[1])

            self.number_frame = LIGHTNING_BOLT_LVL2_NUMBER_FRAME
            self.images = []
            for i in range(2,self.number_frame+2):
                  self.images.append(pygame.image.load(LIGHTNING_BOLT_LVL2_IMAGE_PATH+"light_"+str(i)+".png").convert_alpha())  
            self.images_fading = []
            for i in range(4,self.number_frame+4):
                  self.images_fading.append(pygame.image.load(LIGHTNING_BOLT_LVL2_IMAGE_PATH+"light_"+str(i)+".png").convert_alpha())  
            self.anim_total_time = LIGHTNING_BOLT_LVL2_TOTAL_TIME  # in ms
            self.time_per_frame = LIGHTNING_BOLT_LVL2_TIME_PER_FRAME # in ms

            self.centor_vector = LIGHTNING_BOLT_LVL2_CENTOR_VECTOR

            self.short_images = []
            self.short_images.append(pygame.image.load(LIGHTNING_BOLT_LVL2_IMAGE_PATH+"light_1.png").convert_alpha())
            self.short_images.append(pygame.transform.flip(self.short_images[0], True, False))

            self.stun_time = LIGHTNING_BOLT_LVL2_STUN_TIME

class Light_bolt_lvl3_data():
      def __init__(self):

            self.damage = LIGHTNING_BOLT_LVL3_DAMAGE

            self.static_image = pygame.image.load(LIGHTNING_BOLT_LVL3_IMAGE_PATH+"light_2.png").convert_alpha()
            self.resize_factor = LIGHTNING_BOLT_LVL3_RESIZE_FACTOR
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*LIGHTNING_BOLT_LVL3_RESIZE_FACTOR)  
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(0,1)
            self.offset = vec(LIGHTNING_BOLT_LVL3_CENTOR_VECTOR[0]*self.image_size[0],LIGHTNING_BOLT_LVL3_CENTOR_VECTOR[1]*self.image_size[1])

            self.number_frame = LIGHTNING_BOLT_LVL3_NUMBER_FRAME
            self.images = []
            for i in range(2,self.number_frame+2):
                  self.images.append(pygame.image.load(LIGHTNING_BOLT_LVL3_IMAGE_PATH+"light_"+str(i)+".png").convert_alpha())  
            self.images_fading = []
            for i in range(4,self.number_frame+4):
                  self.images_fading.append(pygame.image.load(LIGHTNING_BOLT_LVL3_IMAGE_PATH+"light_"+str(i)+".png").convert_alpha())  
            self.anim_total_time = LIGHTNING_BOLT_LVL3_TOTAL_TIME  # in ms
            self.time_per_frame = LIGHTNING_BOLT_LVL3_TIME_PER_FRAME # in ms

            self.centor_vector = LIGHTNING_BOLT_LVL3_CENTOR_VECTOR

            self.short_images = []
            self.short_images.append(pygame.image.load(LIGHTNING_BOLT_LVL3_IMAGE_PATH+"light_1.png").convert_alpha())
            self.short_images.append(pygame.transform.flip(self.short_images[0], True, False))

            self.stun_time = LIGHTNING_BOLT_LVL3_STUN_TIME

class Ice_bolt_data():
      def __init__(self):

            self.damage = ICE_BOLT_DAMAGE
            self.slowing_coeff = ICE_BOLT_SLOWING_COEFF

            self.static_image = pygame.image.load(ICE_BOLT_IMAGE_PATH+"frost_ray_00.png").convert_alpha()
            self.resize_factor = ICE_BOLT_RESIZE_FACTOR
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ICE_BOLT_RESIZE_FACTOR)  
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(0,1)
            self.offset = vec(ICE_BOLT_CENTOR_VECTOR[0]*self.image_size[0],ICE_BOLT_CENTOR_VECTOR[1]*self.image_size[1])

            self.number_frame = ICE_BOLT_NUMBER_FRAME
            self.images = []
            for i in range(0,self.number_frame):
                  self.images.append(pygame.image.load(ICE_BOLT_IMAGE_PATH+"frost_ray_"+str(i).zfill(2)+".png").convert_alpha())  
            self.time_per_frame = ICE_BOLT_TIME_PER_FRAME # in ms

            self.centor_vector = ICE_BOLT_CENTOR_VECTOR

            self.images_fading = []
            self.number_frame_fading = ICE_BOLT_NUMBER_FRAME_FADING
            fading_number = 34
            for i in range(fading_number,fading_number+self.number_frame_fading):
                  self.images_fading.append(pygame.image.load(ICE_BOLT_IMAGE_PATH+"frost_ray_"+str(i).zfill(2)+".png").convert_alpha())  
            self.anim_total_time_fading = ICE_BOLT_TOTAL_TIME_FADING  # in ms
            self.time_per_frame_fading = self.anim_total_time_fading/self.number_frame_fading # in ms

            self.range = ICE_BOLT_RANGE
            self.freezing = ICE_BOLT_FREEZING

class Ice_bolt_lvl2_data():
      def __init__(self):

            self.damage = ICE_BOLT_LVL2_DAMAGE
            self.slowing_coeff = ICE_BOLT_LVL2_SLOWING_COEFF

            self.static_image = pygame.image.load(ICE_BOLT_LVL2_IMAGE_PATH+"frost_ray_00.png").convert_alpha()
            self.resize_factor = ICE_BOLT_LVL2_RESIZE_FACTOR
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ICE_BOLT_LVL2_RESIZE_FACTOR)  
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(0,1)
            self.offset = vec(ICE_BOLT_LVL2_CENTOR_VECTOR[0]*self.image_size[0],ICE_BOLT_LVL2_CENTOR_VECTOR[1]*self.image_size[1])

            self.number_frame = ICE_BOLT_LVL2_NUMBER_FRAME
            self.images = []
            for i in range(0,self.number_frame):
                  self.images.append(pygame.image.load(ICE_BOLT_LVL2_IMAGE_PATH+"frost_ray_"+str(i).zfill(2)+".png").convert_alpha())  
            self.time_per_frame = ICE_BOLT_LVL2_TIME_PER_FRAME # in ms

            self.centor_vector = ICE_BOLT_LVL2_CENTOR_VECTOR

            self.images_fading = []
            self.number_frame_fading = ICE_BOLT_LVL2_NUMBER_FRAME_FADING
            fading_number = 34
            for i in range(fading_number,fading_number+self.number_frame_fading):
                  self.images_fading.append(pygame.image.load(ICE_BOLT_LVL2_IMAGE_PATH+"frost_ray_"+str(i).zfill(2)+".png").convert_alpha())  
            self.anim_total_time_fading = ICE_BOLT_LVL2_TOTAL_TIME_FADING  # in ms
            self.time_per_frame_fading = self.anim_total_time_fading/self.number_frame_fading # in ms

            self.range = ICE_BOLT_LVL2_RANGE
            self.freezing = ICE_BOLT_LVL2_FREEZING

class Ice_bolt_lvl3_data():
      def __init__(self):

            self.damage = ICE_BOLT_LVL3_DAMAGE
            self.slowing_coeff = ICE_BOLT_LVL3_SLOWING_COEFF

            self.static_image = pygame.image.load(ICE_BOLT_LVL3_IMAGE_PATH+"frost_ray_00.png").convert_alpha()
            self.resize_factor = ICE_BOLT_LVL2_RESIZE_FACTOR
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ICE_BOLT_LVL3_RESIZE_FACTOR)  
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(0,1)
            self.offset = vec(ICE_BOLT_LVL3_CENTOR_VECTOR[0]*self.image_size[0],ICE_BOLT_LVL3_CENTOR_VECTOR[1]*self.image_size[1])

            self.number_frame = ICE_BOLT_LVL3_NUMBER_FRAME
            self.images = []
            for i in range(0,self.number_frame):
                  self.images.append(pygame.image.load(ICE_BOLT_LVL3_IMAGE_PATH+"frost_ray_"+str(i).zfill(2)+".png").convert_alpha())  
            self.time_per_frame = ICE_BOLT_LVL3_TIME_PER_FRAME # in ms

            self.centor_vector = ICE_BOLT_LVL3_CENTOR_VECTOR

            self.images_fading = []
            self.number_frame_fading = ICE_BOLT_LVL3_NUMBER_FRAME_FADING
            fading_number = 34
            for i in range(fading_number,fading_number+self.number_frame_fading):
                  self.images_fading.append(pygame.image.load(ICE_BOLT_LVL3_IMAGE_PATH+"frost_ray_"+str(i).zfill(2)+".png").convert_alpha())  
            self.anim_total_time_fading = ICE_BOLT_LVL3_TOTAL_TIME_FADING  # in ms
            self.time_per_frame_fading = self.anim_total_time_fading/self.number_frame_fading # in ms

            self.range = ICE_BOLT_LVL3_RANGE
            self.freezing = ICE_BOLT_LVL3_FREEZING

class Bolt_data():
      def __init__(self):      

            self.damage = BOLT_DAMAGE
            self.velocity = BOLT_VELOCITY  # pixel by ms
            self.ratio_for_impact = BOLT_RATIO_FOR_IMPACT

            self.static_image = pygame.image.load(BOLT_IMAGE_PATH).convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*BOLT_RESIZE_FACTOR)        
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(-1,0)
            self.offset = vec(BOLT_CENTOR_VECTOR[0]*self.image_size[0],BOLT_CENTOR_VECTOR[1]*self.image_size[1])
            self.centor_vector = BOLT_CENTOR_VECTOR

class Rock_data():
      def __init__(self):      

            self.damage = ROCK_DAMAGE
            self.velocity = ROCK_VELOCITY  # pixel by ms

            self.static_image = pygame.image.load(ROCK_IMAGE_PATH).convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ROCK_RESIZE_FACTOR)        
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(-1,0)
            self.offset = vec(ROCK_CENTOR_VECTOR[0]*self.image_size[0],ROCK_CENTOR_VECTOR[1]*self.image_size[1])
            self.centor_vector = ROCK_CENTOR_VECTOR

            self.impact_tag = ROCK_IMPACT_TAG

class Projectile(pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target): 
            pygame.sprite.Sprite.__init__(self)

            self.damage = self.my_data.damage
      
            self.current_image = self.my_data.static_image
            self.image_size = self.my_data.image_size

            self.posX = x-self.my_data.offset[0]    
            self.posY = y-self.my_data.offset[1]    
            self.rendering_layer = compute_rendering_layer_number(self)

            self.direction = vec(0,0)

            self.target = target

            self.rect = self.current_image.get_rect()
            self.rect.x = self.posX
            self.rect.y = self.posY

            self.center = vec(self.posX+self.my_data.centor_vector[0]*self.image_size[0],self.posY+self.my_data.centor_vector[1]*self.image_size[1])

      def move(self,game):
            if (pygame.sprite.Sprite.alive(self.target)):
                  self.my_target_center = self.target.rect.center
                  self.direction = (self.target.rect.center[0] - self.center[0], self.target.rect.center[1] - self.center[1])   
                  self.direction /= sqrt(self.direction[0]**2+self.direction[1]**2)     
            self.posX += self.my_data.velocity * game.timestep * self.direction[0]
            self.posY += self.my_data.velocity * game.timestep * self.direction[1]
            self.rect.x = self.posX
            self.rect.y = self.posY
            self.center += self.my_data.velocity * game.timestep * self.direction
            self.rotate(self.my_data.static_image)

            # self.rendering_layer = compute_rendering_layer_number(self)
            self.rendering_layer = TOTAL_NUMBER_RENDERING_LAYER-3

      def rotate(self,image):
            scalar_product = self.my_data.initial_direction[0]*self.direction[0]+self.my_data.initial_direction[1]*self.direction[1]
            if (self.direction[1]<self.my_data.initial_direction[1]):
                  if (scalar_product > 0) : 
                        angle = -np.arccos(scalar_product)
                  else:
                        angle = 2*math.pi-np.arccos(scalar_product)
            else:
                  if (scalar_product > 0) : 
                        angle = np.arccos(scalar_product)
                  else:
                        angle = -(2*math.pi-np.arccos(scalar_product))
            angle = math.degrees(angle)
            self.current_image = pygame.transform.rotate(image, angle)

      def check_impact(self,game):
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False,pygame.sprite.collide_rect_ratio(self.my_data.ratio_for_impact))
            if self.hit_ennemies:
                  pygame.sprite.Sprite.kill(self)
                  game.all_impacts.add_impact(game,self,self.my_data.impact_tag)
            else:
                  ## if ennemy is dead while projectile was travelling, distance is computed with last ennemy position 
                  distance = np.sqrt((self.my_target_center[0] - self.center[0])**2 + (self.my_target_center[1] - self.center[1])**2)
                  if (distance<0.1*BACKGROUND_SQUARE_SIDE):
                        pygame.sprite.Sprite.kill(self)
                        game.all_impacts.add_impact(game,self,self.my_data.impact_tag)  

      def render(self):
            window.blit(self.current_image, (self.posX, self.posY))  

class Arcane_bolt(Projectile,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.arcane_bolt_data

            Projectile.__init__(self,all_p,x,y,target)

class Arcane_bolt_lvl2(Projectile,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.arcane_bolt_lvl2_data

            Projectile.__init__(self,all_p,x,y,target)

class Arcane_bolt_lvl3(Projectile,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.arcane_bolt_lvl3_data

            Projectile.__init__(self,all_p,x,y,target)

class Fire_bolt(Projectile,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.fire_bolt_data

            Projectile.__init__(self,all_p,x,y,target)

            self.all_p = all_p

            self.current_frame = 0

            self.my_timer = 0
                    
      def move(self,game):
            if (pygame.sprite.Sprite.alive(self.target)):
                  self.my_target_center = self.target.rect.center
                  self.direction = (self.target.rect.center[0] - self.center[0], self.target.rect.center[1] - self.center[1])   
                  self.direction /= sqrt(self.direction[0]**2+self.direction[1]**2)     
            self.posX += self.my_data.velocity * game.timestep * self.direction[0]
            self.posY += self.my_data.velocity * game.timestep * self.direction[1]
            self.rect.x = self.posX
            self.rect.y = self.posY
            self.center += self.my_data.velocity * game.timestep * self.direction

            # self.rendering_layer = compute_rendering_layer_number(self)
            self.rendering_layer = TOTAL_NUMBER_RENDERING_LAYER-3

            self.my_timer += game.timestep
            if self.my_timer>self.my_data.time_per_frame:
                  self.current_frame += 1
                  self.current_frame = self.current_frame%self.my_data.number_frame
                  self.my_timer = 0.0
                              
            self.rotate(self.my_data.images[self.current_frame])  

class Fire_bolt_lvl2(Projectile,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.fire_bolt_lvl2_data

            Projectile.__init__(self,all_p,x,y,target)

            self.all_p = all_p

            self.current_frame = 0

            self.my_timer = 0
                    

class Fire_bolt_lvl3(Fire_bolt,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.fire_bolt_lvl3_data

            Projectile.__init__(self,all_p,x,y,target)

            self.all_p = all_p   

            self.current_frame = 0

            self.my_timer = 0


      def check_impact(self,game):
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False,pygame.sprite.collide_rect_ratio(self.my_data.ratio_for_impact))
            if self.hit_ennemies:
                  pygame.sprite.Sprite.kill(self)
                  game.all_impacts.add_impact(game,self,self.my_data.impact_tag)
                  self.all_p.add_fire_bolt_no_target(game,self.posX+self.my_data.margin_spawn[0],self.posY+self.my_data.margin_spawn[1],self.target,vec(1,0))
                  self.all_p.add_fire_bolt_no_target(game,self.posX-self.my_data.margin_spawn[0],self.posY+self.my_data.margin_spawn[1],self.target,vec(-1,0))
            else:
                  ## if ennemy is dead while projectile was travelling, distance is computed with last ennemy position 
                  distance = np.sqrt((self.my_target_center[0] - self.center[0])**2 + (self.my_target_center[1] - self.center[1])**2)
                  if (distance<0.1*BACKGROUND_SQUARE_SIDE):
                        pygame.sprite.Sprite.kill(self)
                        game.all_impacts.add_impact(game,self,self.my_data.impact_tag) 
                        self.all_p.add_fire_bolt_no_target(game,self.posX+self.my_data.margin_spawn[0],self.posY+self.my_data.margin_spawn[1],self.target,vec(1,0))
                        self.all_p.add_fire_bolt_no_target(game,self.posX-self.my_data.margin_spawn[0],self.posY+self.my_data.margin_spawn[1],self.target,vec(-1,0))

class Fire_bolt_no_target(Projectile,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,impact_target,direction):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.fire_bolt_data

            self.all_p = all_p

            self.impact_target = impact_target

            self.damage = self.my_data.damage
      
            self.current_image = self.my_data.static_image
            self.image_size = self.my_data.image_size

            self.current_frame = 0

            self.my_timer = 0

            self.posX = x-self.my_data.offset[0]    
            self.posY = y-self.my_data.offset[1]    
            self.rendering_layer = compute_rendering_layer_number(self)

            self.direction = direction

            self.rect = self.current_image.get_rect()
            self.rect.x = self.posX
            self.rect.y = self.posY

            self.center = vec(self.posX+FIRE_BOLT_CENTOR_VECTOR[0]*self.image_size[0],self.posY+FIRE_BOLT_CENTOR_VECTOR[1]*self.image_size[1])

      def move(self,game):  
            self.posX += self.my_data.velocity * game.timestep * self.direction[0]
            self.posY += self.my_data.velocity * game.timestep * self.direction[1]
            self.rect.x = self.posX
            self.rect.y = self.posY
            self.center += self.my_data.velocity * game.timestep * self.direction

            # self.rendering_layer = compute_rendering_layer_number(self)
            self.rendering_layer = TOTAL_NUMBER_RENDERING_LAYER-3

            self.my_timer += game.timestep
            if self.my_timer>self.my_data.time_per_frame:
                  self.current_frame += 1
                  self.current_frame = self.current_frame%self.my_data.number_frame
                  self.my_timer = 0.0
                              
            self.rotate(self.my_data.images[self.current_frame])  

      def check_impact(self,game):
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False,pygame.sprite.collide_rect_ratio(self.my_data.ratio_for_impact))
            if (self.hit_ennemies and (self.hit_ennemies[0]!=self.impact_target)):
                  self.target = self.hit_ennemies[0]
                  game.all_impacts.add_impact(game,self,self.my_data.impact_tag)
                  pygame.sprite.Sprite.kill(self)
            else:
                  x_bush = game.background.bush_width
                  x_walls = game.base.x_walls
                  side = game.background.square_side
                  if ((self.posX>(x_walls-side*0.5)) or (self.posX<(x_bush*0.2))):
                      self.target = pygame.sprite.Sprite()
                      self.target.rect = pygame.Rect(self.posX,self.posY,0.5*side,0.5*side)
                      game.all_impacts.add_impact(game,self,self.my_data.impact_tag)
                      pygame.sprite.Sprite.kill(self)

class Light_bolt(Projectile,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target,damage):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.light_bolt_data

            self.init(x,y,target,damage)

      def init(self,x,y,target,damage):

            self.damage = damage

            self.target = target

            self.target.velocity = 0

            self.posX = x    
            self.posY = y   
            self.pos = vec(x,y)

            self.current_image = self.my_data.static_image

            self.image_size = self.my_data.image_size
            self.my_target_center = self.target.rect.center
            distance = np.sqrt((self.my_target_center[0] - x)**2 + (self.my_target_center[1] - y)**2)
            resize_ratio = distance/self.image_size[1]
            self.current_image = pygame.transform.scale(self.current_image,self.image_size*resize_ratio)  

            self.image_size = vec(self.current_image.get_size())
            self.origin_pos = vec(self.my_data.centor_vector[0]*self.image_size[0],self.posY+self.my_data.centor_vector[1]*self.image_size[1])
      
            self.current_frame = 0

            self.my_timer = 0
            self.my_total_timer = 0

            self.rendering_layer = compute_rendering_layer_number(self)

            self.direction = vec(0,0)

            self.damage_dealt = False

      def move(self,game):  
            distance = np.sqrt((self.my_target_center[0] - self.posX)**2 + (self.my_target_center[1] - self.posY)**2)
            if (self.my_total_timer < self.my_data.anim_total_time):
                  if (pygame.sprite.Sprite.alive(self.target)):
                        self.my_target_center = self.target.rect.center
                        self.direction = (self.target.rect.center[0] - self.posX, self.target.rect.center[1] - self.posY)   
                        self.direction /= sqrt(self.direction[0]**2+self.direction[1]**2) 

                  
                  self.my_timer += game.timestep
                  if self.my_timer>self.my_data.time_per_frame:
                        # self.current_frame += 1
                        # self.current_frame = self.current_frame%self.my_data.number_frame
                        self.current_frame = random.randint(0,1)
                        self.my_timer = 0.0   
                  if distance>2.0*BACKGROUND_SQUARE_SIDE:
                        self.current_image = self.my_data.images[self.current_frame].convert_alpha()
                  else:
                        self.current_image = self.my_data.short_images[self.current_frame].convert_alpha()
            else:
                  self.my_timer += game.timestep
                  if self.my_timer>(self.my_data.anim_total_time*0.5):
                        self.current_frame += 1
                        self.current_frame = min(1,self.current_frame)
                        self.my_timer = 0.0 
                  self.current_image = self.my_data.images_fading[self.current_frame].convert_alpha()


            image_size = vec(self.current_image.get_size())
            resize_ratio = distance/image_size[1]
            # self.current_image = pygame.transform.scale(self.current_image,image_size*resize_ratio)  ## to preserve dimensions ratio
            self.current_image = pygame.transform.scale(self.current_image,(image_size[0]*self.my_data.resize_factor,image_size[1]*resize_ratio))  

            self.image_size = vec(self.current_image.get_size())
            self.origin_pos = vec(self.my_data.centor_vector[0]*self.image_size[0],self.my_data.centor_vector[1]*self.image_size[1])

            self.rotate(self.current_image)

      def rotate(self,image):
            scalar_product = self.my_data.initial_direction[0]*self.direction[0]+self.my_data.initial_direction[1]*self.direction[1]
            if (self.direction[1]<self.my_data.initial_direction[1]):
                  if (scalar_product > 0) : 
                        angle = -np.arccos(scalar_product)
                  else:
                        angle = 2*math.pi-np.arccos(scalar_product)
            else:
                  if (scalar_product > 0) : 
                        angle = np.arccos(scalar_product)
                  else:
                        angle = -(2*math.pi-np.arccos(scalar_product))
            if (self.direction[0]>self.my_data.initial_direction[0]):
                  angle = -angle


            angle = math.degrees(angle)

            image_rect = image.get_rect(topleft = (self.pos[0] - self.origin_pos[0], self.pos[1]-self.origin_pos[1]))
            offset_center_to_pivot = self.pos - image_rect.center

            rotated_offset = offset_center_to_pivot.rotate(-angle)

            rotated_image_center = (self.pos[0] - rotated_offset.x, self.pos[1] - rotated_offset.y)

            self.current_image = pygame.transform.rotate(image, angle)
            self.rotated_image_rect = self.current_image.get_rect(center = rotated_image_center)


      def check_impact(self,game):
            self.my_total_timer +=  game.timestep 
            if self.my_total_timer > 2*self.my_data.anim_total_time:
                   pygame.sprite.Sprite.kill(self)
            elif ((self.my_total_timer > self.my_data.anim_total_time) and not(self.damage_dealt)):
                  self.target.velocity = self.target.my_data.velocity
                  self.target.hp -= self.damage 
                  self.target.stun_time = self.my_data.stun_time*1000  
                  self.damage_dealt = True
                  self.current_frame = 0
            elif (self.my_total_timer < self.my_data.anim_total_time):
                  self.target.my_timer = 0

      def render(self):
            window.blit(self.current_image, self.rotated_image_rect)  

class Light_bolt_lvl2(Light_bolt,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target,damage=LIGHTNING_BOLT_LVL2_DAMAGE):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.light_bolt_lvl2_data

            self.init(x,y,target,damage=LIGHTNING_BOLT_LVL2_DAMAGE)

class Light_bolt_lvl3(Light_bolt,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target,damage=LIGHTNING_BOLT_LVL3_DAMAGE):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.light_bolt_lvl3_data

            self.init(x,y,target,damage=LIGHTNING_BOLT_LVL3_DAMAGE)

class Ice_bolt(Projectile,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target,tower):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.ice_bolt_data

            self.init(x,y,target,tower)

      def init(self,x,y,target,tower):

            self.target = target
            self.tower = tower
            self.tower.firing = True

            self.target.velocity *= (1.0-self.my_data.slowing_coeff)

            self.posX = x    
            self.posY = y   
            self.pos = vec(x,y)

            self.current_image = self.my_data.static_image

            self.image_size = self.my_data.image_size
            self.my_target_center = self.target.rect.center
            self.distance = np.sqrt((self.my_target_center[0] - x)**2 + (self.my_target_center[1] - y)**2)
            resize_ratio = self.distance/self.image_size[1]
            self.current_image = pygame.transform.scale(self.current_image,self.image_size*resize_ratio)  

            self.image_size = vec(self.current_image.get_size())
            self.origin_pos = vec(self.my_data.centor_vector[0]*self.image_size[0],self.posY+self.my_data.centor_vector[1]*self.image_size[1])
      
            self.current_frame = 0

            self.my_timer = 0
            self.my_total_timer = 0

            self.rendering_layer = compute_rendering_layer_number(self)

            self.direction = vec(0,0)

            self.fading = False

      def move(self,game):  
            if not(self.fading):
                  self.my_target_center = self.target.rect.center
                  self.distance = np.sqrt((self.my_target_center[0] - self.posX)**2 + (self.my_target_center[1] - self.posY)**2)

                  self.my_target_center = self.target.rect.center
                  self.direction = (self.target.rect.center[0] - self.posX, self.target.rect.center[1] - self.posY)   
                  self.direction /= sqrt(self.direction[0]**2+self.direction[1]**2) 
                  
                  self.my_timer += game.timestep
                  if self.my_timer>self.my_data.time_per_frame:
                        self.current_frame += 1
                        self.current_frame = self.current_frame%self.my_data.number_frame
                        self.my_timer = 0.0   

                  self.current_image = self.my_data.images[self.current_frame].convert_alpha()

            else:
                  self.my_timer += game.timestep
                  if self.my_timer>(self.my_data.time_per_frame_fading):
                        self.current_frame += 1
                        self.my_timer = 0.0 

                  if (self.current_frame>(self.my_data.number_frame_fading-1)):
                        pygame.sprite.Sprite.kill(self)
                  else:
                        self.current_image= self.my_data.images_fading[self.current_frame].convert_alpha()



            image_size = vec(self.current_image.get_size())
            resize_ratio = self.distance/image_size[1]
            # self.current_image = pygame.transform.scale(self.current_image,image_size*resize_ratio)  ## to preserve dimensions ratio
            self.current_image = pygame.transform.scale(self.current_image,(image_size[0]*self.my_data.resize_factor,image_size[1]*resize_ratio))  

            self.image_size = vec(self.current_image.get_size())
            self.origin_pos = vec(self.my_data.centor_vector[0]*self.image_size[0],self.my_data.centor_vector[1]*self.image_size[1])

            self.rotate(self.current_image)

      def rotate(self,image):
            scalar_product = self.my_data.initial_direction[0]*self.direction[0]+self.my_data.initial_direction[1]*self.direction[1]
            if (self.direction[1]<self.my_data.initial_direction[1]):
                  if (scalar_product > 0) : 
                        angle = -np.arccos(scalar_product)
                  else:
                        angle = 2*math.pi-np.arccos(scalar_product)
            else:
                  if (scalar_product > 0) : 
                        angle = np.arccos(scalar_product)
                  else:
                        angle = -(2*math.pi-np.arccos(scalar_product))
            if (self.direction[0]>self.my_data.initial_direction[0]):
                  angle = -angle


            angle = math.degrees(angle)

            image_rect = image.get_rect(topleft = (self.pos[0] - self.origin_pos[0], self.pos[1]-self.origin_pos[1]))
            offset_center_to_pivot = self.pos - image_rect.center

            rotated_offset = offset_center_to_pivot.rotate(-angle)

            rotated_image_center = (self.pos[0] - rotated_offset.x, self.pos[1] - rotated_offset.y)

            self.current_image = pygame.transform.rotate(image, angle)
            self.rotated_image_rect = self.current_image.get_rect(center = rotated_image_center)


      def check_impact(self,game):
            if not(self.fading): 
                  if (not(pygame.sprite.Sprite.alive(self.target)) or (self.distance>(self.my_data.range*BACKGROUND_SQUARE_SIDE*1.2))):
                        self.fading = True
                        self.tower.firing = False
                        self.tower.attacking = False
                        self.current_frame = 0
                        self.target.velocity = self.target.my_data.velocity
                  else:
                        self.target.hp -= self.my_data.damage*game.timestep/1000.0
                        self.target.my_timer -= game.timestep*self.my_data.slowing_coeff
                        if self.my_data.freezing:
                              self.target.iced = True                 

      def render(self):
            window.blit(self.current_image, self.rotated_image_rect)  

class Ice_bolt_lvl2(Ice_bolt,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target,tower):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.ice_bolt_lvl2_data

            self.init(x,y,target,tower)

class Ice_bolt_lvl3(Ice_bolt,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target,tower):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.ice_bolt_lvl3_data

            self.init(x,y,target,tower)

class Bolt(Projectile,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.bolt_data

            Projectile.__init__(self,all_p,x,y,target)
                        
      def check_impact(self,game):
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False,pygame.sprite.collide_rect_ratio(self.my_data.ratio_for_impact))
            if self.hit_ennemies:
                  pygame.sprite.Sprite.kill(self)
                  for i in range (len(self.hit_ennemies)):
                        self.hit_ennemies[i].hp -= self.my_data.damage
            else:
                  if ((self.posX>WINDOW_WIDTH) or (self.posX<0)):
                      pygame.sprite.Sprite.kill(self)
 
class Rock(Projectile,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.rock_data

            Projectile.__init__(self,all_p,x,y,target)

            self.my_target_center = self.target.center

            self.my_timer = 0
                        
      def check_impact(self,game):
            distance = np.sqrt((self.my_target_center[0] - self.center[0])**2 + (self.my_target_center[1] - self.center[1])**2)
            if (distance<0.1*BACKGROUND_SQUARE_SIDE):
                  pygame.sprite.Sprite.kill(self)
                  game.all_impacts.add_impact(game,self,self.my_data.impact_tag)  


      def move(self,game):
            if (pygame.sprite.Sprite.alive(self.target)):
                  self.my_target_center = self.target.rect.center
                  self.direction = (self.target.rect.center[0] - self.center[0], self.target.rect.center[1] - self.center[1])   
                  self.direction /= sqrt(self.direction[0]**2+self.direction[1]**2)     
            self.posX += self.my_data.velocity * game.timestep * self.direction[0]
            self.posY += self.my_data.velocity * game.timestep * self.direction[1]
            self.rect.x = self.posX
            self.rect.y = self.posY
            self.center += self.my_data.velocity * game.timestep * self.direction
            self.rotate(game,self.my_data.static_image)

            # self.rendering_layer = compute_rendering_layer_number(self)
            self.rendering_layer = TOTAL_NUMBER_RENDERING_LAYER-3

      def rotate(self,game,image):
            self.my_timer += game.timestep
            if (ROCK_ROTATION_SPEED==0):
                  angle = 0
            else:
                  period = 1/(ROCK_ROTATION_SPEED/1000)
                  self.my_timer = self.my_timer%period
                  angle = 360*(self.my_timer/period)  # marche pas pour le moment car l'axe de rotation pas au milieu de l'image
            self.current_image = pygame.transform.rotate(image, angle)