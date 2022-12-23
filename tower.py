import pygame
from utilitaries import *
from projectile import *

class Tower(pygame.sprite.Sprite):
      def __init__(self,game,x,y):
            pass

      def check_ennemies(self,game):
            if self.range_hitbox.circular:
                  self.detected_ennemies = pygame.sprite.spritecollide(self.range_hitbox, game.all_ennemies, False, pygame.sprite.collide_circle)
            else:
                  self.detected_ennemies = pygame.sprite.spritecollide(self.range_hitbox, game.all_ennemies, False)

            if (self.detected_ennemies):
                  self.attacking = True
                  if not(self.my_target in self.detected_ennemies):
                        self.my_target = self.detected_ennemies[0]
            else:
                  self.attacking = False

      def die(self):
            if (self.hp<=0):
                  pygame.sprite.Sprite.kill(self)

      def render(self):
            window.blit(self.current_image, (self.posX, self.posY))


class Range_Hitbox(pygame.sprite.Sprite):
      def __init__(self,tower,width,height,range,circular):
            super().__init__()
            self.range = range
            if circular:
                  self.circular = True
                  self.rect = pygame.Rect(tower.posX-ARCANE_TOWER_OFFSET[0],tower.posY-ARCANE_TOWER_OFFSET[1],tower.rect.width,tower.rect.height)
                  self.radius = self.range
                  self.posX = tower.posX-ARCANE_TOWER_OFFSET[0]+width*0.5 - self.radius
                  self.posY = tower.posY-ARCANE_TOWER_OFFSET[1]+height*0.5 - self.radius    

                  self.image = pygame.image.load(TOWER_CIRCLE_RANGE_IMAGE_PATH).convert_alpha()
                  self.image.set_alpha(TOWER_CIRCLE_RANGE_IMAGE_ALPHA)
                  self.image = pygame.transform.scale(self.image,(self.range*2,self.range*2))                                
            else:
                  self.circular = False
                  self.rect = pygame.Rect(tower.posX,tower.posY,width,height)   
                  self.rect.x = tower.posX - self.range
                  self.posX = self.rect.x
                  self.rect.w = self.range              
                  self.posY = tower.posY    

                  self.image = pygame.image.load(TOWER_RECT_RANGE_IMAGE_PATH).convert_alpha()
                  self.image.set_alpha(TOWER_RECT_RANGE_IMAGE_ALPHA) 
                  self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.h))         

            self.offset = vec(self.posX-tower.posX,self.posY-tower.posY)

class Arcane_tower(Tower,pygame.sprite.Sprite):
      def __init__(self,game,x,y):
            pygame.sprite.Sprite.__init__(self)

            self.hp_max = ARCANE_TOWER_HP_MAX
            self.hp = self.hp_max

            self.static_image = pygame.image.load(ARCANE_TOWER_IMAGE_PATH).convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,pygame.Vector2(self.static_image.get_size())*ARCANE_TOWER_RESIZE_FACTOR)        
            self.current_image = self.static_image  
            self.posX = x + ARCANE_TOWER_OFFSET[0]
            self.posY = y + ARCANE_TOWER_OFFSET[1]

            self.firing_period = ARCANE_TOWER_FIRING_PERIOD
            self.my_timer = self.firing_period*2

            self.attacking = True
            self.attack_finished = True

            self.detected_ennemies = False
            self.my_target = []
            
            self.hitbox_left = x
            self.hitbox_top = y
            self.hitbox_width = BACKGROUND_SQUARE_SIDE
            self.hitbox_height = BACKGROUND_SQUARE_SIDE
            self.rect = pygame.Rect(self.hitbox_left,self.hitbox_top,self.hitbox_width,self.hitbox_height)

            self.range = ARCANE_TOWER_RANGE * (self.rect.width+self.rect.height)/2.0
            self.range_hitbox = Range_Hitbox(self,self.rect.w,self.rect.h,self.range,circular=True)

      def attack_and_reload(self,game):
            if (self.attacking):
                  self.attack_finished = False
                  self.my_timer += game.timestep
                  if self.my_timer>self.firing_period:
                        self.my_timer = 0.0
                        # game.all_projectiles.add(Bolt(self.posX+ARCANE_TOWER_FIRING_OFFSET[0],self.posY+ARCANE_TOWER_FIRING_OFFSET[1],self.my_target))
                        game.all_projectiles.add(Arcane_bolt(self.posX+ARCANE_TOWER_FIRING_OFFSET[0],self.posY+ARCANE_TOWER_FIRING_OFFSET[1],self.my_target))
            else:
                  if not(self.attack_finished):
                        self.my_timer += game.timestep
                        if self.my_timer>self.firing_period:
                              self.my_timer = 2*self.firing_period
                              self.attack_finished = True  

class Ballista(Tower,pygame.sprite.Sprite):
      def __init__(self,game,x,y):
            pygame.sprite.Sprite.__init__(self)

            self.hp_max = BALLISTA_HP_MAX
            self.hp = self.hp_max

            self.images_path = BALLISTA_ATTACK_IMAGE_PATH
            self.static_image = pygame.image.load(self.images_path+"0001.png").convert_alpha()
            self.static_image = pygame.transform.scale(self.static_image,pygame.Vector2(self.static_image.get_size())*BALLISTA_RESIZE_FACTOR)  
            self.current_image = self.static_image    
            self.posX = x + BALLISTA_OFFSET[0]
            self.posY = y + BALLISTA_OFFSET[1]
            self.number_frame_attacking = BALLISTA_NUMBER_FRAME_ATTACKING

            self.firing_period = BALLISTA_FIRING_PERIOD #in ms
            self.my_timer = 0

            self.attacking = True
            self.attack_finished = True

            self.image_attacking = []
            for i in range(1,self.number_frame_attacking+1):
                  self.image_attacking.append(pygame.image.load(self.images_path+str(i).zfill(4)+".png").convert_alpha())   
                  self.image_attacking[i-1] = pygame.transform.scale(self.image_attacking[i-1],pygame.Vector2(self.image_attacking[i-1].get_size())*BALLISTA_RESIZE_FACTOR)


            self.firing_frame = BALLISTA_FIRING_FRAME-1
            self.anim_frame = 0
            self.time_per_frame = self.firing_period/self.number_frame_attacking # in ms

            self.detected_ennemies = False
            self.my_target = []

            self.hitbox_left = x
            self.hitbox_top = y
            self.hitbox_width = BACKGROUND_SQUARE_SIDE
            self.hitbox_height = BACKGROUND_SQUARE_SIDE
            self.rect = pygame.Rect(self.hitbox_left,self.hitbox_top,self.hitbox_width,self.hitbox_height)

            self.range = BALLISTA_RANGE*(self.rect.width+self.rect.height)/2.0
            self.range_hitbox = Range_Hitbox(self,self.rect.w,self.rect.h,self.range,circular=False)


      def attack_and_reload(self,game):
            if (self.attacking):
                  self.attack_finished = False
                  self.my_timer += game.timestep
                  if self.my_timer>self.time_per_frame:
                        self.anim_frame += 1
                        self.anim_frame = self.anim_frame%self.number_frame_attacking
                        self.my_timer = 0.0
                        if (self.anim_frame==self.firing_frame):
                              game.all_projectiles.add(Bolt(self.posX+BALLISTA_FIRING_OFFSET[0],self.posY+BALLISTA_FIRING_OFFSET[1],self.my_target))
            else:
                  if not(self.attack_finished):
                        self.my_timer += game.timestep
                        if self.my_timer>self.time_per_frame:
                              self.anim_frame += 1
                              self.anim_frame = self.anim_frame%self.number_frame_attacking
                              self.my_timer = 0.0
                              if (self.anim_frame==0):
                                    self.attack_finished = True     

            self.current_image= self.image_attacking[self.anim_frame]
 

