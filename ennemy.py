import pygame
from utilitaries import *

class Ennemy(pygame.sprite.Sprite):
      def __init__(self,x,y):
            pass

      def move(self,game):           
            pass

      def render(self):
            pass  


class Gobelin(Ennemy,pygame.sprite.Sprite):
      def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
 
            self.images_path = GOBELIN_WALKING_IMAGE_PATH
            self.static_image = pygame.image.load(self.images_path+"/001.png").convert_alpha()
            self.current_image = self.static_image
            self.number_frame_walking = GOBELIN_NUMBER_FRAME_WALKING
            self.image_walking = []
            for i in range(1,self.number_frame_walking+1):
                  self.image_walking.append(pygame.image.load(self.images_path+"00"+str(i)+".png").convert_alpha())   

            self.hp_max = GOBELIN_HP_MAX
            self.hp = self.hp_max

            self.posX = x     
            self.posY = y     
            self.velocity = GOBELIN_VELOCITY # pixel by ms
            self.moving = False
            self.move_frame = 0
            self.anim_total_time = GOBELIN_ANIMATION_WALKING_TOTAL_TIME  # in ms
            self.time_per_frame = self.anim_total_time/self.number_frame_walking # in ms
            self.my_timer = 0

            self.rect = self.current_image.get_rect()
            self.radius = GOBELIN_HITBOX_FACTOR*(self.rect.width+self.rect.height)/2.0
            self.rect.x = self.posX
            self.rect.y = self.posY
            self.rect.width *= GOBELIN_HITBOX_FACTOR
            self.rect.height *= GOBELIN_HITBOX_FACTOR

      def move(self,game):           
            self.posX += self.velocity * game.timestep
            self.rect.x = self.posX
            self.moving = True
            if self.moving:
                  self.my_timer += game.timestep
                  if self.my_timer>self.time_per_frame:
                        self.move_frame += 1
                        self.move_frame = self.move_frame%self.number_frame_walking
                        self.my_timer = 0.0
                                    
                  self.current_image= self.image_walking[self.move_frame]

      def die(self,game):
            if (self.hp<=0):
                  pygame.sprite.Sprite.kill(self)

      def render(self):
            window.blit(self.current_image, (self.posX, self.posY))  
 
