import pygame
from utilitaries import *

class Base():
    def __init__(self,game):  
        self.all_gates = pygame.sprite.Group()

        self.name = "Gate"

        self.unit = game.background.square_side

        self.x_walls = game.background.bush_width + game.background.number_square_x*self.unit
        self.y_walls = game.background.menu_height
        self.y_list = [0,0,0]
        j = 0
        for i in range(1,game.background.number_square_y,2):
            self.y_list[j] = game.background.menu_height + i*self.unit
            j += 1
            
        self.all_gates.add(Gate(self,self.x_walls,self.y_list[0],"top"))
        self.all_gates.add(Gate(self,self.x_walls,self.y_list[1],"mid"))
        self.all_gates.add(Gate(self,self.x_walls,self.y_list[2],"bot"))

    def reset(self):
        self.all_gates.empty()    
        self.all_gates.add(Gate(self,self.x_walls,self.y_list[0],"top"))
        self.all_gates.add(Gate(self,self.x_walls,self.y_list[1],"mid"))
        self.all_gates.add(Gate(self,self.x_walls,self.y_list[2],"bot"))
          

class Gate(pygame.sprite.Sprite):
    def __init__(self,base,x,y,position):
            super().__init__()
            side = BACKGROUND_SQUARE_SIDE
            self.rect = pygame.Rect(x,y,side,side)

            self.my_data = base

            self.posX = base.x_walls - 40*RESIZE_COEFF
            self.posY = base.y_walls - 90*RESIZE_COEFF

            self.hp_max = BASE_GATE_HP_MAX
            self.hp = self.hp_max
            self.opened = False

            self.opened_path = BACKGROUND_WALLS_ASSETS_PATH + "wall_" + position + "_opened.png"
            self.opened_image = pygame.image.load(self.opened_path).convert_alpha()
            self.opened_image = pygame.transform.scale(self.opened_image,vec(self.opened_image.get_size())*RESIZE_COEFF) 
 
            self.closed_path = BACKGROUND_WALLS_ASSETS_PATH + "wall_" + position + "_closed.png"
            self.closed_image = pygame.image.load(self.closed_path).convert_alpha()
            self.closed_image = pygame.transform.scale(self.closed_image,vec(self.closed_image.get_size())*RESIZE_COEFF) 

            self.current_image = self.closed_image

            self.rendering_layer = 22

    def check_destroy(self):
        if ((self.hp<=0) and not(self.opened)):
                # pygame.sprite.Sprite.kill(self)
                self.rect.x = -500
                self.current_image = self.opened_image
                self.posX -= 8*RESIZE_COEFF
                self.opened = True

    def render(self):
        window.blit(self.current_image, (self.posX, self.posY))   