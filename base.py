import pygame
from utilitaries import *

class Base():
    def __init__(self,game):  
        self.all_gates = pygame.sprite.Group()

        self.unit = game.background.square_side

        for i in range(1,game.background.number_square_y,2):
            x = game.background.bush_width + game.background.number_square_x*self.unit
            y = game.background.menu_height + i*self.unit
            self.all_gates.add(Gate(x,y))

          

class Gate(pygame.sprite.Sprite):
    def __init__(self,x,y):
            super().__init__()
            side = BACKGROUND_SQUARE_SIDE
            self.rect = pygame.Rect(x,y,side,side)

            self.posX = x
            self.posY = y

            self.hp_max = BASE_GATE_HP_MAX
            self.hp = self.hp_max

    def destroy(self):
        if (self.hp<=0):
                pygame.sprite.Sprite.kill(self)