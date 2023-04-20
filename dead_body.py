import pygame
from utilitaries import *
from functions import *
import random


DEAD_GOBLIN_TAG = 1
DEAD_OGRE_TAG = 2
DEAD_BLUE_NEC_TAG = 3
DEAD_RED_NEC_TAG = 4
DEAD_GREEN_NEC_TAG = 5
DEAD_BLUE_SKEL_TAG = 6
DEAD_RED_SKEL_TAG = 7
DEAD_GREEN_SKEL_TAG = 8
DEAD_DRAGON_TAG = 9


class All_dead_bodies(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self) 

            self.all_iced_bodies = All_iced_bodies()  
            self.all_rezable_bodies = All_rezable_bodies()  

            self.dead_goblin_data = Dead_goblin_data()
            self.dead_ogre_data = Dead_ogre_data()
            self.dead_blue_nec_data = Dead_blue_nec_data()
            self.dead_red_nec_data = Dead_red_nec_data()
            self.dead_green_nec_data = Dead_green_nec_data()
            self.dead_blue_skel_data = Dead_blue_skel_data()
            self.dead_red_skel_data = Dead_red_skel_data()
            self.dead_green_skel_data = Dead_green_skel_data()

            
      def add_dead_body(self,game,emy_alive,tag):
            if (tag==DEAD_GOBLIN_TAG):
                  self.add_dead_goblin(game,emy_alive)
            elif (tag==DEAD_OGRE_TAG):
                  self.add_dead_ogre(game,emy_alive)
            elif (tag==DEAD_BLUE_NEC_TAG):
                  self.add_dead_blue_nec(game,emy_alive)
            elif (tag==DEAD_RED_NEC_TAG):
                  self.add_dead_red_nec(game,emy_alive)
            elif (tag==DEAD_GREEN_NEC_TAG):
                  self.add_dead_green_nec(game,emy_alive)
            elif (tag==DEAD_BLUE_SKEL_TAG):
                  self.add_dead_blue_skel(game,emy_alive)
            elif (tag==DEAD_RED_SKEL_TAG):
                  self.add_dead_red_skel(game,emy_alive)
            elif (tag==DEAD_GREEN_SKEL_TAG):
                  self.add_dead_green_skel(game,emy_alive)


      def add_dead_goblin(self,game,emy_alive):
            self.add(Dead_goblin(self,emy_alive))
            game.all_mixers.ennemy_mixer.falling_sound.play()
            
      def add_dead_ogre(self,game,emy_alive):
            self.add(Dead_ogre(self,emy_alive))
            random.choice(game.all_mixers.ennemy_mixer.ogre_d_list).play()

      def add_dead_blue_nec(self,game,emy_alive):
            self.add(Dead_blue_nec(self,emy_alive))
            game.all_mixers.ennemy_mixer.falling_sound.play()

      def add_dead_red_nec(self,game,emy_alive):
            self.add(Dead_red_nec(self,emy_alive))
            game.all_mixers.ennemy_mixer.falling_sound.play()

      def add_dead_green_nec(self,game,emy_alive):
            self.add(Dead_green_nec(self,emy_alive))
            game.all_mixers.ennemy_mixer.falling_sound.play()

      def add_dead_blue_skel(self,game,emy_alive):
            self.add(Dead_blue_skel(self,emy_alive))
            game.all_mixers.ennemy_mixer.falling_sound.play()

      def add_dead_red_skel(self,game,emy_alive):
            self.add(Dead_red_skel(self,emy_alive))
            game.all_mixers.ennemy_mixer.falling_sound.play()

      def add_dead_green_skel(self,game,emy_alive):
            self.add(Dead_green_skel(self,emy_alive))
            game.all_mixers.ennemy_mixer.falling_sound.play()

class All_iced_bodies(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self) 

class All_rezable_bodies(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self) 

class Dead_body_data():
      def __init__(self):
            self.static_image = pygame.image.load(self.my_dict["DEATH_IMAGE_PATH"]+str(1).zfill(self.number_of_zero_image)+".png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*self.my_dict["RESIZE_FACTOR"])             
            self.image_size = vec(self.static_image.get_size())

            self.number_frame = self.my_dict["NUMBER_FRAME_DEATH"]
            self.images = []
            for i in range(1,self.number_frame+1):
                  self.images.append(pygame.image.load(self.my_dict["DEATH_IMAGE_PATH"]+str(i).zfill(self.number_of_zero_image)+".png").convert_alpha())  
                  self.images[i-1] = pygame.transform.scale(self.images[i-1],vec(self.images[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
            self.anim_total_time = self.my_dict["ANIMATION_DEATH_TOTAL_TIME"]  # in ms
            self.time_per_frame = self.anim_total_time/self.number_frame # in ms

            self.fading_time = self.my_dict["FADING_TIME"]

            self.number_frame_fading = 50
            self.images_fading = []
            for i in range(self.number_frame_fading):
                self.images_fading.append(self.images[self.number_frame-1].convert_alpha())
                self.images_fading[i].set_alpha(255-int(i*255/self.number_frame_fading))

            self.iced_image = pygame.image.load(self.my_dict["ICED_IMAGE_PATH"]).convert_alpha()
            self.iced_image = pygame.transform.scale(self.iced_image,vec(self.iced_image.get_size())*self.my_dict["RESIZE_FACTOR"]) 
            self.iced_time_max = self.my_dict["ICED_TIME_MAX"]
            self.iced_hp_max = self.my_dict["ICED_HP_MAX"]

            ## for selected obj
            self.name = self.my_dict["ICED_NAME"]

class Dead_goblin_data(Dead_body_data):
      def __init__(self):
            self.my_dict = GOBLIN_DICT
            self.number_of_zero_image = 4  # Xavier....
            Dead_body_data.__init__(self)

class Dead_ogre_data(Dead_body_data):
      def __init__(self):
            self.my_dict = OGRE_DICT
            self.number_of_zero_image = 4  # Xavier....
            Dead_body_data.__init__(self)

class Dead_blue_nec_data(Dead_body_data):
      def __init__(self):
            self.my_dict = BLUE_NEC_DICT
            self.number_of_zero_image = 3  # Xavier....
            Dead_body_data.__init__(self)

class Dead_red_nec_data(Dead_body_data):
      def __init__(self):
            self.my_dict = RED_NEC_DICT
            self.number_of_zero_image = 3  # Xavier....
            Dead_body_data.__init__(self)

class Dead_green_nec_data(Dead_body_data):
      def __init__(self):
            self.my_dict = GREEN_NEC_DICT
            self.number_of_zero_image = 3  # Xavier....
            Dead_body_data.__init__(self)

class Dead_blue_skel_data(Dead_body_data):
      def __init__(self):
            self.my_dict = BLUE_SKEL_DICT
            self.number_of_zero_image = 3  # Xavier....
            Dead_body_data.__init__(self)

class Dead_red_skel_data(Dead_body_data):
      def __init__(self):
            self.my_dict = RED_SKEL_DICT
            self.number_of_zero_image = 3  # Xavier....
            Dead_body_data.__init__(self)

class Dead_green_skel_data(Dead_body_data):
      def __init__(self):
            self.my_dict = GREEN_SKEL_DICT
            self.number_of_zero_image = 3  # Xavier....
            Dead_body_data.__init__(self)

class Dead_body(pygame.sprite.Sprite):
    def __init__(self,all_d,emy_alive,rezable=True):
            pygame.sprite.Sprite.__init__(self)

            self.all_d = all_d

            self.current_image = self.my_data.static_image.convert_alpha()

            self.image_size = self.my_data.image_size

            self.posX = emy_alive.posX      
            self.posY = emy_alive.posY    
            self.image_offset = emy_alive.my_data.image_offset
            self.center =  emy_alive.center
            self.rendering_layer = emy_alive.rendering_layer

            self.current_frame = 0

            self.my_timer = 0

            self.iced = emy_alive.iced
            if self.iced:
                  all_d.all_iced_bodies.add(self)
            else:
                  if rezable:
                        all_d.all_rezable_bodies.add(self)

            self.hp_max = self.my_data.iced_hp_max
            self.hp = self.hp_max
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
                  self.all_d.all_iced_bodies.remove(self)
                  self.all_d.all_rezable_bodies.add(self)
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

class Dead_goblin(Dead_body):
      def __init__(self,all_d,emy_alive):
            self.my_data = all_d.dead_goblin_data

            Dead_body.__init__(self,all_d,emy_alive)


class Dead_ogre(Dead_body):
      def __init__(self,all_d,emy_alive):
            self.my_data = all_d.dead_ogre_data

            Dead_body.__init__(self,all_d,emy_alive)

class Dead_blue_nec(Dead_body):
      def __init__(self,all_d,emy_alive):
            self.my_data = all_d.dead_blue_nec_data

            Dead_body.__init__(self,all_d,emy_alive)

class Dead_red_nec(Dead_body):
      def __init__(self,all_d,emy_alive):
            self.my_data = all_d.dead_red_nec_data

            Dead_body.__init__(self,all_d,emy_alive)

class Dead_green_nec(Dead_body):
      def __init__(self,all_d,emy_alive):
            self.my_data = all_d.dead_green_nec_data

            Dead_body.__init__(self,all_d,emy_alive)

class Dead_blue_skel(Dead_body):
      def __init__(self,all_d,emy_alive):
            self.my_data = all_d.dead_blue_skel_data

            Dead_body.__init__(self,all_d,emy_alive,rezable=False)

            self.rendering_layer = compute_rendering_layer_number(self)

class Dead_red_skel(Dead_body):
      def __init__(self,all_d,emy_alive):
            self.my_data = all_d.dead_red_skel_data

            Dead_body.__init__(self,all_d,emy_alive,rezable=False)

            self.rendering_layer = compute_rendering_layer_number(self)

class Dead_green_skel(Dead_body):
      def __init__(self,all_d,emy_alive):
            self.my_data = all_d.dead_green_skel_data

            Dead_body.__init__(self,all_d,emy_alive,rezable=False)

            self.rendering_layer = compute_rendering_layer_number(self)