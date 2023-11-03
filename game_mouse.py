import pygame
from pygame.locals import *
from utilitaries import *
from menu import * 
from tower import *


class Game_mouse(pygame.sprite.Sprite):
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
        self.hit_buttons = []

        self.rendering_layer = TOTAL_NUMBER_RENDERING_LAYER

        self.pressable_keys = [K_a,K_z,K_e,K_r,K_t,K_y]


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

        self.hit_object = None

        self.left_clicked = False
        self.right_clicked = False
        self.event_key = None
        for event in game.all_events:
            if (event.type == MOUSEBUTTONDOWN):
                if event.button==1:  
                    self.left_clicked = True
                if event.button==3:
                    self.right_clicked = True
            elif (event.type == KEYDOWN):
                if event.key in self.pressable_keys:
                    self.event_key = event
                    self.hit_buttons = []
                    self.carrying = False
                    if (self.event_key.key == K_a):
                        for button in game.menu.all_buttons:
                            if button.my_tag==BALLISTA_BUTTON_TAG:
                                self.hit_buttons.append(button)
                                break
                    if (self.event_key.key == K_z):
                        for button in game.menu.all_buttons:
                            if button.my_tag==CATAPULT_BUTTON_TAG:
                                self.hit_buttons.append(button)
                                break
                    if (self.event_key.key == K_e):
                        for button in game.menu.all_buttons:
                            if button.my_tag in ARCANE_TOWER_BUTTONS_TAG:
                                self.hit_buttons.append(button)
                                break
                    if (self.event_key.key == K_r):
                        for button in game.menu.all_buttons:
                            if button.my_tag in ICE_TOWER_BUTTONS_TAG:
                                self.hit_buttons.append(button)
                                break
                    if (self.event_key.key == K_t):
                        for button in game.menu.all_buttons:
                            if button.my_tag in LIGHTNING_TOWER_BUTTONS_TAG:
                                self.hit_buttons.append(button)
                                break
                    if (self.event_key.key == K_y):
                        for button in game.menu.all_buttons:
                            if button.my_tag in FIRE_TOWER_BUTTONS_TAG:
                                self.hit_buttons.append(button)
                                break  

        if not(self.event_key):
            self.hit_buttons = pygame.sprite.spritecollide(self, game.menu.all_buttons, False, pygame.sprite.collide_rect_ratio(self.ratio_for_hitbox))  
            if (self.hit_buttons):
                self.hit_buttons[0].mouse_over = True
                self.hit_buttons[0].rendering_layer = 22
                if self.left_clicked:
                    self.carrying = False

        if not(self.carrying):
            if (self.hit_buttons):
                if (self.left_clicked or self.event_key):
                    self.my_hit_button = self.hit_buttons[0]
                    self.carrying = True
                    self.carried_image = self.my_hit_button.image_to_carry
                    self.carried_image.set_alpha(MOUSE_CARRIED_IMAGE_ALPHA)

                    self.carried_rect = self.carried_image.get_rect()
                    self.carried_width = self.carried_rect.width
                    self.carried_height = self.carried_rect.height               
            else:
                self.hit_opt_buttons = pygame.sprite.spritecollide(self, game.menu.all_options_buttons, False, pygame.sprite.collide_rect_ratio(self.ratio_for_hitbox))
                if (self.hit_opt_buttons):
                    self.hit_opt_buttons[0].mouse_over = True
                    self.hit_opt_buttons[0].rendering_layer = 22
                    if self.left_clicked:
                        self.hit_opt_buttons[0].action(game)   
                if not(self.hit_opt_buttons):
                    if self.left_clicked:
                        self.hit_object = pygame.sprite.spritecollide(self, game.all_towers, False, pygame.sprite.collide_rect_ratio(self.ratio_for_hitbox))
                        if not(self.hit_object):
                            self.hit_object = pygame.sprite.spritecollide(self, game.all_ennemies, False, pygame.sprite.collide_rect_ratio(self.ratio_for_hitbox))
                        if not(self.hit_object):
                            self.hit_object = pygame.sprite.spritecollide(self, game.all_dead_bodies.all_iced_bodies, False, pygame.sprite.collide_rect_ratio(self.ratio_for_hitbox))
                        if not(self.hit_object):
                            self.hit_object = pygame.sprite.spritecollide(self, game.base.all_gates, False, pygame.sprite.collide_rect_ratio(self.ratio_for_hitbox))
                            
                        if self.hit_object:
                            game.selected_object.update(game,self.hit_object[0])                        
                        else:
                            game.selected_object.clear()


        self.box_valid = False
        self.box_not_valid = False
        if self.carrying:
            game.show_grid = True
            self.carried_x = self.posX - self.carried_width*0.4
            self.carried_y = self.posY - self.carried_height*0.75

            self.hit_boxes = pygame.sprite.spritecollide(self, game.grid.all_boxes, False)
            
            if self.hit_boxes:
                self.x_box = self.hit_boxes[0].posX
                self.y_box = self.hit_boxes[0].posY

                if (self.hit_boxes[0].grass and self.my_hit_button.compatible_grass):
                    if not(self.hit_boxes[0].occupied):
                        self.box_valid = True
                        if (self.left_clicked):
                            if (game.gold.amount >= self.my_hit_button.price):
                                game.all_towers.add_tower(game,self.hit_boxes[0],self.my_hit_button.my_tag)
                                self.hit_boxes[0].occupied = True
                                self.carrying = False
                                game.show_grid = False
                            else:
                                game.all_error_messages.add_error_message_anim("Not enough gold",self.x_box,self.y_box)
                    else:
                        self.box_not_valid = True
                        if self.left_clicked:
                            game.all_error_messages.add_error_message_anim("This spot has already been built",self.x_box,self.y_box)  

                elif (self.hit_boxes[0].road and self.my_hit_button.compatible_road):
                    if not(self.hit_boxes[0].occupied):
                        self.box_valid = True
                        if self.left_clicked:
                            if (game.gold.amount >= self.my_hit_button.price):
                                game.all_towers.add_tower(game,self.hit_boxes[0],self.my_hit_button.my_tag)
                                self.hit_boxes[0].occupied = True
                                self.carrying = False
                                game.show_grid = False
                            else:
                                game.all_error_messages.add_error_message_anim("Not enough gold",self.x_box,self.y_box)
                    else:
                        self.box_not_valid = True
                        if self.left_clicked:
                            game.all_error_messages.add_error_message_anim("This spot has already been built",self.x_box,self.y_box)  

                else:
                    self.box_not_valid = True
                    if self.left_clicked:
                        game.all_error_messages.add_error_message_anim("Cannot be build here",self.x_box,self.y_box)
                         
        else: #display range?
            self.hit_towers = pygame.sprite.spritecollide(self, game.all_towers, False, pygame.sprite.collide_rect_ratio(self.ratio_for_hitbox))
      

        if (self.right_clicked):
            self.carrying = False
            game.show_grid = False




    def render(self):
        pygame.mouse.set_visible(False)
        window.blit(self.current_image, (self.posX, self.posY)) 

        if self.carrying:
            hitbox = self.my_hit_button.range_hitbox
            window.blit(hitbox.image, (self.carried_x+hitbox.offset[0], self.carried_y+hitbox.offset[1]))  # display range hitbow while dragging
            window.blit(self.carried_image, (self.carried_x, self.carried_y))
            if self.box_valid:
                window.blit(self.valid_box_image, (self.x_box, self.y_box))
            elif self.box_not_valid:
                window.blit(self.not_valid_box_image, (self.x_box, self.y_box))
        else:
            if self.hit_towers:
                window.blit(self.hit_towers[0].range_hitbox.image, (self.hit_towers[0].range_hitbox.posX, self.hit_towers[0].range_hitbox.posY))
