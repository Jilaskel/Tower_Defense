import pygame
from utilitaries import *
from functions import *
from starting_menu import * 
from pause_menu import * 

class Game_over_menu():
      def __init__(self,game):
            self.all_buttons = pygame.sprite.Group()

            self.game = game

            self.mouse = Pause_mouse(self)

            self.font_size = int(140*RESIZE_COEFF)
            self.font = pygame.font.Font(LOADING_FONT_PATH,self.font_size)
            self.font_color = (243,243,243)
            title = "Game Over"
            self.title1 = self.font.render(title,True,self.font_color)

            self.background = pygame.image.load(PAUSE_MENU_BACKGROUND).convert_alpha()
            self.background.set_alpha(155)
            self.background = pygame.transform.scale(self.background,(WINDOW_WIDTH,WINDOW_HEIGHT))         

            self.pannel_image = pygame.image.load(STARTING_MENU_PANNEL_PATH).convert_alpha()   
            image_size = vec(self.pannel_image.get_size())
            resize_ratio = 0.35 * RESIZE_COEFF
            self.pannel_image = pygame.transform.scale(self.pannel_image,image_size*resize_ratio)  

            self.margin = WINDOW_HEIGHT*0.32
            space = WINDOW_HEIGHT/9

            self.font_menu_size = int(40*RESIZE_COEFF)
            self.font_menu_color = (0,0,0)
            self.font_menu = pygame.font.Font(FONT_PATH,self.font_menu_size)
            self.font_menu_enlarged = pygame.font.Font(FONT_PATH,int(self.font_menu_size*STARTING_MOUSE_OVER_ENLARGED_COEFF))

            path = STARTING_MENU_BUTTON_1_PATH
            resize_factor = 0.25
            x_m = WINDOW_WIDTH*0.5 - 1148*resize_factor*0.5*RESIZE_COEFF

            (x,y) = (x_m,self.margin+2.0*space)
            self.all_buttons.add(Button(self,path,x,y,"Restart",resize_factor,vec(0.30,0.30)))

            (x,y) = (x_m,self.margin+3.0*space)
            self.all_buttons.add(Button(self,path,x,y,"Back to menu",resize_factor,vec(0.10,0.30)))

            (x,y) = (x_m,self.margin+4.0*space)
            self.all_buttons.add(Button(self,path,x,y,"Quit",resize_factor,vec(0.38,0.30)))


      def deal_with_mouse(self):
            self.game.mouse.carrying = False
            self.game.mouse.box_valid = False
            self.game.mouse.box_not_valid = False

            self.mouse.doing_stuff()

      def render(self):
            window.blit(self.background, (0,0))

            image_size = vec(self.title1.get_size())
            x = WINDOW_WIDTH*0.5 - image_size[0]*0.5
            window.blit(self.title1, (x, 50*RESIZE_COEFF))

            image_size = vec(self.pannel_image.get_size())
            x = WINDOW_WIDTH*0.5 - image_size[0]*0.5
            window.blit(self.pannel_image, (x, 250*RESIZE_COEFF))

            message = "Your score is " 
            txt = self.font_menu.render(message,True,self.font_menu_color)
            image_size0 = vec(txt.get_size())
            x = WINDOW_WIDTH*0.5 - image_size0[0]*0.5
            window.blit(txt, (x, self.margin))

            message = convert_time(self.game.timer)
            txt = self.font_menu.render(message,True,self.font_menu_color)
            image_size = vec(txt.get_size())
            x = WINDOW_WIDTH*0.5 - image_size[0]*0.5
            window.blit(txt, (x, self.margin+image_size0[1]*1.5))            

            for button in self.all_buttons:
                  button.render()

            self.mouse.render()
            pygame.display.update()

