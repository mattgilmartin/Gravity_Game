# -*- coding: utf-8 -*-
"""
Created on Mon May 13 20:13:04 2019

@author: Matt
"""

import pygame
from pygame.locals import *
 
import render_engine, physics_engine, events_engine, resources


## Process Events--------------------------------------------------------------     
def process_events(self,event):
    if event.type == pygame.QUIT:
        self._running = False
        
    elif event.type == KEYDOWN:
        
        ## Move Player --------------------------------
#        if event.key == K_RIGHT and self.player.pos[0] < self.size[0]-self.tilesize:
#            self.player.pos[0] += self.tilesize
#            
#        elif event.key == K_LEFT and self.player.pos[0] > 0:
#            self.player.pos[0] -= self.tilesize
#            
#        elif event.key == K_UP and self.player.pos[1] > 0:
#            self.player.pos[1] -= self.tilesize  
#            
#        elif event.key == K_DOWN and self.player.pos[1] < self.size[1]-self.tilesize:
#            self.player.pos[1] += self.tilesize
            
        if event.key == K_SPACE:
            self.objs.append(resources.gas_giant())
                       
        elif event.key == K_c:
            self.player.vel = [0,0]
        
        elif event.key == K_l:
#            print('l')
            self.failure = True
            
        elif event.key == K_o:
#            print('O')
            self.victory = True
            
        elif event.key == K_ESCAPE:
            self._running = False
            self.failure = True
            

            
def process_pressed(self):
    keys = pygame.key.get_pressed()
    
    self.control_acl = [0,0]
    
    if keys[pygame.K_UP]:
        if self.player.fuel>0:
            self.control_acl[1] -= 10
            
            self.jet_objs.append(resources.jet())
            self.jet_objs[-1].pos = [self.player.pos[0]+32,self.player.pos[1]+64]
            self.jet_objs[-1].vel = [0,self.player.ctrl_pwr]
            self.jet_objs[-1].sfx.play()
            self.player.fuel -= 1
        
    if keys[pygame.K_DOWN]:
        if self.player.fuel>0:
            self.control_acl[1] += 10
            
            self.jet_objs.append(resources.jet())
            self.jet_objs[-1].pos = [self.player.pos[0]+32,self.player.pos[1]]
            self.jet_objs[-1].vel = [0,-self.player.ctrl_pwr]
            self.jet_objs[-1].sfx.play()
            self.player.fuel -= 1
        
    if keys[pygame.K_LEFT]:
        if self.player.fuel>0:
            self.control_acl[0] -= 10
            
            self.jet_objs.append(resources.jet())
            self.jet_objs[-1].pos = [self.player.pos[0]+64,self.player.pos[1]+32]
            self.jet_objs[-1].vel = [self.player.ctrl_pwr,0]
            self.jet_objs[-1].sfx.play()
            self.player.fuel -= 1
        
    if keys[pygame.K_RIGHT]:
        if self.player.fuel>0:
            self.control_acl[0] += 10
            
            self.jet_objs.append(resources.jet())
            self.jet_objs[-1].pos = [self.player.pos[0],self.player.pos[1]+32]
            self.jet_objs[-1].vel = [-self.player.ctrl_pwr,0]
            self.jet_objs[-1].sfx.play()
            self.player.fuel -= 1
    