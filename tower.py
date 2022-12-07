import pygame
from utilitaries import *
from projectile import *

class Tower(pygame.sprite.Sprite):
      def __init__(self,game,x,y):
            pass

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

      def render(self):
            window.blit(self.current_image, (self.posX, self.posY))


class Range_Hitbox(pygame.sprite.Sprite):
      def __init__(self,tower,circular):
            super().__init__()
            self.range = tower.range
            if circular:
                  self.circular = True
                  self.rect = pygame.Rect(tower.posX,tower.posY,tower.rect.width,tower.rect.height)
                  self.radius = self.range
                  self.posX = tower.posX+tower.rect.width*0.5 - self.radius
                  self.posY = tower.posY+tower.rect.height*0.5 - self.radius

            else:
                  self.circular = False
                  self.rect = pygame.Rect(tower.posX,tower.posY,tower.rect.width,tower.rect.height)   
                  self.posX = tower.posX              
                  self.posY = tower.posY              

      def  load_and_resize_image(self):
            if self.circular:
                  self.image = pygame.image.load(TOWER_CIRCLE_RANGE_IMAGE_PATH).convert_alpha()
                  self.image.set_alpha(TOWER_CIRCLE_RANGE_IMAGE_ALPHA)
                  self.image = pygame.transform.scale(self.image,(self.range*2,self.range*2))
            else:
                  self.image = pygame.image.load(TOWER_RECT_RANGE_IMAGE_PATH).convert_alpha()
                  self.image.set_alpha(TOWER_RECT_RANGE_IMAGE_ALPHA) 
                  self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.h))

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
            self.rect.x = self.posX
            self.rect.y = self.posY

            self.range = BALLISTA_RANGE*(self.rect.width+self.rect.height)/2.0
            self.range_hitbox = Range_Hitbox(self,circular=False)
            self.range_hitbox.rect.x = self.posX - self.range
            self.range_hitbox.posX = self.range_hitbox.rect.x
            self.range_hitbox.rect.w = self.range 
            self.range_hitbox.load_and_resize_image()


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
            self.rect.x = self.posX
            self.rect.y = self.posY

            self.range = BASIC_TOWER_RANGE * (self.rect.width+self.rect.height)/4.0
            self.range_hitbox = Range_Hitbox(self,circular=True)
            self.range_hitbox.load_and_resize_image()

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
                              self.my_timer = 2*self.firing_period
                              self.attack_finished = True  
