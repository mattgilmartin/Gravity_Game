# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 17:30:23 2019

@author: Matt
"""

import pygame
from pygame.locals import *
 
import render_engine, physics_engine, events_engine, init_game, resources
import random, pickle

## Game Initialization---------------------------------------------------------         
def init_game(self):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.set_num_channels(50)
    
    self._display_surf = pygame.display.set_mode(self.size) #Map Takes up Whole Screen

    pygame.display.set_caption('Gravity Game')
    
    #Initialize Background
    self.background = pygame.image.load(r'../images/HD_Starfield.png')
    
    #Initialize Level
    load_level(self)
    
    #Initialize Player
#    self.player = resources.player()
    self.player.texture = pygame.image.load(self.player.texture_path)
    self.player.cg = self.player.texture.get_rect().center
#    self.PLAYER = pygame.image.load(r'../images/matt_head_icon.png')
#    self.player_cg = self.PLAYER.get_rect().center
#    self.player_radius = 20
#    self.player_pos = [0,0]
#    self.player_vel = [0,0]
#    self.player_acl = [0,0]
#    self.player_mass = 1
#    self.player_fuel = 1000
#    self.player_ctrl_pwr = 15
    
    #Initialize Objects
#    self.map_objs = []
#    generate_map(self)
    
    
    self.jet_objs = []
    self.mag_objs = []
    
#    for ii in range(50):
#        self.mag_objs.append(resources.magnet_particles())
    
#    self.goal = resources.goal()
    
    #Initialize Physics Constants
    self.g = 9.8 # Gravity: m/s^2
    self.G = 6.674 * (10 **3)
    self.dt = 1/24   # Time Delta: s

    
    #Define Text Font(s)
    self.inv_font = pygame.font.SysFont('arial',120)
    self.fuel_font = pygame.font.SysFont('arial',32)
    
    self._running = True
    self.victory = False
    self.failure = False
    
    
    
def generate_map(self):
    for ii in range(5):
        switch = random.randint(0,1) #Won't make Black Holes, chg later
        
        if switch == 0:
            self.map_objs.append(resources.gas_giant())
            self.map_objs[-1].texture = pygame.image.load(self.map_objs[-1].texture_path)
            self.map_objs[-1].width, self.map_objs[-1].height = self.map_objs[-1].texture.get_size()
            
        elif switch == 1:
            self.map_objs.append(resources.star())
        elif switch == 2:
            self.map_objs.append(resources.black_hole())
            
        self.map_objs[ii].pos = [random.randint(240,self.size[0]),random.randint(0,self.size[1])]
        
def load_level(self):
#    level_name = 'test_level.xml'
    
    with open(self.level_name,'rb') as fid:   
        data = pickle.load(fid)
        
#    print(data)
    
    self.map_objs = data['map_objs']
    for cur_obj in self.map_objs:
        try:
            cur_obj.texture = pygame.image.load(cur_obj.texture_path)
        except AttributeError:
            pass
        
    self.goal = data['goal']
    self.player = data['player']
    self.player.fuel = self.player.fuel_max
#    self.goal.pos = data['goal_pos']
#    self.player_pos = data['player_pos']
#    self.player_fuel = data['player_fuel']
    
    
    


    