import pygame
from utilitaries import *


class All_error_message_anim():
    def __init__(self):

          self.list = [] 

          self.current_image = pygame.image.load(ERROR_MESSAGE_IMAGE_PATH).convert_alpha()
          self.current_image = pygame.transform.scale(self.current_image,vec(self.current_image.get_size())*ERROR_MESSAGE_RESIZE_FACTOR)             
          self.image_size = vec(self.current_image.get_size())    

          self.font_error_message_size = int(ERROR_MESSAGE_FONT_SIZE)
          self.font_error_message = pygame.font.Font(FONT_PATH,self.font_error_message_size)

          self.offset = ERROR_MESSAGE_OFFSET  ## offset with the object center
          self.offset_image = vec(-40,-3)*RESIZE_COEFF

          self.time_anim = ERROR_MESSAGE_TIME
          self.anim_vector = ERROR_MESSAGE_TRAVEL_VECTOR

    def add_error_message_anim(self,text,x,y):
          self.list.append(Error_message_anim(self,text,x,y))

class Error_message_anim():
    def __init__(self,all_err,text,x,y):

        self.my_data = all_err

        self.my_text = text

        self.font_error_message_color = ERROR_MESSAGE_RGB   ## red
      
        self.font_posX =  x + all_err.offset[0]
        self.font_posY =  y + all_err.offset[1]

        self.current_image = self.my_data.current_image

        self.posX = self.font_posX + self.my_data.offset_image[0]
        self.posY = self.font_posY + self.my_data.offset_image[1]

        self.rendering_layer = TOTAL_NUMBER_RENDERING_LAYER-1

        self.my_timer = 0

    def move(self,game):
        self.my_timer += game.timestep

        if (self.my_timer<self.my_data.time_anim):
            self.font_posX +=  self.my_data.anim_vector[0]*game.timestep/self.my_data.time_anim
            self.font_posY +=  self.my_data.anim_vector[1]*game.timestep/self.my_data.time_anim

            self.posX = self.font_posX + self.my_data.offset_image[0]
            self.posY = self.font_posY + self.my_data.offset_image[1]
        else:
            self.my_data.list.remove(self)

    def render(self):
        window.blit(self.current_image, (self.posX, self.posY))
        self.text =  self.my_data.font_error_message.render(self.my_text,True,self.font_error_message_color) 
        window.blit(self.text,(self.font_posX,self.font_posY)) 