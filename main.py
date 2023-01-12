import pygame
from pygame.locals import *
import sys
import time
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
while RUNNING:
      for event in pygame.event.get():
            if event.type == QUIT:
                  pygame.quit()
                  RUNNING = False
                  sys.exit()


      if START_WITH_SPACE_BAR:
            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_SPACE:
                        game.has_started = True
      else:
            game.has_started = True

      game.deal_with_mouse()

      if game.has_started:
            game.spawning_ennemies()
            game.fight()
            game.move_objects()
            game.die() 

      game.render()
      game.advance_time()


    
 

