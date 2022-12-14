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
            self.static_image = pygame.transform.scale(self.static_image,(GOBELIN_SIZE[0],GOBELIN_SIZE[1]))        
            self.current_image = self.static_image

            self.hp_max = GOBELIN_HP_MAX
            self.hp = self.hp_max
            self.damage = GOBELIN_DAMAGE

            self.posX = x + GOBELIN_OFFSET[0]     
            self.posY = y + GOBELIN_OFFSET[1]   
            self.center = vec(self.posX+GOBELIN_CENTER_VECTOR[0]*GOBELIN_SIZE[0],self.posY+GOBELIN_CENTER_VECTOR[0]*GOBELIN_SIZE[1]) 
            self.velocity = GOBELIN_VELOCITY # pixel by ms
            self.moving = False

            self.number_frame_walking = GOBELIN_NUMBER_FRAME_WALKING
            self.image_walking = []
            for i in range(1,self.number_frame_walking+1):
                  self.image_walking.append(pygame.image.load(GOBELIN_WALKING_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha())  
                  self.image_walking[i-1] = pygame.transform.scale(self.image_walking[i-1],(GOBELIN_SIZE[0],GOBELIN_SIZE[1]))        

            self.move_frame = 0
            self.anim_total_time_w = GOBELIN_ANIMATION_WALKING_TOTAL_TIME  # in ms
            self.time_per_frame_w = self.anim_total_time_w/self.number_frame_walking # in ms

            self.my_timer = 0

            self.hitbox_left = x
            self.hitbox_top = y
            #self.rect = self.current_image.get_rect()
            self.radius = GOBELIN_HITBOX_FACTOR*(BACKGROUND_SQUARE_SIDE*2)/4.0
            self.hitbox_left = self.hitbox_left + (1-GOBELIN_HITBOX_FACTOR)*BACKGROUND_SQUARE_SIDE*0.5
            self.hitbox_top = self.hitbox_top + (1-GOBELIN_HITBOX_FACTOR)*BACKGROUND_SQUARE_SIDE*0.5
            self.hitbox_width = BACKGROUND_SQUARE_SIDE*GOBELIN_HITBOX_FACTOR
            self.hitbox_height = BACKGROUND_SQUARE_SIDE*GOBELIN_HITBOX_FACTOR
            self.rect = pygame.Rect(self.hitbox_left,self.hitbox_top,self.hitbox_width,self.hitbox_height)

            self.ready_to_attack = False
            self.attacking = False
            self.damage_dealt = False

            self.number_frame_transition = GOBELIN_NUMBER_FRAME_TRANSITION
            self.image_transition = []
            for i in range(1,self.number_frame_transition+1):
                  self.image_transition.append(pygame.image.load(GOBELIN_TRANSITION_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha()) 
                  self.image_transition[i-1] = pygame.transform.scale(self.image_transition[i-1],(GOBELIN_SIZE[0],GOBELIN_SIZE[1]))
            self.transition_frame = 0      
            self.anim_total_time_t = GOBELIN_ANIMATION_TRANSITION_TOTAL_TIME  # in ms
            self.time_per_frame_t = self.anim_total_time_t/self.number_frame_transition # in ms

            self.number_frame_attacking = GOBELIN_NUMBER_FRAME_ATTACKING 
            self.image_attacking = []
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(GOBELIN_ATTACKING_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha()) 
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],(GOBELIN_SIZE[0],GOBELIN_SIZE[1]))
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
                  dx = self.velocity * game.timestep
                  self.posX += dx
                  self.center[0] += dx
                  self.hitbox_left += dx
                  self.rect.x = self.hitbox_left

                  self.my_timer += game.timestep
                  if self.my_timer>self.time_per_frame_w:
                        self.move_frame += 1
                        self.move_frame = self.move_frame%self.number_frame_walking
                        self.my_timer = 0.0
                                    
                  self.current_image= self.image_walking[self.move_frame]

      def attack(self,game):
            self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_towers, False)
            if not self.detected_ennemies:
                  self.detected_ennemies = pygame.sprite.spritecollide(self, game.base.all_gates, False)

            if self.detected_ennemies:
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
                                    for i in range (len(self.detected_ennemies)):
                                          self.detected_ennemies[i].hp -= self.damage
                                    self.damage_dealt = True 
                        else:
                              self.damage_dealt = False
                                                     
            else:
                  self.attacking = False


 
 
class OGRE(Ennemy,pygame.sprite.Sprite):
      def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
 
            self.static_image = pygame.image.load(OGRE_TRANSITION_IMAGE_PATH+"001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,(OGRE_SIZE[0],OGRE_SIZE[1]))        
            self.current_image = self.static_image

            self.hp_max = OGRE_HP_MAX
            self.hp = self.hp_max
            self.damage = OGRE_DAMAGE

            self.posX = x + OGRE_OFFSET[0]     
            self.posY = y + OGRE_OFFSET[1]   
            self.center = vec(self.posX+OGRE_CENTER_VECTOR[0]*OGRE_SIZE[0],self.posY+OGRE_CENTER_VECTOR[0]*OGRE_SIZE[1]) 
            self.velocity = OGRE_VELOCITY # pixel by ms
            self.moving = False

            self.number_frame_walking = OGRE_NUMBER_FRAME_WALKING
            self.image_walking = []
            for i in range(1,self.number_frame_walking+1):
                  self.image_walking.append(pygame.image.load(OGRE_WALKING_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha())  
                  self.image_walking[i-1] = pygame.transform.scale(self.image_walking[i-1],(OGRE_SIZE[0],OGRE_SIZE[1]))        

            self.move_frame = 0
            self.anim_total_time_w = OGRE_ANIMATION_WALKING_TOTAL_TIME  # in ms
            self.time_per_frame_w = self.anim_total_time_w/self.number_frame_walking # in ms

            self.my_timer = 0

            self.hitbox_left = x
            self.hitbox_top = y
            #self.rect = self.current_image.get_rect()
            self.radius = OGRE_HITBOX_FACTOR*(BACKGROUND_SQUARE_SIDE*2)/4.0
            self.hitbox_left = self.hitbox_left + (1-OGRE_HITBOX_FACTOR)*BACKGROUND_SQUARE_SIDE*0.5
            self.hitbox_top = self.hitbox_top + (1-OGRE_HITBOX_FACTOR)*BACKGROUND_SQUARE_SIDE*0.5
            self.hitbox_width = BACKGROUND_SQUARE_SIDE*OGRE_HITBOX_FACTOR
            self.hitbox_height = BACKGROUND_SQUARE_SIDE*OGRE_HITBOX_FACTOR
            self.rect = pygame.Rect(self.hitbox_left,self.hitbox_top,self.hitbox_width,self.hitbox_height)

            self.ready_to_attack = False
            self.attacking = False
            self.damage_dealt = False

            self.number_frame_transition = OGRE_NUMBER_FRAME_TRANSITION
            self.image_transition = []
            for i in range(1,self.number_frame_transition+1):
                  self.image_transition.append(pygame.image.load(OGRE_TRANSITION_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha()) 
                  self.image_transition[i-1] = pygame.transform.scale(self.image_transition[i-1],(OGRE_SIZE[0],OGRE_SIZE[1]))
            self.transition_frame = 0      
            self.anim_total_time_t = OGRE_ANIMATION_TRANSITION_TOTAL_TIME  # in ms
            self.time_per_frame_t = self.anim_total_time_t/self.number_frame_transition # in ms

            self.number_frame_attacking = OGRE_NUMBER_FRAME_ATTACKING 
            self.image_attacking = []
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(OGRE_ATTACKING_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha()) 
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],(OGRE_SIZE[0],OGRE_SIZE[1]))
            self.attack_frame = 0
            self.anim_total_time_a = OGRE_ANIMATION_ATTACKING_TOTAL_TIME  # in ms
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms
            self.hitting_frame = OGRE_HITTING_FRAME -1

      def move(self,game):
            if self.attacking:
                  self.moving = False                  
            else:
                  self.moving = True
                  self.ready_to_attack = False
                  dx = self.velocity * game.timestep
                  self.posX += dx
                  self.center[0] += dx
                  self.hitbox_left += dx
                  self.rect.x = self.hitbox_left

                  self.my_timer += game.timestep
                  if self.my_timer>self.time_per_frame_w:
                        self.move_frame += 1
                        self.move_frame = self.move_frame%self.number_frame_walking
                        self.my_timer = 0.0
                                    
                  self.current_image= self.image_walking[self.move_frame]

      def attack(self,game):
            self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_towers, False)
            if not self.detected_ennemies:
                  self.detected_ennemies = pygame.sprite.spritecollide(self, game.base.all_gates, False)

            if self.detected_ennemies:
                  self.attacking = True
                  self.my_timer += game.timestep

                  if not self.ready_to_attack:
                        if (self.move_frame != (OGRE_STOP_WALKING_FRAME-1)):
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
                                    for i in range (len(self.detected_ennemies)):
                                          self.detected_ennemies[i].hp -= self.damage
                                    self.damage_dealt = True 
                        else:
                              self.damage_dealt = False
                                                     
            else:
                  self.attacking = False