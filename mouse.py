import pygame
from utilitaries import *
from menu import * 
from tower import *


class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.images_path = "Assets/Cursor/"
        self.static_image = pygame.image.load(self.images_path+"cursor4.png").convert_alpha()  
        self.static_image = pygame.transform.scale(self.static_image,(40.8,50))
        self.current_image = self.static_image

        self.ratio_for_hitbox = 1.0

        self.carrying = False
        self.carried_image = self.static_image

    def doing_stuff(self,game):
        (x,y) = pygame.mouse.get_pos()
        self.posX = x
        self.posY = y

        self.rect = self.current_image.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY

        self.state_mouse = pygame.mouse.get_pressed()
        self.left_click_pressed = self.state_mouse[0]
        #print(self.left_click_pressed)
        self.middle_click_pressed = self.state_mouse[1]
        self.right_click_pressed = self.state_mouse[2]


        if not(self.carrying):
            self.hit_buttons = pygame.sprite.spritecollide(self, game.menu.all_buttons, False,pygame.sprite.collide_rect_ratio(self.ratio_for_hitbox))

            if ((self.hit_buttons) and (self.left_click_pressed)):
                self.carrying = True
                self.carried_image = self.hit_buttons[0].current_image.copy()
                self.carried_image.set_alpha(100)

                self.carried_rect = self.hit_buttons[0].current_image.get_rect()
                self.carried_width = self.carried_rect.width
                self.carried_height = self.carried_rect.height

        if self.carrying:
            self.carried_x = self.posX - self.carried_width*0.5
            self.carried_y = self.posY - self.carried_height*0.5
            if not(self.left_click_pressed):
                self.hit_boxes = pygame.sprite.spritecollide(self, game.grid.all_boxes, False)
                if self.hit_boxes:
                    x_box = self.hit_boxes[0].posX
                    y_box = self.hit_boxes[0].posY
                    if (self.hit_boxes[0].grass and self.hit_buttons[0].compatible_grass):
                        if (self.hit_buttons[0].my_tag==BASIC_TOWER_BUTTON_TAG):
                            game.all_towers.add(Basic_tower(game,x_box,y_box))
                    elif (self.hit_boxes[0].road and self.hit_buttons[0].compatible_road):
                        if (self.hit_buttons[0].my_tag==BALLISTA_BUTTON_TAG):
                            game.all_towers.add(Ballista(game,x_box,y_box))

        if not(self.left_click_pressed):
            self.carrying = False
        




    def render(self):
        pygame.mouse.set_visible(False)
        window.blit(self.current_image, (self.posX, self.posY)) 
        if self.carrying:
            window.blit(self.carried_image, (self.carried_x, self.carried_y)) 