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
    next = pygame.mixer.Sound("./sounds/next.wav")                            
    sonido_01.play()
    pantalla = pygame.display.set_mode([900,600])
    pygame.display.set_caption("Mas Alla Del Espacio")    
    reloj1 = pygame.time.Clock()

    salir = False
    iniciar = True
    advertencia = False
    primeraVez = True
    bloqueo_tecla_space = False
    una_opcion = False
    audio = None
    
    fondo = Fondo(1)      
    
    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if una_opcion:
                        if audio == 16:
                            una_opcion = False
                            print "Reproducir sonido de la pagina 17"
                            fondo = Fondo(4)
                            next.play()
                            audio = 17
                        if audio == 33:
                            una_opcion = False
                            print "Reproducir sonido de la pagina 34"
                            fondo = Fondo(4)                            
                            next.play()
                            audio = 34
                if event.key == pygame.K_LEFT:                       
                    if bloqueo_tecla_space:
                        if audio == 88:
                            print "Reproducir sonido de la pagina 94 - FIN"
                            next.play()
                            audio = 94                            
                        if audio == 65:
                            print "Reproducir sonido de la pagina 88"
                            next.play()
                            audio = 88
                        if audio == 46:
                            print "Reproducir sonido de la pagina 65"
                            next.play()
                            audio = 65
                        if audio == 32:
                            print "Reproducir sonido de la pagina 46"
                            next.play()
                            audio = 46
                        if audio == 34:                            
                            print "Reproducir sonido de la pagina 48"
                            next.play()
                            audio = 48
                        if audio == 17:                            
                            print "Reproducir sonido de la pagina 33"
                            fondo = Fondo(5)
                            una_opcion = True
                            next.play()
                            audio = 33
                        if audio == 15:                            
                            print "Reproducir sonido de la pagina 30 - FIN"
                            next.play()
                            audio = 30                            
                        if audio == 7:
                            print "Reproducir sonido de la pagina 15"
                            next.play()
                            audio = 15
                        if audio == 8:
                            print "Reproducir sonido de la pagina 18 - FIN"
                            next.play()
                            audio = 18
                        if audio == 3:
                            print "Reproducir sonido de la pagina 7"
                            next.play()
                            audio = 7                            
                        if audio == 1:
                            print "Reproducir sonido de la pagina 2"
                            next.play()
                            audio = 2                            
                if event.key == pygame.K_RIGHT:
                    if bloqueo_tecla_space:
                        if audio == 88:
                            print "Reproducir sonido de la pagina 96 - FIN"
                            next.play()
                            audio = 96                            
                        if audio == 65:
                            print "Reproducir sonido de la pagina 89 - FIN"
                            next.play()
                            audio = 89                            
                        if audio == 46:
                            print "Reproducir sonido de la pagina 66 - FIN"
                            next.play()
                            audio = 66                            
                        if audio == 32:
                            print "Reproducir sonido de la pagina 49 - FIN"
                            next.play()
                            audio = 49                            
                        if audio == 34:
                            print "Reproducir sonido de la pagina 50 - FIN"
                            next.play()
                            audio = 50                                                    
                        if audio == 17:
                            print "Reproducir sonido de la pagina 35 - FIN"
                            next.play()
                            audio = 35                            
                        if audio == 15:                            
                            print "Reproducir sonido de la pagina 32"
                            next.play()
                            audio = 32                        
                        if audio == 7:
                            print "Reproducir sonido de la pagina 16"
                            fondo = Fondo(5)
                            una_opcion = True                                                        
                            next.play()
                            audio = 16
                        if audio == 8:
                            print "Reproducir sonido de la pagina 19 - FIN"
                            next.play()
                            audio = 19                            
                        if audio == 3:
                            print "Reproducir sonido de la pagina 8"
                            next.play()
                            audio = 8
                        if audio == 1:
                            print "Reproducir sonido de la pagina 3"
                            next.play()
                            audio = 3
                if event.key == pygame.K_SPACE:
                    if not bloqueo_tecla_space:
                        if not primeraVez:
                            advertencia = True                                        
                        if iniciar:
                            print "Iniciar Juego"
                            fondo = Fondo(2)
                            pantalla.blit(fondo,(0,0))
                            pygame.display.update()
                            time.sleep(3)
                            iniciar = False                        
                            fondo = Fondo(3)                        
                            sonido_02 = pygame.mixer.Sound("./sounds/advertencia.wav")
                            sonido_02.play()
                            time.sleep(2)
                            sonido_01.stop()
                            if primeraVez:
                                primeraVez = False
                        if advertencia:
                            sonido_02.stop()
                            fondo = Fondo(4)
                            pantalla.blit(fondo,(0,0))
                            pygame.display.update()
                            bloqueo_tecla_space = True
                            print "Reproducir sonido de la pagina 1"
                            audio = 1
                                                 
        reloj1.tick(20)
        pantalla.blit(fondo,(0,0))
        #pantalla.blit(sprite1.image,sprite1.rect)        
        pygame.display.update()
                    
    pygame.quit()

main()                