# Autores: Liliana Ramos
#          Denny Schuldt
# --------------------
# Descripcion: 
# Main class del proyecto.

#imports
import pygame

class Fondo(pygame.Surface):
    
    fondo = None
    numero = None
    
    def __init__(self, num):
        pygame.Surface.__init__(self,(900,600))
        self.numero = num
        self.createFondo()        
        
    def createSprite(self,x,y,img):
        spt = pygame.sprite.Sprite()
        spt.image = pygame.image.load(img)
        spt.rect = spt.image.get_rect()
        (spt.rect.left, spt.rect.top) = (x,y)
        return spt
    
    def createFondo(self):
        if self.numero == 1:
            self.fondo = self.createSprite(0,0,"./images/img_01.jpg")
        if self.numero == 2:
            self.fondo = self.createSprite(0,0,"./images/img_02.jpg")
        if self.numero == 3:
            self.fondo = self.createSprite(0,0,"./images/img_03.jpg")
        if self.numero == 4:
            self.fondo = self.createSprite(0,0,"./images/img_04.jpg")
        self.blit(self.fondo.image,self.fondo.rect)
        