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
    sprite1.rect.top = 40
    sprite1.rect.left = 40
    (x,y) = (sprite1.rect.top,sprite1.rect.left)
    vx = 0
    vy = 0
    salir = False
    
    fondo = Fondo()    
    
    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:                                            
                    vx+=10
                if event.key == pygame.K_LEFT:                                            
                    vx-=10
                if event.key == pygame.K_UP:                                            
                    y-=10
                if event.key == pygame.K_DOWN:                                            
                    y+=10
            if event.type == pygame.KEYUP:
                if event.type == pygame.K_LEFT:
                    vx = 0
                if event.type == pygame.K_RIGHT:
                    vx = 0
                if event.key == pygame.K_UP:                                            
                    vy = 0
                if event.key == pygame.K_DOWN:                                            
                    vy = 0
        x+=vx
        y+=vy
        reloj1.tick(20)
        pantalla.blit(fondo,(0,0))
        pantalla.blit(sprite1.image,(x,y))        
        pygame.display.update()            
    pygame.quit()
        
main()