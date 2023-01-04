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

            self.all_assets.append(Background_asset("GrassBundle5.png",339*r,131*r,0.3*r,2))
            self.all_assets.append(Background_asset("RockBundle1.png",357*r,148*r,0.8*r,2))
            self.all_assets.append(Background_asset("BushBundle2.png",806*r,104*r,1*r,2))
            self.all_assets.append(Background_asset("GrassBundle1.png",964*r,159*r,1*r,2))            
            self.all_assets.append(Background_asset("BushBundle3.png",1336*r,90*r,1*r,2))

            self.all_assets.append(Background_asset("BushBundle1.png",1092*r,211*r,2.5*r,4))
            self.all_assets.append(Background_asset("RockBundle1.png",1210*r,268*r,0.5*r,4))


            self.all_assets.append(Background_asset("GrassBundle3.png",103*r,400*r,0.3*r,8))
            self.all_assets.append(Background_asset("GrassBundle3.png",107*r,395*r,0.3*r,8))
            self.all_assets.append(Background_asset("GrassBundle2.png",121*r,345*r,1*r,8))
            self.all_assets.append(Background_asset("BushBundle4.png",446*r,354*r,1*r,8))
            self.all_assets.append(Background_asset("GrassBundle3.png",524*r,364*r,0.3*r,8))
            self.all_assets.append(Background_asset("RockBundle1.png",745*r,371*r,0.6*r,8))
            self.all_assets.append(Background_asset("BushBundle2.png",771*r,385*r,1*r,8))
            self.all_assets.append(Background_asset("GrassBundle3.png",835*r,348*r,0.3*r,8))
            self.all_assets.append(Background_asset("GrassBundle2.png",1210*r,356*r,0.3*r,8))

            self.all_assets.append(Background_asset("BushBundle1.png",294*r,493*r,2.5*r,10))
            self.all_assets.append(Background_asset("RockBundle2.png",394*r,540*r,0.7*r,10))
            

            self.all_assets.append(Background_asset("BushBundle3.png",79*r,631*r,1*r,14))
            self.all_assets.append(Background_asset("BushBundle1.png",1009*r,607*r,1*r,14))
            self.all_assets.append(Background_asset("GrassBundle5.png",1456*r,599*r,1*r,14))

            self.all_assets.append(Background_asset("GrassBundle6.png",590*r,777*r,1*r,16))
            self.all_assets.append(Background_asset("BushBundle1.png",626*r,777*r,1*r,16))
            self.all_assets.append(Background_asset("RockBundle2.png",1154*r,809*r,1*r,16))
            self.all_assets.append(Background_asset("BushBundle4.png",1224*r,805*r,1*r,16))


            self.all_assets.append(Background_asset("BushBundle1.png",266*r,858*r,1*r,20))
            self.all_assets.append(Background_asset("GrassBundle6.png",873*r,898*r,1*r,20))
            self.all_assets.append(Background_asset("GrassBundle6.png",1293*r,882*r,1*r,20))
            self.all_assets.append(Background_asset("GrassBundle1.png",1331*r,892*r,1*r,20))
            self.all_assets.append(Background_asset("GrassBundle3.png",1405*r,903*r,1*r,20))

            self.all_assets.append(Background_asset("BushBundle4.png",123*r,1020*r,1*r,22))
            self.all_assets.append(Background_asset("GrassBundle2.png",1083*r,1042*r,1*r,22))
            self.all_assets.append(Background_asset("GrassBundle3.png",1127*r,1029*r,1*r,22))
            


            #self.all_assets.append(Background_asset("BushBundle1_cropped.png",3*s,3.6*s,1*r,9))
            #self.all_assets.append(Background_asset("BushBundle2_cropped.png",1*s,4.6*s,1*r,13))
            #self.all_assets.append(Background_asset("BushBundle3_cropped.png",5*s,1.8*s,1*r,3))
            #self.all_assets.append(Background_asset("BushBundle4_cropped.png",6*s,2.6*s,1*r,7,flip=True))
#
            #self.all_assets.append(Background_asset("GrassBundle1_cropped.png",5*s,5.3*s,1.0*r,14))
            #self.all_assets.append(Background_asset("GrassBundle3_cropped.png",6.5*s,6.7*s,0.7*r,19))
            #self.all_assets.append(Background_asset("GrassBundle4_cropped.png",10.2*s,3.0*s,0.4*r,7))
            #self.all_assets.append(Background_asset("GrassBundle6_cropped.png",9.8*s,5.4*s,0.7*r,15))
#
            #self.all_assets.append(Background_asset("RockBundle1_cropped.png",10.2*s,1.6*s,1.0*r,3))
            #self.all_assets.append(Background_asset("RockBundle2_cropped.png",0.8*s,6.8*s,1.0*r,19))

      def render(self,rendering_layer):
            if self.rendering_layer==rendering_layer:
                  window.blit(self.current_image, (self.posX, self.posY))    

class Background_asset():
      def __init__(self,image_name,posX,posY,resize_factor,rendering_layer,flip=False):
            self.image = pygame.image.load(BACKGROUND_GRASS_ASSETS_PATH+image_name).convert_alpha()
            self.image = pygame.transform.scale(self.image,vec(self.image.get_size())*resize_factor) 
            if flip:
                  self.image = pygame.transform.flip(self.image, True, False)
            self.image_size = vec(self.image.get_size())

            self.posX = posX
            self.posY = posY

            self.rendering_layer = rendering_layer

      def render(self,rendering_layer):
            if self.rendering_layer==rendering_layer:
                  window.blit(self.image, (self.posX, self.posY))   
