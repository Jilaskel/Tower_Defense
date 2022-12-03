import pygame
from utilitaries import *

class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.current_image = pygame.image.load(BACKGROUND_IMAGE_PATH).convert_alpha()    
            self.posX = 0  ## 170
            self.posY = 0  ## 100
            self.rect = self.current_image.get_rect()
            self.rect.x = self.posX
            self.rect.y = self.posY
            self.menu_height = WINDOW_HEIGHT/8.0  ## 135 en 1920x1080
            self.menu_length = WINDOW_WIDTH/1.153115   ## 1665 en en 1920x1080
            self.bush_width = WINDOW_WIDTH/42.6666  ## 45 en 1920x1080
            self.square_side = WINDOW_HEIGHT/8.0  ## 135 en 1920x1080
            self.number_square_x = 12
            self.number_square_y = 7


      def render(self):
            window.blit(self.current_image, (self.posX, self.posY))    

