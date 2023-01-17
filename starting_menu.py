import pygame
from utilitaries import *

class Starting_menu():
      def __init__(self,game):
            self.all_buttons = pygame.sprite.Group()

            self.game = game

            self.mouse = Starting_mouse(self)

            self.font_size = int(140*RESIZE_COEFF)
            self.font = pygame.font.Font(LOADING_FONT_PATH,self.font_size)
            self.font_color = (243,243,243)
            title = "You Shall Not Pass"
            self.title1 = self.font.render("You Shall",True,self.font_color)
            self.title2 = self.font.render("Not Pass",True,self.font_color)

            self.pannel_image = pygame.image.load(STARTING_MENU_PANNEL_PATH).convert_alpha()   
            image_size = vec(self.pannel_image.get_size())
            resize_ratio = 0.45 * RESIZE_COEFF
            self.pannel_image = pygame.transform.scale(self.pannel_image,image_size*resize_ratio)  

            self.margin = vec(WINDOW_WIDTH*0.67,WINDOW_HEIGHT*0.20)
            space = WINDOW_HEIGHT/6

            self.font_menu_size = int(60*RESIZE_COEFF)
            self.font_menu_color = (0,0,0)
            self.font_menu = pygame.font.Font(FONT_PATH,self.font_menu_size)
            self.font_menu_enlarged = pygame.font.Font(FONT_PATH,int(self.font_menu_size*STARTING_MOUSE_OVER_ENLARGED_COEFF))


            path = STARTING_MENU_BUTTON_2_PATH
            (x,y) = (self.margin[0]+0.1*space,self.margin[1]-0.2*space)
            self.all_buttons.add(Starting_button(self,path,x,y,"Play",0.20,vec(0.35,0.35)))

            path = STARTING_MENU_BUTTON_1_PATH
            (x,y) = (self.margin[0],self.margin[1]+1.0*space)
            self.all_buttons.add(Starting_button(self,path,x,y,"Parameters",0.35,vec(0.15,0.30)))

            (x,y) = (self.margin[0],self.margin[1]+2.0*space)
            self.all_buttons.add(Starting_button(self,path,x,y,"Credits",0.35,vec(0.30,0.30)))

            (x,y) = (self.margin[0],self.margin[1]+3.0*space)
            self.all_buttons.add(Starting_button(self,path,x,y,"Quit",0.35,vec(0.38,0.30)))

            self.rendering_layer = 0

            self.my_timer = 0
            self.anim_frame_r = 0
            self.anim_frame_a = 0

            self.image_attacking = []
            self.number_frame_attacking = ARCANE_TOWER_NUMBER_FRAME_ATTACKING
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(ARCANE_TOWER_ATTACK_IMAGE_PATH+str(i).zfill(2)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],vec(self.image_attacking[i-1].get_size())*ARCANE_TOWER_RESIZE_FACTOR*2)
            self.anim_total_time_a = ARCANE_TOWER_ANIMATION_ATTACKING_TOTAL_TIME*2
            self.time_per_frame_a = self.anim_total_time_a/self.number_frame_attacking # in ms

            self.image_reloading = []
            self.number_frame_reloading = ARCANE_TOWER_NUMBER_FRAME_RELOADING
            for i in range(1,self.number_frame_reloading+1):
                  self.image_reloading.append(pygame.image.load(ARCANE_TOWER_RELOAD_IMAGE_PATH+str(i).zfill(2)+".png").convert_alpha())   
                  self.image_reloading[i-1] = pygame.transform.scale(self.image_reloading[i-1],vec(self.image_reloading[i-1].get_size())*ARCANE_TOWER_RESIZE_FACTOR*2)
            self.anim_total_time_r = ARCANE_TOWER_ANIMATION_RELOADING_TOTAL_TIME*2
            self.time_per_frame_r = self.anim_total_time_r/self.number_frame_reloading # in ms

            self.reloading = False
            self.current_image= self.image_attacking[self.anim_frame_a]

      def anim_image(self):
            self.my_timer += self.timestep
            if self.reloading:
                  if self.my_timer>self.time_per_frame_r:
                        self.anim_frame_r += 1
                        self.my_timer = 0.0
                        if (self.anim_frame_r==self.number_frame_reloading):
                              self.anim_frame_r = 0
                              self.reloading = False
                              self.current_image= self.image_attacking[self.anim_frame_a]
                        else:
                              self.current_image= self.image_reloading[self.anim_frame_r]
            else:
                  if self.my_timer>self.time_per_frame_a:
                        self.anim_frame_a += 1
                        self.my_timer = 0.0
                        if (self.anim_frame_a==self.number_frame_attacking):
                              self.anim_frame_a = 0
                              self.reloading = True
                              self.current_image= self.image_reloading[self.anim_frame_r]
                        else:
                              self.current_image= self.image_attacking[self.anim_frame_a]            


      def advance(self):
            CLOCK.tick(FPS)
            self.timestep = CLOCK.get_time()
                              
            self.anim_image()

            self.mouse.doing_stuff()

      def render(self):
            window.fill((0,0,0))

            window.blit(self.title1, (330*RESIZE_COEFF, 100*RESIZE_COEFF))
            window.blit(self.title2, (330*RESIZE_COEFF, 300*RESIZE_COEFF))

            window.blit(self.current_image, (500*RESIZE_COEFF, 500*RESIZE_COEFF))

            window.blit(self.pannel_image, (1050*RESIZE_COEFF, 50*RESIZE_COEFF))

            for button in self.all_buttons:
                  button.render()

            self.mouse.render()
            pygame.display.update()


class Starting_mouse(pygame.sprite.Sprite):
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

                  if (self.hit_buttons[0].tag=="Play"):
                        global_status.in_starting_menu = False
                        global_status.in_game= True
                        self.menu.game.all_mixers.music_mixer.rewind()

                  elif (self.hit_buttons[0].tag=="Parameters"):
                        pass

                  elif (self.hit_buttons[0].tag=="Credits"):
                        pass

                  elif (self.hit_buttons[0].tag=="Quit"):
                        pygame.quit()
                        RUNNING = False
                        sys.exit()


    def render(self):
        pygame.mouse.set_visible(False)
        window.blit(self.current_image, (self.posX, self.posY)) 

class Starting_button(pygame.sprite.Sprite):
      def __init__(self,menu,path,x,y,text,resize_r,text_offset):
            super().__init__()

            self.menu = menu
            self.rendering_layer = 0

            self.current_image = pygame.image.load(path).convert_alpha()   
            image_size = vec(self.current_image.get_size())
            resize_ratio = resize_r * RESIZE_COEFF
            self.current_image = pygame.transform.scale(self.current_image,image_size*resize_ratio)  
            self.image_size = vec(self.current_image.get_size())

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
            self.enlarged_posY = self.posY - int((self.enlarged_size[1]-self.image_size[1])*0.5)

            self.tag = text     

            self.text =  menu.font_menu.render(text,True,menu.font_menu_color)     
            self.text_enlarged =  menu.font_menu_enlarged.render(text,True,menu.font_menu_color)     

            self.text_offset = text_offset


      def render(self):
            if self.mouse_over:
                  window.blit(self.enlarged_image, (self.enlarged_posX, self.enlarged_posY))    
                  window.blit(self.text_enlarged,(self.enlarged_posX+self.enlarged_size[0]*self.text_offset[0], self.enlarged_posY+self.enlarged_size[1]*self.text_offset[1])) 
            else:
                  window.blit(self.current_image, (self.posX, self.posY))  
                  window.blit(self.text,(self.posX+self.image_size[0]*self.text_offset[0], self.posY+self.image_size[1]*self.text_offset[1]))

            self.mouse_over = False 
            self.rendering_layer = 0  
