import pygame
from utilitaries import *
from impact import * 
from functions import *
from numpy import sqrt
import numpy as np
import math
import random

ARCANE_TOWER_BOLT_TAG = 1
FIRE_TOWER_BOLT_TAG = 2
LIGHTNING_TOWER_BOLT_TAG = 3
ICE_TOWER_BOLT_TAG = 4
BALLISTA_BOLT_TAG = 5
CATAPULT_BOLT_TAG = 6

class All_projectiles(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self)  

            self.arcane_bolt_data = Arcane_bolt_data()
            self.fire_bolt_data = Fire_bolt_data()
            
            self.bolt_data = Bolt_data()
            self.rock_data = Rock_data()

      def add_bolt(self,game,x,y,target,tag):
            if (tag==ARCANE_TOWER_BOLT_TAG):
                  self.add_arcane_bolt(game,x,y,target)
            elif (tag==FIRE_TOWER_BOLT_TAG):
                  self.add_fire_bolt(game,x,y,target)
            elif (tag==LIGHTNING_TOWER_BOLT_TAG):
                  self.add_arcane_bolt(game,x,y,target)
            elif (tag==ICE_TOWER_BOLT_TAG):
                  self.add_arcane_bolt(game,x,y,target)
            elif (tag==BALLISTA_BOLT_TAG):
                  self.add_ballista_bolt(game,x,y,target)
            elif (tag==CATAPULT_BOLT_TAG):
                  self.add_catapult_rock(game,x,y,target)

      def add_arcane_bolt(self,game,x,y,target):
            self.add(Arcane_bolt(self,x,y,target))
            game.all_mixers.projectile_mixer.arcane_proj_sound.play(maxtime=SOUND_ARCANE_PROJ_MAX_TIME)

      def add_fire_bolt(self,game,x,y,target):
            self.add(Fire_bolt(self,x,y,target))
            game.all_mixers.projectile_mixer.fire_proj_sound.play(maxtime=SOUND_FIRE_PROJ_MAX_TIME)

      def add_ballista_bolt(self,game,x,y,target):
            self.add(Bolt(self,x,y,target))
            random.choice(game.all_mixers.projectile_mixer.bolt_proj_list).play()

      def add_catapult_rock(self,game,x,y,target):
            self.add(Rock(self,x,y,target))

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

            self.impact_tag = ARCANE_TOWER_IMPACT_TAG

class Fire_bolt_data():
      def __init__(self):

            self.damage = FIRE_BOLT_DAMAGE
            self.velocity = FIRE_BOLT_VELOCITY  # pixel by ms
            self.ratio_for_impact = FIRE_BOLT_RATIO_FOR_IMPACT

            self.static_image = pygame.image.load(FIRE_BOLT_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*FIRE_BOLT_RESIZE_FACTOR)  
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(-1,0)
            self.offset = vec(FIRE_BOLT_CENTOR_VECTOR[0]*self.image_size[0],FIRE_BOLT_CENTOR_VECTOR[1]*self.image_size[1])

            self.number_frame = FIRE_BOLT_NUMBER_FRAME
            self.images = []
            for i in range(1,self.number_frame+1):
                  self.images.append(pygame.image.load(FIRE_BOLT_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())  
                  self.images[i-1] = pygame.transform.scale(self.images[i-1],vec(self.images[i-1].get_size())*FIRE_BOLT_RESIZE_FACTOR)
            self.anim_total_time = FIRE_BOLT_TOTAL_TIME  # in ms
            self.time_per_frame = self.anim_total_time/self.number_frame # in ms

            self.impact_tag = FIRE_TOWER_IMPACT_TAG

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

class Rock_data():
      def __init__(self):      

            self.damage = ROCK_DAMAGE
            self.velocity = ROCK_VELOCITY  # pixel by ms

            self.static_image = pygame.image.load(ROCK_IMAGE_PATH).convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ROCK_RESIZE_FACTOR)        
            self.image_size = vec(self.static_image.get_size())
            self.initial_direction = vec(-1,0)
            self.offset = vec(ROCK_CENTOR_VECTOR[0]*self.image_size[0],ROCK_CENTOR_VECTOR[1]*self.image_size[1])

            self.impact_tag = ROCK_IMPACT_TAG

class Projectile(pygame.sprite.Sprite):
      def __init__(self,x,y): 
            pass

      def move(self,game):
            if (pygame.sprite.Sprite.alive(self.target)):
                  self.my_target_center = self.target.rect.center
                  self.direction = (self.target.rect.center[0] - self.center[0], self.target.rect.center[1] - self.center[1])   
                  self.direction /= sqrt(self.direction[0]**2+self.direction[1]**2)     
            self.posX += self.my_data.velocity * game.timestep * self.direction[0]
            self.posY += self.my_data.velocity * game.timestep * self.direction[1]
            self.rect.x = self.posX
            self.rect.y = self.posY
            self.center += self.my_data.velocity * game.timestep * self.direction
            self.moving = True
            self.rotate(self.my_data.static_image)

            # self.rendering_layer = compute_rendering_layer_number(self)
            self.rendering_layer = TOTAL_NUMBER_RENDERING_LAYER-3

      def rotate(self,image):
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
            self.current_image = pygame.transform.rotate(image, angle)

      def check_impact(self,game):
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False,pygame.sprite.collide_rect_ratio(self.my_data.ratio_for_impact))
            if self.hit_ennemies:
                  pygame.sprite.Sprite.kill(self)
                  game.all_impacts.add_impact(game,self,self.my_data.impact_tag)
            else:
                  ## if ennemy is dead while projectile was travelling, distance is computed with last ennemy position 
                  distance = np.sqrt((self.my_target_center[0] - self.center[0])**2 + (self.my_target_center[1] - self.center[1])**2)
                  if (distance<0.1*BACKGROUND_SQUARE_SIDE):
                        pygame.sprite.Sprite.kill(self)
                        game.all_impacts.add_impact(game,self,self.my_data.impact_tag)  

      def render(self):
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

class Fire_bolt(Projectile,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.fire_bolt_data

            self.damage = self.my_data.damage
      
            self.current_image = self.my_data.static_image
            self.image_size = self.my_data.image_size

            self.current_frame = 0

            self.my_timer = 0

            self.posX = x-self.my_data.offset[0]    
            self.posY = y-self.my_data.offset[1]    
            self.rendering_layer = compute_rendering_layer_number(self)

            self.direction = vec(0,0)
            self.moving = False  

            self.target = target

            self.rect = self.current_image.get_rect()
            self.rect.x = self.posX
            self.rect.y = self.posY

            self.center = vec(self.posX+FIRE_BOLT_CENTOR_VECTOR[0]*self.image_size[0],self.posY+FIRE_BOLT_CENTOR_VECTOR[1]*self.image_size[1])
                    
      def move(self,game):
            if (pygame.sprite.Sprite.alive(self.target)):
                  self.my_target_center = self.target.rect.center
                  self.direction = (self.target.rect.center[0] - self.center[0], self.target.rect.center[1] - self.center[1])   
                  self.direction /= sqrt(self.direction[0]**2+self.direction[1]**2)     
            self.posX += self.my_data.velocity * game.timestep * self.direction[0]
            self.posY += self.my_data.velocity * game.timestep * self.direction[1]
            self.rect.x = self.posX
            self.rect.y = self.posY
            self.center += self.my_data.velocity * game.timestep * self.direction
            self.moving = True

            # self.rendering_layer = compute_rendering_layer_number(self)
            self.rendering_layer = TOTAL_NUMBER_RENDERING_LAYER-3

            self.my_timer += game.timestep
            if self.my_timer>self.my_data.time_per_frame:
                  self.current_frame += 1
                  self.current_frame = self.current_frame%self.my_data.number_frame
                  self.my_timer = 0.0
                              
            self.rotate(self.my_data.images[self.current_frame])  

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
                        
      def check_impact(self,game):
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False,pygame.sprite.collide_rect_ratio(self.my_data.ratio_for_impact))
            if self.hit_ennemies:
                  pygame.sprite.Sprite.kill(self)
                  for i in range (len(self.hit_ennemies)):
                        self.hit_ennemies[i].hp -= self.my_data.damage

 
class Rock(Projectile,pygame.sprite.Sprite):
      def __init__(self,all_p,x,y,target):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_p.rock_data

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

            self.center = vec(self.posX+ROCK_CENTOR_VECTOR[0]*self.image_size[0],self.posY+ROCK_CENTOR_VECTOR[1]*self.image_size[1])

            self.my_target_center = self.target.center

            self.my_timer = 0
                        
      def check_impact(self,game):
            distance = np.sqrt((self.my_target_center[0] - self.center[0])**2 + (self.my_target_center[1] - self.center[1])**2)
            if (distance<0.1*BACKGROUND_SQUARE_SIDE):
                  pygame.sprite.Sprite.kill(self)
                  game.all_impacts.add_impact(game,self,self.my_data.impact_tag)  


      def move(self,game):
            if (pygame.sprite.Sprite.alive(self.target)):
                  self.my_target_center = self.target.rect.center
                  self.direction = (self.target.rect.center[0] - self.center[0], self.target.rect.center[1] - self.center[1])   
                  self.direction /= sqrt(self.direction[0]**2+self.direction[1]**2)     
            self.posX += self.my_data.velocity * game.timestep * self.direction[0]
            self.posY += self.my_data.velocity * game.timestep * self.direction[1]
            self.rect.x = self.posX
            self.rect.y = self.posY
            self.center += self.my_data.velocity * game.timestep * self.direction
            self.moving = True
            self.rotate(game,self.my_data.static_image)

            # self.rendering_layer = compute_rendering_layer_number(self)
            self.rendering_layer = TOTAL_NUMBER_RENDERING_LAYER-3

      def rotate(self,game,image):
            self.my_timer += game.timestep
            if (ROCK_ROTATION_SPEED==0):
                  angle = 0
            else:
                  period = 1/(ROCK_ROTATION_SPEED/1000)
                  self.my_timer = self.my_timer%period
                  angle = 360*(self.my_timer/period)  # marche pas pour le moment car l'axe de rotation au milieu de l'image
            self.current_image = pygame.transform.rotate(image, angle)