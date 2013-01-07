# Autores: Liliana Ramos
#          Denny Schuldt
# --------------------
# Descripcion: 
# Main class del proyecto.

#imports

from Cursor import *
from Boton import *
from Fondo import *
import pygame
import time

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
                        sonido_01 = pygame.mixer.Sound("./sounds/fondo.wav")
                        sonido_01.play(-1)                                
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
                            audio = 1
                            PlayAudio("pagina01.wav")
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
                            StopAudios()
                        if audio == 99:
                            una_opcion = False                                            
                            fondo = Fondo(4)
                            PlayAudio("pagina01.wav")
                            instruccion = "esfera_01.wav"                     
                            audio = 1
                        if audio == 59:
                            una_opcion = False                            
                            fondo = Fondo(4)
                            PlayAudio("pagina60.wav")
                            instruccion = "esfera_60.wav"
                            audio = 60
                        if audio == 67:
                            una_opcion = False                      
                            fondo = Fondo(4)
                            PlayAudio("pagina02.wav")
                            instruccion = "esfera_02.wav"                    
                            audio = 2                        
                        if audio == 48:
                            una_opcion = False                      
                            PlayAudio("pagina02.wav")
                            instruccion = "esfera_02.wav"
                            fondo = Fondo(4)                            
                            audio = 2
                        if audio == 45:
                            una_opcion = False                      
                            PlayAudio("pagina62.wav")
                            instruccion = "esfera_62.wav"
                            fondo = Fondo(4)                            
                            audio = 62
                        if audio == 43:
                            una_opcion = False                      
                            PlayAudio("pagina03.wav")
                            instruccion = "esfera_03.wav"
                            fondo = Fondo(4)                            
                            audio = 3
                        if audio == 39:
                            una_opcion = False                      
                            fondo = Fondo(4)        
                            PlayAudio("pagina40.wav")
                            instruccion = "esfera_40.wav"                    
                            audio = 40
                        if audio == 22:
                            una_opcion = False                                                
                            PlayAudio("pagina03.wav")
                            instruccion = "esfera_03.wav"
                            fondo = Fondo(4)                            
                            audio = 3
                        if audio == 16:
                            una_opcion = False                            
                            fondo = Fondo(4)
                            PlayAudio("pagina17.wav")
                            instruccion = "esfera_17.wav"
                            audio = 17
                        if audio == 33:
                            una_opcion = False                            
                            fondo = Fondo(4)
                            PlayAudio("pagina34.wav")
                            instruccion = "esfera_34.wav"
                            audio = 34
                            
                #Presionar la tecla 'Left'
                if event.key == pygame.K_LEFT:                       
                    if bloqueo_tecla_space:
                        if audio is not "fin":
                            contador = contador + 1
                            StopAudios()
                        if audio == 82:                                            
                            fondo = Fondo('n')
                            PlayAudio("pagina113.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 80:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina111.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 79:                            
                            fondo = Fondo('n')                                                        
                            PlayAudio("pagina109.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 91:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina102.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 90:                      
                            fondo = Fondo('n')
                            PlayAudio("pagina101.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 84:                            
                            fondo = Fondo('n')      
                            PlayAudio("pagina115.wav")
                            instruccion = "fin.wav"                      
                            audio = "fin"
                        if audio == 60:                            
                            PlayAudio("pagina80.wav")
                            instruccion = "esfera_80.wav"                                                        
                            audio = 80
                        if audio == 93:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina107.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 56:                      
                            fondo = Fondo('n')
                            PlayAudio("pagina78.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 55:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina76.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 70:                            
                            fondo = Fondo(5)
                            una_opcion = True
                            PlayAudio("pagina99.wav")
                            instruccion = "abajo.wav"
                            audio = 99
                        if audio == 69:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina97.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 74:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina92.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 72:                            
                            PlayAudio("pagina90.wav")
                            instruccion = "esfera_90.wav"                                                        
                            audio = 90
                        if audio == 64:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina86.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 61:                                                
                            fondo = Fondo('n')
                            PlayAudio("pagina83.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 40:                            
                            PlayAudio("pagina55.wav")
                            instruccion = "esfera_55.wav"                                                        
                            audio = 55
                        if audio == 52:                            
                            PlayAudio("pagina69.wav")
                            instruccion = "esfera_69.wav"                                                        
                            audio = 69
                        if audio == 51:                            
                            fondo = Fondo(5)
                            una_opcion = True       
                            PlayAudio("pagina67.wav")
                            instruccion = "esfera_67.wav"                                                 
                            audio = 67
                        if audio == 54:                      
                            PlayAudio("pagina74.wav")
                            instruccion = "esfera_74.wav"                                                        
                            audio = 74
                        if audio == 53:                            
                            PlayAudio("pagina72.wav")
                            instruccion = "esfera_72.wav"                                                        
                            audio = 72
                        if audio == 62:                            
                            fondo = Fondo('n')
                            PlayAudio("fin.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 44:                            
                            una_opcion = True
                            fondo = Fondo(5)
                            PlayAudio("pagina59.wav")
                            instruccion = "abajo.wav"
                            audio = 59
                        if audio == 28:                                                    
                            PlayAudio("pagina44.wav")
                            instruccion = "esfera_44.wav"                                                        
                            audio = 44
                        if audio == 42:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina57.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 38:                            
                            PlayAudio("pagina51.wav")
                            instruccion = "esfera_51.wav"                                                        
                            audio = 51
                        if audio == 36:                            
                            PlayAudio("pagina53.wav")
                            instruccion = "esfera_53.wav"                                                        
                            audio = 53
                        if audio == 27:                      
                            PlayAudio("pagina42.wav")
                            instruccion = "esfera_42.wav"                                                        
                            audio = 42
                        if audio == 23:                            
                            una_opcion = True
                            fondo = Fondo(5)
                            PlayAudio("pagina39.wav")
                            instruccion = "abajo.wav"
                            audio = 39
                        if audio == 20:                            
                            PlayAudio("pagina36.wav")
                            instruccion = "esfera_36.wav"                                                        
                            audio = 36
                        if audio == 14:                            
                            PlayAudio("pagina28.wav")
                            instruccion = "esfera_28.wav"                                                        
                            audio = 28
                        if audio == 12:                                                
                            fondo = Fondo('n')
                            PlayAudio("pagina24.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 11:                            
                            PlayAudio("pagina23.wav")
                            instruccion = "esfera_23.wav"                                                        
                            audio = 23
                        if audio == 10:                            
                            PlayAudio("pagina20.wav")
                            instruccion = "esfera_20.wav"                                                        
                            audio = 20
                        if audio == 6:                            
                            PlayAudio("pagina12.wav")
                            instruccion = "esfera_12.wav"
                            audio = 12
                        if audio == 4:                      
                            PlayAudio("pagina10.wav")
                            instruccion = "esfera_10.wav"                                                        
                            audio = 10
                        if audio == 2:                            
                            PlayAudio("pagina04.wav")
                            instruccion = "esfera_04.wav"                                                        
                            audio = 4
                        if audio == 88:
                            fondo = Fondo('n')      
                            PlayAudio("pagina94.wav")
                            instruccion = "fin.wav"                      
                            audio = "fin"                         
                        if audio == 65:                            
                            PlayAudio("pagina88.wav")
                            instruccion = "esfera_88.wav"                            
                            audio = 88
                        if audio == 46:                      
                            PlayAudio("pagina65.wav")
                            instruccion = "esfera_65.wav"                            
                            audio = 65
                        if audio == 32:
                            PlayAudio("pagina46.wav")
                            instruccion = "esfera_46.wav"                            
                            audio = 46
                        if audio == 34:                                             
                            fondo = Fondo(5)
                            una_opcion = True   
                            PlayAudio("pagina48.wav")
                            instruccion = "abajo.wav"                         
                            audio = 48
                        if audio == 17:                                                  
                            fondo = Fondo(5)
                            una_opcion = True 
                            PlayAudio("pagina33.wav")
                            instruccion = "abajo.wav"                           
                            audio = 33
                        if audio == 15:                                                        
                            fondo = Fondo('n')      
                            PlayAudio("pagina30.wav")
                            instruccion = "fin.wav"                      
                            audio = "fin"                         
                        if audio == 7:                            
                            PlayAudio("pagina15.wav")
                            instruccion = "esfera_15.wav"                            
                            audio = 15
                        if audio == 8:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina18.wav")
                            instruccion = "fin.wav"                            
                            audio = "fin"
                        if audio == 3:                            
                            PlayAudio("pagina07.wav")
                            instruccion = "esfera_07.wav"                            
                            audio = 7                            
                        if audio == 1:                                                    
                            PlayAudio("pagina02.wav")
                            instruccion = "esfera_02.wav"                            
                            audio = 2
                
                #Presionar la tecla 'Right'                            
                if event.key == pygame.K_RIGHT:
                    if bloqueo_tecla_space:
                        if audio is not "fin":
                            contador = contador + 1
                            StopAudios()
                        if audio == 90:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina106.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 91:                                                        
                            fondo = Fondo('n')
                            PlayAudio("pagina105.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 79:                                                    
                            fondo = Fondo('n')
                            PlayAudio("pagina110.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 80:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina112.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 82:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina114.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 84:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina116.wav")
                            instruccion = "fin.wav"                                                  
                            audio = "fin"
                        if audio == 60:                            
                            PlayAudio("pagina82.wav")
                            instruccion = "esfera_82.wav"                                                        
                            audio = 82
                        if audio == 56:                            
                            PlayAudio("pagina79.wav")
                            instruccion = "esfera_79.wav"                                                        
                            audio = 79
                        if audio == 55:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina77.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 70:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina100.wav")
                            instruccion = "fin.wav"                            
                            audio = "fin"
                        if audio == 69:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina98.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 93:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina108.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 74:                                                                                
                            audio = 93
                            PlayAudio("pagina93.wav")
                            instruccion = "esfera_93.wav"
                        if audio == 72:                            
                            PlayAudio("pagina91.wav")
                            instruccion = "esfera_91.wav"                                                        
                            audio = 91
                        if audio == 64:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina87.wav")
                            instruccion = "esfera_87.wav"                                                  
                            audio = "fin"
                        if audio == 61:                            
                            PlayAudio("pagina84.wav")
                            instruccion = "esfera_84.wav"                                                        
                            audio = 84
                        if audio == 40:                            
                            PlayAudio("pagina56.wav")
                            instruccion = "esfera_56.wav"                                                        
                            audio = 56
                        if audio == 52:                            
                            PlayAudio("pagina70.wav")
                            instruccion = "esfera_70.wav"                                                        
                            audio = 70
                        if audio == 51:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina68.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 54:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina75.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"                     
                        if audio == 53:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina73.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 62:                            
                            PlayAudio("pagina64.wav")
                            instruccion = "esfera_64.wav"                                                        
                            audio = 64
                        if audio == 44:                            
                            PlayAudio("pagina61.wav")
                            instruccion = "esfera_61.wav"                                                        
                            audio = 61
                        if audio == 28:                            
                            fondo = Fondo(5)
                            una_opcion = True 
                            PlayAudio("pagina45.wav")
                            instruccion = "abajo.wav"                                                       
                            audio = 45
                        if audio == 42:                            
                            fondo = Fondo('n')      
                            PlayAudio("pagina58.wav")
                            instruccion = "fin.wav"                                                  
                            audio = "fin"
                        if audio == 38:                            
                            PlayAudio("pagina52.wav")
                            instruccion = "esfera_52.wav"                                                        
                            audio = 52
                        if audio == 36:                            
                            PlayAudio("pagina54.wav")
                            instruccion = "esfera_54.wav"                                                        
                            audio = 54
                        if audio == 27:                            
                            fondo = Fondo(5)
                            una_opcion = True       
                            PlayAudio("pagina43.wav")
                            instruccion = "abajo.wav"                                                 
                            audio = 43
                        if audio == 23:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina41.wav")
                            instruccion = "esfera_41.wav"
                            audio = 41
                        if audio == 20:                            
                            PlayAudio("pagina38.wav")
                            instruccion = "esfera_38.wav"                                                        
                            audio = 38
                        if audio == 14:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina29.wav")
                            instruccion = "fin.wav"
                            audio = "fin"
                        if audio == 12:                            
                            PlayAudio("pagina27.wav")
                            instruccion = "esfera_27.wav"                                                        
                            audio = 27
                        if audio == 11:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina26.wav")
                            instruccion = "fin.wav"                                                        
                            audio = "fin"
                        if audio == 10:                            
                            fondo = Fondo(5)
                            una_opcion = True
                            PlayAudio("pagina22.wav")
                            instruccion = "abajo.wav"
                            audio = 22
                        if audio == 6:                            
                            PlayAudio("pagina14.wav")
                            instruccion = "esfera_14.wav"                                                        
                            audio = 14
                        if audio == 4:                            
                            PlayAudio("pagina11.wav")
                            instruccion = "esfera_11.wav"                                                        
                            audio = 11
                        if audio == 2:                            
                            PlayAudio("pagina06.wav")
                            instruccion = "esfera_06.wav"                                                        
                            audio = 6
                        if audio == 88:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina96.wav")
                            instruccion = "fin.wav"                            
                            audio = "fin"                         
                        if audio == 65:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina89.wav")
                            instruccion = "fin.wav"                            
                            audio = "fin"                         
                        if audio == 46:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina66.wav")
                            instruccion = "fin.wav"                        
                            audio = "fin"                         
                        if audio == 32:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina49.wav")
                            instruccion = "fin.wav"                            
                            audio = "fin"                         
                        if audio == 34:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina50.wav")
                            instruccion = "fin.wav"                            
                            audio = "fin"
                        if audio == 17:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina35.wav")
                            instruccion = "fin.wav"
                            audio = "fin"                         
                        if audio == 15:                            
                            PlayAudio("pagina32.wav")
                            instruccion = "esfera_32.wav"
                            audio = 32                        
                        if audio == 7:                            
                            fondo = Fondo(5)                            
                            una_opcion = True                                                        
                            PlayAudio("pagina16.wav")
                            instruccion = "abajo.wav"
                            audio = 16
                        if audio == 8:                            
                            fondo = Fondo('n')
                            PlayAudio("pagina19.wav")
                            instruccion = "fin.wav"
                            audio = "fin"                         
                        if audio == 3:  
                            PlayAudio("pagina08.wav")
                            instruccion = "esfera_08.wav"
                            audio = 8
                        if audio == 1:                                                                        
                            PlayAudio("pagina03.wav")
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