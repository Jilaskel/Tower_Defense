import pygame
from utilitaries import *
from functions import * 

class Grid():
    def __init__(self,game):  
        self.all_boxes = pygame.sprite.Group()

        self.unit = game.background.square_side

        self.border_box_image = pygame.image.load(MOUSE_BOX_BORDER_IMAGE_PATH).convert_alpha()
        self.border_box_image = pygame.transform.scale(self.border_box_image,(self.unit,self.unit))       
        # self.not_valid_box_image.set_alpha(MOUSE_NOT_VALID_BOX_IMAGE_ALPHA)

        for i in range(game.background.number_square_y):
            for j in range(game.background.number_square_x):
                x = game.background.bush_width + j*self.unit
                y = game.background.menu_height + i*self.unit
                if (i%2==0):  # grass
                    self.all_boxes.add(Box(self,x,y,True))
                else:
                    self.all_boxes.add(Box(self,x,y,False))
            ## ON WALLS BUT ONLY ABOVE GATES
            # if not(i%2==0):
            #     x = game.background.bush_width + (game.background.number_square_x+0.5)*self.unit
            #     y = game.background.menu_height + i*self.unit          
            #     self.all_boxes.add(Box(self,x,y,False,rendering_layer=23))
            ## ON WALLS EVERYWHERE
            x = game.background.bush_width + (game.background.number_square_x+0.5)*self.unit
            y = game.background.menu_height + i*self.unit          
            self.all_boxes.add(Box(self,x,y,False,rendering_layer=23))

class Box(pygame.sprite.Sprite):
    def __init__(self,grid,x,y,grass,rendering_layer=0):
            super().__init__()

            self.occupied = False

            self.rect = pygame.Rect(x,y,grid.unit,grid.unit)

            self.posX = x
            self.posY = y

            self.current_image = grid.border_box_image
            self.image_size = vec(self.current_image.get_size())
            if (rendering_layer==0):
                self.rendering_layer = compute_rendering_layer_number(self)
            else:
                self.rendering_layer = rendering_layer

            if grass:
                self.grass = True
                self.road = False
            else:
                self.grass = False
                self.road = True              


    def render(self):
        window.blit(self.current_image, (self.posX, self.posY))  