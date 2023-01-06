import pygame
from utilitaries import *

class Background():
      def __init__(self):
            self.current_image = pygame.image.load(BACKGROUND_IMAGE_PATH).convert_alpha()   
            self.current_image = pygame.transform.scale(self.current_image,(WINDOW_WIDTH,WINDOW_HEIGHT))         
            self.posX = 0  
            self.posY = 0  
            self.menu_height = WINDOW_HEIGHT/8.0  ## 135 en 1920x1080
            self.menu_length = WINDOW_WIDTH/1.153115   ## 1665 en en 1920x1080
            self.bush_width = WINDOW_WIDTH/42.6666  ## 45 en 1920x1080
            self.square_side = WINDOW_HEIGHT/8.0  ## 135 en 1920x1080
            self.number_square_x = 12
            self.number_square_y = 7

            self.rendering_layer = 0            

            self.arrange_assets()

      def arrange_assets(self):
            s = self.square_side
            r = RESIZE_COEFF

            self.all_assets = []

            # list of arguments : image_name, posX, posY, resize_factor, rendering_layer, (optional: flip = True)

            ### First Grass
            self.all_assets.append(Background_asset("RockBundle1_cropped.png",357*r,148*r,0.8*r,1))
            self.all_assets.append(Background_asset("BushBundle2_cropped.png",806*r,104*r,1*r,1))
            self.all_assets.append(Background_asset("BushBundle3_cropped.png",1336*r,90*r,1*r,1))

            self.all_assets.append(Background_asset("GrassBundle1_cropped.png",264*r,219*r,1*r,3))            
            self.all_assets.append(Background_asset("BushBundle1_cropped.png",1092*r,211*r,1.0*r,3))
            self.all_assets.append(Background_asset("RockBundle1_cropped.png",1210*r,268*r,0.5*r,3))

            ### Second Grass
            self.all_assets.append(Background_asset("GrassBundle3_cropped.png",103*r,400*r,0.5*r,7))
            self.all_assets.append(Background_asset("BushBundle4_cropped.png",446*r,354*r,1*r,6))
            self.all_assets.append(Background_asset("GrassBundle3_cropped.png",584*r,374*r,0.5*r,7,True))
            self.all_assets.append(Background_asset("RockBundle1_cropped.png",745*r,371*r,1.0*r,7))
            self.all_assets.append(Background_asset("BushBundle2_cropped.png",831*r,345*r,1.25*r,6))
            self.all_assets.append(Background_asset("GrassBundle4_cropped.png",1335*r,348*r,0.5*r,7))

            self.all_assets.append(Background_asset("BushBundle1_cropped.png",294*r,463*r,1.0*r,9,True))
            self.all_assets.append(Background_asset("RockBundle2_cropped.png",394*r,520*r,1.0*r,9))
            
            ### Third Grass
            self.all_assets.append(Background_asset("BushBundle3_cropped.png",79*r,631*r,1.25*r,13))
            self.all_assets.append(Background_asset("BushBundle1_cropped.png",1009*r,607*r,1.0*r,13))

            self.all_assets.append(Background_asset("GrassBundle6_cropped.png",590*r,767*r,0.5*r,16))
            self.all_assets.append(Background_asset("BushBundle1_cropped.png",626*r,737*r,1.0*r,15))
            self.all_assets.append(Background_asset("RockBundle2_cropped.png",1154*r,785*r,1*r,16,True))
            self.all_assets.append(Background_asset("BushBundle4_cropped.png",1224*r,755*r,1*r,15))

            ### Fourth Grass
            self.all_assets.append(Background_asset("GrassBundle6_cropped.png",873*r,898*r,0.5*r,19,True))
            self.all_assets.append(Background_asset("GrassBundle1_cropped.png",1331*r,872*r,1*r,18))
            self.all_assets.append(Background_asset("BushBundle4_cropped.png",123*r,900*r,1*r,18,True))
            self.all_assets.append(Background_asset("GrassBundle3_cropped.png",1127*r,909*r,0.5*r,18))
            

      def render(self):
            window.blit(self.current_image, (self.posX, self.posY))    
            

class Background_asset():
      def __init__(self,image_name,posX,posY,resize_factor,rendering_layer,flip=False):
            self.current_image = pygame.image.load(BACKGROUND_GRASS_ASSETS_PATH+image_name).convert_alpha()
            self.current_image = pygame.transform.scale(self.current_image,vec(self.current_image.get_size())*resize_factor) 
            if flip:
                  self.current_image = pygame.transform.flip(self.current_image, True, False)
            self.image_size = vec(self.current_image.get_size())

            self.posX = posX
            self.posY = posY

            self.rendering_layer = rendering_layer

      def render(self):
            window.blit(self.current_image, (self.posX, self.posY))   
