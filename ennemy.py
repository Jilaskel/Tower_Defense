import pygame
from utilitaries import *

class Ennemy(pygame.sprite.Sprite):
      def __init__(self,game,x,y):
            super().__init__()
            self.images_path = "Assets/Ennemies/"
            self.image = pygame.image.load(self.images_path+"ennemy1.png").convert()    
            self.posX = x     # game.background.bush_width
            self.posY = y     # 135
            self.vel = vec(0,0)
            self.vel.x = 20

      def move(self):
            # Will set running to False if the player has slowed down to a certain extent
            self.posX += self.vel.x


      def render(self):
            window.blit(self.image, (self.posX, self.posY))  


#class Gobelin(Ennemy,pygame.sprite.Sprite):
class Gobelin(Ennemy,pygame.sprite.Sprite):
      def __init__(self,game,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.images_path = "Assets/Ennemies/Gobelin/WalkAnim/"
            self.image = pygame.image.load(self.images_path+"/001.png").convert_alpha()
            self.number_frame_walking = 20
            self.image_walking = []
            for i in range(1,self.number_frame_walking+1):
                  self.image_walking.append(pygame.image.load(self.images_path+"00"+str(i)+".png").convert_alpha())   
            self.posX = x     
            self.posY = y     
            self.vel = vec(0,0)
            self.vel.x = 10
            self.moving = False
            self.move_frame = 0

      def move(self):
            # Will set running to False if the player has slowed down to a certain extent
            self.posX += self.vel.x
            self.moving = True


      def render(self):
            if self.moving:
                  self.move_frame += 1 
                  self.move_frame = self.move_frame%self.number_frame_walking
                  window.blit(self.image_walking[self.move_frame], (self.posX, self.posY))
            else:
                  window.blit(self.image, (self.posX, self.posY))  
 
