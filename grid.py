import pygame
from utilitaries import *

class Grid():
    def __init__(self,game):  
        self.all_boxes = pygame.sprite.Group()

        self.unit = game.background.square_side

        for i in range(game.background.number_square_y):
            for j in range(game.background.number_square_x):
                x = game.background.bush_width + j*self.unit
                y = game.background.menu_height + i*self.unit
                if (i%2==0):  # grass
                    self.all_boxes.add(Box(x,y,self.unit,True))
                else:
                    self.all_boxes.add(Box(x,y,self.unit,False))

class Box(pygame.sprite.Sprite):
    def __init__(self,x,y,side,grass):
            super().__init__()
            self.rect = pygame.Rect(x,y,side,side)

            self.posX = x
            self.posY = y

            if grass:
                self.grass = True
                self.road = False
            else:
                self.grass = False
                self.road = True              


