import pygame
from utilitaries import *
from menu import * 
from tower import *


class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.static_image = pygame.image.load(MOUSE_IMAGE_PATH).convert_alpha()  
        self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*MOUSE_RESIZE_FACTOR)        
        self.current_image = self.static_image

        side = BACKGROUND_SQUARE_SIDE
        self.valid_box_image = pygame.image.load(MOUSE_VALID_BOX_IMAGE_PATH).convert_alpha()
        self.valid_box_image = pygame.transform.scale(self.valid_box_image,(side,side))       
        self.valid_box_image.set_alpha(MOUSE_VALID_BOX_IMAGE_ALPHA)

        self.not_valid_box_image = pygame.image.load(MOUSE_NOT_VALID_BOX_IMAGE_PATH).convert_alpha()
        self.not_valid_box_image = pygame.transform.scale(self.not_valid_box_image,(side,side))       
        self.not_valid_box_image.set_alpha(MOUSE_NOT_VALID_BOX_IMAGE_ALPHA)

        self.ratio_for_hitbox = MOUSE_RATIO_FOR_HITBOX

        self.carrying = False
        self.box_valid = False
        self.box_not_valid = False

        self.hit_towers = []

    def doing_stuff(self,game):
        (x,y) = pygame.mouse.get_pos()
        self.posX = x
        self.posY = y

        self.rect = self.current_image.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY

        self.state_mouse = pygame.mouse.get_pressed()
        self.left_click_pressed = self.state_mouse[0]
        self.middle_click_pressed = self.state_mouse[1]
        self.right_click_pressed = self.state_mouse[2]


        if not(self.carrying):
            self.hit_buttons = pygame.sprite.spritecollide(self, game.menu.all_buttons, False, pygame.sprite.collide_rect_ratio(self.ratio_for_hitbox))

            if ((self.hit_buttons) and (self.left_click_pressed)):
                self.carrying = True
                self.carried_image = self.hit_buttons[0].image_to_carry
                self.carried_image.set_alpha(MOUSE_CARRIED_IMAGE_ALPHA)

                self.carried_rect = self.carried_image.get_rect()
                self.carried_width = self.carried_rect.width
                self.carried_height = self.carried_rect.height

        self.box_valid = False
        self.box_not_valid = False
        if self.carrying:
            self.carried_x = self.posX - self.carried_width*0.5
            self.carried_y = self.posY - self.carried_height*0.5

            self.hit_boxes = pygame.sprite.spritecollide(self, game.grid.all_boxes, False)
            
            if self.hit_boxes:
                self.x_box = self.hit_boxes[0].posX
                self.y_box = self.hit_boxes[0].posY
                if (self.hit_boxes[0].grass and self.hit_buttons[0].compatible_grass):
                    self.box_valid = True
                    if not(self.left_click_pressed):
                        if (self.hit_buttons[0].my_tag==ARCANE_TOWER_BUTTON_TAG):
                            game.all_towers.add(Arcane_tower(game,self.x_box,self.y_box))
                elif (self.hit_boxes[0].road and self.hit_buttons[0].compatible_road):
                    self.box_valid = True
                    if not(self.left_click_pressed):
                        if (self.hit_buttons[0].my_tag==BALLISTA_BUTTON_TAG):
                            game.all_towers.add(Ballista(game,self.x_box,self.y_box))
                else:
                    self.box_not_valid = True
        else: #display range?
            self.hit_towers = pygame.sprite.spritecollide(self, game.all_towers, False, pygame.sprite.collide_rect_ratio(self.ratio_for_hitbox))
                

        if not(self.left_click_pressed):
            self.carrying = False

    def render(self):
        pygame.mouse.set_visible(False)
        window.blit(self.current_image, (self.posX, self.posY)) 
        if self.carrying:
            hitbox = self.hit_buttons[0].range_hitbox
            window.blit(hitbox.image, (self.carried_x+hitbox.offset[0], self.carried_y+hitbox.offset[1]))  # display range hitbow while dragging
            window.blit(self.carried_image, (self.carried_x, self.carried_y))
            if self.box_valid:
                window.blit(self.valid_box_image, (self.x_box, self.y_box))
            elif self.box_not_valid:
                window.blit(self.not_valid_box_image, (self.x_box, self.y_box))
        else:
            if self.hit_towers:
                window.blit(self.hit_towers[0].range_hitbox.image, (self.hit_towers[0].range_hitbox.posX, self.hit_towers[0].range_hitbox.posY))
