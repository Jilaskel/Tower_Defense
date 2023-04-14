import pygame
from utilitaries import *
from functions import *


class All_magic_effects(pygame.sprite.Group):
      def __init__(self,game):
            pygame.sprite.Group.__init__(self)   

            self.game = game

            self.wave_data = Wave_data()
            self.heal_effect_data = Heal_effect_data()
            # self.buff_effect_data = Buff_effect_data()


      def add_wave(self,mage):
            self.add(Wave(self,mage))
            self.game.all_mixers.magical_effect_mixer.wave_sound.play(maxtime=SOUND_WAVE_MAX_TIME)

      def add_heal(self,target):
            self.add(Heal(self,target))
            # game.all_mixers.magical_effect_mixer.wave_sound.play(maxtime=SOUND_WAVE_MAX_TIME)


class Magic_effect_data():
      def __init__(self):
            self.number_frame = self.my_dict["NUMBER_FRAME"]
            self.images = []
            for i in range(1,self.number_frame+1):
                  self.images.append(pygame.image.load(self.my_dict["IMAGE_PATH"]+str(i).zfill(3)+".png").convert_alpha()) 
                  self.images[i-1] = pygame.transform.scale(self.images[i-1],vec(self.images[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
            self.time_per_frame = self.my_dict["TIME_PER_FRAME"] # in ms
            self.image_size = vec(self.images[0].get_size())

            self.offset = self.my_dict["OFFSET"]


class Wave_data(Magic_effect_data):
      def __init__(self):
            self.my_dict = WAVE_DICT

            Magic_effect_data.__init__(self)

            self.hitbox_factor = self.my_dict["HITBOX_FACTOR"]

            self.velocity = self.my_dict["VELOCITY"]
            self.damage = self.my_dict["DAMAGE"]

class Heal_data(Magic_effect_data):
      def __init__(self):
            self.my_dict = HEAL_DICT

            Magic_effect_data.__init__(self)

            self.total_time = self.my_dict["TOTAL_TIME"]

            self.damage = self.my_dict["AMOUNT"]

class Magical_effect(pygame.sprite.Sprite):
      def __init__(self,all_ef,mage):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_ef.wave_data

            self.image_size = self.my_data.image_size

            self.current_frame = 0
            self.current_image = self.my_data.images[self.current_frame]

            self.my_timer = 0

            self.posX = mage.posX + self.my_data.offset[0]
            self.posY = mage.posY + self.my_data.offset[1]
            self.rendering_layer = compute_rendering_layer_number(self)

            self.rect = self.current_image.get_rect()
            self.rect.x = self.posX + self.rect.width*0.5
            self.rect.width = self.rect.width*0.5
            self.rect.y = self.posY + self.rect.height*0.5
            self.rect.height = self.rect.height*0.5

            self.damaged_enmy = []

      def advance(self,game):
            self.my_timer += game.timestep
            if self.my_timer>self.my_data.time_per_frame:
                  self.current_frame += 1
                  self.my_timer = 0.0
            
            if (self.current_frame>(self.my_data.number_frame-1)):
                  pygame.sprite.Sprite.kill(self)
            else:
                  self.current_image= self.my_data.images[self.current_frame]  

            dx = self.my_data.velocity * game.timestep
            self.posX += dx
            self.rect.x = self.posX

      def check_impact(self,game):
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_towers.all_siege_engines, False)
            if self.hit_ennemies:
                for i in range (len(self.hit_ennemies)):
                        if not (self.hit_ennemies[i] in self.damaged_enmy):
                              self.hit_ennemies[i].hp -= self.my_data.damage
                              self.damaged_enmy.append(self.hit_ennemies[i])

      def render(self):
            window.blit(self.current_image, (self.posX, self.posY)) 

class Heal(Magical_effect):
      def advance(self,game):
            Magical_effect.advance(game)


class Wave(Magical_effect):
      def __init__(self,all_ef,mage):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_ef.wave_data

            self.image_size = self.my_data.image_size

            self.current_frame = 0
            self.current_image = self.my_data.images[self.current_frame]

            self.my_timer = 0

            self.posX = mage.posX + self.my_data.offset[0]
            self.posY = mage.posY + self.my_data.offset[1]
            self.rendering_layer = compute_rendering_layer_number(self)

            self.rect = self.current_image.get_rect()
            self.rect.x = self.posX + self.rect.width*0.5
            self.rect.width = self.rect.width*0.5
            self.rect.y = self.posY + self.rect.height*0.5
            self.rect.height = self.rect.height*0.5

            self.damaged_enmy = []

      def advance(self,game):
            self.my_timer += game.timestep
            if self.my_timer>self.my_data.time_per_frame:
                  self.current_frame += 1
                  self.my_timer = 0.0
            
            if (self.current_frame>(self.my_data.number_frame-1)):
                  pygame.sprite.Sprite.kill(self)
            else:
                  self.current_image= self.my_data.images[self.current_frame]  

            dx = self.my_data.velocity * game.timestep
            self.posX += dx
            self.rect.x = self.posX

      def check_impact(self,game):
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_towers.all_siege_engines, False)
            if self.hit_ennemies:
                for i in range (len(self.hit_ennemies)):
                        if not (self.hit_ennemies[i] in self.damaged_enmy):
                              self.hit_ennemies[i].hp -= self.my_data.damage
                              self.damaged_enmy.append(self.hit_ennemies[i])

 