import pygame
from utilitaries import *
from functions import *

ARCANE_TOWER_IMPACT_TAG = 1
FIRE_TOWER_IMPACT_TAG = 2
LIGHTNING_TOWER_IMPACT_TAG = 3
ICE_TOWER_IMPACT_TAG = 4


class All_impacts(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self)   

            self.arcane_impact_data = Arcane_impact_data()
            self.fire_impact_data = Fire_impact_data()

      def add_impact(self,projectile,tag):
            if (tag==ARCANE_TOWER_IMPACT_TAG):
                  self.add_arcane_impact(projectile)
            elif (tag==FIRE_TOWER_IMPACT_TAG):
                  self.add_fire_impact(projectile)
            elif (tag==LIGHTNING_TOWER_IMPACT_TAG):
                  self.add_arcane_impact(projectile)
            elif (tag==ICE_TOWER_IMPACT_TAG):
                  self.add_arcane_impact(projectile)            

      def add_arcane_impact(self,projectile):
            self.add(Arcane_impact(self,projectile))

      def add_fire_impact(self,projectile):
            self.add(Fire_impact(self,projectile))

class Arcane_impact_data():
      def __init__(self):

        self.static_image = pygame.image.load(ARCANE_IMPACT_IMAGE_PATH+"001.png").convert_alpha()
        self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*ARCANE_IMPACT_RESIZE_FACTOR)        
        self.image_size = vec(self.static_image.get_size())
        self.offset = vec(ARCANE_IMPACT_CENTOR_VECTOR[0]*self.image_size[0],ARCANE_IMPACT_CENTOR_VECTOR[1]*self.image_size[1])

        self.number_frame = ARCANE_IMPACT_NUMBER_FRAME
        self.images = []
        for i in range(1,self.number_frame+1):
                self.images.append(pygame.image.load(ARCANE_IMPACT_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha())  
                self.images[i-1] = pygame.transform.scale(self.images[i-1],vec(self.images[i-1].get_size())*ARCANE_IMPACT_RESIZE_FACTOR)
        self.anim_total_time = ARCANE_IMPACT_TOTAL_TIME  # in ms
        self.time_per_frame = self.anim_total_time/self.number_frame # in ms

        self.damage_frame = ARCANE_IMPACT_DAMAGE_FRAME - 1

class Fire_impact_data():
      def __init__(self):

        self.static_image = pygame.image.load(FIRE_IMPACT_IMAGE_PATH+"0001.png").convert_alpha()
        self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*FIRE_IMPACT_RESIZE_FACTOR)        
        self.image_size = vec(self.static_image.get_size())
        self.offset = vec(FIRE_IMPACT_CENTOR_VECTOR[0]*self.image_size[0],FIRE_IMPACT_CENTOR_VECTOR[1]*self.image_size[1])

        self.number_frame = FIRE_IMPACT_NUMBER_FRAME
        self.images = []
        for i in range(1,self.number_frame+1):
                self.images.append(pygame.image.load(FIRE_IMPACT_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())  
                self.images[i-1] = pygame.transform.scale(self.images[i-1],vec(self.images[i-1].get_size())*FIRE_IMPACT_RESIZE_FACTOR)
        self.anim_total_time = FIRE_IMPACT_TOTAL_TIME  # in ms
        self.time_per_frame = self.anim_total_time/self.number_frame # in ms

        self.damage_frame = FIRE_IMPACT_DAMAGE_FRAME - 1

class Impact(pygame.sprite.Sprite):
    def __init__(self,projectile):

        self.current_image = self.my_data.static_image
        self.image_size = self.my_data.image_size

        self.current_frame = 0

        self.my_timer = 0

        self.damage = projectile.damage
        self.damage_dealt=False

        self.posX = projectile.target.rect.center[0]-self.my_data.offset[0]
        self.posY = projectile.target.rect.center[1]-self.my_data.offset[1]
        self.rendering_layer = compute_rendering_layer_number(self)

        self.rect = self.current_image.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY + self.rect.height*0.5
        self.rect.height = self.rect.height*0.5

    def check_impact(self,game):
        if (self.current_frame==self.my_data.damage_frame-1 and self.damage_dealt==False):
            self.damage_dealt = True
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False)
            if self.hit_ennemies:
                for i in range (len(self.hit_ennemies)):
                        self.hit_ennemies[i].hp -= self.damage

    def explode(self,game):
        self.my_timer += game.timestep
        if self.my_timer>self.my_data.time_per_frame:
            self.current_frame += 1
            self.my_timer = 0.0
        
        if (self.current_frame>(self.my_data.number_frame-1)):
            pygame.sprite.Sprite.kill(self)
        else:
            self.current_image= self.my_data.images[self.current_frame]

    def render(self):
        window.blit(self.current_image, (self.posX, self.posY))  


class Arcane_impact(Impact,pygame.sprite.Sprite):
    def __init__(self,all_i,projectile):
        pygame.sprite.Sprite.__init__(self)

        self.my_data = all_i.arcane_impact_data

        Impact.__init__(self,projectile)


class Fire_impact(Impact,pygame.sprite.Sprite):
    def __init__(self,all_i,projectile):
        pygame.sprite.Sprite.__init__(self)

        self.my_data = all_i.fire_impact_data

        Impact.__init__(self,projectile)
