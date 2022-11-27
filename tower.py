import pygame
from utilitaries import *

class Tower(pygame.sprite.Sprite):
      def __init__(self,game):
            super().__init__()
            self.image = pygame.image.load("Assets/Tower/tower1.png").convert()    
            self.posX = 800
            self.posY = 500


      def render(self):
            window.blit(self.image, (self.posX, self.posY))  



 

