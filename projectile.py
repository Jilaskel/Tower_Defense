import pygame
from utilitaries import *
from impact import * 
from functions import *
from numpy import sqrt
import numpy as np
import math

class Projectile(pygame.sprite.Sprite):
      def __init__(self,x,y): 
            pass

      def move(self,game):
            if (pygame.sprite.Sprite.alive(self.target)):
                  self.direction = (self.target.rect.center[0] - self.center[0], self.target.rect.center[1] - self.center[1])   
                  self.direction /= sqrt(self.direction[0]**2+self.direction[1]**2)     
            self.posX += self.velocity * game.timestep * self.direction[0]
            self.posY += self.velocity * game.timestep * self.direction[1]
            self.rect.x = self.posX
            self.rect.y = self.posY
            self.center += self.velocity * game.timestep * self.direction
            self.moving = True
            self.rotate()

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
            self.current_image = pygame.transform.rotate(self.static_image, angle)

      def check_impact(self,game):
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False,pygame.sprite.collide_rect_ratio(self.ratio_for_impact))
            if self.hit_ennemies:
                  pygame.sprite.Sprite.kill(self)
                  for i in range (len(self.hit_ennemies)):
                        self.hit_ennemies[i].hp -= self.damage

      def render(self,rendering_layer):
            if self.rendering_layer==rendering_layer:
                  window.blit(self.current_image, (self.posX, self.posY))  
                  # window.blit(self.current_image, (self.posX-self.offset[0], self.posY-self.offset[1]))  

class Bolt(Projectile,pygame.sprite.Sprite):
      def __init__(self,x,y,target):
            pygame.sprite.Sprite.__init__(self)
            self.static_image = pygame.image.load(BOLT_IMAGE_PATH).convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*BOLT_RESIZE_FACTOR)        
            self.current_image = self.static_image
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(-1,0)
            self.offset = vec(BOLT_CENTOR_VECTOR[0]*self.image_size[0],BOLT_CENTOR_VECTOR[1]*self.image_size[1])

            self.damage = BOLT_DAMAGE

            self.posX = x-self.offset[0]    
            self.posY = y-self.offset[1]    
            self.rendering_layer = compute_rendering_layer_number(self)

            self.direction = vec(0,0)
            self.velocity = BOLT_VELOCITY  # pixel by ms
            self.moving = False
  

            self.target = target
            self.ratio_for_impact = BOLT_RATIO_FOR_IMPACT

            self.rect = self.current_image.get_rect()
            self.rect.x = self.posX
            self.rect.y = self.posY

            self.center = vec(self.posX+BOLT_CENTOR_VECTOR[0]*self.image_size[0],self.posY+BOLT_CENTOR_VECTOR[1]*self.image_size[1])

      def move(self,game):
            if (pygame.sprite.Sprite.alive(self.target)):
                  self.direction = (self.target.rect.center[0] - self.center[0], self.target.rect.center[1] - self.center[1])   
                  self.direction /= sqrt(self.direction[0]**2+self.direction[1]**2)     
            self.posX += self.velocity * game.timestep * self.direction[0]
            self.posY += self.velocity * game.timestep * self.direction[1]
            self.rect.x = self.posX
            self.rect.y = self.posY
            self.center += self.velocity * game.timestep * self.direction
            self.moving = True
            self.rotate()

                        
class Arcane_bolt(Projectile,pygame.sprite.Sprite):
      def __init__(self,x,y,target):
            pygame.sprite.Sprite.__init__(self)
            self.static_image = pygame.image.load(ARCANE_BOLT_IMAGE_PATH).convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ARCANE_BOLT_RESIZE_FACTOR)        
            self.current_image = self.static_image
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(-1,0)
            self.offset = vec(ARCANE_BOLT_CENTOR_VECTOR[0]*self.image_size[0],ARCANE_BOLT_CENTOR_VECTOR[1]*self.image_size[1])

            self.damage = ARCANE_BOLT_DAMAGE

            self.posX = x-self.offset[0]    
            self.posY = y-self.offset[1]    
            self.rendering_layer = compute_rendering_layer_number(self)

            self.direction = vec(0,0)
            self.velocity = ARCANE_BOLT_VELOCITY  # pixel by ms
            self.moving = False
  

            self.target = target
            self.ratio_for_impact = ARCANE_BOLT_RATIO_FOR_IMPACT

            self.rect = self.current_image.get_rect()
            self.rect.x = self.posX
            self.rect.y = self.posY

            self.center = vec(self.posX+ARCANE_BOLT_CENTOR_VECTOR[0]*self.image_size[0],self.posY+ARCANE_BOLT_CENTOR_VECTOR[1]*self.image_size[1])

      def check_impact(self,game):
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False,pygame.sprite.collide_rect_ratio(self.ratio_for_impact))
            if self.hit_ennemies:
                  pygame.sprite.Sprite.kill(self)
                  game.all_impacts.add(Arcane_impact(self))

 
