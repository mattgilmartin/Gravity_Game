# -*- coding: utf-8 -*-
"""
Created on Mon May 13 21:17:38 2019

@author: Matt
"""

import pygame, random

class player:
    
    def __init__(self):
        self.texture_path = r'../images/matt_head_icon.png'
    #    self.cg = self.PLAYER.get_rect().center
        self.radius = 20
        self.pos = [0,0]
        self.vel = [0,0]
        self.acl = [0,0]
        self.mass = 1
        self.fuel = 1000
        self.ctrl_pwr = 15
        
    def render(self,surf):
        surf.blit(self.texture,(self.pos[0] , self.pos[1] ))

class star:
    
    def __init__(self):
        
        #Texture Info
        self.texture_path = r'../images/64bit_sun.png'
#        self.texture = pygame.image.load(self.texture_path)
        self.radius = 64
#        self.width, self.height = self.texture.get_size()
#        self.width,self.height = self.radius, self.radius
        self.color = (255,255,0)
        #Physics
        self.mass = 100
        #Positional
        self.pos = [500,500]
#        self.x = 500
#        self.y = 500
#        self.vx = 0
#        self.vy = 0
        self.vel = [0,0]
        self.acl = [0,0]
        
    def render(self,surf):
        pygame.draw.circle(surf,self.color,self.pos,self.radius)
        
class gas_giant:
    
    def __init__(self):
        
        #Texture Info
        self.texture_path = r'../images/64bit_gas_giant.png'
#        self.texture = pygame.image.load(self.texture_path)
#        self.width, self.height = self.texture.get_size()
        self.radius = 20
        #Physics
        self.mass = 25
        #Positional
        self.pos = [500,500]
#        self.x = 500
#        self.y = 500
#        self.vx = 0
#        self.vy = 0
        self.vel = [0,0]
        self.acl = [0,0]
        
    def render(self,surf):
        surf.blit(self.texture, self.pos)
        
class black_hole:
    
    def __init__(self):
        
        #Texture Info
        self.texture_path = r'../images/64bit_black_hole.png'
#        self.texture = pygame.image.load(self.texture_path)
        self.width, self.height = self.texture.get_size()
        self.radius = 75
        #Physics
        self.mass = 200
        #Positional
#        self.x = 1000
#        self.y = 1000
#        self.vx = 0
#        self.vy = 0
        self.vel = [0,0]
        self.acl = [0,0]
        
    def render(self,surf):
        pygame.draw.circle(surf,(255,255,0),self.pos,self.radius)

class jet:
    
    def __init__(self):
        
        self.radius = random.randint(0,20)
        self.pos = [500,500]
        self.vel = [0,0]
        
        #Sound Effects
        self.sfx_file = r'../sounds/psh.wav'
        self.sfx = pygame.mixer.Sound(self.sfx_file)
        self.sfx.set_volume(.5)
        
        
    def render(self,surf):
        pygame.draw.circle(surf,(255,255,255),[round(ii) for ii in self.pos],round(self.radius))
        
class magnet_particles:
    
    def __init__(self):
        self.radius = 5
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.pos = [random.randint(0,1920),random.randint(0,1080)]
        self.vel = [0,0]
        self.acl = [0,0]
        
    def render(self,surf):
        pygame.draw.circle(surf,self.color,[round(ii) for ii in self.pos],self.radius)
        
        
class goal:
    def __init__(self):
        self.radius = 32
#        self.pos = [random.randint(0,1920),random.randint(0,1080)]
        self.pos = [0,0]
        self.color = (0,255,0)
        
    def is_goal(self,player_pos):
        r = ((player_pos[0]-self.pos[0])**2 + (player_pos[1]-self.pos[1])**2)**.5
        
        if r <= self.radius:
            return True
        else: False
        
    def render(self,surf):
        pygame.draw.circle(surf,self.color,self.pos,self.radius)