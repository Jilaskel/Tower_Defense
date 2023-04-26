import pygame
from ennemy import *
from utilitaries import *
import random
import numpy as np

class Spawning_mode():
    def __init__(self,game):
        self.spawning_margin = game.background.bush_width*SPAWNING_MARGIN_SPACE
        
        if SPAWNING_WITH_SCRIPT:
            self.my_script = np.array([[2.0, GOBLIN_TAG, 1],     # temps en s, type, quantite
                        [8.0, GOBLIN_TAG, 2],
                        [16.0, GOBLIN_TAG, 3],
                        [20.0, GOBLIN_TAG, 3],
                        [24.0, GOBLIN_TAG, 3],
                        [100000, GOBLIN_TAG, 1]])
            self.line = 0
        else:
            last_phase = False
            self.my_dict = SPAWNING_DICT

            i = 1
            self.my_phases = []
            while not(last_phase):
                char = "P"+ str(i) + "_DURATION"
                if char in self.my_dict:
                    self.my_phases.append(Spawning_phase(self.my_dict,i))
                    i += 1
                else:
                    last_phase = True

            self.reset()  

            self.last_phase = i-2
            self.time_last_phase = INITIAL_SPAWNING_TIME
            self.display_time = ROUND_DISPLAY_TIME

            self.font_size = int(140*RESIZE_COEFF)
            self.font = pygame.font.Font(LOADING_FONT_PATH,self.font_size)
            self.font_color = (0,0,0) # (243,243,243)
            self.rendering_layer = 26

            self.font_size_small = int(70*RESIZE_COEFF)
            self.font_small = pygame.font.Font(LOADING_FONT_PATH,self.font_size_small)

            self.small_txt = []

            self.display(0,"Prepare Your Defenses!")

    def display(self,i,txt=None):
        if txt:
            text = txt
        else:
            if (i-1==self.last_phase):
                text = "Last Round"
                self.small_txt.clear()
            else:
                text = "Round " + str(i)

                self.small_txt.clear()
                if (self.my_phases[self.current_phase].hp_coeff != 1) :
                    text_small = "HP coeff : x" + str(self.my_phases[self.current_phase].hp_coeff)
                    self.small_txt.append(self.font_small.render(text_small,True,self.font_color))

                if (self.my_phases[self.current_phase].damage_coeff != 1) :
                    text_small = "Damage coeff : x" + str(self.my_phases[self.current_phase].damage_coeff)
                    self.small_txt.append(self.font_small.render(text_small,True,self.font_color))

                if (self.my_phases[self.current_phase].velocity_coeff != 1) :
                    text_small = "Velocity coeff : x" + str(self.my_phases[self.current_phase].velocity_coeff)
                    self.small_txt.append(self.font_small.render(text_small,True,self.font_color))

        self.main_text = self.font.render(text,True,self.font_color)  

        self.timer_display = 0.0

        self.displayed = False

    def render(self):
        if not(self.displayed):
            image_size = vec(self.main_text.get_size())
            x = WINDOW_WIDTH*0.5 - image_size[0]*0.5
            window.blit(self.main_text, (x, 380*RESIZE_COEFF))   

            j = 0
            for small_txt in self.small_txt:
                image_size = vec(small_txt.get_size())
                x = WINDOW_WIDTH*0.5 - image_size[0]*0.5
                window.blit(small_txt, (x, 580*RESIZE_COEFF+j*100))    
                j += 1                           

        if (self.timer_display>self.display_time):
            self.displayed = True


    def reset(self):
        self.number_goblin_spawned = 1.0
        self.last_time_spawning_goblin = INITIAL_SPAWNING_TIME+TIME_BETWEEN_ROUNDS             
        self.number_ogre_spawned = 1.0
        self.last_time_spawning_ogre = INITIAL_SPAWNING_TIME+TIME_BETWEEN_ROUNDS            
        self.number_blue_nec_spawned = 1.0
        self.last_time_spawning_blue_nec = INITIAL_SPAWNING_TIME+TIME_BETWEEN_ROUNDS    
        self.number_red_nec_spawned = 1.0
        self.last_time_spawning_red_nec = INITIAL_SPAWNING_TIME+TIME_BETWEEN_ROUNDS 
        self.number_green_nec_spawned = 1.0
        self.last_time_spawning_green_nec = INITIAL_SPAWNING_TIME+TIME_BETWEEN_ROUNDS 
        self.number_kamikaze_spawned = 1.0
        self.last_time_spawning_kamikaze = INITIAL_SPAWNING_TIME+TIME_BETWEEN_ROUNDS          
        self.number_dragon_spawned = 1.0
        self.last_time_spawning_dragon = INITIAL_SPAWNING_TIME+TIME_BETWEEN_ROUNDS      

        self.current_phase = 0

        spawning_coeff.hp_coeff = self.my_phases[self.current_phase].hp_coeff
        spawning_coeff.damage_coeff = self.my_phases[self.current_phase].damage_coeff
        spawning_coeff.velocity_coeff = self.my_phases[self.current_phase].velocity_coeff        


    def reset_hard(self):
        self.reset()
        self.time_last_phase = INITIAL_SPAWNING_TIME
        self.display(0,"Prepare Your Defenses!")

    def reset_cd(self,time):
        self.number_goblin_spawned = 1.0
        self.last_time_spawning_goblin = time+TIME_BETWEEN_ROUNDS             
        self.number_ogre_spawned = 1.0
        self.last_time_spawning_ogre = time+TIME_BETWEEN_ROUNDS             
        self.number_blue_nec_spawned = 1.0
        self.last_time_spawning_blue_nec = time+TIME_BETWEEN_ROUNDS    
        self.number_red_nec_spawned = 1.0
        self.last_time_spawning_red_nec = time+TIME_BETWEEN_ROUNDS 
        self.number_green_nec_spawned = 1.0
        self.last_time_spawning_green_nec = time+TIME_BETWEEN_ROUNDS 
        self.number_kamikaze_spawned = 1.0
        self.last_time_spawning_kamikaze = time+TIME_BETWEEN_ROUNDS          
        self.number_dragon_spawned = 1.0
        self.last_time_spawning_dragon = time+TIME_BETWEEN_ROUNDS    

    def spawning_ennemies(self,game):
        time = game.timer/1000.0  # in second
        self.timer_display += game.timestep*0.001

        if SPAWNING_WITH_SCRIPT:
            time_next_ennemy = self.my_script[self.line,0]
            if (time>time_next_ennemy):
                self.spawn(game,int(self.my_script[self.line,1]),int(self.my_script[self.line,2]))
                self.line += 1
        else:
            if not(TURN_OFF_NATURAL_SPAWNING):
                if time>INITIAL_SPAWNING_TIME:
                    if (time>(self.my_phases[self.current_phase].duration+self.time_last_phase)):
                        if not(self.current_phase==self.last_phase):
                            self.current_phase += 1
                            self.time_last_phase = time
                            self.reset_cd(time)

                            spawning_coeff.hp_coeff = self.my_phases[self.current_phase].hp_coeff
                            spawning_coeff.damage_coeff = self.my_phases[self.current_phase].damage_coeff
                            spawning_coeff.velocity_coeff = self.my_phases[self.current_phase].velocity_coeff

                        else:
                            dt = game.timestep*0.001
                            spawning_coeff.hp_coeff += LAST_ROUND_HP_COEFF_PER_SEC*dt
                            spawning_coeff.damage_coeff += LAST_ROUND_DAMAGE_COEFF_PER_SEC*dt
                            spawning_coeff.velocity_coeff += LAST_ROUND_VELOCITY_COEFF_PER_SEC*dt                           

                    if (time>(self.time_last_phase+TIME_BETWEEN_ROUNDS*0.5) and (time<(self.time_last_phase+TIME_BETWEEN_ROUNDS*0.5+game.timestep*0.001*2))):
                            self.display(self.current_phase+1)

                    phase = self.my_phases[self.current_phase]

                        
                    cooldown = phase.ennemy_period[GOBLIN_TAG-1]*self.number_goblin_spawned 
                    if ((time-self.last_time_spawning_goblin)>cooldown):
                        self.last_time_spawning_goblin = time
                        max_sim = phase.ennemy_max_sim[GOBLIN_TAG-1]
                        self.number_goblin_spawned = random.randint(1,max_sim)
                        self.spawn(game,GOBLIN_TAG,self.number_goblin_spawned)

                    cooldown = phase.ennemy_period[OGRE_TAG-1]*self.number_ogre_spawned 
                    if ((time-self.last_time_spawning_ogre)>cooldown):
                        self.last_time_spawning_ogre = time
                        max_sim = phase.ennemy_max_sim[OGRE_TAG-1]
                        self.number_ogre_spawned = random.randint(1,max_sim)
                        self.spawn(game,OGRE_TAG,self.number_ogre_spawned)

                    cooldown = phase.ennemy_period[BLUE_NEC_TAG-1]*self.number_blue_nec_spawned 
                    if ((time-self.last_time_spawning_blue_nec)>cooldown):
                        self.last_time_spawning_blue_nec = time
                        max_sim = phase.ennemy_max_sim[BLUE_NEC_TAG-1]
                        self.number_blue_nec_spawned = random.randint(1,max_sim)
                        self.spawn(game,BLUE_NEC_TAG,self.number_blue_nec_spawned)

                    cooldown = phase.ennemy_period[RED_NEC_TAG-1]*self.number_red_nec_spawned 
                    if ((time-self.last_time_spawning_red_nec)>cooldown):
                        self.last_time_spawning_red_nec = time
                        max_sim = phase.ennemy_max_sim[RED_NEC_TAG-1]
                        self.number_red_nec_spawned = random.randint(1,max_sim)
                        self.spawn(game,RED_NEC_TAG,self.number_red_nec_spawned)

                    cooldown = phase.ennemy_period[GREEN_NEC_TAG-1]*self.number_green_nec_spawned 
                    if ((time-self.last_time_spawning_green_nec)>cooldown):
                        self.last_time_spawning_green_nec = time
                        max_sim = phase.ennemy_max_sim[GREEN_NEC_TAG-1]
                        self.number_green_nec_spawned = random.randint(1,max_sim)
                        self.spawn(game,GREEN_NEC_TAG,self.number_green_nec_spawned)

                    cooldown = phase.ennemy_period[KAMIKAZE_TAG-1]*self.number_kamikaze_spawned 
                    if ((time-self.last_time_spawning_kamikaze)>cooldown):
                        self.last_time_spawning_kamikaze = time
                        max_sim = phase.ennemy_max_sim[KAMIKAZE_TAG-1]
                        self.number_kamikaze_spawned = random.randint(1,max_sim)
                        self.spawn(game,KAMIKAZE_TAG,self.number_kamikaze_spawned)

                    cooldown = phase.ennemy_period[DRAGON_TAG-1]*self.number_dragon_spawned 
                    if ((time-self.last_time_spawning_dragon)>cooldown):
                        self.last_time_spawning_dragon = time
                        max_sim = phase.ennemy_max_sim[DRAGON_TAG-1]
                        self.number_dragon_spawned = random.randint(1,max_sim)
                        self.spawn(game,DRAGON_TAG,self.number_dragon_spawned)
                # else:
                #     if time>(INITIAL_SPAWNING_TIME-0.1):
                #         self.display(self.current_phase+1)
                    

    def spawn(self,game,TAG,number_of_ennemies):
        for i in range (number_of_ennemies):
            if i==0:
                path_number = random.randint(0,2)
            else:
                path_number = (path_number+1)%3

            x_path = self.spawning_margin
            side = game.background.square_side
            
            y_path = game.background.menu_height + side*(1+2*path_number) + (random.randint(0,1)-0.5)*side*0.5  #used for tests
            rand_offset = random.random()-0.5
            # y_path = game.background.menu_height + side*(1+2*path_number) + rand_offset*side*0.5

            if (TAG==GOBLIN_TAG):
                game.all_ennemies.add_goblin(x_path,y_path,rand_offset)

            if (TAG==OGRE_TAG):
                game.all_ennemies.add_ogre(x_path,y_path,rand_offset)

            if (TAG==BLUE_NEC_TAG):
                game.all_ennemies.add_blue_nec(x_path,y_path,rand_offset)

            if (TAG==RED_NEC_TAG):
                game.all_ennemies.add_red_nec(x_path,y_path,rand_offset)

            if (TAG==GREEN_NEC_TAG):
                game.all_ennemies.add_green_nec(x_path,y_path,rand_offset)

            if (TAG==BLUE_SKEL_TAG):
                game.all_ennemies.add_blue_skel(x_path,y_path)

            if (TAG==RED_SKEL_TAG):
                game.all_ennemies.add_red_skel(x_path,y_path)

            if (TAG==GREEN_SKEL_TAG):
                game.all_ennemies.add_green_skel(x_path,y_path)

            if (TAG==KAMIKAZE_TAG):
                game.all_ennemies.add_kamikaze(x_path,y_path,rand_offset)

            if (TAG==DRAGON_TAG):
                game.all_ennemies.add_dragon(x_path,y_path,rand_offset)


class Spawning_phase():
        def __init__(self,dict,phase_number):
            self.my_dict = dict
            self.phase_number = phase_number

            char = "DURATION"
            self.duration = self.find_in_dic(char,0.0)

            char = "HP_COEFF"
            self.hp_coeff = self.find_in_dic(char,1.0)
            char = "DAMAGE_COEFF"
            self.damage_coeff = self.find_in_dic(char,1.0)
            char = "VELOCITY_COEFF"
            self.velocity_coeff = self.find_in_dic(char,1.0)

            self.ennemy_period= []
            self.ennemy_max_sim = []
            char = "GOBLIN"
            self.ennemy_period.append(self.find_period_in_dic(char))
            self.ennemy_max_sim.append(self.find_max_sim_in_dic(char))
            char = "OGRE"
            self.ennemy_period.append(self.find_period_in_dic(char))
            self.ennemy_max_sim.append(self.find_max_sim_in_dic(char))
            char = "BLUE_NEC"
            self.ennemy_period.append(self.find_period_in_dic(char))
            self.ennemy_max_sim.append(self.find_max_sim_in_dic(char))
            char = "RED_NEC"
            self.ennemy_period.append(self.find_period_in_dic(char))
            self.ennemy_max_sim.append(self.find_max_sim_in_dic(char))
            char = "GREEN_NEC"
            self.ennemy_period.append(self.find_period_in_dic(char))
            self.ennemy_max_sim.append(self.find_max_sim_in_dic(char))
            char = "KAMIKAZE"
            self.ennemy_period.append(self.find_period_in_dic(char))
            self.ennemy_max_sim.append(self.find_max_sim_in_dic(char))
            char = "DRAGON"
            self.ennemy_period.append(self.find_period_in_dic(char))
            self.ennemy_max_sim.append(self.find_max_sim_in_dic(char))


        def find_in_dic(self,char,default):
            complete_char = "P"+ str(self.phase_number) + "_" + char
            if complete_char in self.my_dict:
                return(self.my_dict[complete_char])
            else:
                return(default)

        def find_period_in_dic(self,char):
            complete_char = "P"+ str(self.phase_number) + "_" + char + "_PERIOD"
            if complete_char in self.my_dict:
                return(self.my_dict[complete_char])
            else:
                return(1e6)

        def find_max_sim_in_dic(self,char):
            complete_char = "P"+ str(self.phase_number) + "_MAX_" + char + "_SIMULTANEOUSLY"
            if complete_char in self.my_dict:
                if ((self.my_dict[complete_char]<1) or (self.my_dict[complete_char]>3)):
                    return(1)
                else:
                    return(self.my_dict[complete_char])
            else:
                return(3)