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

        self.magical_effect_mixer = Magical_effect_mixer()

class Music_mixer():
    def __init__(self):
        pygame.mixer.music.load(MUSIC_FILE_PATH)
        self.start_time_ms = 0.0
        self.fade_up_time_ms = int(FADE_UP_TIME*1000)  # need to be integer
        pygame.mixer.music.play(-1,self.start_time_ms,self.fade_up_time_ms)  #infinite loop   # play(loops=0, start=0.0, fade_ms=0)
        pygame.mixer.music.set_volume(MUSIC_VOLUME)

    def rewind(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1,self.start_time_ms,self.fade_up_time_ms)  #infinite loop   # play(loops=0, start=0.0, fade_ms=0)

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def set_music_volume(self,amount):
        pygame.mixer.music.set_volume(MUSIC_VOLUME*amount)

class Mouse_mixer():
    def __init__(self):

        self.building_rock_sound = pygame.mixer.Sound(SOUND_BUILDING_ROCK_PATH)
        self.building_rock_sound.set_volume(SOUND_BUILDING_ROCK_VOLUME*AUDIO_EFFECTS_COEFF)

        self.building_wood_sound = pygame.mixer.Sound(SOUND_BUILDING_WOOD_PATH)
        self.building_wood_sound.set_volume(SOUND_BUILDING_WOOD_VOLUME*AUDIO_EFFECTS_COEFF)

        self.gold_gain_sound = pygame.mixer.Sound(SOUND_GOLD_GAIN_PATH)
        self.gold_gain_sound.set_volume(SOUND_GOLD_GAIN_VOLUME)
        self.big_gold_gain_sound = pygame.mixer.Sound(SOUND_BIG_GOLD_GAIN_PATH)
        self.big_gold_gain_sound.set_volume(SOUND_GOLD_GAIN_VOLUME)

class Ennemy_mixer():
    def __init__(self):

        self.falling_sound = pygame.mixer.Sound(SOUND_FALLING_PATH)
        self.falling_sound.set_volume(SOUND_FALLING_VOLUME*AUDIO_EFFECTS_COEFF)

        self.ogre_d_sound_1 = pygame.mixer.Sound(SOUND_OGRE_D_1_PATH)
        self.ogre_d_sound_1.set_volume(SOUND_OGRE_D_VOLUME*AUDIO_EFFECTS_COEFF)
        self.ogre_d_sound_2 = pygame.mixer.Sound(SOUND_OGRE_D_2_PATH)
        self.ogre_d_sound_2.set_volume(SOUND_OGRE_D_VOLUME*AUDIO_EFFECTS_COEFF)
        self.ogre_d_sound_3 = pygame.mixer.Sound(SOUND_OGRE_D_3_PATH)
        self.ogre_d_sound_3.set_volume(SOUND_OGRE_D_VOLUME*AUDIO_EFFECTS_COEFF)
        self.ogre_d_list = []
        self.ogre_d_list.append(self.ogre_d_sound_1)
        self.ogre_d_list.append(self.ogre_d_sound_2)
        self.ogre_d_list.append(self.ogre_d_sound_3)

class Projectile_mixer():
    def __init__(self):

        self.bolt_proj_sound_1 = pygame.mixer.Sound(SOUND_BOLT_PROJ_1_PATH)
        self.bolt_proj_sound_1.set_volume(SOUND_BOLT_PROJ_VOLUME*AUDIO_EFFECTS_COEFF)
        self.bolt_proj_sound_2 = pygame.mixer.Sound(SOUND_BOLT_PROJ_2_PATH)
        self.bolt_proj_sound_2.set_volume(SOUND_BOLT_PROJ_VOLUME*AUDIO_EFFECTS_COEFF)
        self.bolt_proj_list = []
        self.bolt_proj_list.append(self.bolt_proj_sound_1)
        self.bolt_proj_list.append(self.bolt_proj_sound_2)
        
        self.arcane_proj_sound = pygame.mixer.Sound(SOUND_ARCANE_PROJ_PATH)
        self.arcane_proj_sound.set_volume(SOUND_ARCANE_PROJ_VOLUME*AUDIO_EFFECTS_COEFF)

        self.fire_proj_sound = pygame.mixer.Sound(SOUND_FIRE_PROJ_PATH)
        self.fire_proj_sound.set_volume(SOUND_FIRE_PROJ_VOLUME*AUDIO_EFFECTS_COEFF)

        self.light_proj_sound_1 = pygame.mixer.Sound(SOUND_LIGHT_PROJ_1_PATH)
        self.light_proj_sound_1.set_volume(SOUND_LIGHT_PROJ_VOLUME*AUDIO_EFFECTS_COEFF)
        self.light_proj_sound_2 = pygame.mixer.Sound(SOUND_LIGHT_PROJ_2_PATH)
        self.light_proj_sound_2.set_volume(SOUND_LIGHT_PROJ_VOLUME*AUDIO_EFFECTS_COEFF)
        self.light_proj_sound_3 = pygame.mixer.Sound(SOUND_LIGHT_PROJ_3_PATH)
        self.light_proj_sound_3.set_volume(SOUND_LIGHT_PROJ_VOLUME*AUDIO_EFFECTS_COEFF)
        self.light_proj_sound_4 = pygame.mixer.Sound(SOUND_LIGHT_PROJ_4_PATH)
        self.light_proj_sound_4.set_volume(SOUND_LIGHT_PROJ_VOLUME*AUDIO_EFFECTS_COEFF)
        self.light_proj_list = []
        self.light_proj_list.append(self.light_proj_sound_1)
        self.light_proj_list.append(self.light_proj_sound_2)
        self.light_proj_list.append(self.light_proj_sound_3)
        self.light_proj_list.append(self.light_proj_sound_4)


        self.ice_bolt_proj_sound_1 = pygame.mixer.Sound(SOUND_ICE_BOLT_PROJ_1_PATH)
        self.ice_bolt_proj_sound_1.set_volume(SOUND_ICE_BOLT_PROJ_VOLUME*AUDIO_EFFECTS_COEFF)
        self.ice_bolt_proj_sound_2 = pygame.mixer.Sound(SOUND_ICE_BOLT_PROJ_2_PATH)
        self.ice_bolt_proj_sound_2.set_volume(SOUND_ICE_BOLT_PROJ_VOLUME*AUDIO_EFFECTS_COEFF)
        self.ice_bolt_proj_list = []
        self.ice_bolt_proj_list.append(self.ice_bolt_proj_sound_1)
        self.ice_bolt_proj_list.append(self.ice_bolt_proj_sound_2)

class Impact_mixer():
    def __init__(self):

        self.rock_sound = pygame.mixer.Sound(SOUND_ROCK_PATH)
        self.rock_sound.set_volume(SOUND_ROCK_VOLUME*AUDIO_EFFECTS_COEFF)

        self.arcane_impact_sound = pygame.mixer.Sound(SOUND_ARCANE_IMPACT_PATH)
        self.arcane_impact_sound.set_volume(SOUND_ARCANE_IMPACT_VOLUME*AUDIO_EFFECTS_COEFF)


class Magical_effect_mixer():
    def __init__(self):

        self.wave_sound = pygame.mixer.Sound(SOUND_WAVE_PATH)
        self.wave_sound.set_volume(SOUND_WAVE_VOLUME*AUDIO_EFFECTS_COEFF)
