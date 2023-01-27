import threading
from game import * 
from starting_menu import *
from pause_menu import *
from game_over_menu import *
import pygame
from utilitaries import *

class myThread (threading.Thread):
   def __init__(self,id):
      threading.Thread.__init__(self)
      self.id = id

   def run(self):
        # print("Starting thread"+str(self.id))
        if self.id == 1:
            self.load_game()    
            # while(True):
            #     pass
     
        

   def load_game(self):
        print("Loading game")

        self.game = Game()
        self.starting_menu = Starting_menu(self.game)
        self.pause_menu = Pause_menu(self.game)
        self.game_over_menu = Game_over_menu(self.game)

        loading_progress.value += 10


   def waiting(self,thread1):
        # print("Start waiting")
        self.loading_screen = Loading_screen()
        while (thread1.is_alive()):  # True as long as thread1 is in run()
            self.loading_screen.advance()
            self.loading_screen.render()
        self.join()   # not sure, seems useless


class Loading_screen():
    def __init__(self):
        self.my_timer = 0
        self.move_frame = 0

        self.number_frame_walking = GOBLIN_NUMBER_FRAME_WALKING
        self.image_walking = []
        for i in range(1,self.number_frame_walking+1):
                self.image_walking.append(pygame.image.load(GOBLIN_WALKING_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha())  
                self.image_walking[i-1] = pygame.transform.scale(self.image_walking[i-1],vec(self.image_walking[i-1].get_size())*RESIZE_COEFF)
        self.anim_total_time_w = GOBLIN_ANIMATION_WALKING_TOTAL_TIME  # in ms
        self.time_per_frame_w = self.anim_total_time_w/self.number_frame_walking # in ms  

        self.font_size = int(140*RESIZE_COEFF)
        self.font = pygame.font.Font(LOADING_FONT_PATH,self.font_size)
        self.font_color = (243,243,243)

    def advance(self):
        CLOCK.tick(FPS)
        self.my_timer += CLOCK.get_time()
        if self.my_timer>self.time_per_frame_w:
            self.move_frame += 1
            self.move_frame = self.move_frame%self.number_frame_walking
            self.my_timer = 0.0
                        
        self.current_image= self.image_walking[self.move_frame]

    def render(self):
        window.fill((0,0,0))  # black background
        message = "Loading..."
        text = self.font.render(message,True,self.font_color)
        window.blit(text, (680*RESIZE_COEFF, 200*RESIZE_COEFF))
        message = str(loading_progress.value) + "%"
        text = self.font.render(message,True,self.font_color)
        window.blit(text, (820*RESIZE_COEFF, 380*RESIZE_COEFF))
        window.blit(self.current_image, (850*RESIZE_COEFF, 600*RESIZE_COEFF))
        pygame.display.update()

