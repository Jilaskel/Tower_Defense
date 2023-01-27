import pygame
from utilitaries import *
from menu import * 

class Selected_object():
    def __init__(self):
        self.on = False
        self.mask_color = (255,255,255)
        self.mask_transparency = 100
        self.rendering_layer = 24

        side = BACKGROUND_SQUARE_SIDE
        self.size_mini = [0.75*side,0.6*side]

        self.mini_posX = 8.1*side
        self.mini_posY = 0.08*side

        self.font_size = int(25*RESIZE_COEFF)
        self.font_color = (0,0,0)  ## black
        self.font = pygame.font.Font(FONT_PATH,self.font_size)
        self.font_posX = 9.0 * side
        self.font_posY = 0.15 * side

        self.destroy_path = MENU_DESTROY_BUTTON_IMAGE_PATH
        self.destroy_posX= 10*side
        self.destroy_posY= 0.5*side

        self.destroyable = False

    def update(self,game,object):
        self.clear()
        self.on = True
        self.obj = object

        if (hasattr(object,'destroy')) and (callable(object.destroy)):
            self.destroyable = True
            self.destroy_button = Option_button(self.destroy_path,self.destroy_posX,self.destroy_posY,0.15,"destroy",object)
            game.menu.all_options_buttons.add(self.destroy_button)
        else:
            self.destroyable = False

    def clear(self):
        if self.on:
            self.on = False
            if self.destroyable:
                pygame.sprite.Sprite.kill(self.destroy_button)


    def render(self):
        if self.on:
            if (pygame.sprite.Sprite.alive(self.obj)):
                img = self.obj.current_image
                mask = pygame.mask.from_surface(img)
                mask_image = mask.to_surface(setcolor=self.mask_color)
                mask_image.set_colorkey((0, 0, 0))
                mask_image.set_alpha(self.mask_transparency)
                window.blit(mask_image, (self.obj.posX,self.obj.posY))

                self.mini_image = self.obj.current_image.convert_alpha()
                image_size = vec(self.mini_image.get_size())
                resize_ratio = min(self.size_mini[0]/image_size[0],self.size_mini[1]/image_size[1])
                self.mini_image = pygame.transform.scale(self.mini_image,image_size*resize_ratio) 
                window.blit(self.mini_image, (self.mini_posX,self.mini_posY))

                txt = "HP :  " + str(int(self.obj.hp)) + " / " + str(int(self.obj.my_data.hp_max))
                txt_hp = self.font.render(txt,True,self.font_color)
                window.blit(txt_hp,(self.font_posX,self.font_posY)) 
            else:
                self.clear()

