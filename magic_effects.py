import pygame
from utilitaries import *
from functions import *


class All_magic_effects(pygame.sprite.Group):
      def __init__(self,game):
            pygame.sprite.Group.__init__(self)   

            self.game = game

            self.wave_data = Wave_data()
            self.heal_data = Heal_data()
            self.buff_data = Buff_data()
            self.explosion_data = Explosion_data()


      def add_wave(self,nec):
            self.add(Wave(self,nec))
            self.game.all_mixers.magical_effect_mixer.wave_sound.play(maxtime=SOUND_WAVE_MAX_TIME)

      def add_heal(self,target):
            self.add(Heal(self,target))
            # game.all_mixers.magical_effect_mixer.wave_sound.play(maxtime=SOUND_WAVE_MAX_TIME)

      def add_buff(self,target):
            self.add(Buff(self,target))
            # game.all_mixers.magical_effect_mixer.wave_sound.play(maxtime=SOUND_WAVE_MAX_TIME)

      def add_explosion(self,kam):
            self.add(Explosion(self,kam))
            self.game.all_mixers.magical_effect_mixer.explosion_sound.play(maxtime=SOUND_EXPLOSION_MAX_TIME)

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

            self.velocity = self.my_dict["VELOCITY"]
            self.damage = self.my_dict["DAMAGE"]

class Heal_data(Magic_effect_data):
      def __init__(self):
            self.my_dict = HEAL_DICT

            Magic_effect_data.__init__(self)

            self.total_time = self.my_dict["TOTAL_TIME"]

            self.amount = self.my_dict["AMOUNT"]

class Buff_data(Magic_effect_data):
      def __init__(self):
            self.my_dict = BUFF_DICT

            Magic_effect_data.__init__(self)

            self.total_time = self.my_dict["TOTAL_TIME"]

            self.velocity_coeff = self.my_dict["VELOCITY_COEFF"]

            self.damage_coeff = self.my_dict["DAMAGE_COEFF"]

class Explosion_data(Magic_effect_data):
      def __init__(self):
            self.my_dict = EXPLOSION_DICT

            Magic_effect_data.__init__(self)

            self.hitbox_factor = self.my_dict["HITBOX_FACTOR"]

            self.damage = self.my_dict["DAMAGE"]

            self.damage_frame = self.my_dict["DAMAGE_FRAME"]

class Magical_effect(pygame.sprite.Sprite):
      def __init__(self,target):
            pygame.sprite.Sprite.__init__(self)

            self.my_target = target

            self.image_size = self.my_data.image_size

            self.current_frame = 0
            self.current_image = self.my_data.images[self.current_frame]

            self.my_timer = 0
            self.my_total_timer = 0

            self.posX = target.posX + target.my_data.image_size[0] - self.image_size[0] + self.my_data.offset[0]
            self.posY = target.posY + target.my_data.image_size[1] - self.image_size[1] + self.my_data.offset[1]
            
            self.rendering_layer = target.rendering_layer + self.rendering_layer_offset
            # self.rendering_layer = compute_rendering_layer_number(self)

      def advance(self,game):
            self.my_timer += game.timestep
            if self.my_timer>self.my_data.time_per_frame:
                  self.current_frame += 1
                  self.current_frame = self.current_frame%self.my_data.number_frame
                  self.my_total_timer += self.my_timer
                  self.my_timer = 0.0
            
            if ((self.my_total_timer>self.my_data.total_time*1000) or not(pygame.sprite.Sprite.alive(self.my_target))):
                  self.stop_effect()
                  pygame.sprite.Sprite.kill(self)
            else:
                  self.current_image= self.my_data.images[self.current_frame]  

            self.posX = self.my_target.posX + self.my_data.offset[0]

      def check_impact(self,game):
            pass

      def stop_effect(self):
            pass

      def render(self):
            window.blit(self.current_image, (self.posX, self.posY)) 

class Heal(Magical_effect):
      def __init__(self,all_ef,target):
            self.my_data = all_ef.heal_data
            self.rendering_layer_offset = - 0.1

            Magical_effect.__init__(self,target)


      def check_impact(self,game):
            self.my_target.hp += self.my_data.amount*game.timestep*0.001
            self.my_target.hp = min(self.my_target.hp,self.my_target.hp_max)

class Buff(Magical_effect):
      def __init__(self,all_ef,target):
            self.my_data = all_ef.buff_data
            self.rendering_layer_offset = 0.1

            Magical_effect.__init__(self,target)

            self.buff_applied = False

      def check_impact(self,game):
            if not(self.buff_applied):
                  self.my_target.velocity = self.my_target.velocity*self.my_data.velocity_coeff
                  self.my_target.damage = self.my_target.damage*self.my_data.damage_coeff
                  self.buff_applied = True

      def stop_effect(self):
            self.my_target.velocity = self.my_target.velocity/self.my_data.velocity_coeff
            self.my_target.damage = self.my_target.damage/self.my_data.damage_coeff

class Wave(Magical_effect):
      def __init__(self,all_ef,nec):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_ef.wave_data

            self.all_ef = all_ef

            self.image_size = self.my_data.image_size

            self.current_frame = 0
            self.current_image = self.my_data.images[self.current_frame]

            self.my_timer = 0

            self.posX = nec.posX + self.my_data.offset[0]
            self.posY = nec.posY + self.my_data.offset[1]
            self.rendering_layer = compute_rendering_layer_number(self)

            self.rect = self.current_image.get_rect()
            self.rect.x = self.posX + self.rect.width*0.5
            self.rect.width = self.rect.width*0.5
            self.rect.y = self.posY + self.rect.height*0.5
            self.rect.height = self.rect.height*0.5

            self.damaged_enmy = []
            self.healed_allies = []

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

            self.hit_allies = pygame.sprite.spritecollide(self, game.all_ennemies, False)
            if self.hit_allies:
                for i in range (len(self.hit_allies)):
                        if not (self.hit_allies[i] in self.healed_allies):
                              self.all_ef.add_heal(self.hit_allies[i])
                              self.healed_allies.append(self.hit_allies[i])


class Explosion(Magical_effect):
      def __init__(self,all_ef,kam):
            pygame.sprite.Sprite.__init__(self)

            self.my_data = all_ef.explosion_data

            self.kam = kam

            self.image_size = self.my_data.image_size

            self.current_frame = 0
            self.current_image = self.my_data.images[self.current_frame]

            self.my_timer = 0

            self.posX = kam.posX + self.my_data.offset[0]
            self.posY = kam.posY + self.my_data.offset[1]
            self.rendering_layer = 23
            # self.rendering_layer = kam.rendering_layer
            # self.rendering_layer = compute_rendering_layer_number(self)

            self.rect = self.current_image.get_rect()
            old_width = self.rect.width 
            old_height = self.rect.height
            self.rect.width = self.rect.width*self.my_data.hitbox_factor
            self.rect.height = self.rect.height*self.my_data.hitbox_factor
            self.rect.x = self.posX + (old_width-self.rect.width)*0.5
            self.rect.y = self.posY + (old_height-self.rect.height)*0.5

            self.damage_dealt = False

      def advance(self,game):
            self.my_timer += game.timestep
            if self.my_timer>self.my_data.time_per_frame:
                  self.current_frame += 1
                  self.my_timer = 0.0
            
            if (self.current_frame>(self.my_data.number_frame-1)):
                  pygame.sprite.Sprite.kill(self)
            else:
                  self.current_image= self.my_data.images[self.current_frame]  

      def check_impact(self,game):
            if (self.current_frame==self.my_data.damage_frame-1 and self.damage_dealt==False):
                  self.damage_dealt = True
                  self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_towers, False)
                  if self.hit_ennemies:
                        for i in range (len(self.hit_ennemies)):
                                    self.hit_ennemies[i].hp -= self.my_data.damage
                  self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_dead_bodies.all_iced_bodies, False)
                  if self.hit_ennemies:
                        for i in range (len(self.hit_ennemies)):
                                    self.hit_ennemies[i].hp -= self.my_data.damage
                  self.hit_ennemies = pygame.sprite.spritecollide(self, game.base.all_gates, False)
                  if self.hit_ennemies:
                        for i in range (len(self.hit_ennemies)):
                                    self.hit_ennemies[i].hp -= self.my_data.damage                  
                  self.kam.hp = 0.0

