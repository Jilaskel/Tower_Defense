import pygame
from utilitaries import *


class All_dead_bodies(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self)   

            self.dead_gobelin_data = Dead_gobelin_data()
            
      def add_dead_gobelin(self,el_alive):
            self.add(Dead_gobelin(self,el_alive))


class Dead_gobelin_data():
      def __init__(self):

            self.static_image = pygame.image.load(GOBELIN_DEATH_IMAGE_PATH+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*GOBELIN_RESIZE_FACTOR)             
            self.image_size = vec(self.static_image.get_size())

            self.number_frame = GOBELIN_NUMBER_FRAME_DEATH
            self.images = []
            for i in range(1,self.number_frame+1):
                  self.images.append(pygame.image.load(GOBELIN_DEATH_IMAGE_PATH+str(i).zfill(4)+".png").convert_alpha())  
                  self.images[i-1] = pygame.transform.scale(self.images[i-1],vec(self.images[i-1].get_size())*GOBELIN_RESIZE_FACTOR)
            self.anim_total_time = GOBELIN_ANIMATION_DEATH_TOTAL_TIME  # in ms
            self.time_per_frame = self.anim_total_time/self.number_frame # in ms

            self.fading_time = GOBELIN_FADING_TIME

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

class Dead_gobelin(Dead_body,pygame.sprite.Sprite):
      def __init__(self,all_d,gob_alive):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_d.dead_gobelin_data

            self.current_image = self.my_data.static_image.convert_alpha()

            self.image_size = self.my_data.image_size

            self.posX = gob_alive.posX      
            self.posY = gob_alive.posY    
            self.center =  gob_alive.center
            self.rendering_layer = gob_alive.rendering_layer-1

            self.current_frame = 0

            self.my_timer = 0