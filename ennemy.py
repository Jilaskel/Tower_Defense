import pygame
from utilitaries import *
from functions import *
from dead_body import *
from tower import * 

class All_ennemies(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self)   

            self.goblin_data = Goblin_data()
            self.ogre_data = Ogre_data()
            self.blue_nec_data = Blue_nec_data()
            self.dragon_data = Dragon_data()

      def add_goblin(self,x,y,rand_offset):
            self.add(Goblin(self,x,y,rand_offset))

      def add_ogre(self,x,y,rand_offset):
            self.add(Ogre(self,x,y,rand_offset))

      def add_blue_nec(self,x,y,rand_offset):
            self.add(Blue_Necromancer(self,x,y,rand_offset))

      def add_dragon(self,x,y,rand_offset):
            self.add(Dragon(self,x,y,rand_offset))

class Ennemy_data():
      def __init__(self):
            self.name = self.my_dict["NAME"]

            self.hp_max = self.my_dict["HP_MAX"]
            self.damage = self.my_dict["DAMAGE"]
            self.velocity = self.my_dict["VELOCITY"] # pixel by ms
            self.gold_earning = self.my_dict["GOLD_EARNING"]     

            self.static_image = pygame.image.load(self.my_dict["TRANSITION_IMAGE_PATH"]+"001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*self.my_dict["RESIZE_FACTOR"])             
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = self.my_dict["OFFSET"]
            self.centor_vector = self.my_dict["CENTER_VECTOR"]
            self.hitbox_factor = self.my_dict["HITBOX_FACTOR"]

            self.number_frame_walking = self.my_dict["NUMBER_FRAME_WALKING"]
            self.image_walking = []
            for i in range(1,self.number_frame_walking+1):
                  self.image_walking.append(pygame.image.load(self.my_dict["WALKING_IMAGE_PATH"]+str(i).zfill(3)+".png").convert_alpha())  
                  self.image_walking[i-1] = pygame.transform.scale(self.image_walking[i-1],vec(self.image_walking[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
            self.anim_total_time_w = self.my_dict["ANIMATION_WALKING_TOTAL_TIME"]  # in ms
            self.time_per_frame_w = self.anim_total_time_w/self.number_frame_walking # in ms
            self.stop_walking_frame = self.my_dict["STOP_WALKING_FRAME"]    

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
            self.number_frame_transition = self.my_dict["NUMBER_FRAME_TRANSITION"]
            self.image_transition = []
            for i in range(1,self.number_frame_transition+1):
                  self.image_transition.append(pygame.image.load(self.my_dict["TRANSITION_IMAGE_PATH"]+str(i).zfill(3)+".png").convert_alpha()) 
                  self.image_transition[i-1] = pygame.transform.scale(self.image_transition[i-1],vec(self.image_transition[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
            self.anim_total_time_t = self.my_dict["ANIMATION_TRANSITION_TOTAL_TIME"]  # in ms
            self.time_per_frame_t = self.anim_total_time_t/self.number_frame_transition # in ms

class Goblin_data(Ennemy_data):
      def __init__(self):
            self.my_dict = GOBLIN_DICT

            Ennemy_data.__init__(self)
            self.init_transition_data()

            self.dead_body_tag = DEAD_GOBLIN_TAG


class Ogre_data():
      def __init__(self):
            self.name = "Ogre"

            self.hp_max = OGRE_HP_MAX
            self.damage = OGRE_DAMAGE
            self.velocity = OGRE_VELOCITY # pixel by ms
            self.gold_earning = OGRE_GOLD_EARNING

            self.static_image = pygame.image.load(OGRE_TRANSITION_IMAGE_PATH+"001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*OGRE_RESIZE_FACTOR)             
            self.current_image = self.static_image
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = OGRE_OFFSET
            self.centor_vector = OGRE_CENTER_VECTOR
            self.hitbox_factor = OGRE_HITBOX_FACTOR

            self.number_frame_walking = OGRE_NUMBER_FRAME_WALKING
            self.image_walking = []
            for i in range(1,self.number_frame_walking+1):
                  self.image_walking.append(pygame.image.load(OGRE_WALKING_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha())  
                  self.image_walking[i-1] = pygame.transform.scale(self.image_walking[i-1],vec(self.image_walking[i-1].get_size())*OGRE_RESIZE_FACTOR)
            self.anim_total_time_w = OGRE_ANIMATION_WALKING_TOTAL_TIME  # in ms
            self.time_per_frame_w = self.anim_total_time_w/self.number_frame_walking # in ms
            self.stop_walking_frame = OGRE_STOP_WALKING_FRAME

            self.number_frame_transition = OGRE_NUMBER_FRAME_TRANSITION
            self.image_transition = []
            for i in range(1,self.number_frame_transition+1):
                  self.image_transition.append(pygame.image.load(OGRE_TRANSITION_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha()) 
                  self.image_transition[i-1] = pygame.transform.scale(self.image_transition[i-1],vec(self.image_transition[i-1].get_size())*OGRE_RESIZE_FACTOR)
            self.anim_total_time_t = OGRE_ANIMATION_TRANSITION_TOTAL_TIME  # in ms
            self.time_per_frame_t = self.anim_total_time_t/self.number_frame_transition # in ms

            self.number_frame_attacking = OGRE_NUMBER_FRAME_ATTACKING 
            self.image_attacking = []
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(OGRE_ATTACKING_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha()) 
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*OGRE_RESIZE_FACTOR)
            self.anim_total_time_a = OGRE_ANIMATION_ATTACKING_TOTAL_TIME  # in ms
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms
            self.hitting_frame = OGRE_HITTING_FRAME - 1

            self.number_frame_stun = OGRE_STUN_NUMBER_FRAME
            self.image_stun = []
            for i in range(1,self.number_frame_stun+1):
                  self.image_stun.append(pygame.image.load(OGRE_STUN_IMAGE_PATH+str(i)+".png").convert_alpha()) 
                  self.image_stun[i-1] = pygame.transform.scale(self.image_stun[i-1],vec(self.image_stun[i-1].get_size())*OGRE_RESIZE_FACTOR)  
            self.time_per_frame_s = OGRE_STUN_TIME_PER_FRAME

            self.dead_body_tag = DEAD_OGRE_TAG


class Blue_nec_data():
      def __init__(self):
            self.name = "Ice Necromancer"

            self.hp_max = BLUE_NEC_HP_MAX
            self.damage = BLUE_NEC_DAMAGE
            self.velocity = BLUE_NEC_VELOCITY # pixel by ms
            self.gold_earning = BLUE_NEC_GOLD_EARNING

            self.rez_radius = BLUE_NEC_REZ_RADIUS*BACKGROUND_SQUARE_SIDE
            self.rez_cd = BLUE_NEC_REZ_COOLDOWN*1000

            self.static_image = pygame.image.load(BLUE_NEC_WALKING_IMAGE_PATH+"001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*BLUE_NEC_RESIZE_FACTOR)             
            self.current_image = self.static_image
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = BLUE_NEC_OFFSET
            self.centor_vector = BLUE_NEC_CENTER_VECTOR
            self.hitbox_factor = BLUE_NEC_HITBOX_FACTOR

            self.number_frame_walking = BLUE_NEC_NUMBER_FRAME_WALKING
            self.image_walking = []
            for i in range(1,self.number_frame_walking+1):
                  self.image_walking.append(pygame.image.load(BLUE_NEC_WALKING_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha())  
                  self.image_walking[i-1] = pygame.transform.scale(self.image_walking[i-1],vec(self.image_walking[i-1].get_size())*BLUE_NEC_RESIZE_FACTOR)
            self.anim_total_time_w = BLUE_NEC_ANIMATION_WALKING_TOTAL_TIME  # in ms
            self.time_per_frame_w = self.anim_total_time_w/self.number_frame_walking # in ms

            self.number_frame_attacking = BLUE_NEC_NUMBER_FRAME_ATTACKING 
            self.image_attacking = []
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(BLUE_NEC_ATTACKING_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha()) 
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*BLUE_NEC_RESIZE_FACTOR)
            self.anim_total_time_a = BLUE_NEC_ANIMATION_ATTACKING_TOTAL_TIME  # in ms
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms
            self.hitting_frame = BLUE_NEC_HITTING_FRAME - 1

            self.number_frame_casting = BLUE_NEC_NUMBER_FRAME_CASTING 
            self.image_casting = []
            for i in range(1,self.number_frame_casting+1):
                  self.image_casting.append(pygame.image.load(BLUE_NEC_CASTING_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha()) 
                  self.image_casting[i-1] = pygame.transform.scale(self.image_casting[i-1],vec(self.image_casting[i-1].get_size())*BLUE_NEC_RESIZE_FACTOR)
            self.anim_total_time_c = BLUE_NEC_ANIMATION_CASTING_TOTAL_TIME  # in ms
            self.time_per_frame_c = self.anim_total_time_a/self.number_frame_casting # in ms
            self.casting_frame = 1


            self.number_frame_stun = BLUE_NEC_STUN_NUMBER_FRAME
            self.image_stun = []
            for i in range(1,self.number_frame_stun+1):
                  self.image_stun.append(pygame.image.load(BLUE_NEC_STUN_IMAGE_PATH+str(i)+".png").convert_alpha()) 
                  self.image_stun[i-1] = pygame.transform.scale(self.image_stun[i-1],vec(self.image_stun[i-1].get_size())*BLUE_NEC_RESIZE_FACTOR)  
            self.time_per_frame_s = BLUE_NEC_STUN_TIME_PER_FRAME

            self.dead_body_tag = DEAD_BLUE_NEC_TAG

class Dragon_data():
      def __init__(self):
            self.name = "Dragon"

            self.hp_max = DRAGON_HP_MAX
            self.damage = DRAGON_DAMAGE
            self.velocity = DRAGON_VELOCITY # pixel by ms
            self.gold_earning = DRAGON_GOLD_EARNING

            self.static_image = pygame.image.load(DRAGON_TRANSITION_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*DRAGON_RESIZE_FACTOR)             
            self.current_image = self.static_image
            self.image_size = vec(self.static_image.get_size())

            self.image_offset = DRAGON_OFFSET
            self.centor_vector = DRAGON_CENTER_VECTOR
            self.hitbox_factor = DRAGON_HITBOX_FACTOR

            self.number_frame_walking = DRAGON_NUMBER_FRAME_WALKING
            self.image_walking = []
            for i in range(1,self.number_frame_walking+1):
                  self.image_walking.append(pygame.image.load(DRAGON_WALKING_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())  
                  self.image_walking[i-1] = pygame.transform.scale(self.image_walking[i-1],vec(self.image_walking[i-1].get_size())*DRAGON_RESIZE_FACTOR)
                  self.image_walking[i-1] = pygame.transform.flip(self.image_walking[i-1], True, False)
            self.anim_total_time_w = DRAGON_ANIMATION_WALKING_TOTAL_TIME  # in ms
            self.time_per_frame_w = self.anim_total_time_w/self.number_frame_walking # in ms
            self.stop_walking_frame = DRAGON_STOP_WALKING_FRAME

            # self.number_frame_transition = DRAGON_NUMBER_FRAME_TRANSITION
            # self.image_transition = []
            # for i in range(1,self.number_frame_transition+1):
            #       self.image_transition.append(pygame.image.load(DRAGON_TRANSITION_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha()) 
            #       self.image_transition[i-1] = pygame.transform.scale(self.image_transition[i-1],vec(self.image_transition[i-1].get_size())*DRAGON_RESIZE_FACTOR)
            # self.anim_total_time_t = DRAGON_ANIMATION_TRANSITION_TOTAL_TIME  # in ms
            # self.time_per_frame_t = self.anim_total_time_t/self.number_frame_transition # in ms

            # self.number_frame_attacking = DRAGON_NUMBER_FRAME_ATTACKING 
            # self.image_attacking = []
            # for i in range(1,self.number_frame_attacking+1):
            #       self.image_attacking.append(pygame.image.load(DRAGON_ATTACKING_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha()) 
            #       self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*DRAGON_RESIZE_FACTOR)
            # self.anim_total_time_a = DRAGON_ANIMATION_ATTACKING_TOTAL_TIME  # in ms
            # self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms
            # self.hitting_frame = DRAGON_HITTING_FRAME -1

            # self.dead_body_tag = DEAD_DRAGON_TAG

class Ennemy(pygame.sprite.Sprite):
      def __init__(self,x,y,rand_offset):
            self.hp = self.my_data.hp_max

            self.velocity = self.my_data.velocity

            self.current_image = self.my_data.static_image

            self.image_size = self.my_data.image_size

            self.posX = x + self.my_data.image_offset[0]     
            self.posY = y + self.my_data.image_offset[1]   
            self.center = vec(self.posX+self.my_data.centor_vector[0]*self.image_size[0],self.posY+self.my_data.centor_vector[0]*self.image_size[1]) 
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
                                                self.detected_ennemies[i].hp -= self.my_data.damage
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


class Necromancer(Ennemy,pygame.sprite.Sprite):
      def __init__(self):
            self.cast_frame = 0
            self.rez_done = False
            self.rez_timer = self.my_data.rez_cd*2
            self.detected_bodies = None
            self.image_offset = self.my_data.image_offset

            self.range_hitbox = Range_Hitbox(self,self.rect.w,self.rect.h,self.my_data.rez_radius,circular=True)

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
                                          self.detected_ennemies[i].hp -= self.my_data.damage

                        self.current_image = self.my_data.image_attacking[self.attack_frame]
                              
                  else:
                        self.attacking = False

      def rez_dead_bodies(self,game):
            self.rez_timer += game.timestep
            if (not(self.stunned) and (self.rez_timer>self.my_data.rez_cd)):
                  self.detected_bodies = pygame.sprite.spritecollide(self.range_hitbox, game.all_dead_bodies.all_rezable_bodies, False, pygame.sprite.collide_circle)
                  if self.detected_bodies:
                        game.all_dead_bodies.all_rezable_bodies.remove(self.detected_bodies[0])

            if self.detected_bodies:
                  self.casting = True
                  self.my_timer += game.timestep
                  self.rez_timer = 0.0

                  if self.my_timer>self.my_data.time_per_frame_c:
                        self.cast_frame += 1
                        self.my_timer = 0.0
                  if (self.cast_frame<self.my_data.number_frame_casting):
                        if (self.cast_frame==self.my_data.casting_frame):
                              #rezing
                              pass
                  
                        self.current_image = self.my_data.image_casting[self.cast_frame]

                  else:
                        pygame.sprite.Sprite.kill(self.detected_bodies[0])
                        self.detected_bodies = None
                        self.casting = False
                        self.current_image = self.my_data.image_casting[self.cast_frame-1]

            else:
                  self.casting = False            

class Blue_Necromancer(Necromancer,pygame.sprite.Sprite):
      def __init__(self,all_e,x,y,rand_offset):
            pygame.sprite.Sprite.__init__(self)
 
            self.my_data = all_e.blue_nec_data

            Ennemy.__init__(self,x,y,rand_offset)
            Necromancer.__init__(self)

      def use_power(self,game):
            self.rez_dead_bodies(game)

class Goblin(Ennemy,pygame.sprite.Sprite):
      def __init__(self,all_e,x,y,rand_offset):
            pygame.sprite.Sprite.__init__(self)
 
            self.my_data = all_e.goblin_data

            Ennemy.__init__(self,x,y,rand_offset)

 
class Ogre(Ennemy,pygame.sprite.Sprite):
      def __init__(self,all_e,x,y,rand_offset):
            pygame.sprite.Sprite.__init__(self)
 
            self.my_data = all_e.ogre_data

            Ennemy.__init__(self,x,y,rand_offset)


class Dragon(Ennemy,pygame.sprite.Sprite):
      def __init__(self,all_e,x,y,rand_offset):
            pygame.sprite.Sprite.__init__(self)
 
            self.my_data = all_e.dragon_data

            Ennemy.__init__(self,x,y,rand_offset)

      def attack(self,game):
            pass

      def die(self,game):
            if (self.hp<=0):
                  game.gold.gold_gain(game,self,self.my_data.gold_earning)
                  pygame.sprite.Sprite.kill(self)
