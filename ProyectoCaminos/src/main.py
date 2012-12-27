import pygame
import pygame.locals 
from random import uniform
from Muneco import *
from ventana import *
from vec2d import *

class Main(Ventana):
    def __init__(self):
        self.ancho, self.alto = 900, 600
        Ventana.__init__(self, size=(self.ancho, self.alto), fill=((255,255,255)))
        
        self.fondo= pygame.image.load("images/camino.jpg")
        self.screen.blit(self.fondo, (0,0))
        
        self.muneco=Muneco()
        self.muneco.posicion= vec2d(400, 300)
        self.muneco.objetivo= vec2d(300,300)
        
        
        #for n in range(5):
         #   posi=vec2d(uniform(0,800),uniform(0,800))
            #pygame.draw.circle(self.screen, (0,0,0), (100,100), 30, 1)
        
    def draw(self):
       # self.screen.fill((255,255,255))
        self.screen.blit(self.fondo, (0,0))
        pygame.draw.circle(self.screen, (255,255,255), self.muneco.objetivo, 30, 1)
        pygame.draw.circle(self.screen, (0,0,0), self.muneco.posicion.inttup(), 20)
        
        pygame.draw.circle(self.screen, (0,0,0), (100,100), 30, 1)
        pygame.draw.circle(self.screen, (0,0,0), (100,200), 30, 1)
        pygame.draw.circle(self.screen, (0,0,0), (200,100), 30, 1)
        pygame.draw.circle(self.screen, (0,0,0), (200,200), 30, 1)
        
        
    def keyUp(self, key):
        pass
    
    def mouseUp(self, button, pos):
        if pos[0]>=69 and pos[0]<=127 and pos[1]>=69 and pos[1]<=127:
            self.muneco.objetivo= vec2d(100,100)
            
        if pos[0]>=169 and pos[0]<=227 and pos[1]>=69 and pos[1]<=127:
            self.muneco.objetivo= vec2d(200,100)
            
        if pos[0]>=69 and pos[0]<=127 and pos[1]>=169 and pos[1]<=227:
            self.muneco.objetivo= vec2d(100,200)
            
        if pos[0]>=169 and pos[0]<=227 and pos[1]>=169 and pos[1]<=227:
            self.muneco.objetivo= vec2d(200,200)
        
    def mouseMotion(self, buttons, pos, rel):
        print pos[0],pos[1]
        
    def update(self):
        direccion= self.muneco.objetivo- self.muneco.posicion
        
        if direccion.length>3:
            direccion.length= 3
            self.muneco.posicion= self.muneco.posicion+ direccion

        
        
          
s = Main()
s.mainLoop(40)
