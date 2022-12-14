import pygame
from ennemy import *
from utilitaries import *
import random
import numpy as np


GOBELIN_TAG = 1
OGRE_TAG = 2

class Spawning_mode():
    def __init__(self,game):
        self.spawning_margin = game.background.bush_width*SPAWNING_MARGIN_SPACE
        
        if SPAWNING_WITH_SCRIPT:
            self.my_script = np.array([[2.0, GOBELIN_TAG, 1],     # temps en s, type, quantite
                        [8.0, GOBELIN_TAG, 2],
                        [16.0, GOBELIN_TAG, 3],
                        [20.0, GOBELIN_TAG, 3],
                        [24.0, GOBELIN_TAG, 3],
                        [100000, GOBELIN_TAG, 1]])
            self.line = 0
        else:
            self.number_gobelin_spawned = 1.0
            self.last_time_spawning_gobelin = SPAWNING_INITIAL_TIME - P1_GOBELIN_SPAWNING_PERIOD*self.number_gobelin_spawned            
            self.number_ogre_spawned = 1.0
            self.last_time_spawning_ogre = SPAWNING_INITIAL_TIME - P1_OGRE_SPAWNING_PERIOD*self.number_gobelin_spawned            
        

    def spawning_ennemies(self,game):
        time = game.timer/1000.0  # in second
        if SPAWNING_WITH_SCRIPT:
            time_next_ennemy = self.my_script[self.line,0]
            if (time>time_next_ennemy):
                self.spawn(game,int(self.my_script[self.line,1]),int(self.my_script[self.line,2]))
                self.line += 1
        else:
            if (time<(TIME_P1)):
                
                cooldown = P1_GOBELIN_SPAWNING_PERIOD*self.number_gobelin_spawned 
                if ((time-self.last_time_spawning_gobelin)>cooldown):
                    self.last_time_spawning_gobelin = time
                    self.number_gobelin_spawned = random.randint(1,3)
                    self.spawn(game,GOBELIN_TAG,self.number_gobelin_spawned)

                cooldown = P1_OGRE_SPAWNING_PERIOD*self.number_ogre_spawned 
                if ((time-self.last_time_spawning_ogre)>cooldown):
                    self.last_time_spawning_ogre = time
                    self.number_ogre_spawned = random.randint(1,3)
                    self.spawn(game,OGRE_TAG,self.number_ogre_spawned)
                        

    def spawn(self,game,TAG,number_of_ennemies):
        for i in range (number_of_ennemies):
            if i==0:
                path_number = random.randint(0,2)
            else:
                path_number = (path_number+1)%3

            x_path = self.spawning_margin
            side = game.background.square_side
            y_path = game.background.menu_height + side*(1+2*path_number) 

            if (TAG==GOBELIN_TAG):
                game.all_ennemies.add(Gobelin(x_path,y_path))

            if (TAG==OGRE_TAG):
                game.all_ennemies.add(OGRE(x_path,y_path))