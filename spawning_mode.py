import pygame
from ennemy import *
from utilitaries import *
import random
import numpy as np


GOBLIN_TAG = 1
OGRE_TAG = 2
BLUE_NEC_TAG = 3
RED_NEC_TAG = 4
GREEN_NEC_TAG = 5
KAMIKAZE_TAG = 6
DRAGON_TAG = 7


class Spawning_mode():
    def __init__(self,game):
        self.spawning_margin = game.background.bush_width*SPAWNING_MARGIN_SPACE
        
        if SPAWNING_WITH_SCRIPT:
            self.my_script = np.array([[2.0, GOBLIN_TAG, 1],     # temps en s, type, quantite
                        [8.0, GOBLIN_TAG, 2],
                        [16.0, GOBLIN_TAG, 3],
                        [20.0, GOBLIN_TAG, 3],
                        [24.0, GOBLIN_TAG, 3],
                        [100000, GOBLIN_TAG, 1]])
            self.line = 0
        else:
            self.number_goblin_spawned = 1.0
            self.last_time_spawning_goblin = SPAWNING_INITIAL_TIME - P1_GOBLIN_SPAWNING_PERIOD*self.number_goblin_spawned            
            self.number_ogre_spawned = 1.0
            self.last_time_spawning_ogre = SPAWNING_INITIAL_TIME - P1_OGRE_SPAWNING_PERIOD*self.number_ogre_spawned 
            self.number_blue_nec_spawned = 1.0
            self.last_time_spawning_blue_nec = SPAWNING_INITIAL_TIME - P1_BLUE_NEC_SPAWNING_PERIOD*self.number_blue_nec_spawned             
            self.number_dragon_spawned = 1.0
            self.last_time_spawning_dragon = SPAWNING_INITIAL_TIME - P1_DRAGON_SPAWNING_PERIOD*self.number_dragon_spawned   

    def reset(self):
        self.number_goblin_spawned = 1.0
        self.last_time_spawning_goblin = SPAWNING_INITIAL_TIME - P1_GOBLIN_SPAWNING_PERIOD*self.number_goblin_spawned            
        self.number_ogre_spawned = 1.0
        self.last_time_spawning_ogre = SPAWNING_INITIAL_TIME - P1_OGRE_SPAWNING_PERIOD*self.number_goblin_spawned            
        self.number_blue_nec_spawned = 1.0
        self.last_time_spawning_blue_nec = SPAWNING_INITIAL_TIME - P1_BLUE_NEC_SPAWNING_PERIOD*self.number_blue_nec_spawned   
        self.number_dragon_spawned = 1.0
        self.last_time_spawning_dragon = SPAWNING_INITIAL_TIME - P1_DRAGON_SPAWNING_PERIOD*self.number_dragon_spawned              

    def spawning_ennemies(self,game):
        time = game.timer/1000.0  # in second
        if SPAWNING_WITH_SCRIPT:
            time_next_ennemy = self.my_script[self.line,0]
            if (time>time_next_ennemy):
                self.spawn(game,int(self.my_script[self.line,1]),int(self.my_script[self.line,2]))
                self.line += 1
        else:
            if (time<(TIME_P1)):
                
                cooldown = P1_GOBLIN_SPAWNING_PERIOD*self.number_goblin_spawned*1000 
                if ((time-self.last_time_spawning_goblin)>cooldown):
                    self.last_time_spawning_goblin = time
                    self.number_goblin_spawned = random.randint(1,3)
                    self.spawn(game,GOBLIN_TAG,self.number_goblin_spawned)

                cooldown = P1_OGRE_SPAWNING_PERIOD*self.number_ogre_spawned*1000 
                if ((time-self.last_time_spawning_ogre)>cooldown):
                    self.last_time_spawning_ogre = time
                    self.number_ogre_spawned = random.randint(1,3)
                    self.spawn(game,OGRE_TAG,self.number_ogre_spawned)

                cooldown = P1_BLUE_NEC_SPAWNING_PERIOD*self.number_blue_nec_spawned 
                if ((time-self.last_time_spawning_blue_nec)>cooldown):
                    self.last_time_spawning_blue_nec = time
                    self.number_blue_nec_spawned = random.randint(1,3)
                    self.spawn(game,BLUE_NEC_TAG,self.number_blue_nec_spawned)

                cooldown = P1_DRAGON_SPAWNING_PERIOD*self.number_dragon_spawned*1000 ## comment *0 to have normal spawning 
                if ((time-self.last_time_spawning_dragon)>cooldown):
                    self.last_time_spawning_dragon = time
                    self.number_dragon_spawned = random.randint(1,3)
                    self.spawn(game,DRAGON_TAG,self.number_dragon_spawned)                        

    def spawn(self,game,TAG,number_of_ennemies):
        for i in range (number_of_ennemies):
            if i==0:
                path_number = random.randint(0,2)
            else:
                path_number = (path_number+1)%3

            x_path = self.spawning_margin
            side = game.background.square_side
            
            # y_path = game.background.menu_height + side*(1+2*path_number) + (random.randint(0,1)-0.5)*side*0.5  #used for tests
            rand_offset = random.random()-0.5
            y_path = game.background.menu_height + side*(1+2*path_number) + rand_offset*side*0.5

            if (TAG==GOBLIN_TAG):
                game.all_ennemies.add_goblin(x_path,y_path,rand_offset)

            if (TAG==OGRE_TAG):
                game.all_ennemies.add_ogre(x_path,y_path,rand_offset)

            if (TAG==BLUE_NEC_TAG):
                game.all_ennemies.add_blue_nec(x_path,y_path,rand_offset)

            if (TAG==DRAGON_TAG):
                game.all_ennemies.add_dragon(x_path,y_path,rand_offset)