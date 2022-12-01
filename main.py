import pygame
from pygame.locals import *
import sys
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
            # if event.type == pygame.KEYDOWN:
            #       if event.key == pygame.K_SPACE:
            #             game.has_started = True

      game.has_started = True
      game.deal_with_mouse()

      if game.has_started:
            game.spawning_ennemies()
            game.fight()
            game.move_objects()
            game.die() 

      game.render()
      game.advance_time()


    
 

