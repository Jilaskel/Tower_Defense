import pygame
from utilitaries import *
from functions import *
from dead_body import *
from tower import * 
from magic_effects import * 

GOBLIN_TAG = 1
OGRE_TAG = 2
BLUE_NEC_TAG = 3
RED_NEC_TAG = 4
GREEN_NEC_TAG = 5
KAMIKAZE_TAG = 6
DRAGON_TAG = 7
BLUE_SKEL_TAG = 8
RED_SKEL_TAG = 9
GREEN_SKEL_TAG = 10


class All_ennemies(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self)   

            self.goblin_data = Goblin_data()
            self.ogre_data = Ogre_data()
            self.blue_nec_data = Blue_nec_data()
            self.red_nec_data = Red_nec_data()
            self.green_nec_data = Green_nec_data()
            self.blue_skel_data = Blue_skel_data()
            self.red_skel_data = Red_skel_data()
            self.green_skel_data = Green_skel_data()
            self.kamikaze_data = Kamikaze_data()
            self.dragon_data = Dragon_data()

      def add_goblin(self,x,y,rand_offset):
            self.add(Goblin(self,x,y,rand_offset))

      def add_ogre(self,x,y,rand_offset):
            self.add(Ogre(self,x,y,rand_offset))

      def add_blue_nec(self,x,y,rand_offset):
            self.add(Blue_Necromancer(self,x,y,rand_offset))

      def add_red_nec(self,x,y,rand_offset):
            self.add(Red_Necromancer(self,x,y,rand_offset))

      def add_green_nec(self,x,y,rand_offset):
            self.add(Green_Necromancer(self,x,y,rand_offset))

      def add_skel(self,x,y,tag):
            if (tag==BLUE_SKEL_TAG):
                  self.add_blue_skel(x,y,0)
            elif (tag==RED_SKEL_TAG):
                  self.add_red_skel(x,y,0)
            elif (tag==GREEN_SKEL_TAG):
                  self.add_green_skel(x,y,0)

      def add_blue_skel(self,x,y,rand_offset):
            self.add(Blue_Skeleton(self,x,y,rand_offset))

      def add_red_skel(self,x,y,rand_offset):
            self.add(Red_Skeleton(self,x,y,rand_offset))

      def add_green_skel(self,x,y,rand_offset):
            self.add(Green_Skeleton(self,x,y,rand_offset))

      def add_kamikaze(self,x,y,rand_offset):
            self.add(Kamikaze(self,x,y,rand_offset))

      def add_dragon(self,x,y,rand_offset):
            self.add(Dragon(self,x,y,rand_offset))

class Ennemy_data():
      def __init__(self):
            self.name = self.my_dict["NAME"]

            self.hp_max = self.my_dict["HP_MAX"]
            self.damage = self.my_dict["DAMAGE"]
            self.velocity = self.my_dict["VELOCITY"] # pixel by ms
            self.gold_earning = self.my_dict["GOLD_EARNING"]     

            self.static_image = pygame.image.load(self.my_dict["WALKING_IMAGE_PATH"]+"001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*self.my_dict["RESIZE_FACTOR"])             
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = self.my_dict["OFFSET"]
            self.center_vector = self.my_dict["CENTER_VECTOR"]
            self.hitbox_factor = self.my_dict["HITBOX_FACTOR"]

            self.number_frame_walking = self.my_dict["NUMBER_FRAME_WALKING"]
            self.image_walking = []
            for i in range(1,self.number_frame_walking+1):
                  self.image_walking.append(pygame.image.load(self.my_dict["WALKING_IMAGE_PATH"]+str(i).zfill(3)+".png").convert_alpha())  
                  self.image_walking[i-1] = pygame.transform.scale(self.image_walking[i-1],vec(self.image_walking[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
            self.anim_total_time_w = self.my_dict["ANIMATION_WALKING_TOTAL_TIME"]  # in ms
            self.time_per_frame_w = self.anim_total_time_w/self.number_frame_walking # in ms

            self.number_frame_attacking = self.my_dict["NUMBER_FRAME_ATTACKING"] 
            self.image_attacking = []
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(self.my_dict["ATTACKING_IMAGE_PATH"]+str(i).zfill(3)+".png").convert_alpha()) 
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
            self.anim_total_time_a = self.my_dict["ANIMATION_ATTACKING_TOTAL_TIME"]  # in ms
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms
            self.hitting_frame = self.my_dict["HITTING_FRAME"] - 1

            self.number_frame_stun = self.my_dict["STUN_NUMBER_FRAME"]
            self.image_stun = []
            for i in range(1,self.number_frame_stun+1):
                  self.image_stun.append(pygame.image.load(self.my_dict["STUN_IMAGE_PATH"]+str(i)+".png").convert_alpha()) 
                  self.image_stun[i-1] = pygame.transform.scale(self.image_stun[i-1],vec(self.image_stun[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])            
            self.time_per_frame_s = self.my_dict["STUN_TIME_PER_FRAME"]


      def init_transition_data(self):
            self.stop_walking_frame = self.my_dict["STOP_WALKING_FRAME"]    

            self.number_frame_transition = self.my_dict["NUMBER_FRAME_TRANSITION"]
            self.image_transition = []
            for i in range(1,self.number_frame_transition+1):
                  self.image_transition.append(pygame.image.load(self.my_dict["TRANSITION_IMAGE_PATH"]+str(i).zfill(3)+".png").convert_alpha()) 
                  self.image_transition[i-1] = pygame.transform.scale(self.image_transition[i-1],vec(self.image_transition[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
            self.anim_total_time_t = self.my_dict["ANIMATION_TRANSITION_TOTAL_TIME"]  # in ms
            self.time_per_frame_t = self.anim_total_time_t/self.number_frame_transition # in ms

      def init_casting_data(self):
            self.number_frame_casting = self.my_dict["NUMBER_FRAME_CASTING"] 
            self.image_casting = []
            for i in range(1,self.number_frame_casting+1):
                  self.image_casting.append(pygame.image.load(self.my_dict["CASTING_IMAGE_PATH"]+str(i).zfill(3)+".png").convert_alpha()) 
                  self.image_casting[i-1] = pygame.transform.scale(self.image_casting[i-1],vec(self.image_casting[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
            self.anim_total_time_c = self.my_dict["ANIMATION_CASTING_TOTAL_TIME"]  # in ms
            self.time_per_frame_c = self.anim_total_time_a/self.number_frame_casting # in ms
            self.casting_frame = 1

            self.rez_radius = self.my_dict["REZ_RADIUS"]*BACKGROUND_SQUARE_SIDE
            self.rez_cd = self.my_dict["REZ_COOLDOWN"]*1000

      def init_spawning_data(self):
            self.number_frame_spawning = self.my_dict["NUMBER_FRAME_SPAWNING"]
            self.image_spawning = []
            for i in range(1,self.number_frame_spawning+1):
                  self.image_spawning.append(pygame.image.load(self.my_dict["SPAWNING_IMAGE_PATH"]+str(i).zfill(3)+".png").convert_alpha()) 
                  self.image_spawning[i-1] = pygame.transform.scale(self.image_spawning[i-1],vec(self.image_spawning[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
            self.anim_total_time_sp = self.my_dict["ANIMATION_SPAWNING_TOTAL_TIME"]  # in ms
            self.time_per_frame_sp = self.anim_total_time_sp/self.number_frame_spawning # in ms

class Goblin_data(Ennemy_data):
      def __init__(self):
            self.my_dict = GOBLIN_DICT

            Ennemy_data.__init__(self)
            self.init_transition_data()

            self.dead_body_tag = DEAD_GOBLIN_TAG

class Ogre_data(Ennemy_data):
      def __init__(self):
            self.my_dict = OGRE_DICT

            Ennemy_data.__init__(self)
            self.init_transition_data()

            self.dead_body_tag = DEAD_OGRE_TAG

class Blue_nec_data(Ennemy_data):
      def __init__(self):
            self.my_dict = BLUE_NEC_DICT

            Ennemy_data.__init__(self)
            self.init_casting_data()

            self.summon_tag = BLUE_SKEL_TAG
            self.dead_body_tag = DEAD_BLUE_NEC_TAG

            self.wave_cd = self.my_dict["WAVE_COOLDOWN"]
            self.first_wave_time = self.my_dict["FIRST_WAVE_TIME"]

class Red_nec_data(Ennemy_data):
      def __init__(self):
            self.my_dict = RED_NEC_DICT

            Ennemy_data.__init__(self)
            self.init_casting_data()

            self.summon_tag = RED_SKEL_TAG
            self.dead_body_tag = DEAD_RED_NEC_TAG

            self.buff_cd = self.my_dict["BUFF_COOLDOWN"]
            self.first_buff_time = self.my_dict["FIRST_BUFF_TIME"]


class Green_nec_data(Ennemy_data):
      def __init__(self):
            self.my_dict = GREEN_NEC_DICT

            Ennemy_data.__init__(self)
            self.init_casting_data()

            self.summon_tag = GREEN_SKEL_TAG
            self.dead_body_tag = DEAD_GREEN_NEC_TAG

            self.root_cd = self.my_dict["ROOT_COOLDOWN"]
            self.first_root_time = self.my_dict["FIRST_ROOT_TIME"]
            self.number_max_tower_root = self.my_dict["NUMBER_MAX_OF_TOWER_ROOT"]

class Blue_skel_data(Ennemy_data):
      def __init__(self):
            self.my_dict = BLUE_SKEL_DICT

            Ennemy_data.__init__(self)
            self.init_spawning_data()

            self.dead_body_tag = DEAD_BLUE_SKEL_TAG 

class Red_skel_data(Ennemy_data):
      def __init__(self):
            self.my_dict = RED_SKEL_DICT

            Ennemy_data.__init__(self)
            self.init_spawning_data()

            self.dead_body_tag = DEAD_RED_SKEL_TAG 

class Green_skel_data(Ennemy_data):
      def __init__(self):
            self.my_dict = GREEN_SKEL_DICT

            Ennemy_data.__init__(self)
            self.init_spawning_data()

            self.dead_body_tag = DEAD_GREEN_SKEL_TAG 

class Kamikaze_data(Ennemy_data):
      def __init__(self):
            self.my_dict = KAMIKAZE_DICT

            Ennemy_data.__init__(self)

            self.explosion_killed = self.my_dict["EXPLOSION_WHEN_KILLED"]

class Dragon_data():
      def __init__(self):
            self.my_dict = DRAGON_DICT

            self.name = self.my_dict["NAME"]

            self.hp_max = self.my_dict["HP_MAX"]
            self.velocity = self.my_dict["VELOCITY"] # pixel by ms
            self.gold_earning = self.my_dict["GOLD_EARNING"] 
            self.damage = 0.0 #for enemy init    

            self.static_image = pygame.image.load(self.my_dict["WALKING_IMAGE_PATH"]+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*self.my_dict["RESIZE_FACTOR"])             
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = self.my_dict["OFFSET"]
            self.center_vector = self.my_dict["CENTER_VECTOR"]
            self.hitbox_factor = self.my_dict["HITBOX_FACTOR"]

            self.number_frame_walking = self.my_dict["NUMBER_FRAME_WALKING"]
            self.image_walking = []
            for i in range(1,self.number_frame_walking+1):
                  self.image_walking.append(pygame.image.load(self.my_dict["WALKING_IMAGE_PATH"]+str(i).zfill(4)+".png").convert_alpha())  
                  self.image_walking[i-1] = pygame.transform.scale(self.image_walking[i-1],vec(self.image_walking[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
                  self.image_walking[i-1] = pygame.transform.flip(self.image_walking[i-1], True, False)
            self.anim_total_time_w = self.my_dict["ANIMATION_WALKING_TOTAL_TIME"]  # in ms
            self.time_per_frame_w = self.anim_total_time_w/self.number_frame_walking # in ms

            self.dead_body_tag = DEAD_DRAGON_TAG

class Ennemy(pygame.sprite.Sprite):
      def __init__(self,x,y,rand_offset):
            pygame.sprite.Sprite.__init__(self)

            self.hp_max = self.my_data.hp_max*spawning_coeff.hp_coeff
            self.hp = self.hp_max

            self.velocity = self.my_data.velocity*spawning_coeff.velocity_coeff
            self.damage = self.my_data.damage*spawning_coeff.damage_coeff

            self.current_image = self.my_data.static_image

            self.image_size = self.my_data.image_size

            self.posX = x + self.my_data.image_offset[0]     
            self.posY = y + self.my_data.image_offset[1]   
            self.center = vec(self.posX+self.my_data.center_vector[0]*self.image_size[0],self.posY+self.my_data.center_vector[0]*self.image_size[1]) 
            self.rendering_layer = compute_rendering_layer_number(self)
            self.rendering_layer += rand_offset

            self.moving = False

            self.move_frame = 0
            self.transition_frame = 0      
            self.attack_frame = 0
            self.stun_frame = 0

            self.my_timer = 0

            self.hitbox_left = x
            self.hitbox_top = y
            side = BACKGROUND_SQUARE_SIDE
            self.radius = self.my_data.hitbox_factor*(side*2)/4.0
            self.hitbox_left = self.hitbox_left + (1-self.my_data.hitbox_factor)*side*0.5
            self.hitbox_top = self.hitbox_top + (1-self.my_data.hitbox_factor)*side*0.5
            self.hitbox_width = side*self.my_data.hitbox_factor
            self.hitbox_height = side*self.my_data.hitbox_factor
            self.rect = pygame.Rect(self.hitbox_left,self.hitbox_top,self.hitbox_width,self.hitbox_height)

            self.ready_to_attack = False
            self.attacking = False
            self.casting = False
            self.range_hitbox = None

            self.stun_time = 0.0
            self.stunned = False
            self.iced = False

      def move(self,game):
            if self.stun_time>0.0:
                  self.stunned = True
                  self.stun_time -= game.timestep

                  self.my_timer += game.timestep
                  if self.my_timer>self.my_data.time_per_frame_s:
                        self.stun_frame += 1
                        self.stun_frame = self.stun_frame%self.my_data.number_frame_stun
                        self.my_timer = 0.0
                                    
                  self.current_image= self.my_data.image_stun[self.stun_frame]
            else:
                  self.stunned = False
                  if self.attacking or self.casting:
                        self.moving = False                  
                  else:
                        self.moving = True
                        self.ready_to_attack = False
                        dx = self.velocity * game.timestep
                        self.posX += dx
                        self.center[0] += dx
                        self.hitbox_left += dx
                        self.rect.x = self.hitbox_left

                        if self.range_hitbox:
                              buff = self.range_hitbox.rect.x
                              buff = buff + dx
                              self.range_hitbox.rect.x = buff

                        self.my_timer += game.timestep
                        if self.my_timer>self.my_data.time_per_frame_w:
                              self.move_frame += 1
                              self.move_frame = self.move_frame%self.my_data.number_frame_walking
                              self.my_timer = 0.0
                                          
                        self.current_image= self.my_data.image_walking[self.move_frame]

      def attack(self,game):
            if (not(self.stunned) and not(self.casting)):
                  # self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_towers, False)
                  self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_towers.all_siege_engines, False)
                  if not self.detected_ennemies:
                        self.detected_ennemies = pygame.sprite.spritecollide(self, game.base.all_gates, False)
                  if not self.detected_ennemies:
                        self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_dead_bodies.all_iced_bodies, False)

                  if self.detected_ennemies:
                        self.attacking = True
                        self.my_timer += game.timestep

                        if self.my_timer>self.my_data.time_per_frame_a:
                              self.attack_frame += 1
                              self.attack_frame = self.attack_frame%self.my_data.number_frame_attacking
                              self.my_timer = 0.0
                              if (self.attack_frame==self.my_data.hitting_frame):
                                    for i in range (len(self.detected_ennemies)):
                                          self.detected_ennemies[i].hp -= self.damage

                        self.current_image = self.my_data.image_attacking[self.attack_frame]
                              
                  else:
                        self.attacking = False

      def attack_with_transition(self,game):
            if not(self.stunned):
                  # self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_towers, False)
                  self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_towers.all_siege_engines, False)
                  if not self.detected_ennemies:
                        self.detected_ennemies = pygame.sprite.spritecollide(self, game.base.all_gates, False)
                  if not self.detected_ennemies:
                        self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_dead_bodies.all_iced_bodies, False)

                  if self.detected_ennemies:
                        self.attacking = True
                        self.my_timer += game.timestep

                        if not self.ready_to_attack:
                              if (self.move_frame != (self.my_data.stop_walking_frame-1)):
                                    if self.my_timer>self.my_data.time_per_frame_w:
                                          self.move_frame += 1
                                          self.move_frame = self.move_frame%self.my_data.number_frame_walking
                                          self.my_timer = 0.0   
                                    self.current_image = self.my_data.image_walking[self.move_frame]
                              else:
                                    if self.my_timer>self.my_data.time_per_frame_t:
                                          self.transition_frame += 1
                                          self.my_timer = 0.0  
                                    if (self.transition_frame==self.my_data.number_frame_transition-1):
                                          self.ready_to_attack = True   
                                    self.current_image = self.my_data.image_transition[self.transition_frame]                                                
                        else:
                              if self.my_timer>self.my_data.time_per_frame_a:
                                    self.attack_frame += 1
                                    self.attack_frame = self.attack_frame%self.my_data.number_frame_attacking
                                    self.my_timer = 0.0
                                    if (self.attack_frame==self.my_data.hitting_frame):
                                          for i in range (len(self.detected_ennemies)):
                                                self.detected_ennemies[i].hp -= self.damage
                              self.current_image = self.my_data.image_attacking[self.attack_frame]

                                                      
                  else:
                        self.attacking = False

      def use_power(self,game):
            pass

      def die(self,game):
            if (self.hp<=0):
                  game.gold.gold_gain(game,self,self.my_data.gold_earning)
                  game.all_dead_bodies.add_dead_body(game,self,self.my_data.dead_body_tag)
                  pygame.sprite.Sprite.kill(self)
            else:
                  self.iced = False

      def render(self):
            window.blit(self.current_image, (self.posX, self.posY))  


class Necromancer(Ennemy):
      def __init__(self,all_e):
            self.all_e = all_e

            self.cast_frame = 0
            self.rez_done = False
            self.rez_timer = self.my_data.rez_cd*2
            self.detected_bodies = None
            self.image_offset = self.my_data.image_offset

            self.using_power = False

            self.range_hitbox = Range_Hitbox(self,self.rect.w,self.rect.h,self.my_data.rez_radius,circular=True)

      def rez_dead_bodies(self,game):
            self.rez_timer += game.timestep
            if (not(self.stunned) and (self.rez_timer>self.my_data.rez_cd)):
                  self.detected_bodies = pygame.sprite.spritecollide(self.range_hitbox, game.all_dead_bodies.all_rezable_bodies, False, pygame.sprite.collide_circle)
                  if self.detected_bodies:
                        game.all_dead_bodies.all_rezable_bodies.remove(self.detected_bodies[0])
                        self.rez_done = False
                        self.cast_frame = 0
                        self.my_timer = 0.0

            if self.detected_bodies:
                  self.casting = True
                  self.my_timer += game.timestep
                  self.rez_timer = 0.0

                  if self.my_timer>self.my_data.time_per_frame_c:
                        self.cast_frame += 1
                        self.my_timer = 0.0
                  if (self.cast_frame<self.my_data.number_frame_casting):
                        if ((self.cast_frame==self.my_data.casting_frame) and not(self.rez_done)):
                              #rezing
                              self.all_e.add_skel(self.detected_bodies[0].posX - self.detected_bodies[0].image_offset[0],self.detected_bodies[0].posY - self.detected_bodies[0].image_offset[1],self.my_data.summon_tag)
                              self.rez_done = True
                  
                        self.current_image = self.my_data.image_casting[self.cast_frame]

                  else:
                        pygame.sprite.Sprite.kill(self.detected_bodies[0])
                        self.detected_bodies = None
                        self.casting = False
                        self.current_image = self.my_data.image_casting[self.my_data.number_frame_casting-1]

            elif (self.using_power):
                  self.casting = True
                  self.my_timer += game.timestep
                  self.rez_timer = 0.0

                  if self.my_timer>self.my_data.time_per_frame_c:
                        self.cast_frame += 1
                        self.my_timer = 0.0    
                  if (self.cast_frame<self.my_data.number_frame_casting):
                        self.current_image = self.my_data.image_casting[self.cast_frame]
                  else:
                        self.current_image = self.my_data.image_casting[self.my_data.number_frame_casting-1]
                        self.casting = False
                        self.using_power = False

            else:
                  self.casting = False            

class Blue_Necromancer(Necromancer):
      def __init__(self,all_e,x,y,rand_offset):
            self.my_data = all_e.blue_nec_data

            Ennemy.__init__(self,x,y,rand_offset)
            Necromancer.__init__(self,all_e)
            self.wave_timer = self.my_data.first_wave_time*1000

      def use_power(self,game):
            self.rez_dead_bodies(game)

            self.wave_timer -= game.timestep
            if self.wave_timer < 0.0:
                  game.all_magic_effects.add_wave(self)
                  self.wave_timer = self.my_data.wave_cd*1000
                  self.using_power = True
                  self.cast_frame = 0
                  self.my_timer = 0.0

class Red_Necromancer(Necromancer):
      def __init__(self,all_e,x,y,rand_offset):
            self.my_data = all_e.red_nec_data

            Ennemy.__init__(self,x,y,rand_offset)
            Necromancer.__init__(self,all_e)
            self.buff_timer = self.my_data.first_buff_time*1000

      def use_power(self,game):
            self.rez_dead_bodies(game)

            self.buff_timer -= game.timestep
            if self.buff_timer < 0.0:
                  self.detected_allies = pygame.sprite.spritecollide(self.range_hitbox, game.all_ennemies, False, pygame.sprite.collide_circle)
                  if self.detected_allies:
                        for ally in self.detected_allies:
                              game.all_magic_effects.add_buff(ally)
                        self.buff_timer = self.my_data.buff_cd*1000
                        self.using_power = True
                        self.cast_frame = 0
                        self.my_timer = 0.0

class Green_Necromancer(Necromancer):
      def __init__(self,all_e,x,y,rand_offset):
            self.my_data = all_e.green_nec_data

            Ennemy.__init__(self,x,y,rand_offset)
            Necromancer.__init__(self,all_e)
            self.root_timer = self.my_data.first_root_time*1000

      def use_power(self,game):
            self.rez_dead_bodies(game)

            self.root_timer -= game.timestep
            if self.root_timer < 0.0:
                  tower_rooted = 0
                  self.detected_towers = pygame.sprite.spritecollide(self.range_hitbox, game.all_towers, False, pygame.sprite.collide_circle)
                  if self.detected_towers:
                        for tower in self.detected_towers:
                              if (tower_rooted == self.my_data.number_max_tower_root):
                                    break
                              #if (not(tower in game.all_towers.all_siege_engines) and not(tower.rooted)): C'EST LA MERDE !!!!
                              if (not(tower in game.all_towers.all_siege_engines) and not(tower.rooted) and not(tower in game.all_towers.all_engines_on_wall)):
                                    tower.rooted = True
                                    tower.my_timer = 0.0
                                    tower_rooted += 1
                  if tower_rooted > 0:
                        self.root_timer = self.my_data.root_cd*1000
                        self.using_power = True
                        self.cast_frame = 0
                        self.my_timer = 0.0
                        game.all_mixers.magical_effect_mixer.root_sound.play(maxtime=SOUND_ROOT_MAX_TIME)

class Skeleton(Ennemy):
      def __init__(self,all_e,x,y,rand_offset): 
            Ennemy.__init__(self,x,y,rand_offset)

            if rand_offset==0:   #summoned
                  self.stunned = True # to pass attack() while summoning
                  self.my_timer_sp = 0.0
                  self.spawn_frame = 0
            else:
                  self.stunned = False
                  self.my_timer_sp = self.my_data.anim_total_time_sp*2      

      def move(self,game):
            if (self.my_timer_sp<self.my_data.anim_total_time_sp):
                  self.my_timer_sp += game.timestep
                  self.my_timer += game.timestep

                  if self.my_timer>self.my_data.time_per_frame_sp:
                        self.spawn_frame += 1
                        self.my_timer = 0.0  
                  self.spawn_frame = min(self.spawn_frame,self.my_data.number_frame_spawning-1)
                  self.current_image = self.my_data.image_spawning[self.spawn_frame]   

            else:
                  Ennemy.move(self,game)           

class Blue_Skeleton(Skeleton):
      def __init__(self,all_e,x,y,rand_offset):
            self.my_data = all_e.blue_skel_data

            Skeleton.__init__(self,all_e,x,y,rand_offset)

class Red_Skeleton(Skeleton):
      def __init__(self,all_e,x,y,rand_offset):
            self.my_data = all_e.red_skel_data

            Skeleton.__init__(self,all_e,x,y,rand_offset)

class Green_Skeleton(Skeleton):
      def __init__(self,all_e,x,y,rand_offset):
            self.my_data = all_e.green_skel_data

            Skeleton.__init__(self,all_e,x,y,rand_offset)

class Goblin(Ennemy):
      def __init__(self,all_e,x,y,rand_offset): 
            self.my_data = all_e.goblin_data

            Ennemy.__init__(self,x,y,rand_offset)

      def attack(self,game):
            self.attack_with_transition(game)

class Ogre(Ennemy):
      def __init__(self,all_e,x,y,rand_offset): 
            self.my_data = all_e.ogre_data

            Ennemy.__init__(self,x,y,rand_offset)

      def attack(self,game):
            self.attack_with_transition(game)

class Kamikaze(Ennemy):
      def __init__(self,all_e,x,y,rand_offset): 
            self.my_data = all_e.kamikaze_data

            Ennemy.__init__(self,x,y,rand_offset)

            self.launch_explosion = False

      def attack(self,game):
            if (not(self.stunned) and not(self.casting)):
                  # self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_towers, False)
                  self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_towers.all_siege_engines, False)
                  if not self.detected_ennemies:
                        self.detected_ennemies = pygame.sprite.spritecollide(self, game.base.all_gates, False)
                  if not self.detected_ennemies:
                        self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_dead_bodies.all_iced_bodies, False)

                  if self.detected_ennemies:
                        self.attacking = True
                        if not(self.launch_explosion):
                              self.launch_explosion = True
                              game.all_magic_effects.add_explosion(self)                              
                  else:
                        self.attacking = False

      def die(self,game):
            if (self.hp<=0):
                  if self.my_data.explosion_killed and not(self.launch_explosion):
                        game.all_magic_effects.add_explosion(self)
                  game.gold.gold_gain(game,self,self.my_data.gold_earning)
                  pygame.sprite.Sprite.kill(self)

class Dragon(Ennemy):
      def __init__(self,all_e,x,y,rand_offset): 
            self.my_data = all_e.dragon_data

            Ennemy.__init__(self,x,y,rand_offset)

            self.rendering_layer = 23

            self.rect.width *= 2

      def attack(self,game):
            self.stun_time = 0.0
            pass

      def die(self,game):
            if (self.hp<=0):
                  game.gold.gold_gain(game,self,self.my_data.gold_earning)
                  pygame.sprite.Sprite.kill(self)
