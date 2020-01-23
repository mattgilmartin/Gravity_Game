# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 11:11:17 2019

Gravity Game Map Builder

@author: Matt
"""

import pygame
from pygame.locals import *
 
import gravity_game_core as ggc

import render_engine, physics_engine, events_engine, init_game, resources
import random, pickle

class Launcher:
    
    def __init__(self):
        pygame.init()
        
        self._running = True
        self._display_surf = None
        
        ##################################
        ##           User Inputs        ##
        self.filename = 'Level_2.xml'
        self.fuel_max = 1000
        ##################################
        
        
        
        self.tilesize = 64
        self.mapwidth = 25
        self.mapheight = 12
        
        
        self.size = (1920,1080)
        
        self.title_font = pygame.font.SysFont('arial',120)
        
#        self._display_surf = pygame.display.set_mode(self.size) #Map Takes up Whole Screen
        self.background = pygame.image.load(r'../images/HD_Starfield.png')
        
        self._display_surf = pygame.display.set_mode(self.size) 
        
        self.player = resources.player()
        self.player.texture = pygame.image.load(self.player.texture_path)
        self.goal = resources.goal()
        self.map_objs = []
        
        self.actv_key = None
        
        self.is_running = True
        
   
    def cleanup_(self):
        pygame.quit()
        
    def execute_(self):
        
        while self.is_running:
            for event in pygame.event.get():
                self.process_events(event)
                
            self.render_()
            pygame.display.update()
            
#            print(len(self.map_objs))
            
        self.cleanup_()
    
    def render_(self):
        self._display_surf.blit(self.background,(0,0))

        #Draw Map Objects
        for cur_obj in self.map_objs:
            cur_obj.render(self._display_surf)
            
        #Draw Goal
        self.goal.render(self._display_surf)
        
        #Draw Player
        self.player.render(self._display_surf)
        
#        pygame.display.update()
#        print(self.map_objs)
        
    def process_events(self,event):
        
        if event.type == pygame.QUIT:
            self.is_running = False
        
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.is_running = False
                
            elif event.key == K_s:
                self.save_level()
                print(self.filename + ' Saved!')
                
            elif event.key == K_r:
                self.render_()
                pygame.display.update()
                print('Manually Re-Rendered')
                
            elif event.key == K_0:
                self.actv_obj = resources.player()
                self.actv_key = 0
            elif event.key == K_1:
                self.actv_obj = resources.star()
                self.actv_key = 1
            elif event.key == K_2:
                self.actv_obj = resources.gas_giant()
                self.actv_obj.texture = pygame.image.load(self.actv_obj.texture_path)
                self.actv_key = 2
            elif event.key == K_3:
                self.actv_obj = resources.goal()
                self.actv_key = 3
                
                
        elif event.type == MOUSEBUTTONDOWN:
#            print(pygame.mouse.get_pos())
            mouse_pos = pygame.mouse.get_pos()
#            print(mouse_pos)
            
            #Place Player
            if self.actv_key == 0:
#                self.player = self.actv_obj
                self.player.pos = mouse_pos
                
            #Place Star
            elif self.actv_key == 1:         
                radius = self.size_circle(mouse_pos)     
                self.actv_obj.pos = mouse_pos
                self.actv_obj.radius = radius
                
                self.map_objs.append(self.actv_obj)
            
            #Place Gas Giant
            elif self.actv_key == 2:
                
                self.actv_obj.pos = mouse_pos 
                self.map_objs.append(self.actv_obj)
                
                
            #Place Goal    
            elif self.actv_key == 3:
#                self.goal = self.actv_obj
                radius = self.size_circle(mouse_pos)
                self.goal.pos = mouse_pos
                self.map_objs[-1].radius = radius
                
            self.render_()
#            pygame.display.update()
                
                
    def size_circle(self,p1):
        self.sizing = True
        
        while self.sizing:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    self.sizing = False
                    
            self.render_()
            
            p2 = pygame.mouse.get_pos()
            r = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**.5
            
            pygame.draw.circle(self._display_surf,self.actv_obj.color,p1,round(r))
            pygame.display.update()
        
        return round(r)
    
    def save_level(self):
        
#        self.map_objs.append(resources.star())
#        self.map_objs[0].pos = [500,250]
#        
#        self.map_objs.append(resources.star())
#        self.map_objs[1].pos = [500,750]
#        
#        self.map_objs.append(resources.star())
#        self.map_objs[2].pos = [1400,250]
#        
#        self.map_objs.append(resources.star())
#        self.map_objs[3].pos = [1400,750]
#        
#        self.player_fuel = 750
#        
#        self.goal = resources.goal()
#        self.goal.pos = [920,450]
#        
#        self.player = resources.player()
        # Remove Textures
        texture = self.player.texture
        self.player.texture = None
        for cur_obj in self.map_objs:
            try:
                cur_obj.texture = None
            except AttributeError:
                pass
        
        self.player.pos = list(self.player.pos)
        
        self.player.fuel_max = self.fuel_max
#        self.player.pos = [50,500]
        
        
        
        data = {'map_objs'      : self.map_objs,
                'goal'          : self.goal,
#                'goal_pos'      : self.goal.pos,
                'player'        : self.player}
#                'player_fuel'   : self.player_fuel,
#                'player_pos'    : self.player_pos}
        
        with open(self.filename, 'wb') as outfile:
            pickle.dump(data,outfile)  
            
        # Reload Textures    
        self.player.texture = texture
        for cur_obj in self.map_objs:
            try:
                cur_obj.texture = pygame.image.load(cur_obj.texture_path)
            except AttributeError:
                pass
      
if __name__ == "__main__" :
    theApp = Launcher()
    theApp.execute_()
#    theApp.save_level()
    theApp.cleanup_()