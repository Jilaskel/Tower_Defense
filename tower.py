import pygame
from utilitaries import *
from projectile import *

class Tower(pygame.sprite.Sprite):
      def __init__(self,game,x,y):
            pass

      def check_ennemies(self,game):
            pass

      def render(self):
            pass  


class Ballista(Tower,pygame.sprite.Sprite):
      def __init__(self,game,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.images_path = BALLISTA_ATTACK_IMAGE_PATH
            self.static_image = pygame.image.load(self.images_path+"0001.png").convert_alpha()    
            self.current_image = self.static_image    
            self.posX = x
            self.posY = y
            self.number_frame_attacking = BALLISTA_NUMBER_FRAME_ATTACKING

            self.firing_period = BALLISTA_FIRING_PERIOD #in ms
            self.my_timer = 0

            self.attacking = True
            self.attack_finished = True

            self.image_attacking = []
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(self.images_path+str(i).zfill(4)+".png").convert_alpha())   
            self.firing_frame = BALLISTA_FIRING_FRAME
            self.anim_frame = 0
            self.time_per_frame = self.firing_period/self.number_frame_attacking # in ms

            self.detected_ennemies = False
            self.my_target = []

            self.rect = self.current_image.get_rect()
            self.range = BALLISTA_RANGE*(self.rect.width+self.rect.height)/2.0
            self.rect.x = self.posX - self.range
            self.rect.y = self.posY
            self.rect.w = self.range 

      def check_ennemies(self,game):
            self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False)
            if (self.detected_ennemies):
                  self.attacking = True
                  if not(self.my_target in self.detected_ennemies):
                        self.my_target = self.detected_ennemies[0]
            else:
                  self.attacking = False

      def attack_and_reload(self,game):
            if (self.attacking):
                  self.attack_finished = False
                  self.my_timer += game.timestep
                  if self.my_timer>self.time_per_frame:
                        self.anim_frame += 1
                        self.anim_frame = self.anim_frame%self.number_frame_attacking
                        self.my_timer = 0.0
                        if (self.anim_frame==self.firing_frame):
                              game.all_projectiles.add(Bolt(self.posX,self.posY,self.my_target))
            else:
                  if not(self.attack_finished):
                        self.my_timer += game.timestep
                        if self.my_timer>self.time_per_frame:
                              self.anim_frame += 1
                              self.anim_frame = self.anim_frame%self.number_frame_attacking
                              self.my_timer = 0.0
                              if (self.anim_frame==0):
                                    self.attack_finished = True     

            self.current_image= self.image_attacking[self.anim_frame]


      def render(self):
            window.blit(self.current_image, (self.posX, self.posY))  
 

class Basic_tower(Tower,pygame.sprite.Sprite):
      def __init__(self,game,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.static_image = pygame.image.load(BASIC_TOWER_IMAGE_PATH).convert_alpha()    
            self.current_image = self.static_image  
            self.posX = x
            self.posY = y

            self.firing_period = BASIC_TOWER_FIRING_PERIOD
            self.my_timer = self.firing_period*2

            self.attacking = True
            self.attack_finished = True

            self.detected_ennemies = False
            self.my_target = []
            
            self.rect = self.current_image.get_rect()
            self.range = BASIC_TOWER_RANGE * (self.rect.width+self.rect.height)/2.0
            self.radius = self.range
            self.rect.x = self.posX
            self.rect.y = self.posY

      def check_ennemies(self,game):
            self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False, pygame.sprite.collide_circle)
            if (self.detected_ennemies):
                  self.attacking = True
                  if not(self.my_target in self.detected_ennemies):
                        self.my_target = self.detected_ennemies[0]
            else:
                  self.attacking = False

      def attack_and_reload(self,game):
            if (self.attacking):
                  self.attack_finished = False
                  self.my_timer += game.timestep
                  if self.my_timer>self.firing_period:
                        self.my_timer = 0.0
                        game.all_projectiles.add(Bolt(self.posX,self.posY,self.my_target))
            else:
                  if not(self.attack_finished):
                        self.my_timer += game.timestep
                        if self.my_timer>self.firing_period:
                              self.my_timer = 0.0
                              self.attack_finished = True  

      def render(self):
            window.blit(self.current_image, (self.posX, self.posY))  