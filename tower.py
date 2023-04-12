import pygame
from utilitaries import *
from projectile import *
from functions import *

ARCANE_TOWER_LVL1_BUTTON_TAG = 1
ARCANE_TOWER_LVL2_BUTTON_TAG = 2
ARCANE_TOWER_LVL3_BUTTON_TAG = 3
FIRE_TOWER_LVL1_BUTTON_TAG = 4
FIRE_TOWER_LVL2_BUTTON_TAG = 5
FIRE_TOWER_LVL3_BUTTON_TAG = 6
LIGHTNING_TOWER_LVL1_BUTTON_TAG = 7
LIGHTNING_TOWER_LVL2_BUTTON_TAG = 8
LIGHTNING_TOWER_LVL3_BUTTON_TAG = 9
ICE_TOWER_LVL1_BUTTON_TAG = 10
ICE_TOWER_LVL2_BUTTON_TAG = 11
ICE_TOWER_LVL3_BUTTON_TAG = 12
BALLISTA_BUTTON_TAG = 13
CATAPULT_BUTTON_TAG = 14


class All_towers(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self)   

            self.all_siege_engines = All_siege_engines()

            self.arcane_tower_lvl1_data = Arcane_tower_lvl1_data()
            self.arcane_tower_lvl2_data = Arcane_tower_lvl2_data()
            self.arcane_tower_lvl3_data = Arcane_tower_lvl3_data()
            self.fire_tower_lvl1_data = Fire_tower_lvl1_data()
            self.fire_tower_lvl2_data = Fire_tower_lvl2_data()
            self.fire_tower_lvl3_data = Fire_tower_lvl3_data()
            self.lightning_tower_lvl1_data = Lightning_tower_lvl1_data()
            self.lightning_tower_lvl2_data = Lightning_tower_lvl2_data()
            self.lightning_tower_lvl3_data = Lightning_tower_lvl3_data()
            self.ice_tower_lvl1_data = Ice_tower_lvl1_data()
            self.ice_tower_lvl2_data = Ice_tower_lvl2_data()
            self.ice_tower_lvl3_data = Ice_tower_lvl3_data()
                        
            self.ballista_data = Ballista_data()
            self.catapult_data = Catapult_data()

      def add_tower(self,game,box,tag):
            if (tag==ARCANE_TOWER_LVL1_BUTTON_TAG):
                  self.add_arcane_tower_lvl1(game,box)
            elif (tag==ARCANE_TOWER_LVL2_BUTTON_TAG):
                  self.add_arcane_tower_lvl2(game,box)
            elif (tag==ARCANE_TOWER_LVL3_BUTTON_TAG):
                  self.add_arcane_tower_lvl3(game,box)
            elif (tag==FIRE_TOWER_LVL1_BUTTON_TAG):
                  self.add_fire_tower_lvl1(game,box)
            elif (tag==FIRE_TOWER_LVL2_BUTTON_TAG):
                  self.add_fire_tower_lvl2(game,box)
            elif (tag==FIRE_TOWER_LVL3_BUTTON_TAG):
                  self.add_fire_tower_lvl3(game,box)
            elif (tag==LIGHTNING_TOWER_LVL1_BUTTON_TAG):
                  self.add_lightning_tower_lvl1(game,box)
            elif (tag==LIGHTNING_TOWER_LVL2_BUTTON_TAG):
                  self.add_lightning_tower_lvl2(game,box)
            elif (tag==LIGHTNING_TOWER_LVL3_BUTTON_TAG):
                  self.add_lightning_tower_lvl3(game,box)
            elif (tag==ICE_TOWER_LVL1_BUTTON_TAG):
                  self.add_ice_tower_lvl1(game,box)
            elif (tag==ICE_TOWER_LVL2_BUTTON_TAG):
                  self.add_ice_tower_lvl2(game,box)
            elif (tag==ICE_TOWER_LVL3_BUTTON_TAG):
                  self.add_ice_tower_lvl3(game,box)
            elif (tag==BALLISTA_BUTTON_TAG):
                  self.add_ballista(game,box)
            elif (tag==CATAPULT_BUTTON_TAG):
                  self.add_catapult(game,box)      
          

      def add_arcane_tower_lvl1(self,game,box):
            self.add(Arcane_tower_lvl1(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()  

      def add_arcane_tower_lvl2(self,game,box):
            self.add(Arcane_tower_lvl2(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()  

      def add_arcane_tower_lvl3(self,game,box):
            self.add(Arcane_tower_lvl3(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()  

      def add_fire_tower_lvl1(self,game,box):
            self.add(Fire_tower_lvl1(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()

      def add_fire_tower_lvl2(self,game,box):
            self.add(Fire_tower_lvl2(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()

      def add_fire_tower_lvl3(self,game,box):
            self.add(Fire_tower_lvl3(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()
      
      def add_lightning_tower_lvl1(self,game,box):
            self.add(Lightning_tower_lvl1(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()

      def add_lightning_tower_lvl2(self,game,box):
            self.add(Lightning_tower_lvl2(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()

      def add_lightning_tower_lvl3(self,game,box):
            self.add(Lightning_tower_lvl3(game,self,box))
            game.all_mixers.mouse_mixer.building_rock_sound.play()

      def add_ice_tower_lvl1(self,game,box):
            self.add(Ice_tower_lvl1(game,self,box))
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

class Tower_data():
      def __init__(self):
            self.name = self.my_dict["NAME"] 

            self.hp_max = self.my_dict["HP_MAX"]

            self.gold_cost = -self.my_dict["PRICE"]

            self.static_image = pygame.image.load(self.my_dict["ATTACK_IMAGE_PATH"]+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*self.my_dict["RESIZE_FACTOR"])        
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = self.my_dict["OFFSET"]
            self.firing_offset = self.my_dict["FIRING_OFFSET"]
            self.range = self.my_dict["RANGE"]

            self.image_attacking = []
            self.number_frame_attacking = self.my_dict["NUMBER_FRAME_ATTACKING"]
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(self.my_dict["ATTACK_IMAGE_PATH"]+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
            self.anim_total_time_a = self.my_dict["ANIMATION_ATTACKING_TOTAL_TIME"]
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            self.number_frame_reloading = self.my_dict["NUMBER_FRAME_ATTACKING"]
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(self.my_dict["ATTACK_IMAGE_PATH"]+str(self.number_frame_reloading-i+1).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
            self.anim_total_time_r = self.my_dict["ANIMATION_RELOADING_TOTAL_TIME"]
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms

class Siege_engine_data():
      def __init__(self):
            self.name = self.my_dict["NAME"] 

            self.hp_max = self.my_dict["HP_MAX"]

            self.gold_cost = -self.my_dict["PRICE"]

            self.static_image = pygame.image.load(self.my_dict["ATTACK_IMAGE_PATH"]+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*self.my_dict["RESIZE_FACTOR"])        
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = self.my_dict["OFFSET"]
            self.firing_offset = self.my_dict["FIRING_OFFSET"]
            self.range = self.my_dict["RANGE"]

            self.image_attacking = []
            self.number_frame_attacking = self.my_dict["NUMBER_FRAME_ATTACKING"]
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(self.my_dict["ATTACK_IMAGE_PATH"]+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
            self.anim_total_time_a = self.my_dict["ANIMATION_ATTACKING_TOTAL_TIME"]
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            self.number_frame_reloading = self.my_dict["NUMBER_FRAME_ATTACKING"]
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(self.my_dict["ATTACK_IMAGE_PATH"]+str(self.number_frame_reloading-i+1).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
            self.anim_total_time_r = self.my_dict["ANIMATION_RELOADING_TOTAL_TIME"]
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms

            self.image_reloading = []
            offset_degeu = 5
            self.number_frame_reloading = self.my_dict["NUMBER_FRAME_RELOADING"]
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(self.my_dict["RELOAD_IMAGE_PATH"]+str(i+offset_degeu).zfill(4)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
            self.anim_total_time_r = self.my_dict["ANIMATION_RELOADING_TOTAL_TIME"]
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms


class Arcane_tower_lvl1_data(Tower_data):
      def __init__(self):
            self.my_dict = ARCANE_TOWER_LVL1_DICT

            Tower_data.__init__(self)

            self.bolt_tag = ARCANE_TOWER_LVL1_BOLT_TAG

class Arcane_tower_lvl2_data(Tower_data):
      def __init__(self):
            self.my_dict = ARCANE_TOWER_LVL2_DICT

            Tower_data.__init__(self)

            self.bolt_tag = ARCANE_TOWER_LVL2_BOLT_TAG


class Arcane_tower_lvl3_data(Tower_data):
      def __init__(self):
            self.my_dict = ARCANE_TOWER_LVL3_DICT

            Tower_data.__init__(self)

            self.bolt_tag = ARCANE_TOWER_LVL3_BOLT_TAG


class Fire_tower_lvl1_data(Tower_data):
      def __init__(self):
            self.my_dict = FIRE_TOWER_LVL1_DICT

            Tower_data.__init__(self)

            self.bolt_tag = FIRE_TOWER_LVL1_BOLT_TAG


class Fire_tower_lvl2_data(Tower_data):
      def __init__(self):
            self.my_dict = FIRE_TOWER_LVL2_DICT

            Tower_data.__init__(self)

            self.bolt_tag = FIRE_TOWER_LVL2_BOLT_TAG


class Fire_tower_lvl3_data(Tower_data):
      def __init__(self):
            self.my_dict = FIRE_TOWER_LVL3_DICT

            Tower_data.__init__(self)

            self.bolt_tag = FIRE_TOWER_LVL3_BOLT_TAG


class Lightning_tower_lvl1_data(Tower_data):
      def __init__(self):
            self.my_dict = LIGHTNING_TOWER_LVL1_DICT

            Tower_data.__init__(self)

            self.bolt_tag = LIGHTNING_TOWER_LVL1_BOLT_TAG


class Lightning_tower_lvl2_data(Tower_data):
      def __init__(self):
            self.my_dict = LIGHTNING_TOWER_LVL2_DICT

            Tower_data.__init__(self)

            self.bolt_tag = LIGHTNING_TOWER_LVL2_BOLT_TAG


class Lightning_tower_lvl3_data(Tower_data):
      def __init__(self):
            self.my_dict = LIGHTNING_TOWER_LVL3_DICT

            Tower_data.__init__(self)

            self.bolt_tag = LIGHTNING_TOWER_LVL3_BOLT_TAG


class Ice_tower_lvl1_data(Tower_data):
      def __init__(self):
            self.my_dict = ICE_TOWER_LVL1_DICT

            Tower_data.__init__(self)

            self.bolt_tag = ICE_TOWER_LVL1_BOLT_TAG


class Ice_tower_lvl2_data(Tower_data):
      def __init__(self):
            self.my_dict = ICE_TOWER_LVL2_DICT

            Tower_data.__init__(self)

            self.bolt_tag = ICE_TOWER_LVL2_BOLT_TAG


class Ice_tower_lvl3_data(Tower_data):
      def __init__(self):
            self.my_dict = ICE_TOWER_LVL3_DICT

            Tower_data.__init__(self)

            self.bolt_tag = ICE_TOWER_LVL3_BOLT_TAG

class Ballista_data(Siege_engine_data):
      def __init__(self):
            self.my_dict = BALLISTA_DICT

            Siege_engine_data.__init__(self)

            self.bolt_tag = BALLISTA_BOLT_TAG


class Catapult_data(Siege_engine_data):
      def __init__(self):
            self.my_dict = CATAPULT_DICT

            Siege_engine_data.__init__(self)

            self.bolt_tag = CATAPULT_BOLT_TAG


class Tower(pygame.sprite.Sprite):
      def __init__(self,game,box):
            
            x = box.posX
            y = box.posY
            self.box = box

            self.hp = self.my_data.hp_max
      
            self.current_image = self.my_data.static_image  
            self.posX = x + self.my_data.image_offset[0]
            self.posY = y + self.my_data.image_offset[1]
            self.image_offset = self.my_data.image_offset   ## for range hitbox beacause it is also used in menu....
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


class Arcane_tower_lvl1(Tower):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.arcane_tower_lvl1_data

            Tower.__init__(self,game,box)

class Arcane_tower_lvl2(Tower):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.arcane_tower_lvl2_data

            Tower.__init__(self,game,box)

class Arcane_tower_lvl3(Tower):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.arcane_tower_lvl3_data

            Tower.__init__(self,game,box)

class Fire_tower_lvl1(Tower):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.fire_tower_lvl1_data

            Tower.__init__(self,game,box)

class Fire_tower_lvl2(Tower):
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

class Lightning_tower_lvl1(Tower):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.lightning_tower_lvl1_data

            Tower.__init__(self,game,box)

class Lightning_tower_lvl2(Tower):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.lightning_tower_lvl2_data

            Tower.__init__(self,game,box)

class Lightning_tower_lvl3(Tower):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.lightning_tower_lvl3_data

            Tower.__init__(self,game,box)

class Ice_tower_lvl1(Tower):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.ice_tower_lvl1_data

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

class Ice_tower_lvl2(Ice_tower_lvl1,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.ice_tower_lvl2_data

            self.firing = False

            Tower.__init__(self,game,box)

class Ice_tower_lvl3(Ice_tower_lvl1,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.ice_tower_lvl3_data

            self.firing = False

            Tower.__init__(self,game,box)

class Siege_engine(Tower):
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

            self.anim_frame_a = 0
            self.anim_frame_r = 0

            self.detected_ennemies = False
            self.my_target = []

            self.hitbox_left = x
            self.hitbox_top = y
            self.hitbox_width = BACKGROUND_SQUARE_SIDE
            self.hitbox_height = BACKGROUND_SQUARE_SIDE
            self.rect = pygame.Rect(self.hitbox_left,self.hitbox_top,self.hitbox_width,self.hitbox_height)            
            self.range = self.my_data.range*(self.rect.width+self.rect.height)/2.0

            game.gold.gold_gain(game,self,self.my_data.gold_cost)


class Ballista(Siege_engine,pygame.sprite.Sprite):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.ballista_data

            Siege_engine.__init__(self,game,box)

            self.range_hitbox = Range_Hitbox(self,self.rect.w,self.rect.h,self.range,circular=False,tag="Ballista")


class Catapult(Siege_engine):
      def __init__(self,game,all_t,box):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_t.catapult_data

            Siege_engine.__init__(self,game,box)

            self.range_hitbox = Range_Hitbox(self,self.rect.w,self.rect.h,self.range,circular=False,tag="Catapult")


            
class Range_Hitbox(pygame.sprite.Sprite):
      def __init__(self,tower,width,height,range,circular,tag="Ballista"):
            super().__init__()
            self.range = range
            if circular:
                  self.image_offset = tower.image_offset
                  self.circular = True
                  self.rect = pygame.Rect(tower.posX-self.image_offset[0],tower.posY-self.image_offset[1],tower.rect.width,tower.rect.height)
                  self.radius = self.range
                  self.posX = tower.posX-self.image_offset[0]+width*0.5 - self.radius
                  self.posY = tower.posY-self.image_offset[1]+height*0.5 - self.radius    

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

