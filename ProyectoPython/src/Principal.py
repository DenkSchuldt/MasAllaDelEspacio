# Autores: Liliana Ramos
#          Denny Schuldt
# --------------------
# Descripcion: 
# Main class del proyecto.

#imports
import pygame
from Fondo import *

#funciones
def main():
    pygame.init()
    pantalla = pygame.display.set_mode([900,600])
    pygame.display.set_caption("Proyecto")    
    reloj1 = pygame.time.Clock()
    imagen1 = pygame.image.load("./images/personaje.png").convert_alpha()
    sprite1 = pygame.sprite.Sprite()
    sprite1.image = imagen1
    sprite1.rect = imagen1.get_rect()    
    sprite1.rect.top = 75
    sprite1.rect.left = 75    
         
    salir = False
    
    fondo = Fondo()    
    
    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    n = 0 
                    while n <= 300:                             
                        sprite1.rect.move_ip(1,0)
                        pantalla.blit(fondo,(0,0))
                        pantalla.blit(sprite1.image,sprite1.rect)
                        pygame.display.update()                                                
                        n = n + 1                                            
                if event.key == pygame.K_LEFT:                                            
                    n = 0 
                    while n <= 300:                             
                        sprite1.rect.move_ip(-1,0)
                        pantalla.blit(fondo,(0,0))
                        pantalla.blit(sprite1.image,sprite1.rect)
                        pygame.display.update()                                                
                        n = n + 1
                if event.key == pygame.K_UP:                                            
                    n = 0 
                    while n <= 200:                             
                        sprite1.rect.move_ip(0,-1)
                        pantalla.blit(fondo,(0,0))
                        pantalla.blit(sprite1.image,sprite1.rect)
                        pygame.display.update()                                                
                        n = n + 1
                if event.key == pygame.K_DOWN:                                            
                    n = 0 
                    while n <= 200:                             
                        sprite1.rect.move_ip(0,1)
                        pantalla.blit(fondo,(0,0))
                        pantalla.blit(sprite1.image,sprite1.rect)
                        pygame.display.update()                                                
                        n = n + 1                            
                            
        reloj1.tick(20)
        pantalla.blit(fondo,(0,0))
        pantalla.blit(sprite1.image,sprite1.rect)        
        pygame.display.update()
                    
    pygame.quit()

main()                