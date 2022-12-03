import pygame
from utilitaries import *


class Mixer():
    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC_FILE_PATH)
    start_time_ms = 0.0
    fade_up_time_ms = int(FADE_UP_TIME*1000)  # need to be integer
    pygame.mixer.music.play(-1,start_time_ms,fade_up_time_ms)  #infinite loop   # play(loops=0, start=0.0, fade_ms=0)
    pygame.mixer.music.set_volume(MUSIC_VOLUME)