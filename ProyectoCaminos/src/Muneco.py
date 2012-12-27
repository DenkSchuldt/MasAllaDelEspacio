'''
Created on Dec 26, 2012

@author: Lilly
'''
from vec2d import *
import pygame


class Muneco:
    def __init__(self):
        try:
            self.marciano= pygame.image.load("images/nave.png")
        except:
            print "no se encontro"
        
        self.posicion=vec2d(0,0)
        self.objetivo=vec2d(0,0)