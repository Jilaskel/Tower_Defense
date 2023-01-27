import pygame
from utilitaries import *
import random

DEAD_GOBLIN_TAG = 1
DEAD_OGRE_TAG = 2


class All_dead_bodies(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self)   

            self.dead_goblin_data = Dead_goblin_data()

            self.dead_ogre_data = Dead_ogre_data()
            
      def add_dead_body(self,game,el_alive,tag):
            if (tag==DEAD_GOBLIN_TAG):
                  self.add_dead_goblin(game,el_alive)
            elif (tag==DEAD_OGRE_TAG):
                  self.add_dead_ogre(game,el_alive)

      def add_dead_goblin(self,game,el_alive):
            self.add(Dead_goblin(self,el_alive))
            game.all_mixers.ennemy_mixer.falling_sound.play()
            
      def add_dead_ogre(self,game,el_alive):
            self.add(Dead_ogre(self,el_alive))
            random.choice(game.all_mixers.ennemy_mixer.ogre_d_list).play()

class Dead_goblin_data():
      def __init__(self):

            self.static_image = pygame.image.load(GOBLIN_DEATH_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*GOBLIN_RESIZE_FACTOR)             
            self.image_size = vec(self.static_image.get_size())

            self.number_frame = GOBLIN_NUMBER_FRAME_DEATH
            self.images = []
            for i in range(1,self.number_frame+1):
                  self.images.append(pygame.image.load(GOBLIN_DEATH_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())  
                  self.images[i-1] = pygame.transform.scale(self.images[i-1],vec(self.images[i-1].get_size())*GOBLIN_RESIZE_FACTOR)
            self.anim_total_time = GOBLIN_ANIMATION_DEATH_TOTAL_TIME  # in ms
            self.time_per_frame = self.anim_total_time/self.number_frame # in ms

            self.fading_time = GOBLIN_FADING_TIME

            self.number_frame_fading = 50
            self.images_fading = []
            for i in range(self.number_frame_fading):
                self.images_fading.append(self.images[self.number_frame-1].convert_alpha())
                self.images_fading[i].set_alpha(255-int(i*255/self.number_frame_fading))

class Dead_ogre_data():
      def __init__(self):

            self.static_image = pygame.image.load(OGRE_DEATH_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*OGRE_RESIZE_FACTOR)             
            self.image_size = vec(self.static_image.get_size())

            self.number_frame = OGRE_NUMBER_FRAME_DEATH
            self.images = []
            for i in range(1,self.number_frame+1):
                  self.images.append(pygame.image.load(OGRE_DEATH_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())  
                  self.images[i-1] = pygame.transform.scale(self.images[i-1],vec(self.images[i-1].get_size())*OGRE_RESIZE_FACTOR)
            self.anim_total_time = OGRE_ANIMATION_DEATH_TOTAL_TIME  # in ms
            self.time_per_frame = self.anim_total_time/self.number_frame # in ms

            self.fading_time = OGRE_FADING_TIME

            self.number_frame_fading = 50
            self.images_fading = []
            for i in range(self.number_frame_fading):
                self.images_fading.append(self.images[self.number_frame-1].convert_alpha())
                self.images_fading[i].set_alpha(255-int(i*255/self.number_frame_fading))

class Dead_body(pygame.sprite.Sprite):
    def __init__(self,e_alive):
        pass

    def fall(self,game):
        self.my_timer += game.timestep
        if (self.current_frame<(self.my_data.number_frame-1)):
            if self.my_timer>self.my_data.time_per_frame:
                self.current_frame += 1
                self.my_timer = 0.0
        if (self.current_frame<(self.my_data.number_frame-1)):     
                self.current_image= self.my_data.images[self.current_frame].convert_alpha()  
        else:
            if self.my_timer<self.my_data.fading_time:
                self.current_image= self.my_data.images_fading[int(self.my_timer/self.my_data.fading_time*self.my_data.number_frame_fading)]
            else:
                pygame.sprite.Sprite.kill(self)

    def render(self):
        window.blit(self.current_image, (self.posX, self.posY))  

class Dead_goblin(Dead_body,pygame.sprite.Sprite):
      def __init__(self,all_d,el_alive):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_d.dead_goblin_data

            self.current_image = self.my_data.static_image.convert_alpha()

            self.image_size = self.my_data.image_size

            self.posX = el_alive.posX      
            self.posY = el_alive.posY    
            self.center =  el_alive.center
            self.rendering_layer = el_alive.rendering_layer

            self.current_frame = 0

            self.my_timer = 0

class Dead_ogre(Dead_body,pygame.sprite.Sprite):
      def __init__(self,all_d,el_alive):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_d.dead_ogre_data

            self.current_image = self.my_data.static_image.convert_alpha()

            self.image_size = self.my_data.image_size

            self.posX = el_alive.posX      
            self.posY = el_alive.posY    
            self.center =  el_alive.center
            self.rendering_layer = el_alive.rendering_layer

            self.current_frame = 0

            self.my_timer = 0