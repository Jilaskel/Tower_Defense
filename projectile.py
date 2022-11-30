import pygame
from utilitaries import *
from numpy import sqrt
import numpy as np
import math

class Projectile(pygame.sprite.Sprite):
      def __init__(self,x,y):
            super().__init__()   
            self.posX = x     # game.background.bush_width
            self.posY = y     # 135
            self.velocity = 0.2 # pixel by ms

      def move(self,game):           
            self.posX += self.velocity * game.timestep

      def render(self,game):
            window.blit(self.current_image, (self.posX, self.posY))  

      def rotate(self):
            scalar_product = self.initial_direction[0]*self.direction[0]+self.initial_direction[1]*self.direction[1]
            if (self.direction[1]<self.initial_direction[1]):
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
            self.current_image = pygame.transform.rotate(self.inital_image, angle)
            #self.rect = self.current_image.get_rect(center = self.current_image.get_rect(topleft = (self.posX,self.posY)).center)

class Bolt(Projectile,pygame.sprite.Sprite):
      def __init__(self,x,y,target):
            pygame.sprite.Sprite.__init__(self)
            self.images_path = "Assets/Tower/Baliste/"
            self.inital_image = pygame.image.load(self.images_path+"/CarreauBaliste.png").convert_alpha()
            self.current_image = self.inital_image
            self.initial_direction = vec(-1,0)

            self.damage = 5.0

            self.posX = x     
            self.posY = y     
            self.direction = vec(0,0)
            self.velocity = 2.0 #0.6  # pixel by ms
            self.moving = False
            self.rect = self.current_image.get_rect()

            self.target = target
            self.ratio_for_impact = 0.25

            self.rect.x = self.posX
            self.rect.y = self.posY

      def move(self,game):
            if (pygame.sprite.Sprite.alive(self.target)):
                  self.direction = (self.target.posX - self.posX, self.target.posY - self.posY)   
                  self.direction /= sqrt(self.direction[0]**2+self.direction[1]**2)     
            self.posX += self.velocity * game.timestep * self.direction[0]
            self.posY += self.velocity * game.timestep * self.direction[1]
            self.rect.x = self.posX
            self.rect.y = self.posY
            self.moving = True
            self.rotate()

      def check_impact(self,game):
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False,pygame.sprite.collide_rect_ratio(self.ratio_for_impact))
            if self.hit_ennemies:
                  pygame.sprite.Sprite.kill(self)
                  for i in range (len(self.hit_ennemies)):
                        self.hit_ennemies[i].hp -= self.damage



      def render(self,game):
            window.blit(self.current_image, (self.posX, self.posY))  
 
