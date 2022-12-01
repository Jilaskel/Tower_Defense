import pygame
from utilitaries import *


class Mixer():
    pygame.mixer.init()
    pygame.mixer.music.load("Audio/Music/Age_of_War_Theme Soundtrack.mp3")
    start_time_ms = 0.0
    fade_up_time_ms = 3000
    pygame.mixer.music.play(-1,start_time_ms,fade_up_time_ms)  #infinite loop   # play(loops=0, start=0.0, fade_ms=0)
    pygame.mixer.music.set_volume(0.1)