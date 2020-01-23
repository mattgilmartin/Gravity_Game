# -*- coding: utf-8 -*-
"""
Created on Mon May 13 20:10:24 2019

@author: Matt
"""

import pygame
from pygame.locals import *
 
import render_engine, physics_engine, events_engine, resources


def run_physics(self):
    
    ## Calculate Player Physics
    self.player.acl = [0,0]
    cg = self.player.cg
    
    # Calculate remaining fuel
    self.player.fuel_pct = self.player.fuel / self.player.fuel_max
    
    for cur_obj in self.map_objs:
        #Star Physics-axis Physics
#        cur_obj.vy += self.g * self.dt
#        cur_obj.y += cur_obj.vy *self.dt
#        
#        if cur_obj.y > self.size[1] - cur_obj.height:
#            cur_obj.vy = -cur_obj.vy
#            cur_obj.y = self.size[1] - cur_obj.height
            
        #Calculate Player Gravity

        r = ((self.player.pos[0]+cg[0]-cur_obj.pos[0])**2 + (self.player.pos[1]+cg[1]-cur_obj.pos[1])**2)**.5
        if r < cur_obj.radius+self.player.radius:
            self.failure = True
        
        acl_g = self.G * cur_obj.mass/(r ** 2)
        
        self.player.acl[0] -= acl_g * (self.player.pos[0]+cg[0]-cur_obj.pos[0]) / r
        self.player.acl[1] -= acl_g * (self.player.pos[1]+cg[1]-cur_obj.pos[1]) / r
    
    #Key Controls
    
    self.player.acl = [self.player.acl[ii] + self.control_acl[ii] for ii in [0,1]]
    
    
    #Player Vel
    self.player.vel[0] += self.player.acl[0] * self.dt
    self.player.vel[1] += self.player.acl[1] * self.dt    
    
    #Player Position
    print(self.player.pos)
    self.player.pos[0] += self.player.vel[0] * self.dt
    self.player.pos[1] += self.player.vel[1] * self.dt    
    
    #Keep Player on Screen
    if self.player.pos[0] < 0:
        self.player.pos[0] = 0
    elif self.player.pos[0] >  self.size[0]-self.tilesize:
        self.player.pos[0] = self.size[0]-self.tilesize
        
    if self.player.pos[1] < 0:
        self.player.pos[1] = 0
    elif self.player.pos[1] >  self.size[1]-self.tilesize:
        self.player.pos[1] = self.size[1]-self.tilesize
        
    ## Jet Physics
    
    #Delete tiny objects
    idx = 0
    while idx < len(self.jet_objs): #and not len(self.jet_objs) == 0:
        if self.jet_objs[idx].radius < .5:
            self.jet_objs.pop(idx)
        else:
            idx += 1    
        
    for cur_obj in self.jet_objs:
        
        cur_obj.radius = cur_obj.radius * .95
        cur_obj.pos[0] += cur_obj.vel[0] * self.dt
        cur_obj.pos[1] += cur_obj.vel[1] * self.dt   
        
    particle_physics(self)

    ## Determine Win State
    play_pos = [self.player.pos[ii]+self.player.radius for ii in [0,1]]
    if self.goal.is_goal(play_pos):
        self.victory = True
        
    ## Particle Physics -Currently Broken
def particle_physics(self):
    for cur_obj in self.mag_objs:
        r = ((self.player.pos[0]+self.player.cg[0]-cur_obj.pos[0])**2 + (self.player.pos[1]+self.player.cg[1]-cur_obj.pos[1])**2)**.5
        
        acl_g = self.G * self.player.mass/(r ** 3)
        
        cur_obj.acl[0] = -acl_g * ( (self.player.pos[0]+self.player.cg[0]-cur_obj.pos[0]) /r)
        cur_obj.acl[1] = -acl_g * ( (self.player.pos[1]+self.player.cg[1]-cur_obj.pos[1]) /r)
        
        cur_obj.vel[0] += cur_obj.acl[0] * self.dt
        cur_obj.vel[1] += cur_obj.acl[1] * self.dt
        
        cur_obj.pos[0] += cur_obj.vel[0] * self.dt
        cur_obj.pos[1] += cur_obj.vel[1] * self.dt
        
        #Keep Player on Screen
#        if cur_obj.pos[0] < cur_obj.radius:
#            cur_obj.pos[0] = cur_obj.radius
#        elif cur_obj.pos[0] >  self.size[0]-cur_obj.radius:
#            cur_obj.pos[0] = self.size[0]-cur_obj.radius
#            
#        if cur_obj.pos[1] < cur_obj.radius:
#            cur_obj.pos[1] = cur_obj.radius
#        elif cur_obj.pos[1] >  self.size[1]-cur_obj.radius:
#            cur_obj.pos[1] = self.size[1]-cur_obj.radius
        
def find_collides(self):
    pass