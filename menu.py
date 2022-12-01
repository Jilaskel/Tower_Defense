import pygame
from utilitaries import *

BASIC_TOWER_BUTTON_TAG = 1
BALLISTA_BUTTON_TAG = 2

class Menu():
      def __init__(self,game):
            self.all_buttons = pygame.sprite.Group()

            self.margin = game.background.bush_width*2
            side = game.background.square_side

            path = MENU_BASIC_TOWER_BUTTON_IMAGE_PATH
            (x,y) = (self.margin,0)
            self.all_buttons.add(Button(path,x,y,BASIC_TOWER_BUTTON_TAG))

            path = MENU_BALLISTA_BUTTON_IMAGE_PATH
            (x,y) = (self.margin+1.5*side,0)
            self.all_buttons.add(Button(path,x,y,BALLISTA_BUTTON_TAG))

      def render(self):
            for button in self.all_buttons:
                  button.render()

class Button(pygame.sprite.Sprite):
      def __init__(self,path,x,y,tag):
            super().__init__()
            self.current_image = pygame.image.load(path).convert_alpha()   
            self.rect = self.current_image.get_rect() 
            self.posX = x  ## 170
            self.posY = y  ## 100 
            self.rect.x = self.posX
            self.rect.y = self.posY   

            self.my_tag = tag
            if (self.my_tag==BASIC_TOWER_BUTTON_TAG):
                self.compatible_grass = True
                self.compatible_road = False
            elif (self.my_tag==BALLISTA_BUTTON_TAG):
                self.compatible_grass = False
                self.compatible_road = True
            else : 
                self.compatible_grass = False
                self.compatible_road = False               

      def render(self):
            window.blit(self.current_image, (self.posX, self.posY))         