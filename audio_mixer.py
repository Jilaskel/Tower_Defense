import pygame
from utilitaries import *


class All_mixers():
    def __init__(self):
        pygame.mixer.init()
        self.music_mixer = Music_mixer()
        self.mouse_mixer = Mouse_mixer()
        self.ennemy_mixer = Ennemy_mixer()
        self.projectile_mixer = Projectile_mixer()
        self.impact_mixer = Impact_mixer()

class Music_mixer():
    def __init__(self):
        pygame.mixer.music.load(MUSIC_FILE_PATH)
        start_time_ms = 0.0
        fade_up_time_ms = int(FADE_UP_TIME*1000)  # need to be integer
        pygame.mixer.music.play(-1,start_time_ms,fade_up_time_ms)  #infinite loop   # play(loops=0, start=0.0, fade_ms=0)
        pygame.mixer.music.set_volume(MUSIC_VOLUME)

    def set_music_volume(self,amount):
        pygame.mixer.music.set_volume(MUSIC_VOLUME*amount)

class Mouse_mixer():
    def __init__(self):

        self.building_sound = pygame.mixer.Sound(SOUND_BUILDING_PATH)
        self.building_sound.set_volume(SOUND_BUILDING_VOLUME*AUDIO_EFFECTS_COEF)


class Ennemy_mixer():
    def __init__(self):

        self.falling_sound = pygame.mixer.Sound(SOUND_FALLING_PATH)
        self.falling_sound.set_volume(SOUND_FALLING_VOLUME*AUDIO_EFFECTS_COEF)

class Projectile_mixer():
    def __init__(self):
        
        self.arcane_proj_sound = pygame.mixer.Sound(SOUND_ARCANE_PROJ_PATH)
        self.arcane_proj_sound.set_volume(SOUND_ARCANE_PROJ_VOLUME*AUDIO_EFFECTS_COEF)


class Impact_mixer():
    def __init__(self):

        self.rock_sound = pygame.mixer.Sound(SOUND_ROCK_PATH)
        self.rock_sound.set_volume(SOUND_ROCK_VOLUME*AUDIO_EFFECTS_COEF)

        self.arcane_impact_sound = pygame.mixer.Sound(SOUND_ARCANE_IMPACT_PATH)
        self.arcane_impact_sound.set_volume(SOUND_ARCANE_IMPACT_VOLUME*AUDIO_EFFECTS_COEF)