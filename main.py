import pygame
from pygame.locals import *
import sys
import random
import time
from game import *
 
 
############################# 
## MAIN LOOP
#############################

game_has_started = False
game = Game()
while RUNNING:
      for event in pygame.event.get():
            if event.type == QUIT:
                  pygame.quit()
                  RUNNING = False
                  sys.exit()

      # Event handling for a range of different key presses    
            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_SPACE:
                        game_has_started = True

      if game_has_started:
            game.move_objects()
            game.fight()
            
      game.render()

    
 

