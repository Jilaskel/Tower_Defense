import pygame
from utilitaries import *
import random


DEAD_GOBLIN_TAG = 1
DEAD_OGRE_TAG = 2
DEAD_BLUE_NEC_TAG = 3
DEAD_RED_NEC_TAG = 4
DEAD_GREEN_NEC_TAG = 5
DEAD_KAMIKAZE_TAG = 6
DEAD_DRAGON_TAG = 7


class All_dead_bodies(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self) 

            self.all_iced_bodies = All_iced_bodies()  
            self.all_rezable_bodies = All_rezable_bodies()  

            self.dead_goblin_data = Dead_goblin_data()
            self.dead_ogre_data = Dead_ogre_data()
            self.dead_blue_nec_data = Dead_blue_nec_data()

            
      def add_dead_body(self,game,emy_alive,tag):
            if (tag==DEAD_GOBLIN_TAG):
                  self.add_dead_goblin(game,emy_alive)
            elif (tag==DEAD_OGRE_TAG):
                  self.add_dead_ogre(game,emy_alive)
            elif (tag==DEAD_BLUE_NEC_TAG):
                  self.add_dead_blue_nec(game,emy_alive)


      def add_dead_goblin(self,game,emy_alive):
            self.add(Dead_goblin(self,emy_alive))
            game.all_mixers.ennemy_mixer.falling_sound.play()
            
      def add_dead_ogre(self,game,emy_alive):
            self.add(Dead_ogre(self,emy_alive))
            random.choice(game.all_mixers.ennemy_mixer.ogre_d_list).play()

      def add_dead_blue_nec(self,game,emy_alive):
            self.add(Dead_blue_nec(self,emy_alive))
            game.all_mixers.ennemy_mixer.falling_sound.play()


class All_iced_bodies(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self) 

class All_rezable_bodies(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self) 

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

            self.iced_image = pygame.image.load(GOBLIN_ICED_IMAGE_PATH).convert_alpha()
            self.iced_image = pygame.transform.scale(self.iced_image,vec(self.iced_image.get_size())*GOBLIN_RESIZE_FACTOR) 
            self.iced_time_max = GOBLIN_ICED_TIME_MAX
            self.iced_hp_max = GOBLIN_ICED_HP_MAX

            ## for selected obj
            self.hp_max = self.iced_hp_max
            self.name = "Iced Goblin"

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

            self.iced_image = pygame.image.load(OGRE_ICED_IMAGE_PATH).convert_alpha()
            self.iced_image = pygame.transform.scale(self.iced_image,vec(self.iced_image.get_size())*OGRE_RESIZE_FACTOR) 
            self.iced_time_max = OGRE_ICED_TIME_MAX
            self.iced_hp_max = OGRE_ICED_HP_MAX

            ## for selected obj
            self.hp_max = self.iced_hp_max
            self.name = "Iced Ogre"

class Dead_blue_nec_data():
      def __init__(self):

            self.static_image = pygame.image.load(BLUE_NEC_DEATH_IMAGE_PATH+"001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*BLUE_NEC_RESIZE_FACTOR)             
            self.image_size = vec(self.static_image.get_size())

            self.number_frame = BLUE_NEC_NUMBER_FRAME_DEATH
            self.images = []
            for i in range(1,self.number_frame+1):
                  self.images.append(pygame.image.load(BLUE_NEC_DEATH_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha())  
                  self.images[i-1] = pygame.transform.scale(self.images[i-1],vec(self.images[i-1].get_size())*BLUE_NEC_RESIZE_FACTOR)
            self.anim_total_time = BLUE_NEC_ANIMATION_DEATH_TOTAL_TIME  # in ms
            self.time_per_frame = self.anim_total_time/self.number_frame # in ms

            self.fading_time = BLUE_NEC_FADING_TIME

            self.number_frame_fading = 50
            self.images_fading = []
            for i in range(self.number_frame_fading):
                self.images_fading.append(self.images[self.number_frame-1].convert_alpha())
                self.images_fading[i].set_alpha(255-int(i*255/self.number_frame_fading))

            self.iced_image = pygame.image.load(BLUE_NEC_ICED_IMAGE_PATH).convert_alpha()
            self.iced_image = pygame.transform.scale(self.iced_image,vec(self.iced_image.get_size())*BLUE_NEC_RESIZE_FACTOR) 
            self.iced_time_max = BLUE_NEC_ICED_TIME_MAX
            self.iced_hp_max = BLUE_NEC_ICED_HP_MAX

            ## for selected obj
            self.hp_max = self.iced_hp_max
            self.name = "Iced Ice Necro"

class Dead_body(pygame.sprite.Sprite):
    def __init__(self,all_d,emy_alive):
            self.all_d = all_d

            self.current_image = self.my_data.static_image.convert_alpha()

            self.image_size = self.my_data.image_size

            self.posX = emy_alive.posX      
            self.posY = emy_alive.posY    
            self.center =  emy_alive.center
            self.rendering_layer = emy_alive.rendering_layer

            self.current_frame = 0

            self.my_timer = 0

            self.iced = emy_alive.iced
            if self.iced:
                  all_d.all_iced_bodies.add(self)
            else:
                  all_d.all_rezable_bodies.add(self)

            self.hp = self.my_data.iced_hp_max
            self.rect = emy_alive.rect
            self.radius = emy_alive.radius

    def fall(self,game):
        self.my_timer += game.timestep
        if (self.hp<0):
              self.iced = False
              self.all_d.all_iced_bodies.remove(self)
              self.all_d.all_rezable_bodies.add(self)

        if (self.iced):
            if (self.my_timer<self.my_data.iced_time_max*1000):
                  self.current_image = self.my_data.iced_image
            else:
                 self.iced = False
                 self.my_timer = 0
            
        if (not(self.iced)):    
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
      def __init__(self,all_d,emy_alive):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_d.dead_goblin_data

            Dead_body.__init__(self,all_d,emy_alive)


class Dead_ogre(Dead_body,pygame.sprite.Sprite):
      def __init__(self,all_d,emy_alive):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_d.dead_ogre_data

            Dead_body.__init__(self,all_d,emy_alive)

class Dead_blue_nec(Dead_body,pygame.sprite.Sprite):
      def __init__(self,all_d,emy_alive):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_d.dead_blue_nec_data

            Dead_body.__init__(self,all_d,emy_alive)