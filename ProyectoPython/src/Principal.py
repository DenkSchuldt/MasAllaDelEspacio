# Autores: Liliana Ramos
#          Denny Schuldt
# --------------------
# Descripcion: 
# Main class del proyecto.

#imports
import pygame
from Fondo import *
import time

sonido_03 = None
ultimo_audio = None
audio_disponible = False

#funciones
def main():
    pygame.init()
    pygame.mixer.init()
    sonido_01 = PlayAudio("sound_01.wav")
    next = pygame.mixer.Sound("./sounds/next.wav")
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
    global sonido_03
       
    
    fondo = Fondo(1)      
    
    while salir != True:
        for event in pygame.event.get():
            #Cerrar ventana
            if event.type == pygame.QUIT:
                salir = True
            #Presionar cualquier tecla
            if event.type == pygame.KEYDOWN:
                #Presionar la tecla espacio
                if event.key == pygame.K_SPACE:
                    if not bloqueo_tecla_space:
                        if not primeraVez:
                            advertencia = True                                        
                        if iniciar:
                            print "Iniciar Juego"
                            fondo = Fondo(2)
                            pantalla.blit(fondo,(0,0))
                            pygame.display.update()                            
                            iniciar = False                        
                            fondo = Fondo(3) 
                            time.sleep(3)                            
                            sonido_02 = PlayAudio("advertencia.wav")                                             
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
                            PlayAudio("pagina1.wav")
                            global audio_disponible
                            audio_disponible = True
                
                #Presionar la tecla 'Up'                
                if event.key == pygame.K_UP:
                    if audio_disponible:
                        RepeatAudio()                        
                            
                #Presionar la tecla 'Down'                
                if event.key == pygame.K_DOWN:
                    if una_opcion:
                        if audio == 99:
                            una_opcion = False
                            print "Reproducir sonido de la pagina 1"
                            fondo = Fondo(4)
                            next.play()
                            audio = 1
                        if audio == 59:
                            una_opcion = False
                            print "Reproducir sonido de la pagina 60"
                            fondo = Fondo(4)
                            next.play()
                            audio = 60
                        if audio == 67:
                            una_opcion = False
                            print "Reproducir sonido de la pagina 2"
                            fondo = Fondo(4)
                            next.play()
                            audio = 2                        
                        if audio == 48:
                            una_opcion = False
                            print "Reproducir sonido de la pagina 2"
                            fondo = Fondo(4)
                            next.play()
                            audio = 2
                        if audio == 45:
                            una_opcion = False
                            print "Reproducir sonido de la pagina 62"
                            fondo = Fondo(4)
                            next.play()
                            audio = 62
                        if audio == 43:
                            una_opcion = False
                            print "Reproducir sonido de la pagina 3"
                            fondo = Fondo(4)
                            next.play()
                            audio = 3
                        if audio == 39:
                            una_opcion = False
                            print "Reproducir sonido de la pagina 40"
                            fondo = Fondo(4)
                            next.play()
                            audio = 40
                        if audio == 22:
                            una_opcion = False
                            print "Reproducir sonido de la pagina 3"
                            fondo = Fondo(4)
                            next.play()
                            audio = 3
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
                            
                #Presionar la tecla 'Left'
                if event.key == pygame.K_LEFT:                       
                    if bloqueo_tecla_space:
                        if audio == 82:
                            print "Reproducir sonido de la pagina 113 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 113
                        if audio == 80:
                            print "Reproducir sonido de la pagina 111 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 111
                        if audio == 79:
                            print "Reproducir sonido de la pagina 109 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 109
                        if audio == 91:
                            print "Reproducir sonido de la pagina 102 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 102
                        if audio == 90:
                            print "Reproducir sonido de la pagina 101 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 101
                        if audio == 84:
                            print "Reproducir sonido de la pagina 115 - FIN"
                            fondo = Fondo('n')
                            next.play()
                            audio = 115
                        if audio == 60:
                            print "Reproducir sonido de la pagina 80"                            
                            next.play()
                            audio = 80
                        if audio == 93:
                            print "Reproducir sonido de la pagina 107 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 107
                        if audio == 56:
                            print "Reproducir sonido de la pagina 78 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 78
                        if audio == 55:
                            print "Reproducir sonido de la pagina 76 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 76
                        if audio == 70:
                            print "Reproducir sonido de la pagina 99"
                            fondo = Fondo(5)
                            una_opcion = True                            
                            next.play()
                            audio = 99
                        if audio == 69:
                            print "Reproducir sonido de la pagina 97 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 97
                        if audio == 74:
                            print "Reproducir sonido de la pagina 92 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 92
                        if audio == 72:
                            print "Reproducir sonido de la pagina 90"                            
                            next.play()
                            audio = 90
                        if audio == 64:
                            print "Reproducir sonido de la pagina 86 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 74
                        if audio == 61:
                            print "Reproducir sonido de la pagina 83 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 83
                        if audio == 40:
                            print "Reproducir sonido de la pagina 55"                            
                            next.play()
                            audio = 55
                        if audio == 52:
                            print "Reproducir sonido de la pagina 69"                            
                            next.play()
                            audio = 69
                        if audio == 51:
                            print "Reproducir sonido de la pagina 67"
                            fondo = Fondo(5)
                            una_opcion = True                            
                            next.play()
                            audio = 67
                        if audio == 54:
                            print "Reproducir sonido de la pagina 74"                            
                            next.play()
                            audio = 74
                        if audio == 53:
                            print "Reproducir sonido de la pagina 72"                            
                            next.play()
                            audio = 72
                        if audio == 62:
                            print "Has elejido el FIN"
                            fondo = Fondo('n')
                            next.play()
                            audio = 'fin'
                        if audio == 44:
                            print "Reproducir sonido de la pagina 59"
                            una_opcion = True
                            fondo = Fondo(5)                            
                            next.play()
                            audio = 59
                        if audio == 28:
                            print "Reproducir sonido de la pagina 44"                            
                            next.play()
                            audio = 44
                        if audio == 42:                            
                            print "Reproducir sonido de la pagina 57 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 57
                        if audio == 38:
                            print "Reproducir sonido de la pagina 51"                            
                            next.play()
                            audio = 51
                        if audio == 36:
                            print "Reproducir sonido de la pagina 53"                            
                            next.play()
                            audio = 53
                        if audio == 27:
                            print "Reproducir sonido de la pagina 42"                            
                            next.play()
                            audio = 42
                        if audio == 23:                            
                            print "Reproducir sonido de la pagina 39"
                            una_opcion = True
                            fondo = Fondo(5)
                            next.play()
                            audio = 39
                        if audio == 20:
                            print "Reproducir sonido de la pagina 36"                            
                            next.play()
                            audio = 36
                        if audio == 14:
                            print "Reproducir sonido de la pagina 28"                            
                            next.play()
                            audio = 28
                        if audio == 12:
                            print "Reproducir sonido de la pagina 24"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 24
                        if audio == 11:
                            print "Reproducir sonido de la pagina 23"                            
                            next.play()
                            audio = 23
                        if audio == 10:
                            print "Reproducir sonido de la pagina 20"                            
                            next.play()
                            audio = 20
                        if audio == 6:
                            print "Reproducir sonido de la pagina 12"                            
                            next.play()
                            audio = 12
                        if audio == 4:
                            print "Reproducir sonido de la pagina 10"                            
                            next.play()
                            audio = 10
                        if audio == 2:
                            print "Reproducir sonido de la pagina 4"                            
                            next.play()
                            audio = 4
                        if audio == 88:
                            print "Reproducir sonido de la pagina 94 - FIN"
                            fondo = Fondo('n')
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
                            fondo = Fondo(5)
                            una_opcion = True
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
                            fondo = Fondo('n')
                            next.play()
                            audio = 30                            
                        if audio == 7:
                            print "Reproducir sonido de la pagina 15"
                            next.play()
                            audio = 15
                        if audio == 8:
                            print "Reproducir sonido de la pagina 18 - FIN"
                            fondo = Fondo('n')
                            next.play()
                            audio = 18
                        if audio == 3:
                            print "Reproducir sonido de la pagina 7"
                            next.play()
                            audio = 7                            
                        if audio == 1:
                            print "Reproducir sonido de la pagina 2"
                            next.play()
                            sonido_03.stop()
                            audio = 2
                
                #Presionar la tecla 'Right'                            
                if event.key == pygame.K_RIGHT:
                    if bloqueo_tecla_space:
                        if audio == 90:
                            print "Reproducir sonido de la pagina 106 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 106
                        if audio == 91:
                            print "Reproducir sonido de la pagina 105 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 105
                        if audio == 79:
                            print "Reproducir sonido de la pagina 110 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 110
                        if audio == 80:
                            print "Reproducir sonido de la pagina 112 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 112
                        if audio == 82:
                            print "Reproducir sonido de la pagina 114 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 114
                        if audio == 84:
                            print "Reproducir sonido de la pagina 116 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 116
                        if audio == 60:
                            print "Reproducir sonido de la pagina 82"                            
                            next.play()
                            audio = 82
                        if audio == 56:
                            print "Reproducir sonido de la pagina 79"                            
                            next.play()
                            audio = 79
                        if audio == 55:
                            print "Reproducir sonido de la pagina 77 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 77
                        if audio == 70:
                            print "Reproducir sonido de la pagina 100 - FIN"
                            fondo = Fondo('n')
                            next.play()
                            audio = 100
                        if audio == 69:
                            print "Reproducir sonido de la pagina 98 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 98
                        if audio == 93:
                            print "Reproducir sonido de la pagina 108 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 108
                        if audio == 74:
                            print "Reproducir sonido de la pagina 93"                            
                            next.play()
                            audio = 93
                        if audio == 72:
                            print "Reproducir sonido de la pagina 91"                            
                            next.play()
                            audio = 91
                        if audio == 64:
                            print "Reproducir sonido de la pagina 87 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 87
                        if audio == 61:
                            print "Reproducir sonido de la pagina 84"                            
                            next.play()
                            audio = 84
                        if audio == 40:
                            print "Reproducir sonido de la pagina 56"                            
                            next.play()
                            audio = 56
                        if audio == 52:
                            print "Reproducir sonido de la pagina 70"                            
                            next.play()
                            audio = 70
                        if audio == 51:
                            print "Reproducir sonido de la pagina 68"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 68
                        if audio == 54:
                            print "Reproducir sonido de la pagina 75 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 75                        
                        if audio == 53:
                            print "Reproducir sonido de la pagina 73 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 73
                        if audio == 62:
                            print "Reproducir sonido de la pagina 64"                            
                            next.play()
                            audio = 64
                        if audio == 44:
                            print "Reproducir sonido de la pagina 61"                            
                            next.play()
                            audio = 61
                        if audio == 28:
                            print "Reproducir sonido de la pagina 45"
                            fondo = Fondo(5)
                            una_opcion = True                            
                            next.play()
                            audio = 45
                        if audio == 42:
                            print "Reproducir sonido de la pagina 58 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 58
                        if audio == 38:
                            print "Reproducir sonido de la pagina 52"                            
                            next.play()
                            audio = 52
                        if audio == 36:
                            print "Reproducir sonido de la pagina 54"                            
                            next.play()
                            audio = 54
                        if audio == 27:
                            print "Reproducir sonido de la pagina 43"
                            fondo = Fondo(5)
                            una_opcion = True                            
                            next.play()
                            audio = 43
                        if audio == 23:
                            print "Reproducir sonido de la pagina 41"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 41
                        if audio == 20:
                            print "Reproducir sonido de la pagina 38"                            
                            next.play()
                            audio = 38
                        if audio == 14:
                            print "Reproducir sonido de la pagina 29 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 29
                        if audio == 12:
                            print "Reproducir sonido de la pagina 27"                            
                            next.play()
                            audio = 27
                        if audio == 11:
                            print "Reproducir sonido de la pagina 26 - FIN"
                            fondo = Fondo('n')                            
                            next.play()
                            audio = 26
                        if audio == 10:
                            print "Reproducir sonido de la pagina 22"
                            fondo = Fondo(5)
                            una_opcion = True                            
                            next.play()
                            audio = 22
                        if audio == 6:
                            print "Reproducir sonido de la pagina 14"                            
                            next.play()
                            audio = 14
                        if audio == 4:
                            print "Reproducir sonido de la pagina 11"                            
                            next.play()
                            audio = 11
                        if audio == 2:
                            print "Reproducir sonido de la pagina 6"                            
                            next.play()
                            audio = 6
                        if audio == 88:
                            print "Reproducir sonido de la pagina 96 - FIN"
                            fondo = Fondo('n')
                            next.play()
                            audio = 96                            
                        if audio == 65:
                            print "Reproducir sonido de la pagina 89 - FIN"
                            fondo = Fondo('n')
                            next.play()
                            audio = 89                            
                        if audio == 46:
                            print "Reproducir sonido de la pagina 66 - FIN"
                            fondo = Fondo('n')
                            next.play()
                            audio = 66                            
                        if audio == 32:
                            print "Reproducir sonido de la pagina 49 - FIN"
                            fondo = Fondo('n')
                            next.play()
                            audio = 49                            
                        if audio == 34:
                            print "Reproducir sonido de la pagina 50 - FIN"
                            fondo = Fondo('n')
                            next.play()
                            audio = 50
                        if audio == 17:
                            print "Reproducir sonido de la pagina 35 - FIN"
                            fondo = Fondo('n')
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
                            fondo = Fondo('n')
                            next.play()
                            audio = 19                            
                        if audio == 3:
                            print "Reproducir sonido de la pagina 8"
                            next.play()
                            audio = 8
                        if audio == 1:
                            print "Reproducir sonido de la pagina 3"
                            next.play()
                            sonido_03.stop()
                            audio = 3                        
                                                 
        reloj1.tick(20)
        pantalla.blit(fondo,(0,0))        
        pygame.display.update()
    pygame.quit()
    
    
def PlayAudio (audio):
    global sonido_03
    global ultimo_audio
    if audio != ultimo_audio:
        dir = "./sounds/"
        ruta = dir + audio    
        ultimo_audio = ruta 
        sonido_03 = pygame.mixer.Sound(ruta)
    else:
        sonido_03 = pygame.mixer.Sound(ultimo_audio)     
    return sonido_03.play()

def RepeatAudio():    
    global sonido_03
    global ultimo_audio    
    sonido_03.stop()
    sonido_03 = PlayAudio(ultimo_audio)    

'''def Funcion(imp, num):
    print "Reproducir sonido de la pagina " + str(imp)
    next = PlayAudio("next.wav")    
    print num'''

main()                