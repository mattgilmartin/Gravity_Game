# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 11:11:17 2019

Gravity Launcher

@author: Matt
"""

import pygame
from pygame.locals import *
 
import gravity_game_core as ggc


class Launcher:
    
    def __init__(self):
        pygame.init()
        
        self._running = True
        self._display_surf = None
        
        self.tilesize = 64
        self.mapwidth = 25
        self.mapheight = 12
        
        #Initialize Background Music
#        self.bkg_music = pygame.mixer.Sound(r'..\sounds\Eyes_of_Glory.wav')
#        self.bkg_music.set_volume(.5)
#        self.bkg_music.play()
    
        
        self.size = (1920,1080)
        
        self.title_font = pygame.font.SysFont('arial',120)
        
        self._display_surf = pygame.display.set_mode(self.size) #Map Takes up Whole Screen
        self.background = pygame.image.load(r'../images/HD_Starfield.png')
        
        self.is_running = True
        
   
    def cleanup_(self):
        pygame.quit()
        
    def execute_(self):
        
        while self.is_running:
            for event in pygame.event.get():
                self.process_events(event)
                
            self.render_()
            
        self.cleanup_()
    
    def render_(self):
        self._display_surf.blit(self.background,(0,0))
                
        text_obj = self.title_font.render(str('Matt''s Amazing Gravity Game'),True,[255,255,255])
        self._display_surf.blit(text_obj,(20,10))
        
        self.play_text = self.title_font.render(str('Play'),True,[255,255,255])
        self.play_text_pos = (20,160)
        self._display_surf.blit(self.play_text,self.play_text_pos)
        
        self.exit_text = self.title_font.render(str('Exit'),True,[255,255,255])
        self.exit_text_pos = (20,310)
        self._display_surf.blit(self.exit_text,self.exit_text_pos)
        
        pygame.display.update()
        
    def process_events(self,event):
        
        if event.type == pygame.QUIT:
            self.is_running = False
        
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.is_running = False
                
        elif event.type == MOUSEBUTTONDOWN:
#            print(pygame.mouse.get_pos())
            mouse_pos = pygame.mouse.get_pos()
            
            #Play Button
            if self.button_click_(mouse_pos, self.play_text_pos,self.play_text.get_rect()):
                game = ggc.App
                self.failure = False
                self.score = 0
                self.level_name = 'Level_2.xml'
                while not self.failure: 
                    game.execute_(self)
                    
            #Exit Button
            if self.button_click_(mouse_pos, self.exit_text_pos,self.exit_text.get_rect()):
                self.is_running = False
                
    def button_click_(self,mouse_pos,text_pos,text_rect):
        inx = mouse_pos[0] > text_pos[0] and mouse_pos[0] < text_pos[0]+text_rect[2]
        iny = mouse_pos[1] > text_pos[1] and mouse_pos[1] < text_pos[1]+text_rect[3]
        
        if inx and iny:
            return True
        else:
            return False
            
       
if __name__ == "__main__" :
    theApp = Launcher()
    theApp.execute_()