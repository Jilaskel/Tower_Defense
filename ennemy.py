import pygame
from utilitaries import *

class Ennemy(pygame.sprite.Sprite):
      def __init__(self,game):
            super().__init__()
            self.image = pygame.image.load("Assets/Ennemies/ennemy1.png").convert()    
            self.posX = game.background.bush_width
            self.posY = 135
            self.vel = vec(0,0)
            self.vel.x = 20

      def move(self):
            # Will set running to False if the player has slowed down to a certain extent
            self.posX += self.vel.x


      def render(self):
            window.blit(self.image, (self.posX, self.posY))  


    
 

