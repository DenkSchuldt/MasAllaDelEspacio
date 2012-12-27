'''
Created on Dec 26, 2012

@author: Lilly
'''
from vec2d import *
import pygame

class Muneco:
    def __init__(self):
        self.marciano= pygame.image.load("images/personaje.png")
        self.posicion=vec2d(0,0)
        self.objetivo=vec2d(0,0)