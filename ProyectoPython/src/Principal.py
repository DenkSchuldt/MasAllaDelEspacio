# Autores: Liliana Ramos
#          Denny Schuldt
# --------------------
# Descripcion: 
# Main class del proyecto.

#imports
import pygame
import time
from Fondo import *
from Boton import *
from Cursor import *
from threading import activeCount

sonido_03 = None
ultimo_audio = None
ultima_instruccion = None
audio_disponible = False
instruccion_disponible = False
instruccion = None
instruccion_audio = None
instruccion_sonando = None

#funciones
def main():
    pygame.init()
    pygame.mixer.init()
    sonido_01 = PlayAudio("fondo.wav")    
    pantalla = pygame.display.set_mode([900,600])
    logo = pygame.image.load("./images/logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Mas Alla Del Espacio")    
    reloj1 = pygame.time.Clock()
    fuente1 = pygame.font.SysFont("BadaBoom BB",42,False,False)
    fuente2 = pygame.font.SysFont("BadaBoom BB",300,False,False)    
    
    active_on = pygame.image.load("./images/sound_on_active.png")
    passive_on = pygame.image.load("./images/sound_on_passive.png")
    active_off = pygame.image.load("./images/sound_off_active.png")    
    passive_off = pygame.image.load("./images/sound_off_passive.png")
    help_on = pygame.image.load("./images/help_active.png")
    help_off = pygame.image.load("./images/help_passive.png")
    back_on = pygame.image.load("./images/back_active.png")
    back_off = pygame.image.load("./images/back.png")
    sound_button = Boton(passive_on,active_on,820,30)
    help = Boton(help_off,help_on,760,30)
    back = Boton(back_off,back_on,50,520)
    cursor = Cursor()    
    
    contador = 0    

    salir = False
    iniciar = True
    advertencia = False
    primeraVez = True
    bloqueo_tecla_space = False
    una_opcion = False
    audio = None
    sonido_fondo = True
    activar_ayuda = False
    tmp = None
    global sonido_03
    global instruccion
    global instruccion_sonando
    
    fondo = Fondo(1)      
    
    while salir != True:        
        for event in pygame.event.get():
            #Cerrar ventana
            if event.type == pygame.QUIT:
                salir = True                    
            
            #Presionar un boton 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(help.rect):                    
                    tmp = fondo
                    fondo = Fondo(6)                    
                    activar_ayuda = True
                if cursor.colliderect(back.rect):
                    back = Boton(back_off,back_on,50,520)
                    activar_ayuda = False
                    fondo = tmp                
                if cursor.colliderect(sound_button.rect):
                    if sonido_fondo:
                        sound_button = Boton(passive_off,active_off,820,30)
                        sonido_fondo = False
                        sonido_01.stop()
                    else:
                        sound_button = Boton(passive_on,active_on,820,30)
                        sonido_fondo = True
                        sonido_01 = PlayAudio("fondo.wav")                
            #Presionar cualquier tecla
            if event.type == pygame.KEYDOWN:
                #Presionar la tecla espacio
                if event.key == pygame.K_SPACE:
                    back = Boton(back_off,back_on,50,520)
                    activar_ayuda = False                    
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
                            global instruccion_disponible
                            instruccion_disponible = True
                            global instruccion
                            instruccion = "esfera_01.wav"
                            global instruccion_sonando
                            instruccion_sonando = False                            
                
                #Presionar la tecla 'Up'                
                if event.key == pygame.K_UP:
                    if audio_disponible:
                        RepeatAudio()
                
                #Presionar la tecla 'O'                
                if event.key == pygame.K_o:
                    if instruccion_disponible:
                        PlayInstruction(instruccion)
                        instruccion_sonando = True                             
                            
                #Presionar la tecla 'Down'                
                if event.key == pygame.K_DOWN:
                    if una_opcion:
                        if audio is not "fin":
                            contador = contador + 1
                        if audio == 99:
                            una_opcion = False
                            StopAudios()
                            print "Reproducir sonido de la pagina 1"
                            fondo = Fondo(4)
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_01.wav"                     
                            audio = 1
                        if audio == 59:
                            una_opcion = False
                            StopAudios()
                            print "Reproducir sonido de la pagina 60"
                            fondo = Fondo(4)
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_60.wav"
                            audio = 60
                        if audio == 67:
                            una_opcion = False
                            StopAudios()
                            print "Reproducir sonido de la pagina 2"
                            fondo = Fondo(4)
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_02.wav"                    
                            audio = 2                        
                        if audio == 48:
                            una_opcion = False
                            StopAudios()
                            print "Reproducir sonido de la pagina 2"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_02.wav"
                            fondo = Fondo(4)                            
                            audio = 2
                        if audio == 45:
                            una_opcion = False
                            StopAudios()
                            print "Reproducir sonido de la pagina 62"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_62.wav"
                            fondo = Fondo(4)                            
                            audio = 62
                        if audio == 43:
                            una_opcion = False
                            StopAudios()
                            print "Reproducir sonido de la pagina 3"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_03.wav"
                            fondo = Fondo(4)                            
                            audio = 3
                        if audio == 39:
                            una_opcion = False
                            StopAudios()
                            print "Reproducir sonido de la pagina 40"
                            fondo = Fondo(4)        
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_40.wav"                    
                            audio = 40
                        if audio == 22:
                            una_opcion = False
                            StopAudios()
                            print "Reproducir sonido de la pagina 3"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_03.wav"
                            fondo = Fondo(4)                            
                            audio = 3
                        if audio == 16:
                            una_opcion = False
                            StopAudios()
                            print "Reproducir sonido de la pagina 17"
                            fondo = Fondo(4)
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_17.wav"
                            audio = 17
                        if audio == 33:
                            una_opcion = False
                            StopAudios()
                            print "Reproducir sonido de la pagina 34"
                            fondo = Fondo(4)
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_34.wav"
                            audio = 34
                            
                #Presionar la tecla 'Left'
                if event.key == pygame.K_LEFT:                       
                    if bloqueo_tecla_space:
                        if audio is not "fin":
                            contador = contador + 1
                        if audio == 82:
                            StopAudios()
                            print "Reproducir sonido de la pagina 113 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 80:
                            StopAudios()
                            print "Reproducir sonido de la pagina 111 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 79:
                            StopAudios()
                            print "Reproducir sonido de la pagina 109 - FIN"
                            fondo = Fondo('n')                                                        
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 91:
                            StopAudios()
                            print "Reproducir sonido de la pagina 102 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 90:
                            StopAudios()
                            print "Reproducir sonido de la pagina 101 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 84:
                            StopAudios()
                            print "Reproducir sonido de la pagina 115 - FIN"
                            fondo = Fondo('n')      
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                      
                            audio = "fin"
                        if audio == 60:
                            StopAudios()
                            print "Reproducir sonido de la pagina 80"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_80.wav"                                                        
                            audio = 80
                        if audio == 93:
                            StopAudios()
                            print "Reproducir sonido de la pagina 107 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 56:
                            StopAudios()
                            print "Reproducir sonido de la pagina 78 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 55:
                            StopAudios()
                            print "Reproducir sonido de la pagina 76 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 70:
                            StopAudios()
                            print "Reproducir sonido de la pagina 99"
                            fondo = Fondo(5)
                            una_opcion = True
                            PlayAudio("pagina1.wav")
                            instruccion = "abajo.wav"
                            audio = 99
                        if audio == 69:
                            StopAudios()
                            print "Reproducir sonido de la pagina 97 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 74:
                            StopAudios()
                            print "Reproducir sonido de la pagina 92 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 72:
                            StopAudios()
                            print "Reproducir sonido de la pagina 90"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_90.wav"                                                        
                            audio = 90
                        if audio == 64:
                            StopAudios()
                            print "Reproducir sonido de la pagina 86 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 61:
                            StopAudios()
                            print "Reproducir sonido de la pagina 83 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 40:
                            StopAudios()
                            print "Reproducir sonido de la pagina 55"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_55.wav"                                                        
                            audio = 55
                        if audio == 52:
                            StopAudios()
                            print "Reproducir sonido de la pagina 69"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_69.wav"                                                        
                            audio = 69
                        if audio == 51:
                            StopAudios()
                            print "Reproducir sonido de la pagina 67"
                            fondo = Fondo(5)
                            una_opcion = True       
                            PlayAudio("pagina1.wav")
                            instruccion = "abajo.wav"                                                 
                            audio = 67
                        if audio == 54:
                            StopAudios()
                            print "Reproducir sonido de la pagina 74"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_74.wav"                                                        
                            audio = 74
                        if audio == 53:
                            StopAudios()
                            print "Reproducir sonido de la pagina 72"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_72.wav"                                                        
                            audio = 72
                        if audio == 62:
                            StopAudios()
                            print "Has elejido el FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 44:
                            StopAudios()
                            print "Reproducir sonido de la pagina 59"
                            una_opcion = True
                            fondo = Fondo(5)
                            PlayAudio("pagina1.wav")
                            instruccion = "abajo.wav"
                            audio = 59
                        if audio == 28:
                            StopAudios()
                            print "Reproducir sonido de la pagina 44"                            
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_44.wav"                                                        
                            audio = 44
                        if audio == 42:
                            StopAudios()
                            print "Reproducir sonido de la pagina 57 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 38:
                            StopAudios()
                            print "Reproducir sonido de la pagina 51"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_51.wav"                                                        
                            audio = 51
                        if audio == 36:
                            StopAudios()
                            print "Reproducir sonido de la pagina 53"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_53.wav"                                                        
                            audio = 53
                        if audio == 27:
                            StopAudios()
                            print "Reproducir sonido de la pagina 42"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_42.wav"                                                        
                            audio = 42
                        if audio == 23:
                            StopAudios()
                            print "Reproducir sonido de la pagina 39"
                            una_opcion = True
                            fondo = Fondo(5)
                            PlayAudio("pagina1.wav")
                            instruccion = "abajo.wav"
                            audio = 39
                        if audio == 20:
                            StopAudios()
                            print "Reproducir sonido de la pagina 36"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_36.wav"                                                        
                            audio = 36
                        if audio == 14:
                            StopAudios()
                            print "Reproducir sonido de la pagina 28"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_28.wav"                                                        
                            audio = 28
                        if audio == 12:
                            StopAudios()
                            print "Reproducir sonido de la pagina 24 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 11:
                            StopAudios()
                            print "Reproducir sonido de la pagina 23"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_23.wav"                                                        
                            audio = 23
                        if audio == 10:
                            StopAudios()
                            print "Reproducir sonido de la pagina 20"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_20.wav"                                                        
                            audio = 20
                        if audio == 6:
                            StopAudios()
                            print "Reproducir sonido de la pagina 12"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_12.wav"
                            audio = 12
                        if audio == 4:
                            StopAudios()
                            print "Reproducir sonido de la pagina 10"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_10.wav"                                                        
                            audio = 10
                        if audio == 2:
                            StopAudios()
                            print "Reproducir sonido de la pagina 4"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_04.wav"                                                        
                            audio = 4
                        if audio == 88:
                            StopAudios()
                            print "Reproducir sonido de la pagina 94 - FIN"
                            fondo = Fondo('n')      
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                      
                            audio = "fin"                         
                        if audio == 65:
                            StopAudios()
                            print "Reproducir sonido de la pagina 88"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_88.wav"                            
                            audio = 88
                        if audio == 46:
                            StopAudios()
                            print "Reproducir sonido de la pagina 65"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_65.wav"                            
                            audio = 65
                        if audio == 32:
                            StopAudios()
                            print "Reproducir sonido de la pagina 46"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_46.wav"                            
                            audio = 46
                        if audio == 34:
                            StopAudios()                      
                            print "Reproducir sonido de la pagina 48"
                            fondo = Fondo(5)
                            una_opcion = True   
                            PlayAudio("pagina1.wav")
                            instruccion = "abajo.wav"                         
                            audio = 48
                        if audio == 17:      
                            StopAudios()                      
                            print "Reproducir sonido de la pagina 33"
                            fondo = Fondo(5)
                            una_opcion = True 
                            PlayAudio("pagina1.wav")
                            instruccion = "abajo.wav"                           
                            audio = 33
                        if audio == 15:       
                            StopAudios()                     
                            print "Reproducir sonido de la pagina 30 - FIN"
                            fondo = Fondo('n')      
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                      
                            audio = "fin"                         
                        if audio == 7:
                            StopAudios()
                            print "Reproducir sonido de la pagina 15"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_15.wav"                            
                            audio = 15
                        if audio == 8:
                            StopAudios()
                            print "Reproducir sonido de la pagina 18 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                            
                            audio = "fin"
                        if audio == 3:
                            StopAudios()
                            print "Reproducir sonido de la pagina 7"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_07.wav"                            
                            audio = 7                            
                        if audio == 1:
                            StopAudios()
                            print "Reproducir sonido de la pagina 2"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_02.wav"                            
                            audio = 2
                
                #Presionar la tecla 'Right'                            
                if event.key == pygame.K_RIGHT:
                    if bloqueo_tecla_space:
                        if audio is not "fin":
                            contador = contador + 1
                        if audio == 90:
                            StopAudios()
                            print "Reproducir sonido de la pagina 106 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 91:
                            StopAudios()
                            print "Reproducir sonido de la pagina 105 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 79:
                            StopAudios()
                            print "Reproducir sonido de la pagina 110 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 80:
                            StopAudios()
                            print "Reproducir sonido de la pagina 112 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 82:
                            StopAudios()
                            print "Reproducir sonido de la pagina 114 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 84:
                            StopAudios()
                            print "Reproducir sonido de la pagina 116 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                  
                            audio = "fin"
                        if audio == 60:
                            StopAudios()
                            print "Reproducir sonido de la pagina 82"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_82.wav"                                                        
                            audio = 82
                        if audio == 56:
                            StopAudios()
                            print "Reproducir sonido de la pagina 79"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_79.wav"                                                        
                            audio = 79
                        if audio == 55:
                            StopAudios()
                            print "Reproducir sonido de la pagina 77 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 70:
                            StopAudios()
                            print "Reproducir sonido de la pagina 100 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                            
                            audio = "fin"
                        if audio == 69:
                            StopAudios()
                            print "Reproducir sonido de la pagina 98 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 93:
                            StopAudios()
                            print "Reproducir sonido de la pagina 108 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 74:
                            StopAudios()
                            print "Reproducir sonido de la pagina 93"                                                        
                            audio = 93
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_93.wav"
                        if audio == 72:
                            StopAudios()
                            print "Reproducir sonido de la pagina 91"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_91.wav"                                                        
                            audio = 91
                        if audio == 64:
                            StopAudios()
                            print "Reproducir sonido de la pagina 87 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_87.wav"                                                  
                            audio = "fin"
                        if audio == 61:
                            StopAudios()
                            print "Reproducir sonido de la pagina 84"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_84.wav"                                                        
                            audio = 84
                        if audio == 40:
                            StopAudios()
                            print "Reproducir sonido de la pagina 56"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_56.wav"                                                        
                            audio = 56
                        if audio == 52:
                            StopAudios()
                            print "Reproducir sonido de la pagina 70"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_70.wav"                                                        
                            audio = 70
                        if audio == 51:
                            StopAudios()
                            print "Reproducir sonido de la pagina 68 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 54:
                            StopAudios()
                            print "Reproducir sonido de la pagina 75 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"                     
                        if audio == 53:
                            StopAudios()
                            print "Reproducir sonido de la pagina 73 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 62:
                            StopAudios()
                            print "Reproducir sonido de la pagina 64"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_64.wav"                                                        
                            audio = 64
                        if audio == 44:
                            StopAudios()
                            print "Reproducir sonido de la pagina 61"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_61.wav"                                                        
                            audio = 61
                        if audio == 28:
                            StopAudios()
                            print "Reproducir sonido de la pagina 45"
                            fondo = Fondo(5)
                            una_opcion = True 
                            PlayAudio("pagina1.wav")
                            instruccion = "abajo.wav"                                                       
                            audio = 45
                        if audio == 42:
                            StopAudios()
                            print "Reproducir sonido de la pagina 58 - FIN"
                            fondo = Fondo('n')      
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                  
                            audio = "fin"
                        if audio == 38:
                            StopAudios()
                            print "Reproducir sonido de la pagina 52"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_52.wav"                                                        
                            audio = 52
                        if audio == 36:
                            StopAudios()
                            print "Reproducir sonido de la pagina 54"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_54.wav"                                                        
                            audio = 54
                        if audio == 27:
                            StopAudios()
                            print "Reproducir sonido de la pagina 43"
                            fondo = Fondo(5)
                            una_opcion = True       
                            PlayAudio("pagina1.wav")
                            instruccion = "abajo.wav"                                                 
                            audio = 43
                        if audio == 23:
                            StopAudios()
                            print "Reproducir sonido de la pagina 41"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_41.wav"
                            audio = 41
                        if audio == 20:
                            StopAudios()
                            print "Reproducir sonido de la pagina 38"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_38.wav"                                                        
                            audio = 38
                        if audio == 14:
                            StopAudios()
                            print "Reproducir sonido de la pagina 29 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 12:
                            StopAudios()
                            print "Reproducir sonido de la pagina 27"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_27.wav"                                                        
                            audio = 27
                        if audio == 11:
                            StopAudios()
                            print "Reproducir sonido de la pagina 26 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 10:
                            StopAudios()
                            print "Reproducir sonido de la pagina 22"
                            fondo = Fondo(5)
                            una_opcion = True
                            PlayAudio("pagina1.wav")
                            instruccion = "abajo.wav"
                            audio = 22
                        if audio == 6:
                            StopAudios()
                            print "Reproducir sonido de la pagina 14"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_14.wav"                                                        
                            audio = 14
                        if audio == 4:
                            StopAudios()
                            print "Reproducir sonido de la pagina 11"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_11.wav"                                                        
                            audio = 11
                        if audio == 2:
                            StopAudios()
                            print "Reproducir sonido de la pagina 6"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_06.wav"                                                        
                            audio = 6
                        if audio == 88:
                            StopAudios()
                            print "Reproducir sonido de la pagina 96 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                            
                            audio = "fin"                         
                        if audio == 65:
                            StopAudios()
                            print "Reproducir sonido de la pagina 89 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                            
                            audio = "fin"                         
                        if audio == 46:
                            StopAudios()
                            print "Reproducir sonido de la pagina 66 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                        
                            audio = "fin"                         
                        if audio == 32:
                            StopAudios()
                            print "Reproducir sonido de la pagina 49 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                            
                            audio = "fin"                         
                        if audio == 34:
                            StopAudios()
                            print "Reproducir sonido de la pagina 50 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"                            
                            audio = "fin"
                        if audio == 17:
                            StopAudios()
                            print "Reproducir sonido de la pagina 35 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"
                            audio = "fin"                         
                        if audio == 15:
                            StopAudios()
                            print "Reproducir sonido de la pagina 32"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_32.wav"
                            audio = 32                        
                        if audio == 7:
                            StopAudios()
                            print "Reproducir sonido de la pagina 16"
                            fondo = Fondo(5)                            
                            una_opcion = True                                                        
                            PlayAudio("pagina1.wav")
                            instruccion = "abajo.wav"
                            audio = 16
                        if audio == 8:
                            StopAudios()
                            print "Reproducir sonido de la pagina 19 - FIN"
                            fondo = Fondo('n')
                            PlayAudio("pagina1.wav")
                            instruccion = "fin.wav"
                            audio = "fin"                         
                        if audio == 3:
                            StopAudios()
                            print "Reproducir sonido de la pagina 8"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_08.wav"
                            audio = 8
                        if audio == 1:                            
                            StopAudios()
                            print "Reproducir sonido de la pagina 3"
                            PlayAudio("pagina1.wav")
                            instruccion = "esfera_03.wav"
                            audio = 3                        
        reloj1.tick(20)
        pantalla.blit(fondo,(0,0))
        if advertencia and audio is not "fin":
            texto1 = fuente1.render("Pasos dados:",0,(255,255,255))
            texto2 = fuente2.render(str(contador),0,(255,255,255)) 
            if not activar_ayuda:            
                pantalla.blit(texto1,(100,80))                    
                pantalla.blit(texto2,(370,165))
        if audio is "fin":
            texto1 = fuente1.render("Score: " + str(contador) + " pasos dados!",0,(255,255,255))
            if not activar_ayuda:
                pantalla.blit(texto1,(80,530))
        cursor.update()
        sound_button.update(pantalla,cursor)
        help.update(pantalla,cursor)
        if activar_ayuda:
            back.update(pantalla,cursor)
        pygame.display.update()
    pygame.quit()    

def PlayAudio(audio):
    global sonido_03
    global ultimo_audio
    if audio != ultimo_audio:
        dir = "./sounds/"
        ruta = dir + audio    
        ultimo_audio = ruta 
        sonido_03 = pygame.mixer.Sound(ruta)
    else:
        sonido_03 = pygame.mixer.Sound(ultimo_audio)
    if audio == "fondo.wav":     
        return sonido_03.play(-1)
    else:
        return sonido_03.play()

def RepeatAudio():    
    global sonido_03
    global ultimo_audio
    global instruccion_audio
    global instruccion_sonando
    if instruccion_sonando:
        instruccion_audio.stop()    
    sonido_03.stop()
    sonido_03 = PlayAudio(ultimo_audio)    
    
def PlayInstruction(instruccion):    
    global sonido_03    
    global instruccion_audio
    global instruccion_sonando
    if pygame.mixer.get_busy():
        sonido_03.stop()
    if instruccion_sonando:
        instruccion_audio.stop()
    ruta = "./sounds/" + instruccion
    instruccion_audio = pygame.mixer.Sound(ruta)
    instruccion_audio.play()
    
def StopAudios():
    global sonido_03    
    global instruccion_audio
    next = pygame.mixer.Sound("./sounds/next.wav")
    next.play()
    sonido_03.stop()
    if instruccion_audio != None:
        instruccion_audio.stop()    

main()                