import pygame
from utilitaries import *


class Gold():
    def __init__(self):
        self.amount = GOLD_STARTING_AMOUNT

        self.font_gold_size = int(50*RESIZE_COEFF)
        self.font_gold_color = (0,0,0)
        self.font_gold = pygame.font.Font(FONT_PATH,self.font_gold_size)

        self.font_posX = 11.2 * BACKGROUND_SQUARE_SIDE
        self.font_posY = 0.45 * BACKGROUND_SQUARE_SIDE

        self.rendering_layer = TOTAL_NUMBER_RENDERING_LAYER-1
 
    def gold_gain(self,game,obj,amount):
        self.amount += amount
        game.all_gold_anim.add_gold_anim(obj,amount)

    def render(self):
        self.text_price =  self.font_gold.render(str(self.amount),True,self.font_gold_color) 
        window.blit(self.text_price,(self.font_posX,self.font_posY)) 


class All_gold_anim(pygame.sprite.Group):
    def __init__(self):
          pygame.sprite.Group.__init__(self)  

          self.current_image = pygame.image.load(GOLD_GAIN_IMAGE_PATH).convert_alpha()
          self.current_image = pygame.transform.scale(self.current_image,vec(self.current_image.get_size())*GOLD_GAIN_RESIZE_FACTOR)             
          self.image_size = vec(self.current_image.get_size())        

          self.font_gold_gain_size = int(GOLD_GAIN_FONT_SIZE*RESIZE_COEFF)
          self.font_gold_gain_color = (0,0,0)
          self.font_gold_gain = pygame.font.Font(FONT_PATH,self.font_gold_gain_size)

          self.offset = GOLD_GAIN_OFFSET

    def add_gold_anim(self,obj,amount):
          self.add(Gold_anim(self,obj,amount))

class Gold_anim(pygame.sprite.Sprite):
    def __init__(self,all_g,obj,amount):
        pygame.sprite.Sprite.__init__(self)

        self.my_data = all_g

        self.amount = amount

        self.current_image = self.my_data.current_image

        self.font_posX =  obj.center[0] + all_g.offset[0]
        self.font_posY =  obj.center[1] + all_g.offset[1]

        offset_image = vec(10,-20)
        self.posX = self.font_posX + offset_image[0]
        self.posY = self.font_posY + offset_image[1]

        self.rendering_layer = TOTAL_NUMBER_RENDERING_LAYER-1

    def render(self):
        window.blit(self.current_image, (self.posX, self.posY))
        self.text_price =  self.my_data.font_gold_gain.render("+"+str(self.amount),True,self.my_data.font_gold_gain_color) 
        window.blit(self.text_price,(self.font_posX,self.font_posY)) 