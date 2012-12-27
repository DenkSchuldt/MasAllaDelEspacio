# Autores: Liliana Ramos
#          Denny Schuldt
# --------------------
# Descripcion: 
# Main class del proyecto.

#imports
import pygame
from Fondo import *
import time

#funciones
def main():
    pygame.init()
    pygame.mixer.init()
    sonido_01 = pygame.mixer.Sound("./sounds/sound_01.wav")
    sonido_01.play()
    pantalla = pygame.display.set_mode([900,600])
    pygame.display.set_caption("Proyecto")    
    reloj1 = pygame.time.Clock()

    salir = False
    iniciar = True
    
    fondo = Fondo(1)      
    
    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print "Derecha"
                if event.key == pygame.K_LEFT:                                            
                    print "Izquierda"
                if event.key == pygame.K_SPACE:
                    if iniciar:
                        print "Iniciar Juego"
                        fondo = Fondo(2)
                        pantalla.blit(fondo,(0,0))
                        pygame.display.update()
                        time.sleep(3)                        
                        fondo = Fondo(3)                        
                        sonido_02 = pygame.mixer.Sound("./sounds/advertencia.wav")
                        sonido_02.play()
                        time.sleep(2)
                        sonido_01.stop()
                        iniciar = False                     
        reloj1.tick(20)
        pantalla.blit(fondo,(0,0))
        #pantalla.blit(sprite1.image,sprite1.rect)        
        pygame.display.update()
                    
    pygame.quit()

main()                