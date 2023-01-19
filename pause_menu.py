import pygame
from utilitaries import *
from starting_menu import * 

class Pause_menu():
      def __init__(self,game):
            self.all_buttons = pygame.sprite.Group()

            self.game = game

            self.mouse = Pause_mouse(self)

            self.font_size = int(140*RESIZE_COEFF)
            self.font = pygame.font.Font(LOADING_FONT_PATH,self.font_size)
            self.font_color = (243,243,243)
            title = "You Shall Not Pass"
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
            (x,y) = (x_m,self.margin)
            self.all_buttons.add(Button(self,path,x,y,"Resume",resize_factor,vec(0.30,0.30)))

            (x,y) = (x_m,self.margin+1.0*space)
            self.all_buttons.add(Button(self,path,x,y,"Restart",resize_factor,vec(0.30,0.30)))
 
            (x,y) = (x_m,self.margin+2.0*space)
            self.all_buttons.add(Button(self,path,x,y,"Parameters",resize_factor,vec(0.15,0.30)))

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

            window.blit(self.title1, (330*RESIZE_COEFF, 50*RESIZE_COEFF))

            image_size = vec(self.pannel_image.get_size())
            x = WINDOW_WIDTH*0.5 - image_size[0]*0.5
            window.blit(self.pannel_image, (x, 250*RESIZE_COEFF))

            for button in self.all_buttons:
                  button.render()

            self.mouse.render()
            pygame.display.update()


class Pause_mouse(pygame.sprite.Sprite):
    def __init__(self,menu):
        super().__init__()

        self.menu = menu

        self.static_image = pygame.image.load(MOUSE_IMAGE_PATH).convert_alpha()  
        self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*MOUSE_RESIZE_FACTOR)        
        self.current_image = self.static_image

        self.ratio_for_hitbox = MOUSE_RATIO_FOR_HITBOX


    def doing_stuff(self):
        (x,y) = pygame.mouse.get_pos()
        self.posX = x
        self.posY = y

        self.rect = self.current_image.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY

        self.state_mouse = pygame.mouse.get_pressed()
        self.left_click_pressed = self.state_mouse[0]

        self.hit_buttons = pygame.sprite.spritecollide(self, self.menu.all_buttons, False, pygame.sprite.collide_rect_ratio(self.ratio_for_hitbox))
        if (self.hit_buttons):
            self.hit_buttons[0].mouse_over = True
            if (self.left_click_pressed):
                  match self.hit_buttons[0].tag:
                        case "Resume":
                            global_status.status = "In game"

                        case "Restart":
                            pass

                        case "Parameters":
                            pass

                        case "Back to menu":
                            global_status.status = "Starting menu"

                        case "Quit":
                            global_status.status = "Quitting"


    def render(self):
        pygame.mouse.set_visible(False)
        window.blit(self.current_image, (self.posX, self.posY)) 