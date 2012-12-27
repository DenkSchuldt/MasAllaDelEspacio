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
    
    base1 = False
    base2 = False
    base3 = False
    base4 = False
    base5 = False
    base6 = False
    base7 = False
    base8 = False
        
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
                        #pantalla.blit(fondo,(0,0))
                        pantalla.blit(sprite1.image,sprite1.rect)
                        pygame.display.update()                                                
                        n = n + 1                    
                    y = sprite1.rect.top
                    x = sprite1.rect.left
                    
                    if x == 376 and y == 75 and base1 == False:
                        print "Reproducir el audio de la Base 1"
                        base1 = True
                    elif x == 677 and y == 75 and base2 == False:
                        print "Reproducir el audio de la Base 2"
                        base2 = True
                    elif x == 677 and y == 276 and base3 == False:
                        print "Reproducir el audio de la Base 3"
                        base3 = True
                    elif x == 376 and y == 276 and base4 == False:
                        print "Reproducir el audio de la Base 4"
                        base4 = True
                    elif x == 75 and y == 276 and base5 == False:
                        print "Reproducir el audio de la Base 5"
                        base5 = True
                    elif x == 75 and y == 477 and base6 == False:
                        print "Reproducir el audio de la Base 6"
                        base6 = True
                    elif x == 376 and y == 477 and base7 == False:
                        print "Reproducir el audio de la Base 7"
                        base7 = True
                    elif x == 677 and y == 477 and base8 == False:
                        print 'Reproducir: "Felicitaciones, has ganado y salvado al planeta de una catastrofe".'
                        base8 = True                    
                    print "CoordX: " + str(x) + " y CoordY: " + str(y) 
                if event.key == pygame.K_LEFT:                                            
                    n = 0 
                    while n <= 300:                             
                        sprite1.rect.move_ip(-1,0)
                        #pantalla.blit(fondo,(0,0))
                        pantalla.blit(sprite1.image,sprite1.rect)
                        pygame.display.update()                                                
                        n = n + 1
                    y = sprite1.rect.top
                    x = sprite1.rect.left
                    
                    if x == 376 and y == 75 and base1 == False:
                        print "Reproducir el audio de la Base 1"
                        base1 = True
                    elif x == 677 and y == 75 and base2 == False:
                        print "Reproducir el audio de la Base 2"
                        base2 = True
                    elif x == 677 and y == 276 and base3 == False:
                        print "Reproducir el audio de la Base 3"
                        base3 = True
                    elif x == 376 and y == 276 and base4 == False:
                        print "Reproducir el audio de la Base 4"
                        base4 = True
                    elif x == 75 and y == 276 and base5 == False:
                        print "Reproducir el audio de la Base 5"
                        base5 = True
                    elif x == 75 and y == 477 and base6 == False:
                        print "Reproducir el audio de la Base 6"
                        base6 = True
                    elif x == 376 and y == 477 and base7 == False:
                        print "Reproducir el audio de la Base 7"
                        base7 = True
                    elif x == 677 and y == 477 and base8 == False:
                        print 'Reproducir: "Felicitaciones, has ganado y salvado al planeta de una catastrofe".'
                        base8 = True   
                        
                    print "CoordX: " + str(x) + " y CoordY: " + str(y)
                if event.key == pygame.K_UP:                                            
                    n = 0 
                    while n <= 200:                             
                        sprite1.rect.move_ip(0,-1)
                        #pantalla.blit(fondo,(0,0))
                        pantalla.blit(sprite1.image,sprite1.rect)
                        pygame.display.update()                                                
                        n = n + 1
                    y = sprite1.rect.top
                    x = sprite1.rect.left

                    if x == 376 and y == 75 and base1 == False:
                        print "Reproducir el audio de la Base 1"
                        base1 = True
                    elif x == 677 and y == 75 and base2 == False:
                        print "Reproducir el audio de la Base 2"
                        base2 = True
                    elif x == 677 and y == 276 and base3 == False:
                        print "Reproducir el audio de la Base 3"
                        base3 = True
                    elif x == 376 and y == 276 and base4 == False:
                        print "Reproducir el audio de la Base 4"
                        base4 = True
                    elif x == 75 and y == 276 and base5 == False:
                        print "Reproducir el audio de la Base 5"
                        base5 = True
                    elif x == 75 and y == 477 and base6 == False:
                        print "Reproducir el audio de la Base 6"
                        base6 = True
                    elif x == 376 and y == 477 and base7 == False:
                        print "Reproducir el audio de la Base 7"
                        base7 = True
                    elif x == 677 and y == 477 and base8 == False:
                        print 'Reproducir: "Felicitaciones, has ganado y salvado al planeta de una catastrofe".'
                        base8 = True   
                        
                    print "CoordX: " + str(x) + " y CoordY: " + str(y)
                if event.key == pygame.K_DOWN:                                            
                    n = 0 
                    while n <= 200:                             
                        sprite1.rect.move_ip(0,1)
                        #pantalla.blit(fondo,(0,0))
                        pantalla.blit(sprite1.image,sprite1.rect)
                        pygame.display.update()                                                
                        n = n + 1                            
                    y = sprite1.rect.top
                    x = sprite1.rect.left
                    
                    if x == 376 and y == 75 and base1 == False:
                        print "Reproducir el audio de la Base 1"
                        base1 = True
                    elif x == 677 and y == 75 and base2 == False:
                        print "Reproducir el audio de la Base 2"
                        base2 = True
                    elif x == 677 and y == 276 and base3 == False:
                        print "Reproducir el audio de la Base 3"
                        base3 = True
                    elif x == 376 and y == 276 and base4 == False:
                        print "Reproducir el audio de la Base 4"
                        base4 = True
                    elif x == 75 and y == 276 and base5 == False:
                        print "Reproducir el audio de la Base 5"
                        base5 = True
                    elif x == 75 and y == 477 and base6 == False:
                        print "Reproducir el audio de la Base 6"
                        base6 = True
                    elif x == 376 and y == 477 and base7 == False:
                        print "Reproducir el audio de la Base 7"
                        base7 = True
                    elif x == 677 and y == 477 and base8 == False:
                        print 'Reproducir: "Felicitaciones, has ganado y salvado al planeta de una catastrofe".'
                        base8 = True   
                    
                    print "CoordX: " + str(x) + " y CoordY: " + str(y)
        reloj1.tick(20)
        pantalla.blit(fondo,(0,0))
        pantalla.blit(sprite1.image,sprite1.rect)        
        pygame.display.update()
                    
    pygame.quit()

main()                