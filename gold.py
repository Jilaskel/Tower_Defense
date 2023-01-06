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
 

    def render(self):
        self.text_price =  self.font_gold.render(str(self.amount),True,self.font_gold_color) 
        window.blit(self.text_price,(self.font_posX,self.font_posY)) 