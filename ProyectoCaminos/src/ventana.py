import pygame
from pygame.locals import *

#float range. Start=a, End=b, Step=c
        
class Ventana:
    def __init__(self, size=(900,600), fill=(255,255,255)):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.screen.fill(fill)
        pygame.display.flip()
        self.running = False
        self.clock = pygame.time.Clock()
        self.size = size
        self.fps= 0
        
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                self.keyDown(event.key)
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    self.running = False
                self.keyUp(event.key)
            elif event.type == MOUSEBUTTONUP:
                self.mouseUp(event.button, event.pos)
            elif event.type == MOUSEMOTION:
                self.mouseMotion(event.buttons, event.pos, event.rel)
    
               
    #enter the main loop, possibly setting max FPS
    def mainLoop(self, fps=0):
        self.running = True
        self.fps= fps
        
        while self.running:
            pygame.display.set_caption("Jugando")
            self.handleEvents()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)
            
            
            
    def update(self):
        pass
        
    def draw(self):
        pass
        
    def keyDown(self, key):
        pass
        
    def keyUp(self, key):
        pass
    
    def mouseUp(self, button, pos):
        pass
        
    def mouseMotion(self, buttons, pos, rel):
        pass