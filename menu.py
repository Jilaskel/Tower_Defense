import pygame
from utilitaries import *
from functions import * 
from tower import * 

class Menu():
      def __init__(self,game):
            self.all_buttons = pygame.sprite.Group()
            self.all_options_buttons = pygame.sprite.Group()

            self.game = game

            self.margin = game.background.bush_width*5
            side = game.background.square_side
            self.space = side

            self.font_menu_size = int(30*RESIZE_COEFF)
            self.font_menu_color = (0,0,0)
            self.font_menu = pygame.font.Font(FONT_PATH,self.font_menu_size)
            self.font_menu_enlarged = pygame.font.Font(FONT_PATH,int(self.font_menu_size*MOUSE_OVER_ENLARGED_COEFF))

            self.text_price_offset = vec(0.40,0.67)  # multiplied by the button image size

            path = MENU_ARCANE_TOWER_BUTTON_IMAGE_PATH
            (x,y) = (self.margin,0)
            self.all_buttons.add(Tower_button(self,path,x,y,ARCANE_TOWER_BUTTON_TAG))

            path = MENU_FIRE_TOWER_BUTTON_IMAGE_PATH
            (x,y) = (self.margin+1.0*side,0)
            self.all_buttons.add(Tower_button(self,path,x,y,FIRE_TOWER_BUTTON_TAG))

            path = MENU_LIGHTNING_TOWER_BUTTON_IMAGE_PATH
            (x,y) = (self.margin+2.0*side,0)
            self.all_buttons.add(Tower_button(self,path,x,y,LIGHTNING_TOWER_BUTTON_TAG))

            path = MENU_ICE_TOWER_BUTTON_IMAGE_PATH
            (x,y) = (self.margin+3.0*side,0)
            self.all_buttons.add(Tower_button(self,path,x,y,ICE_TOWER_BUTTON_TAG))

            path = MENU_BALLISTA_BUTTON_IMAGE_PATH
            (x,y) = (self.margin+4.0*side,0)
            self.all_buttons.add(Tower_button(self,path,x,y,BALLISTA_BUTTON_TAG))

            path = MENU_CATAPULT_BUTTON_IMAGE_PATH
            (x,y) = (self.margin+5.0*side,0)
            self.all_buttons.add(Tower_button(self,path,x,y,CATAPULT_BUTTON_TAG))

            path = MENU_MENU_BUTTON_IMAGE_PATH
            (x,y) = (self.margin+11.5*side,0)
            self.all_options_buttons.add(Option_button(path,x,y,0.15,"menu"))

            self.rendering_layer = 0

            path_gold = MENU_GOLD_RESERVE_BUTTON_IMAGE_PATH
            self.gold_reserve_image = pygame.image.load(path_gold).convert_alpha()  
            image_size = vec(self.gold_reserve_image.get_size()) 
            self.gold_reserve_image = pygame.transform.scale(self.gold_reserve_image,image_size*MENU_GOLD_RESERVE_BUTTON_RESIZE_FACTOR) 
            self.gold_posX = 11*side
            self.gold_posY = 0*side

            path_score = MENU_SELECTION_IMAGE_PATH
            self.selection_image = pygame.image.load(path_score).convert_alpha()  
            image_size = vec(self.selection_image.get_size()) 
            # self.selection_image = pygame.transform.scale(self.selection_image,image_size*MENU_SELECTION_RESIZE_FACTOR) 
            self.selection_image = pygame.transform.scale(self.selection_image,MENU_SELECTION_SIZE) 
            self.selection_posX = 7.80*side
            self.selection_posY = 0.05*side

            path_score = MENU_SCORE_BUTTON_IMAGE_PATH
            self.score_image = pygame.image.load(path_score).convert_alpha()  
            image_size = vec(self.score_image.get_size()) 
            self.score_image = pygame.transform.scale(self.score_image,image_size*MENU_GOLD_RESERVE_BUTTON_RESIZE_FACTOR) 
            self.score_posX = 0.075*side
            self.score_posY = -0.075*side

            self.font_score_size = int(35*RESIZE_COEFF)
            self.font_score_color = (0,0,0)  ## black
            self.font_score = pygame.font.Font(FONT_PATH,self.font_score_size)
            self.font_posX = 0.45 * side
            self.font_posY = 0.60 * side

      def render(self):
            window.blit(self.selection_image,(self.selection_posX,self.selection_posY))
            window.blit(self.gold_reserve_image,(self.gold_posX,self.gold_posY))

            window.blit(self.score_image,(self.score_posX,self.score_posY))
            score = "Score"
            txt = self.font_score.render(score,True,self.font_score_color)
            window.blit(txt,(self.font_posX,self.font_posY-0.3*self.space))             
            score = convert_time(self.game.timer)
            txt = self.font_score.render(score,True,self.font_score_color)
            window.blit(txt,(self.font_posX,self.font_posY)) 

            # for opt_button in  self.all_options_buttons:
            #       opt_button.render()


class Tower_button(pygame.sprite.Sprite):
      def __init__(self,menu,path,x,y,tag):
            super().__init__()

            self.menu = menu
            self.rendering_layer = 0

            self.current_image = pygame.image.load(path).convert_alpha()   
            image_size = vec(self.current_image.get_size())
            resize_ratio = min(MENU_BUTTON_SIZE[0]/image_size[0],MENU_BUTTON_SIZE[1]/image_size[1])
            self.current_image = pygame.transform.scale(self.current_image,image_size*resize_ratio)  
            self.image_size = vec(self.current_image.get_size())

            self.rect = self.current_image.get_rect() 
            self.posX = x  
            self.posY = y   
            self.rect.x = self.posX
            self.rect.y = self.posY   

            self.mouse_over = False
            self.enlarged_image = pygame.image.load(path).convert_alpha()
            self.enlarged_image = pygame.transform.scale(self.enlarged_image,self.image_size*MOUSE_OVER_ENLARGED_COEFF) 
            self.enlarged_size = vec(self.enlarged_image.get_size()) 
            self.enlarged_posX = self.posX - int((self.enlarged_size[0]-self.image_size[0])*0.5)
            self.enlarged_posY = self.posY

            self.my_tag = tag
            if (self.my_tag==ARCANE_TOWER_BUTTON_TAG):
                  self.compatible_grass = True
                  self.compatible_road = False

                  self.image_to_carry = pygame.image.load(ARCANE_TOWER_ATTACK_IMAGE_PATH+"01.png").convert_alpha()
                  self.image_to_carry = pygame.transform.scale(self.image_to_carry,vec(self.image_to_carry.get_size())*ARCANE_TOWER_RESIZE_FACTOR)

                  self.range = ARCANE_TOWER_RANGE*(BACKGROUND_SQUARE_SIDE+BACKGROUND_SQUARE_SIDE)/2.0
                  self.range_hitbox = Range_Hitbox(self,BACKGROUND_SQUARE_SIDE,BACKGROUND_SQUARE_SIDE,self.range,circular=True)  

                  self.price = ARCANE_TOWER_PRICE 

            elif (self.my_tag==FIRE_TOWER_BUTTON_TAG):
                  self.compatible_grass = True
                  self.compatible_road = False

                  self.image_to_carry = pygame.image.load(FIRE_TOWER_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
                  self.image_to_carry = pygame.transform.scale(self.image_to_carry,vec(self.image_to_carry.get_size())*FIRE_TOWER_RESIZE_FACTOR)

                  self.range = FIRE_TOWER_RANGE*(BACKGROUND_SQUARE_SIDE+BACKGROUND_SQUARE_SIDE)/2.0
                  self.range_hitbox = Range_Hitbox(self,BACKGROUND_SQUARE_SIDE,BACKGROUND_SQUARE_SIDE,self.range,circular=True)  

                  self.price = FIRE_TOWER_PRICE 

            elif (self.my_tag==LIGHTNING_TOWER_BUTTON_TAG):
                  self.compatible_grass = True
                  self.compatible_road = False

                  self.image_to_carry = pygame.image.load(LIGHTNING_TOWER_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
                  self.image_to_carry = pygame.transform.scale(self.image_to_carry,vec(self.image_to_carry.get_size())*LIGHTNING_TOWER_RESIZE_FACTOR)

                  self.range = LIGHTNING_TOWER_RANGE*(BACKGROUND_SQUARE_SIDE+BACKGROUND_SQUARE_SIDE)/2.0
                  self.range_hitbox = Range_Hitbox(self,BACKGROUND_SQUARE_SIDE,BACKGROUND_SQUARE_SIDE,self.range,circular=True)  

                  self.price = LIGHTNING_TOWER_PRICE 

            elif (self.my_tag==ICE_TOWER_BUTTON_TAG):
                  self.compatible_grass = True
                  self.compatible_road = False

                  self.image_to_carry = pygame.image.load(ICE_TOWER_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
                  self.image_to_carry = pygame.transform.scale(self.image_to_carry,vec(self.image_to_carry.get_size())*ICE_TOWER_RESIZE_FACTOR)

                  self.range = ICE_TOWER_RANGE*(BACKGROUND_SQUARE_SIDE+BACKGROUND_SQUARE_SIDE)/2.0
                  self.range_hitbox = Range_Hitbox(self,BACKGROUND_SQUARE_SIDE,BACKGROUND_SQUARE_SIDE,self.range,circular=True)  

                  self.price = ICE_TOWER_PRICE 

            elif (self.my_tag==BALLISTA_BUTTON_TAG):
                  self.compatible_grass = False
                  self.compatible_road = True

                  self.image_to_carry = pygame.image.load(BALLISTA_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
                  self.image_to_carry = pygame.transform.scale(self.image_to_carry,vec(self.image_to_carry.get_size())*BALLISTA_RESIZE_FACTOR)  

                  self.range = BALLISTA_RANGE*(BACKGROUND_SQUARE_SIDE+BACKGROUND_SQUARE_SIDE)/2.0
                  self.range_hitbox = Range_Hitbox(self,BACKGROUND_SQUARE_SIDE,BACKGROUND_SQUARE_SIDE,self.range,circular=False,tag="Ballista")  

                  self.price = BALLISTA_PRICE 

            elif (self.my_tag==CATAPULT_BUTTON_TAG):
                  self.compatible_grass = False
                  self.compatible_road = True

                  self.image_to_carry = pygame.image.load(CATAPULT_ATTACK_IMAGE_PATH+"0001.png").convert_alpha()
                  self.image_to_carry = pygame.transform.scale(self.image_to_carry,vec(self.image_to_carry.get_size())*CATAPULT_RESIZE_FACTOR)  

                  self.range = CATAPULT_RANGE*(BACKGROUND_SQUARE_SIDE+BACKGROUND_SQUARE_SIDE)/2.0
                  self.range_hitbox = Range_Hitbox(self,BACKGROUND_SQUARE_SIDE,BACKGROUND_SQUARE_SIDE,self.range,circular=False,tag="Catapult")  

                  self.price = CATAPULT_PRICE 

            else : 
                self.compatible_grass = False
                self.compatible_road = False         

            self.text_price =  menu.font_menu.render(str(self.price),True,menu.font_menu_color)     
            self.text_price_enlarged =  menu.font_menu_enlarged.render(str(self.price),True,menu.font_menu_color)     

      def render(self):
            if self.mouse_over:
                  window.blit(self.enlarged_image, (self.enlarged_posX, self.enlarged_posY))    
                  window.blit(self.text_price_enlarged,(self.enlarged_posX+self.enlarged_size[0]*self.menu.text_price_offset[0], self.enlarged_posY+self.enlarged_size[1]*self.menu.text_price_offset[1])) 
            else:
                  window.blit(self.current_image, (self.posX, self.posY))  
                  window.blit(self.text_price,(self.posX+self.image_size[0]*self.menu.text_price_offset[0], self.posY+self.image_size[1]*self.menu.text_price_offset[1]))

            self.mouse_over = False 
            self.rendering_layer = 0  


class Option_button(pygame.sprite.Sprite):
      def __init__(self,path,x,y,resize_r,tag,obj=None):
            super().__init__()

            self.current_image = pygame.image.load(path).convert_alpha()   
            image_size = vec(self.current_image.get_size())
            resize_ratio = resize_r * RESIZE_COEFF
            self.current_image = pygame.transform.scale(self.current_image,image_size*resize_ratio)  
            self.image_size = vec(self.current_image.get_size())

            self.rendering_layer = 24.1

            self.rect = self.current_image.get_rect() 
            self.posX = x  
            self.posY = y   
            self.rect.x = self.posX
            self.rect.y = self.posY   

            self.mouse_over = False
            self.enlarged_image = pygame.image.load(path).convert_alpha()
            self.enlarged_image = pygame.transform.scale(self.enlarged_image,self.image_size*STARTING_MOUSE_OVER_ENLARGED_COEFF) 
            self.enlarged_size = vec(self.enlarged_image.get_size()) 
            self.enlarged_posX = self.posX - int((self.enlarged_size[0]-self.image_size[0])*0.5)
            # self.enlarged_posY = self.posY - int((self.enlarged_size[1]-self.image_size[1])*0.5)
            self.enlarged_posY = self.posY

            self.my_tag = tag
            if (obj):
                  self.obj = obj

      def action(self):
            match self.my_tag:
                  case "menu":
                        global_status.status = "In pause"
                  case "destroy":
                        self.obj.destroy()


      def render(self):
            if self.mouse_over:
                  window.blit(self.enlarged_image, (self.enlarged_posX, self.enlarged_posY))    
            else:
                  window.blit(self.current_image, (self.posX, self.posY))  

            self.mouse_over = False 