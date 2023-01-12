import pygame
import numpy as np
from utilitaries import *

def compute_rendering_layer_number(object):
    menu_height = WINDOW_HEIGHT/8.0
    side = BACKGROUND_SQUARE_SIDE
    y_obj = object.posY + object.image_size[1]*0.8
    number_of_layer = np.floor((y_obj-menu_height)/side)*3+2

    return number_of_layer