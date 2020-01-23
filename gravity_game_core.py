# -*- coding: utf-8 -*-
"""
Created on Mon May 13 20:01:57 2019

@author: Matt
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:01:52 2019

http://usingpython.com/pygame-tilemaps/

@author: usingpython.com
"""

import pygame
from pygame.locals import *
 
import render_engine, physics_engine, events_engine, init_game, resources
import random, time

class App:
    
    def __init__(self):
        self._running = True
        self._display_surf = None
        
        self.tilesize = 64
        self.mapwidth = 25
        self.mapheight = 12
        
        
        self.size = (1920,1080)
        
## Clean Up Game (Exit) -------------------------------------------------------    
    def cleanup_(self):
        pygame.quit()

## Execute Game Functions -----------------------------------------------------        
    def execute_(self):
        
        init_game.init_game(self)
#        if self.init_game.init_game() == False:
#            self._running = False
            
        while self._running:
            for event in pygame.event.get():
                events_engine.process_events(self,event)
            
            events_engine.process_pressed(self)
            
            physics_engine.run_physics(self)
            render_engine.render(self)
            
#            print(len(self.jet_objs)) # Number of Active Jet particles
            
            #Endgame Conditions
            if self.victory:
#                render_engine.message_display(self,'Mission Sucess!')
                #Play Victory Sound
                pygame.mixer.Sound(r'..\sounds\airhorn_mult.wav').play()
                self.score =+self.player.fuel
                self._running = False
                
            if self.failure:
#                render_engine.message_display(self,'Failure!')
                pygame.mixer.Sound(r'..\sounds\priceIsRightTrombone.wav').play()
                
                self._running = False
                
#            print(self._running,self.victory, self.failure)
                
#        while True:
#            if pygame.event.get():  
        
        text_obj = self.fuel_font.render(str('Press Any Key to Continue'),True,[255,255,255])
        self._display_surf.blit(text_obj,(1000,1750))
        pygame.display.update()
        
        hold_screen = True
        while hold_screen:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    hold_screen = False
                
#        time.sleep(10)
#        self.cleanup_()
        
   
if __name__ == "__main__" :
    theApp = App()
    theApp.execute_()