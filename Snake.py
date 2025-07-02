import pygame
import random
from tkinter import simpledialog
import json

ANCHO = 735
ALTO = 815
CUADRO = ANCHO/21

verdeC = (69, 226, 64)
verdeO = (57, 198, 53)
verdes=[verdeC,verdeO]
blue=(18, 117, 216)
pygame.display.init()
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.mixer_music.load("theme.mp3")
pygame.mixer_music.set_volume(0.7)
comer = pygame.mixer.Sound("comer.mp3")
perder = pygame.mixer.Sound("perder.wav")

perder.set_volume(0.2)

pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Snake")
class Snake():
    def __init__ (self,xh,yh,xt,yt):
        self.head = [xh,yh]
        self.tail = [xt,yt]
        self.largo=3
        self.direccion = "r"

def dibujarPantalla(matriz,puntuacion,snake):
    pantalla.fill((30,30,30))
    verde=1
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            verde -=1
            pygame.draw.rect(pantalla,verdes[verde%len(verdes)],(i*CUADRO,j*CUADRO,CUADRO,CUADRO))
            if matriz[j][i] == -2:
                pygame.draw.rect(pantalla,"grey",(i*CUADRO,j*CUADRO,CUADRO,CUADRO))
                pygame.draw.rect(pantalla,"black",(i*CUADRO,j*CUADRO,CUADRO,CUADRO),1)
            elif matriz[j][i] == 1:
                pygame.draw.rect(pantalla,blue,(i*CUADRO,j*CUADRO,CUADRO,CUADRO))
            elif matriz[j][i] == 2:
                pygame.draw.circle(pantalla,"red",(i*CUADRO+CUADRO//2,j*CUADRO+CUADRO//2),CUADRO//2)
    pygame.font.init()
    fuente = pygame.font.SysFont("calibri",25,True)
    puntos = fuente.render(f"Puntuacion: {puntuacion}",1,"white")
    pantalla.blit(puntos, (ANCHO // 2 - puntos.get_width() // 2, ALTO-CUADRO*1.8))
    fuente = pygame.font.SysFont("calibri",20,True)
    dev = fuente.render("Dev: Alejandro Amador Ruiz",1,"white")
    pantalla.blit(dev, (ANCHO // 2 - dev.get_width() // 2, ALTO-35))
    if snake.direccion == "u": #
        pygame.draw.circle(pantalla,blue,(snake.head[1]*CUADRO+CUADRO//2,snake.head[0]*CUADRO),CUADRO//2)
        pygame.draw.circle(pantalla,"white",(snake.head[1]*CUADRO+CUADRO//3,snake.head[0]*CUADRO),CUADRO//6)
        pygame.draw.circle(pantalla,"white",(snake.head[1]*CUADRO+CUADRO//3*2,snake.head[0]*CUADRO),CUADRO//6)
        pygame.draw.circle(pantalla,"black",(snake.head[1]*CUADRO+CUADRO//3,snake.head[0]*CUADRO),CUADRO//10)
        pygame.draw.circle(pantalla,"black",(snake.head[1]*CUADRO+CUADRO//3*2,snake.head[0]*CUADRO),CUADRO//10)
    elif snake.direccion == "d":
        pygame.draw.circle(pantalla,blue,(snake.head[1]*CUADRO+CUADRO//2,snake.head[0]*CUADRO+CUADRO),CUADRO//2)
        pygame.draw.circle(pantalla,"white",(snake.head[1]*CUADRO+CUADRO//3,snake.head[0]*CUADRO+CUADRO),CUADRO//6)
        pygame.draw.circle(pantalla,"white",(snake.head[1]*CUADRO+CUADRO//3*2,snake.head[0]*CUADRO+CUADRO),CUADRO//6)
        pygame.draw.circle(pantalla,"black",(snake.head[1]*CUADRO+CUADRO//3,snake.head[0]*CUADRO+CUADRO),CUADRO//10)
        pygame.draw.circle(pantalla,"black",(snake.head[1]*CUADRO+CUADRO//3*2,snake.head[0]*CUADRO+CUADRO),CUADRO//10)
    elif snake.direccion == "r":
        pygame.draw.circle(pantalla,blue,(snake.head[1]*CUADRO+CUADRO,snake.head[0]*CUADRO+CUADRO//2),CUADRO//2)
        pygame.draw.circle(pantalla,"white",(snake.head[1]*CUADRO+CUADRO,snake.head[0]*CUADRO+CUADRO//3),CUADRO//6)
        pygame.draw.circle(pantalla,"white",(snake.head[1]*CUADRO+CUADRO,snake.head[0]*CUADRO+CUADRO//3*2),CUADRO//6)
        pygame.draw.circle(pantalla,"black",(snake.head[1]*CUADRO+CUADRO,snake.head[0]*CUADRO+CUADRO//3),CUADRO//10)
        pygame.draw.circle(pantalla,"black",(snake.head[1]*CUADRO+CUADRO,snake.head[0]*CUADRO+CUADRO//3*2),CUADRO//10)
    elif snake.direccion == "l": #
        pygame.draw.circle(pantalla,blue,(snake.head[1]*CUADRO,snake.head[0]*CUADRO+CUADRO//2),CUADRO//2)
        pygame.draw.circle(pantalla,"white",(snake.head[1]*CUADRO,snake.head[0]*CUADRO+CUADRO//3),CUADRO//6)
        pygame.draw.circle(pantalla,"white",(snake.head[1]*CUADRO,snake.head[0]*CUADRO+CUADRO//3*2),CUADRO//6)
        pygame.draw.circle(pantalla,"black",(snake.head[1]*CUADRO,snake.head[0]*CUADRO+CUADRO//3),CUADRO//10)
        pygame.draw.circle(pantalla,"black",(snake.head[1]*CUADRO,snake.head[0]*CUADRO+CUADRO//3*2),CUADRO//10)
    if matriz[snake.tail[0]][snake.tail[1]+1]==1: # derecha
        pygame.draw.circle(pantalla,blue,(snake.tail[1]*CUADRO,snake.tail[0]*CUADRO+CUADRO//2),CUADRO//2)
    elif matriz[snake.tail[0]][snake.tail[1]-1]==1: # izquierda
        pygame.draw.circle(pantalla,blue,(snake.tail[1]*CUADRO+CUADRO,snake.tail[0]*CUADRO+CUADRO//2),CUADRO//2)
    elif matriz[snake.tail[0]+1][snake.tail[1]]==1: # abajo
        pygame.draw.circle(pantalla,blue,(snake.tail[1]*CUADRO+CUADRO//2,snake.tail[0]*CUADRO),CUADRO//2)
    elif matriz[snake.tail[0]-1][snake.tail[1]]==1: # arriba
        pygame.draw.circle(pantalla,blue,(snake.tail[1]*CUADRO+CUADRO//2,snake.tail[0]*CUADRO+CUADRO),CUADRO//2)
    pygame.display.update()
    
def insertarSnake(snake,matriz):
    matriz[snake.head[0]][snake.head[1]] = 1
    matriz[snake.tail[0]][snake.tail[1]] = 1
    matriz[snake.head[0]][snake.head[1]-1] = 1
    
def actualizarSnake(snake=Snake(0,0,0,0), matriz=[], agrandar=False):
    if not agrandar:
        if matriz[snake.head[0]][snake.head[1]]==1 or matriz[snake.head[0]][snake.head[1]]==-2:
            matriz[snake.head[0]][snake.head[1]]=-1
        else:
            matriz[snake.head[0]][snake.head[1]]=1
            if matriz[snake.tail[0]][snake.tail[1]+1]==1: # derecha
                matriz[snake.tail[0]][snake.tail[1]]=0
                snake.tail=[snake.tail[0],snake.tail[1]+1]
            elif matriz[snake.tail[0]][snake.tail[1]-1]==1: # izquierda
                matriz[snake.tail[0]][snake.tail[1]]=0
                snake.tail=[snake.tail[0],snake.tail[1]-1]
            elif matriz[snake.tail[0]+1][snake.tail[1]]==1: # abajo
                matriz[snake.tail[0]][snake.tail[1]]=0
                snake.tail=[snake.tail[0]+1,snake.tail[1]]
            elif matriz[snake.tail[0]-1][snake.tail[1]]==1: # arriba
                matriz[snake.tail[0]][snake.tail[1]]=0
                snake.tail=[snake.tail[0]-1,snake.tail[1]]
    else:
        matriz[snake.head[0]][snake.head[1]]=1
    agrandar=False
    
def checkComer(matriz):
    for i in matriz:
        if 2 in i:
            return False
    return True

def checkGameOver(matriz):
    for i in matriz:
        if -1 in i:
            return True
    return False
                
def spawnFruta(matriz):
    aceptadas = [[(i,j) for i in range(20) if matriz[j][i] == 0] for j in range(20)]
    aceptadas = [elemento for fila in aceptadas for elemento in fila]
    
    posFruta = random.choice(aceptadas)
    
    matriz[posFruta[1]][posFruta[0]] = 2
    
def pausado():
    pygame.font.init()
    fuente = pygame.font.SysFont("console",60,True)
    pause = fuente.render("PAUSA",1,"Red")
    pantalla.blit(pause,(CUADRO,CUADRO))
    pygame.display.update()
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False  
                return False  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mainMenu()
                    return True
                if event.key == pygame.K_ESCAPE:
                    run=False
                    return True
                if event.key == pygame.K_p:
                    run=False
                    return False
    return False

def gameOver(pantalla,puntuacion):
    perder.play()
    pantalla.fill("black")
    pygame.font.init()
    fuente = pygame.font.SysFont("console",80,True)
    gameOver = fuente.render(f"FIN DEL JUEGO",1,"red")
    fuente = pygame.font.SysFont("calibri",30,True)
    puntos = fuente.render(f"Puntuacion: {puntuacion}",1,"white")
    r = fuente.render("ESC: Salir       R: Reiniciar",1,"white") 
    pantalla.blit(puntos, (ANCHO // 2 - puntos.get_width() // 2, ALTO//2))
    pantalla.blit(gameOver, (ANCHO // 2 - gameOver.get_width() // 2, ALTO//2-100))
    pantalla.blit(r,(ANCHO//2-r.get_width()//2,ALTO-CUADRO*2))
    fuente = pygame.font.SysFont("arial",20,True)
    dev = fuente.render("Dev: Alejandro Amador Ruiz",1,"white")
    pantalla.blit(dev, (ANCHO // 2 - dev.get_width() // 2, ALTO-35))
    pygame.display.update()
    run=True
        
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mainMenu()
                if event.key == pygame.K_ESCAPE:
                    run=False
    
            
def main(dif):
    snake = Snake(5,10,5,8)
    matriz = [[0 for i in range(21)] for j in range(21)]
    for i,j in enumerate(matriz[0]): 
        matriz[0][i]=-2
        matriz[len(matriz)-1][i]=-2
        matriz[i][0]=-2
        matriz[i][len(matriz)-1]=-2
    for i in range(0,len(matriz),2):
        for j in range(0,21,2):
            matriz[i][j] = -2
    insertarSnake(snake,matriz)
    clock = pygame.time.Clock()
    tiempo = 0
    velocidad = dif
    moved=False
    agrandar=False
    spawnFruta(matriz)
    puntuacion = 0
    enfriamiento=True
    
    pygame.mixer_music.play(-1)
    music = True
    
    running = True
    while running:
        dibujarPantalla(matriz,puntuacion,snake)
        
        tiempo += clock.get_rawtime()
        clock.tick()
        
        if tiempo/1000>velocidad:
            tiempo = 0
            if snake.direccion == "l":
                snake.head[1]-=1
            if snake.direccion == "u":
                snake.head[0]-=1
            if snake.direccion == "r":
                snake.head[1]+=1
            if snake.direccion == "d":
                snake.head[0]+=1
            actualizarSnake(snake,matriz,agrandar)
            agrandar=False
            if moved:
                enfriamiento=True
            else:
                if enfriamiento:
                    enfriamiento=False
                else:
                    enfriamiento=True
            moved=False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not moved and not enfriamiento:
                if event.key == pygame.K_LEFT:
                    if snake.direccion != "r":
                        snake.direccion="l"
                        moved=True
                if event.key == pygame.K_RIGHT:
                    if snake.direccion != "l":
                        snake.direccion="r"
                        moved=True
                if event.key == pygame.K_DOWN:
                    if snake.direccion != "u":
                        snake.direccion="d"
                        moved=True
                if event.key == pygame.K_UP:
                    if snake.direccion != "d":
                        snake.direccion="u"
                        moved=True
                if event.key == pygame.K_p:
                    pygame.mixer_music.pause()
                    if pausado():
                        running=False
                    pygame.mixer_music.unpause()
                if event.key == pygame.K_m:
                    if music:
                        pygame.mixer_music.pause()
                        music=False
                    else:
                        pygame.mixer_music.unpause()
                        music=True                
                        
        if moved:
            enfriamiento=True
    
        if checkComer(matriz):
            comer.play()
            spawnFruta(matriz)
            agrandar=True
            puntuacion+=1
            
            
        if checkGameOver(matriz):
            pygame.mixer_music.stop()
            gameOver(pantalla,puntuacion)
            
            running=False

        
def mainMenu():
    pantalla.fill("black")
    pygame.font.init()
    fuente = pygame.font.SysFont("console",100,True)
    titulo = fuente.render("SNAKE",1,"green")
    fuente = pygame.font.SysFont("calibri",40,True)
    dif1 = fuente.render ("1: Facil",1,"white")
    dif2 = fuente.render ("2: Normal",1,"white")
    dif3 = fuente.render ("3: Dificil",1,"white")
    esc = fuente.render("ESC: Salir.",1,"white")

    pantalla.blit(titulo,(ANCHO//2-titulo.get_width()//2,ALTO//2-titulo.get_height()//2-120))
    pantalla.blit(dif1,(ANCHO//2-dif1.get_width()//2,ALTO//2-dif1.get_height()//2-50))
    pantalla.blit(dif2,(ANCHO//2-dif2.get_width()//2,ALTO//2-dif2.get_height()//2))
    pantalla.blit(dif3,(ANCHO//2-dif3.get_width()//2,ALTO//2-dif3.get_height()//2+50))
    pantalla.blit(esc,(ANCHO//2-esc.get_width()//2,ALTO-CUADRO*2))
    
    fuente = pygame.font.SysFont("calibri",20,True)
    dev = fuente.render("Dev: Alejandro Amador Ruiz",1,"white")
    pantalla.blit(dev, (ANCHO // 2 - dev.get_width() // 2, ALTO-35))

    pygame.display.update()
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    main(0.5)
                    run=False
                if event.key == pygame.K_2:
                    main(0.3)
                    run=False
                if event.key == pygame.K_3:
                    main(0.15)
                    run=False
                if event.key == pygame.K_ESCAPE:
                    run=False
    
mainMenu()