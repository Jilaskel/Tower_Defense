import pygame
from utilitaries import *
from functions import *

ARCANE_TOWER_LVL1_IMPACT_TAG = 1
ARCANE_TOWER_LVL2_IMPACT_TAG = 2
ARCANE_TOWER_LVL3_IMPACT_TAG = 3
FIRE_TOWER_LVL1_IMPACT_TAG = 4
FIRE_TOWER_LVL2_IMPACT_TAG = 5
FIRE_TOWER_LVL3_IMPACT_TAG = 6
ROCK_IMPACT_TAG = 7


class All_impacts(pygame.sprite.Group):
      def __init__(self):
            pygame.sprite.Group.__init__(self)   

            self.arcane_impact_lvl1_data = Arcane_impact_lvl1_data()
            self.arcane_impact_lvl2_data = Arcane_impact_lvl2_data()
            self.arcane_impact_lvl3_data = Arcane_impact_lvl3_data()
            self.fire_impact_lvl1_data = Fire_impact_lvl1_data()
            self.fire_impact_lvl2_data = Fire_impact_lvl2_data()
            self.fire_impact_lvl3_data = Fire_impact_lvl3_data()
            self.rock_impact_data = Rock_impact_data()

      def add_impact(self,game,projectile,tag):
            if (tag==ARCANE_TOWER_LVL1_IMPACT_TAG):
                  self.add_arcane_impact_lvl1(game,projectile)
            if (tag==ARCANE_TOWER_LVL2_IMPACT_TAG):
                  self.add_arcane_impact_lvl2(game,projectile)
            if (tag==ARCANE_TOWER_LVL3_IMPACT_TAG):
                  self.add_arcane_impact_lvl3(game,projectile)
            elif (tag==FIRE_TOWER_LVL1_IMPACT_TAG):
                  self.add_fire_impact_lvl1(game,projectile)          
            elif (tag==FIRE_TOWER_LVL2_IMPACT_TAG):
                  self.add_fire_impact_lvl2(game,projectile)  
            elif (tag==FIRE_TOWER_LVL3_IMPACT_TAG):
                  self.add_fire_impact_lvl3(game,projectile)  
            elif (tag==ROCK_IMPACT_TAG):
                  self.add_rock_impact(game,projectile)  


      def add_arcane_impact_lvl1(self,game,projectile):
            self.add(Arcane_impact_lvl1(self,projectile))
            game.all_mixers.impact_mixer.arcane_impact_sound.play(maxtime=SOUND_ARCANE_IMPACT_MAX_TIME)

      def add_arcane_impact_lvl2(self,game,projectile):
            self.add(Arcane_impact_lvl2(self,projectile))
            game.all_mixers.impact_mixer.arcane_impact_sound.play(maxtime=SOUND_ARCANE_IMPACT_MAX_TIME)

      def add_arcane_impact_lvl3(self,game,projectile):
            self.add(Arcane_impact_lvl3(self,projectile))
            game.all_mixers.impact_mixer.arcane_impact_sound.play(maxtime=SOUND_ARCANE_IMPACT_MAX_TIME)

      def add_fire_impact_lvl1(self,game,projectile):
            self.add(Fire_impact_lvl1(self,projectile))

      def add_fire_impact_lvl2(self,game,projectile):
            self.add(Fire_impact_lvl2(self,projectile))

      def add_fire_impact_lvl3(self,game,projectile):
            self.add(Fire_impact_lvl3(self,projectile))

      def add_rock_impact(self,game,projectile):
            self.add(Rock_impact(self,projectile))
            game.all_mixers.impact_mixer.rock_sound.play()


class Impact_data():
      def __init__(self):

        self.damage = self.my_dict["DAMAGE"]
        self.static_image = pygame.image.load(self.my_dict["IMAGE_PATH"]+"0001.png").convert_alpha()
        self.static_image = pygame.transform.scale(self.static_image,vec(self.static_image.get_size())*self.my_dict["RESIZE_FACTOR"])        
        self.image_size = vec(self.static_image.get_size())
        self.offset = vec(self.my_dict["CENTOR_VECTOR"][0]*self.image_size[0],self.my_dict["CENTOR_VECTOR"][1]*self.image_size[1])

        self.number_frame = self.my_dict["NUMBER_FRAME"]
        self.images = []
        for i in range(1,self.number_frame+1):
                self.images.append(pygame.image.load(self.my_dict["IMAGE_PATH"]+str(i).zfill(4)+".png").convert_alpha())  
                self.images[i-1] = pygame.transform.scale(self.images[i-1],vec(self.images[i-1].get_size())*self.my_dict["RESIZE_FACTOR"])
        self.anim_total_time = self.my_dict["TOTAL_TIME"]  # in ms
        self.time_per_frame = self.anim_total_time/self.number_frame # in ms

        self.damage_frame = self.my_dict["DAMAGE_FRAME"] - 1

class Arcane_impact_lvl1_data(Impact_data):
      def __init__(self):
        self.my_dict = ARCANE_IMPACT_LVL1_DICT

        Impact_data.__init__(self)

class Arcane_impact_lvl2_data(Impact_data):
      def __init__(self):
        self.my_dict = ARCANE_IMPACT_LVL2_DICT

        Impact_data.__init__(self)

class Arcane_impact_lvl3_data(Impact_data):
      def __init__(self):
        self.my_dict = ARCANE_IMPACT_LVL3_DICT

        Impact_data.__init__(self)

class Fire_impact_lvl1_data(Impact_data):
      def __init__(self):
        self.my_dict = FIRE_IMPACT_LVL1_DICT

        Impact_data.__init__(self)

class Fire_impact_lvl2_data(Impact_data):
      def __init__(self):
        self.my_dict = FIRE_IMPACT_LVL2_DICT

        Impact_data.__init__(self)

class Fire_impact_lvl3_data(Impact_data):
      def __init__(self):
        self.my_dict = FIRE_IMPACT_LVL3_DICT

        Impact_data.__init__(self)


class Rock_impact_data(Impact_data):
      def __init__(self):
        self.my_dict = ROCK_IMPACT_DICT

        Impact_data.__init__(self)


class Impact(pygame.sprite.Sprite):
    def __init__(self,projectile):
        pygame.sprite.Sprite.__init__(self)

        self.current_image = self.my_data.static_image
        self.image_size = self.my_data.image_size

        self.current_frame = 0

        self.my_timer = 0

        self.damage_dealt=False

        self.posX = projectile.target.rect.center[0]-self.my_data.offset[0]
        self.posY = projectile.target.rect.center[1]-self.my_data.offset[1]
        margin = - 20.0 * RESIZE_COEFF
        if ((projectile.posY+margin)<projectile.target.posY):
             self.rendering_layer = projectile.target.rendering_layer - 0.1
        else:
             self.rendering_layer = projectile.target.rendering_layer + 0.1

      #   self.rendering_layer = compute_rendering_layer_number(self)

        self.rect = self.current_image.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY + self.rect.height*0.5
        self.rect.height = self.rect.height*0.5

    def check_impact(self,game):
        if (self.current_frame==self.my_data.damage_frame-1 and self.damage_dealt==False):
            self.damage_dealt = True
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False)
            if self.hit_ennemies:
                for i in range (len(self.hit_ennemies)):
                        self.hit_ennemies[i].hp -= self.my_data.damage

    def explode(self,game):
        self.my_timer += game.timestep
        if self.my_timer>self.my_data.time_per_frame:
            self.current_frame += 1
            self.my_timer = 0.0
        
        if (self.current_frame>(self.my_data.number_frame-1)):
            pygame.sprite.Sprite.kill(self)
        else:
            self.current_image= self.my_data.images[self.current_frame]

    def render(self):
        window.blit(self.current_image, (self.posX, self.posY))  


class Arcane_impact_lvl1(Impact):
    def __init__(self,all_i,projectile):
        self.my_data = all_i.arcane_impact_lvl1_data

        Impact.__init__(self,projectile)

class Arcane_impact_lvl2(Impact):
    def __init__(self,all_i,projectile):
        self.my_data = all_i.arcane_impact_lvl2_data

        Impact.__init__(self,projectile)

class Arcane_impact_lvl3(Impact):
    def __init__(self,all_i,projectile):
        self.my_data = all_i.arcane_impact_lvl3_data

        Impact.__init__(self,projectile)

class Fire_impact_lvl1(Impact):
    def __init__(self,all_i,projectile):
        self.my_data = all_i.fire_impact_lvl1_data

        Impact.__init__(self,projectile)

class Fire_impact_lvl2(Impact):
    def __init__(self,all_i,projectile):
        self.my_data = all_i.fire_impact_lvl2_data

        Impact.__init__(self,projectile)

class Fire_impact_lvl3(Impact):
    def __init__(self,all_i,projectile):
        self.my_data = all_i.fire_impact_lvl3_data

        Impact.__init__(self,projectile)

class Rock_impact(Impact):
    def __init__(self,all_i,projectile):
        self.my_data = all_i.rock_impact_data

        Impact.__init__(self,projectile)