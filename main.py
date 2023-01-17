import pygame
from pygame.locals import *
import sys
import time
from starting_menu import *
from game import *
from thread import * 
 
 
############################# 
## MAIN LOOP
#############################

game_has_started = False

threadLock = threading.Lock()

thread1 = myThread(1)
thread2 = myThread(2)

# Start new Threads : call the run method
thread1.start()
thread2.start()

thread2.waiting(thread1)
game = thread1.game
thread1.join()  # not sure, seems useless

print("Starting game")
starting_menu = Starting_menu(game)
while RUNNING:
      for event in pygame.event.get():
            if event.type == QUIT:
                  pygame.quit()
                  RUNNING = False
                  sys.exit()

      if (global_status.in_starting_menu):

            starting_menu.advance()
            starting_menu.render()

      elif (global_status.in_game):

            game.deal_with_mouse()

            if game.is_running:
                  game.spawning_ennemies()
                  game.fight()
                  game.move_objects()
                  game.die() 

            game.render()
            game.advance_time()


    
 

