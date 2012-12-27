# Autores: Liliana Ramos
#          Denny Schuldt
# --------------------
# Descripcion: 
# Main class del proyecto.

#imports
import pygame

class Fondo(pygame.Surface):
    
    fondo = None
    
    def __init__(self):
        pygame.Surface.__init__(self,(900,600))
        self.createFondo()
        
    def createSprite(self,x,y,img):
        spt = pygame.sprite.Sprite()
        spt.image = pygame.image.load(img)
        spt.rect = spt.image.get_rect()
        (spt.rect.left, spt.rect.top) = (x,y)
        return spt
    
    def createFondo(self):
        self.fondo = self.createSprite(0,0,"./images/camino.jpg")
        self.blit(self.fondo.image,self.fondo.rect)        
        