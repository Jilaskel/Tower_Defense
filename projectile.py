import pygame
from utilitaries import *
from impact import * 
from functions import *
from numpy import sqrt
import numpy as np
import math

class All_projectiles(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self)  

            self.arcane_bolt_data = Arcane_bolt_data()
            
            self.bolt_data = Bolt_data()

      def add_arcane_bolt(self,x,y,target):
            self.add(Arcane_bolt(self,x,y,target))

      def add_bolt(self,x,y,target):
            self.add(Bolt(self,x,y,target))

class Arcane_bolt_data():
      def __init__(self):

            self.damage = ARCANE_BOLT_DAMAGE
            self.velocity = ARCANE_BOLT_VELOCITY  # pixel by ms
            self.ratio_for_impact = ARCANE_BOLT_RATIO_FOR_IMPACT

            self.static_image = pygame.image.load(ARCANE_BOLT_IMAGE_PATH).convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ARCANE_BOLT_RESIZE_FACTOR)  
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(-1,0)
            self.offset = vec(ARCANE_BOLT_CENTOR_VECTOR[0]*self.image_size[0],ARCANE_BOLT_CENTOR_VECTOR[1]*self.image_size[1])

class Bolt_data():
      def __init__(self):      

            self.damage = BOLT_DAMAGE
            self.velocity = BOLT_VELOCITY  # pixel by ms
            self.ratio_for_impact = BOLT_RATIO_FOR_IMPACT

            self.static_image = pygame.image.load(BOLT_IMAGE_PATH).convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*BOLT_RESIZE_FACTOR)        
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(-1,0)
            self.offset = vec(BOLT_CENTOR_VECTOR[0]*self.image_size[0],BOLT_CENTOR_VECTOR[1]*self.image_size[1])



class Projectile(pygame.sprite.Sprite):
      def __init__(self,x,y): 
            pass

      def move(self,game):
            if (pygame.sprite.Sprite.alive(self.target)):
                  self.direction = (self.target.rect.center[0] - self.center[0], self.target.rect.center[1] - self.center[1])   
                  self.direction /= sqrt(self.direction[0]**2+self.direction[1]**2)     
            self.posX += self.my_data.velocity * game.timestep * self.direction[0]
            self.posY += self.my_data.velocity * game.timestep * self.direction[1]
            self.rect.x = self.posX
            self.rect.y = self.posY
            self.center += self.my_data.velocity * game.timestep * self.direction
            self.moving = True
            self.rotate()

            # self.rendering_layer = compute_rendering_layer_number(self)
            self.rendering_layer = TOTAL_NUMBER_RENDERING_LAYER-3

      def rotate(self):
            scalar_product = self.my_data.initial_direction[0]*self.direction[0]+self.my_data.initial_direction[1]*self.direction[1]
            if (self.direction[1]<self.my_data.initial_direction[1]):
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
            self.current_image = pygame.transform.rotate(self.my_data.static_image, angle)

      def check_impact(self,game):
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False,pygame.sprite.collide_rect_ratio(self.my_data.ratio_for_impact))
            if self.hit_ennemies:
                  pygame.sprite.Sprite.kill(self)
                  for i in range (len(self.hit_ennemies)):
                        self.hit_ennemies[i].hp -= self.my_data.damage

      def render(self,rendering_layer):
            if self.rendering_layer==rendering_layer:
                  window.blit(self.current_image, (self.posX, self.posY))   

class Arcane_bolt(Projectile,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.arcane_bolt_data

            self.damage = self.my_data.damage
      
            self.current_image = self.my_data.static_image
            self.image_size = self.my_data.image_size

            self.posX = x-self.my_data.offset[0]    
            self.posY = y-self.my_data.offset[1]    
            self.rendering_layer = compute_rendering_layer_number(self)

            self.direction = vec(0,0)
            self.moving = False  

            self.target = target

            self.rect = self.current_image.get_rect()
            self.rect.x = self.posX
            self.rect.y = self.posY

            self.center = vec(self.posX+ARCANE_BOLT_CENTOR_VECTOR[0]*self.image_size[0],self.posY+ARCANE_BOLT_CENTOR_VECTOR[1]*self.image_size[1])

      def check_impact(self,game):
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False,pygame.sprite.collide_rect_ratio(self.my_data.ratio_for_impact))
            if self.hit_ennemies:
                  pygame.sprite.Sprite.kill(self)
                  game.all_impacts.add_arcane_impact(self)


class Bolt(Projectile,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.bolt_data

            self.damage = self.my_data.damage

            self.current_image = self.my_data.static_image
            self.image_size = self.my_data.image_size

            self.posX = x-self.my_data.offset[0]    
            self.posY = y-self.my_data.offset[1]    
            self.rendering_layer = compute_rendering_layer_number(self)

            self.direction = vec(0,0)
            self.moving = False
  
            self.target = target

            self.rect = self.current_image.get_rect()
            self.rect.x = self.posX
            self.rect.y = self.posY

            self.center = vec(self.posX+BOLT_CENTOR_VECTOR[0]*self.image_size[0],self.posY+BOLT_CENTOR_VECTOR[1]*self.image_size[1])


                        


 
