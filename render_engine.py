# -*- coding: utf-8 -*-
"""
Created on Mon May 13 20:09:43 2019

@author: Matt
"""

import pygame
from pygame.locals import *
 
import render_engine, physics_engine, events_engine, resources


def render(self):
    
    ## Draw Background
    self._display_surf.blit(self.background,(0,0))
    
    ## Draw Objects
    for cur_obj in self.map_objs:
#        self._display_surf.blit(cur_obj.texture, (cur_obj.pos[0],cur_obj.pos[1]))
        cur_obj.render(self._display_surf)
        
    for cur_obj in self.mag_objs:
        cur_obj.render(self._display_surf)
        
    ## Draw Jets
    for cur_obj in self.jet_objs:
        cur_obj.render(self._display_surf)       
   
    ## Draw Goal
    self.goal.render(self._display_surf)
    
    ## Draw Player-------------------------------
    self._display_surf.blit(self.player.texture,(self.player.pos[0] , self.player.pos[1] ))
   
    ## Draw Fuel Inventory
    text_obj = self.fuel_font.render(str(self.player.fuel),True,[255,255,255])
    self._display_surf.blit(text_obj,(10,10))
    
    rect_ = [0, 0, round(self.size[1]/22), round(self.size[1]/22)]
    rect_[1] = round(self.size[1]/20) * 19
#    print(rect_)
    for ii in range(round(self.player.fuel_pct * 20)):
        
        pygame.draw.rect(self._display_surf,(255,0,0), rect_)
        
        rect_[1] -= round(self.size[1]/20)
    
    #Draw Victory
    if self.victory:
        text_obj = self.inv_font.render(str('Mission Sucess!'),True,[255,255,255])
        self._display_surf.blit(text_obj,(500,500))
#        print('Mission Sucess!')
        
    if self.failure:
        text_obj = self.inv_font.render('Failure!',True,(255,255,255))
        self._display_surf.blit(text_obj,(700,500))   
        
        text_obj = self.inv_font.render(('Final Score: ' + str(self.score)), True, [255,255,255])
        self._display_surf.blit(text_obj,(500,750))
    
    ## Update surface----------------------------
    pygame.display.update()
    
def message_display(self, text):
#    text_fmt = pygame.font.SysFont('arial',120)
    
    text_surf = self.inv_font.render(text,True,(255,255,255))
    
    text_rect = text_surf.get_rect()
    text_rect.center = (self.size[0]/2,self.size[1]/2)
    
    self._display_surf.blit(text_surf,(500,500))
    pygame.display.update()

   