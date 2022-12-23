import pygame
from utilitaries import *

class Impact(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        pass

    def check_impact(self,game):
        if (self.current_frame==self.damage_frame-1 and self.damage_dealt==False):
            self.damage_dealt = True
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False)
            if self.hit_ennemies:
                for i in range (len(self.hit_ennemies)):
                        self.hit_ennemies[i].hp -= self.damage

    def render(self):
        window.blit(self.current_image, (self.posX, self.posY))  


class Arcane_impact(Impact,pygame.sprite.Sprite):
    def __init__(self,projectile):
        pygame.sprite.Sprite.__init__(self)

        self.inital_image = pygame.image.load(ARCANE_IMPACT_IMAGE_PATH+"001.png").convert_alpha()
        self.inital_image = pygame.transform.scale(self.inital_image,pygame.Vector2(self.inital_image.get_size())*ARCANE_IMPACT_RESIZE_FACTOR)        
        self.current_image = self.inital_image
        self.image_size = pygame.Vector2(self.inital_image.get_size())
        self.offset = vec(ARCANE_IMPACT_CENTOR_VECTOR[0]*self.image_size[0],ARCANE_IMPACT_CENTOR_VECTOR[1]*self.image_size[1])

        self.number_frame = ARCANE_IMPACT_NUMBER_FRAME
        self.images = []
        for i in range(1,self.number_frame+1):
                self.images.append(pygame.image.load(ARCANE_IMPACT_IMAGE_PATH+str(i).zfill(3)+".png").convert_alpha())  
                self.images[i-1] = pygame.transform.scale(self.images[i-1],pygame.Vector2(self.images[i-1].get_size())*ARCANE_IMPACT_RESIZE_FACTOR)
        self.current_frame = 0
        self.anim_total_time = ARCANE_IMPACT_TOTAL_TIME  # in ms
        self.time_per_frame = self.anim_total_time/self.number_frame # in ms

        self.my_timer = 0

        self.damage = projectile.damage
        self.damage_dealt=False
        self.damage_frame = ARCANE_IMPACT_DAMAGE_FRAME - 1

        self.posX = projectile.target.rect.center[0]-self.offset[0]
        self.posY = projectile.target.rect.center[1]-self.offset[1]

        self.rect = self.current_image.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY + self.rect.height*0.5
        self.rect.height = self.rect.height*0.5


    def explode(self,game):
        self.my_timer += game.timestep
        if self.my_timer>self.time_per_frame:
            self.current_frame += 1
            self.my_timer = 0.0
        
        if (self.current_frame>(self.number_frame-1)):
            pygame.sprite.Sprite.kill(self)
        else:
            self.current_image= self.images[self.current_frame]