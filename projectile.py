import pygame
from utilitaries import *
from numpy import sqrt

class Projectile(pygame.sprite.Sprite):
      def __init__(self,x,y):
            super().__init__()   
            self.posX = x     # game.background.bush_width
            self.posY = y     # 135
            self.vel = vec(0,0)
            self.vel[0] = 0.2 # pixel by ms

      def move(self,game):           
            self.posX += self.vel[0] * game.timestep

      def render(self,game):
            window.blit(self.current_image, (self.posX, self.posY))  


class Bolt(Projectile,pygame.sprite.Sprite):
      def __init__(self,x,y,target):
            pygame.sprite.Sprite.__init__(self)
            self.images_path = "Assets/Tower/Baliste/"
            self.current_image = pygame.image.load(self.images_path+"/CarreauBaliste.png").convert_alpha()
 
            self.posX = x     
            self.posY = y     
            self.direction = vec(0,0)
            self.vel = vec(0.6,0.6)  # pixel by ms
            self.moving = False
            self.rect = self.current_image.get_rect()

            self.target = target
            self.ratio_for_impact = 0.25

            self.rect.x = self.posX
            self.rect.y = self.posY

      def move(self,game):
            self.direction = (self.target.posX - self.posX, self.target.posY - self.posY)   
            self.direction /= sqrt(self.direction[0]**2+self.direction[1]**2)     
            self.posX += self.vel[0] * game.timestep * self.direction[0]
            self.posY += self.vel[1] * game.timestep * self.direction[1]
            self.rect.x = self.posX
            self.rect.y = self.posY
            self.moving = True

      def check_impact(self,game):
            self.hit_ennemies = pygame.sprite.spritecollide(self, game.all_ennemies, False,pygame.sprite.collide_rect_ratio(self.ratio_for_impact))
            if self.hit_ennemies:
                  pygame.sprite.Sprite.kill(self)


      def render(self,game):
            window.blit(self.current_image, (self.posX, self.posY))  
 
