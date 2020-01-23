# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 13:15:34 2019

@author: Matt
"""

from distutils.core import setup
import py2exe

#from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QSizePolicy
#from PyQt5.QtWidgets import QGridLayout, QPushButton, QWidget, QFileDialog
#from PyQt5.QtWidgets import QAction, QStackedWidget
#import sys
#import math
#from os import path
#import pandas as pd
#import pygame as pg


setup(console = ['gravity_launcher.py'], packages = ['random','time','events_engine','gravity_game_core','init_game','map_builder','physics_engine','render_engine'])