import pygame
import numpy as np
from utilitaries import *

def compute_rendering_layer_number(object):
    menu_height = WINDOW_HEIGHT/8.0
    side = BACKGROUND_SQUARE_SIDE
    y_obj = object.posY + object.image_size[1]*0.8
    number_of_layer = np.floor((y_obj-menu_height)/side)*3+2
    # y_obj = object.posY + object.image_size[1]*1.0
    # number_of_layer = ((y_obj-menu_height)/side)*3+2

    return number_of_layer

def convert_time(mseconde):
    seconde = mseconde/1000
    hour = seconde /3600
    seconde %= 3600
    minute = seconde/60
    seconde%=60

    txt_hour = str(int(hour)).zfill(2)
    txt_minute = str(int(minute)).zfill(2)
    txt_seconde = str(int(seconde)).zfill(2)

    if int(hour)>0:
        format = txt_hour + ":" + txt_minute + ":" + txt_seconde
    else:
        format = txt_minute + ":" + txt_seconde

    return format