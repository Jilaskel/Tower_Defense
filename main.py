import pygame
import sys
from thread import * 
 
 
############################# 
## MAIN LOOP
#############################

threadLock = threading.Lock()

thread1 = myThread(1)
thread2 = myThread(2)

# Start new Threads : call the run method
thread1.start()
thread2.start()

thread2.waiting(thread1)
game = thread1.game
starting_menu = thread1.starting_menu
pause_menu = thread1.pause_menu
game_over_menu = thread1.game_over_menu
thread1.join()  # not sure, seems useless

print("Starting game")

while RUNNING:

      game.get_event()

      match global_status.status:

            case "Starting menu":
                  starting_menu.advance()
                  starting_menu.render()

            case "In game":
                  game.deal_with_mouse()

                  game.spawning_ennemies()
                  game.fight()
                  game.move_objects()
                  game.die() 

                  game.render()
                  game.advance_time()

            case "In pause":
                  game.render(update=False)

                  pause_menu.deal_with_mouse()                  
                  pause_menu.render()                  

            case "Game Over":
                  game.render(update=False)

                  game_over_menu.deal_with_mouse()                  
                  game_over_menu.render()  

            case "Quitting":
                  pygame.quit()
                  RUNNING = False
                  sys.exit()

    
 

