
import pygame 
        
class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen_01,imagen_02,x=200,y=200):
        self.imagen_normal = imagen_01
        self.imagen_seleccion = imagen_02
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left,self.rect.top = (x,y)

    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        else:
            self.imagen_actual = self.imagen_normal
        pantalla.blit(self.imagen_actual,self.rect)
        
    
    
        