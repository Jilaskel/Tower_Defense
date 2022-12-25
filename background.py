import pygame
from utilitaries import *

class Background():
      def __init__(self):
            self.current_image = pygame.image.load(BACKGROUND_IMAGE_PATH).convert_alpha()   
            self.current_image = pygame.transform.scale(self.current_image,(WINDOW_WIDTH,WINDOW_HEIGHT))         
            self.posX = 0  
            self.posY = 0  
            self.menu_height = WINDOW_HEIGHT/8.0  ## 135 en 1920x1080
            self.menu_length = WINDOW_WIDTH/1.153115   ## 1665 en en 1920x1080
            self.bush_width = WINDOW_WIDTH/42.6666  ## 45 en 1920x1080
            self.square_side = WINDOW_HEIGHT/8.0  ## 135 en 1920x1080
            self.number_square_x = 12
            self.number_square_y = 7

            self.rendering_layer = 0


      def render(self,rendering_layer):
            if self.rendering_layer==rendering_layer:
                  window.blit(self.current_image, (self.posX, self.posY))    

