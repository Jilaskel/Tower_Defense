import pygame
from utilitaries import *

class Tower(pygame.sprite.Sprite):
      def __init__(self,x,y):
            super().__init__()
            self.images_path = "Assets/Tower/Baliste/AnimAttack/"
            self.current_image = pygame.image.load(self.images_path+"0001.png").convert_alpha()    
            self.posX = x
            self.posY = y
            self.detection_radius = 100.0
            self.detected_ennemies = False
            self.rect = self.current_image.get_rect()
            self.range = 1.0
            self.radius = (self.rect.width+self.rect.height)/2.0 * self.range
            self.rect.x = self.posX
            self.rect.y = self.posY

      def check_ennemies(self,game):
            #self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False)
            self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False, pygame.sprite.collide_circle)
            if (self.detected_ennemies):
                  print("Attack!")
            else:
                  print("Nothing")

      def render(self,game):
            window.blit(self.current_image, (self.posX, self.posY))  


class Ballista(Tower,pygame.sprite.Sprite):
      def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.images_path = "Assets/Tower/Baliste/AnimAttack/"
            self.static_image = pygame.image.load(self.images_path+"0001.png").convert_alpha()    
            self.current_image = self.static_image
            self.ammo_image = pygame.image.load("Assets/Tower/Baliste/CarreauBaliste.png").convert_alpha()    
            self.posX = x
            self.posY = y

            self.attacking = True
            self.number_frame_attacking = 15
            self.image_attacking = []
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(self.images_path+str(i).zfill(4)+".png").convert_alpha())   
            self.anim_frame = 0
            self.time_per_frame = 120 # in ms
            self.my_timer = 0
            self.attack_finished = True

            self.detected_ennemies = False
            self.rect = self.current_image.get_rect()
            self.range = 1.0
            self.radius = (self.rect.width+self.rect.height)/2.0 * self.range
            self.rect.x = self.posX
            self.rect.y = self.posY

      def check_ennemies(self,game):
            #self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False)
            self.detected_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False, pygame.sprite.collide_circle)
            if (self.detected_ennemies):
                  self.attacking = True
                  self.my_target = self.detected_ennemies[0]
                  print("Attack!")
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


      def render(self,game):
            window.blit(self.current_image, (self.posX, self.posY))  
 

