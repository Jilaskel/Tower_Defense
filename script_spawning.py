import pygame
from ennemy import *
from utilitaries import *
import random
import numpy as np


GOBELIN_TAG = 1

class Script():
    def __init__(self):
        self.my_script = np.array([[2.0, GOBELIN_TAG, 1],     # temps en s, type, quantite
                       [8.0, GOBELIN_TAG, 2],
                       [16.0, GOBELIN_TAG, 3],
                       [20.0, GOBELIN_TAG, 3],
                       [24.0, GOBELIN_TAG, 3],
                       [100000, GOBELIN_TAG, 1]])
        self.line = 0
        

    def spawning_ennemies(self,game):
        time_next_ennemy = self.my_script[self.line,0]*1000
        if (game.timer>time_next_ennemy):
            for i in range (int(self.my_script[self.line,2])):
                if i==0:
                    path_number = random.randint(0,2)
                else:
                    path_number = (path_number+1)%3

                x_path = game.background.bush_width*0.1
                side = game.background.square_side
                y_path = game.background.menu_height + side*(1+2*path_number) 

                if (self.my_script[self.line,1]==GOBELIN_TAG):
                    game.all_ennemies.add(Gobelin(x_path,y_path))
            self.line += 1


