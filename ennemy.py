import pygame
from utilitaries import *

class Ennemy(pygame.sprite.Sprite):
      def __init__(self,x,y):
            pass

      def move(self,game):           
            pass

      def die(self):
            if (self.hp<=0):
                  pygame.sprite.Sprite.kill(self)

      def render(self):
            window.blit(self.current_image, (self.posX, self.posY)) 


class Gobelin(Ennemy,pygame.sprite.Sprite):
      def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
 
            self.static_image = pygame.image.load(GOBELIN_TRANSITION_IMAGE_PATH+"001.png").convert_alpha()
            self.current_image = self.static_image

            self.hp_max = GOBELIN_HP_MAX
            self.hp = self.hp_max
            self.damage = GOBELIN_DAMAGE

            self.posX = x     
            self.posY = y     
            self.velocity = GOBELIN_VELOCITY # pixel by ms
            self.moving = False

            self.number_frame_walking = GOBELIN_NUMBER_FRAME_WALKING
            self.image_walking = []
            for i in range(1,self.number_frame_walking+1):
                  self.image_walking.append(pygame.image.load(GOBELIN_WALKING_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha())   
            self.move_frame = 0
            self.anim_total_time_w = GOBELIN_ANIMATION_WALKING_TOTAL_TIME  # in ms
            self.time_per_frame_w = self.anim_total_time_w/self.number_frame_walking # in ms

            self.my_timer = 0

            self.rect = self.current_image.get_rect()
            self.radius = GOBELIN_HITBOX_FACTOR*(self.rect.width+self.rect.height)/4.0
            self.rect.x = self.posX + (1-GOBELIN_HITBOX_FACTOR)*self.rect.width
            self.rect.y = self.posY + (1-GOBELIN_HITBOX_FACTOR)*self.rect.height
            self.rect.width *= GOBELIN_HITBOX_FACTOR
            self.rect.height *= GOBELIN_HITBOX_FACTOR

            self.ready_to_attack = False
            self.attacking = False
            self.damage_dealt = False

            self.number_frame_transition = GOBELIN_NUMBER_FRAME_TRANSITION
            self.image_transition = []
            for i in range(1,self.number_frame_transition+1):
                  self.image_transition.append(pygame.image.load(GOBELIN_TRANSITION_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha()) 
            self.transition_frame = 0      
            self.anim_total_time_t = GOBELIN_ANIMATION_TRANSITION_TOTAL_TIME  # in ms
            self.time_per_frame_t = self.anim_total_time_t/self.number_frame_transition # in ms

            self.number_frame_attacking = GOBELIN_NUMBER_FRAME_ATTACKING 
            self.image_attacking = []
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(GOBELIN_ATTACKING_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha()) 
            self.attack_frame = 0
            self.anim_total_time_a = GOBELIN_ANIMATION_ATTACKING_TOTAL_TIME  # in ms
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms
            self.hitting_frame = GOBELIN_HITTING_FRAME -1

      def move(self,game):
            if self.attacking:
                  self.moving = False                  
            else:
                  self.moving = True
                  self.ready_to_attack = False
                  self.posX += self.velocity * game.timestep
                  self.rect.x = self.posX

                  self.my_timer += game.timestep
                  if self.my_timer>self.time_per_frame_w:
                        self.move_frame += 1
                        self.move_frame = self.move_frame%self.number_frame_walking
                        self.my_timer = 0.0
                                    
                  self.current_image= self.image_walking[self.move_frame]

      def attack(self,game):
            self.detected_towers = pygame.sprite.spritecollide(self, game.all_towers, False)
            if self.detected_towers:
                  self.attacking = True
                  self.my_timer += game.timestep

                  if not self.ready_to_attack:
                        if (self.move_frame != (GOBELIN_STOP_WALKING_FRAME-1)):
                              if self.my_timer>self.time_per_frame_w:
                                    self.move_frame += 1
                                    self.move_frame = self.move_frame%self.number_frame_walking
                                    self.my_timer = 0.0   
                              self.current_image = self.image_walking[self.move_frame]
                        else:
                              if self.my_timer>self.time_per_frame_t:
                                    self.transition_frame += 1
                                    self.my_timer = 0.0  
                              if (self.transition_frame==self.number_frame_transition-1):
                                    self.ready_to_attack = True   
                              self.current_image = self.image_transition[self.transition_frame]                                                
                  else:
                        if self.my_timer>self.time_per_frame_a:
                              self.attack_frame += 1
                              self.attack_frame = self.attack_frame%self.number_frame_attacking
                              self.my_timer = 0.0
                        self.current_image = self.image_attacking[self.attack_frame]
                        if (self.attack_frame==self.hitting_frame):
                              if not self.damage_dealt:
                                    for i in range (len(self.detected_towers)):
                                          self.detected_towers[i].hp -= self.damage
                                    self.damage_dealt = True 
                        else:
                              self.damage_dealt = False
                                                     
            else:
                  self.attacking = False


 
 
