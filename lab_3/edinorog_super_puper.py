import math as m
import pygame
from pygame.draw import *
import random as r
pygame.init()

FPS = 30
sc = pygame.display.set_mode((600, 800))

NEBO = (130,202,250)
RED = (255, 40, 40)
ORANGE = (255, 165, 60)
YELLOW = (255, 255, 0)
GREEN = (92, 205, 50)
BLUE = (0, 127, 253)
DARK_BLUE = (40, 8, 253)
VIOLET = (117, 87, 253)
TRAVA = (80, 200, 120)

def nebo(color):
    '''
    функция рисует небо
    '''
    sc.fill(color)

def rainbow( x, y):
    '''
    функция рисует радугу
    x,y - координаты начала
    '''
    A = [RED, ORANGE, YELLOW, GREEN, BLUE, DARK_BLUE, VIOLET]
    for i in range (0, 7, 1):
        arc(sc, A[i], (x, y+8*i, 750-8*i, 750-8*1), 0, m.pi, 10)

def trava(screen, color, b):
    '''
    функция рисует траву как прямоугольник
    '''
    rect(screen, color, b)

def flowers(number):
    '''
    функция рисует цветы
    scale - зона появления цветов по х
    l - зона появления цветов по у
    size - размер
    number - количество цветов
    '''
    for i in range(1,number,1):
        scale=r.randint(0,600)
        l=r.randint(300,800)
        size=r.randint(10,30)/10
        line(sc, (0, 100, 0), [scale,l],[scale+2*size,l+3*size])
        line(sc, (0, 100, 0), [scale+2*size, l-1*size],[scale+2*size,l+3*size])
        ellipse(sc, (r.randint(100, 255), r.randint(50, 255), r.randint(50, 255)), (scale+1*size, l-8*size , 3*size, 8*size), 0)

#солнце)
def sun():
    '''
    фунцкия рисует солнце
    '''
    for i in range(1,200,1):
        circle(sc,  (255-6.25/10*i, 202, 1.275*i), (500, 100), i, 2)      


#единорог
def edinorog (x, y, i, p, k, f):
    '''
    функция рисует единорогов
    x,y - координаты единорогов
    i,p,k - коэффициенты для удобства
    f - коэффициент для определения цвета
    '''
    #хвост
    ellipse(sc, (255-f, 143+f, 193), (x-i*k*53-p*40, y+k*80, k*40,k*9), 0)
    ellipse(sc, (255-f, 143+f, 193), (x-i*k*41-p*k*60, y+k*50, k*60,k*9), 0)
    ellipse(sc, (255-f, 143+f, 193), (x-i*k*39-p*k*40, y+k*10, k*40,k*30), 0)

    ellipse(sc, (191-f, 143+f, 193), (x-i*k*46-p*k*50, y+k*10, k*50,k*20), 0)
    ellipse(sc, (191-f, 143+f, 193), (x-i*k*41-p*k*40, y+k*50, k*40,k*9), 0)
    ellipse(sc, (191-f, 143+f, 193), (x-i*k*36-p*k*36, y+k*68, k*36,k*16), 0)

    ellipse(sc, (191-f, 79+f, 193), (x-i*k*56-p*k*36, y+k*90, k*36,k*26), 0)
    ellipse(sc, (191-f, 79+f, 193), (x-i*k*26-p*k*36, y+k*46, k*36,k*14), 0)
    ellipse(sc, (191-f, 79+f, 193), (x-i*k*48-p*k*26, y+k*51, k*26,k*20), 0)
    ellipse(sc, (191-f, 79+f, 193), (x-i*k*21-p*k*25, y, k*25,k*13), 0)

    ellipse(sc, (254-f, 142+f, 193), (x-i*k*18-p*k*26, y+k*21, k*26,k*20), 0)
    ellipse(sc, (254-f, 142+f, 193), (x-i*k*28-p*k*26, y+k*51, k*26,k*20), 0)
    ellipse(sc, (254-f, 142+f, 193), (x-i*k*33-p*k*26, y+k*31, k*26,k*20), 0)
    
    #туловище
    ellipse(sc, (255, 255, 255), (x-i*k*10-p*k*170, y, k*170, k*70), 0)
    
    #ноги
    rect(sc, (255, 255, 255), (x+i*k*10-p*k*3, y+k*30, k*13, k*100))
    rect(sc, (255, 255, 255), (x+i*k*30-p*k*3, y+k*30, k*13, k*110))
    rect(sc, (255, 255, 255), (x+i*k*120-p*k*3, y+k*30, k*13, k*100))
    rect(sc, (255, 255, 255), (x+i*k*140-p*k*3, y+k*30, k*13, k*110))
    
    #шея
    rect(sc, (255, 255, 255), (x+i*k*120-p*k*30, y-k*40, k*30, k*70))
    
    #голова
    ellipse(sc, (255, 255, 255), (x+i*k*112-p*k*50, y-k*65, k*51, k*30), 0)
    ellipse(sc, (255, 255, 255), (x+i*k*142-p*k*36, y-k*55, k*36, k*18), 0)
    
    #глаз
    circle(sc, (241, 79, 193), (x+i*k*149, y-k*55), k*7, 0)
    circle(sc, (0, 0, 0), (x+i*k*151, y-k*53), k*4, 0)
    
    #рог
    polygon(sc, (216, 78, 193), [(x+i*k*135, y-k*65), (x+k*i*135,y-k*115),
                               (x+i*k*143, y-k*65)], 0)
    #грива
    ellipse(sc, (191-f, 79+f, 193), (x-i*k*62+i*k*140-p*k*40, y+k*80-k*70, k*40,k*9), 0)
    ellipse(sc, (191-f, 79+f, 193), (x-i*k*50+i*k*140-p*k*60, y+k*50-k*70, k*60,k*9), 0)
    ellipse(sc, (191-f, 79+f, 193), (x-i*k*48+i*k*140-p*k*40, y+k*10-k*70, k*40,k*30), 0)
    
    ellipse(sc, (191-f, 79+f, 193), (x-i*k*30+i*k*140-p*k*25, y-k*70, k*25,k*13), 0)

    ellipse(sc, (255-f, 143+f, 193), (x-i*k*55+i*k*140-p*k*50, y+k*10-k*70, k*50, k*20), 0)
    ellipse(sc, (255-f, 143+f, 193), (x-i*k*50+i*k*140-p*k*40, y+k*50-k*70, k*40, k*9), 0)
    ellipse(sc, (255-f, 143+f, 193), (x-i*k*45+k*i*140-p*k*36, y+k*68-k*70, k*36, k*16), 0)

    ellipse(sc, (254-f, 142+f, 193), (x-i*k*65+i*k*140-p*k*36, y+k*90-k*70, k*36, k*26), 0)
    ellipse(sc, (254-f, 142+f, 193), (x-i*k*35+i*k*140-p*k*36, y+k*46-k*70, k*36, k*14), 0)
    ellipse(sc, (254-f, 142+f, 193), (x-i*k*57+i*k*140-p*k*26, y+k*51-k*70, k*26, k*20), 0)

    ellipse(sc, (191-f, 143+f, 193), (x-i*k*27+i*k*140-p*k*26, y+k*21-k*70, k*26, k*20), 0)
    ellipse(sc, (191-f, 143+f, 193), (x-i*k*37+i*k*140-p*k*26, y+k*51-k*70, k*26, k*20), 0)
    ellipse(sc, (191-f, 143+f, 193), (x-i*k*45+i*k*140-p*k*26, y+k*31-k*70, k*26, k*20), 0)

def derevo (x, y, k, p, spelost):
    '''
    функия рисует деревья с яблоками разной спелости
    х,у - координаты дерева
    k,p - коэффициенты для длины ствола/размера листвы
    spelost - спелость яблока(насыщенность цвета)
    '''
    #ствол
    rect(sc, (255, 255, 255), (x+6*k, y, 35*k, 110*p), 0)
    
    #верхний ярус
    ellipse(sc, (49, 136, 87), (x-k*56, y-p*290, k*140, p*180), 0)
    ellipse(sc, (0, 255, 0), (x-k*56, y-p*290, k*140, p*180), 2)

    #средний ярус
    ellipse(sc, (49, 136, 87), (x-k*96, y-p*190, k*240, p*120), 0)
    ellipse(sc, (0, 255, 0), (x-k*96, y-p*190, k*240, p*120), 2)

    #нижний ярус
    ellipse(sc, (49, 136, 87), (x-k*56, y-p*100, k*160, p*120), 0)
    ellipse(sc, (0, 255, 0), (x-k*56, y-p*100, k*160, p*120), 2)
    
    #яблоки
    t=spelost
    ellipse(sc, (255, 218-t, 185-t), (x+k*50, y-p*25, k*35, p*30), 0)
    ellipse(sc, (255, 238-t, 205-t), (x+k*50, y-p*25, k*35, p*30), 2)
    for e in range (12):
        if e<7:
            ellipse(sc, (255, 255, 255), (x+k*74-k*e, y-p*13-p*e, 2*p*e, 2*p*e), 2)
        else:   
            ellipse(sc, (255, 255-t-5*(e-7), 255-t-14*(e-7)), (x+k*74-k*e, y-p*13-p*e, 2*p*e, 2*p*e), 2)
    
    ellipse(sc, (255, 218-t, 185-t), (x+k*100, y-p*150, k*35, p*30), 0)
    ellipse(sc, (255, 238-t, 205-t), (x+k*100, y-p*150, k*35, p*30), 2)
    for e in range (12):
        if e<7:
            ellipse(sc, (255, 255, 255), (x+k*124-k*e, y-p*138-p*e, 2*p*e, 2*p*e), 2)
        else:   
            ellipse(sc, (255, 255-t-5*(e-7), 255-t-14*(e-7)), (x+k*124-k*e, y-p*138-p*e, 2*p*e, 2*p*e), 2)
    
    ellipse(sc, (255, 218-t, 185-t), (x-k*90, y-p*150, k*35, p*30), 0)
    ellipse(sc, (255, 238-t, 205-t), (x-k*90, y-p*150, k*35, p*30), 2)
    for e in range (12):
        if e<7:
            ellipse(sc, (255, 255, 255), (x-k*66-k*e, y-p*138-p*e, 2*p*e, 2*p*e), 2)
        else:   
            ellipse(sc, (255, 255-t-5*(e-7), 255-t-14*(e-7)), (x-k*66-k*e, y-p*138-p*e, 2*p*e, 2*p*e), 2)
    
    ellipse(sc, (255, 218-t, 185-t), (x+k*25, y-p*245, k*35, p*30), 0)
    ellipse(sc, (255, 238-t, 205-t), (x+k*25, y-p*245, k*35, p*30), 2)
    for e in range (12):
        if e<7:
            ellipse(sc, (255, 255, 255), (x+k*49-k*e, y-p*233-p*e, 2*p*e, 2*p*e), 2)
        else:   
            ellipse(sc, (255, 255-t-5*(e-7), 255-t-14*(e-7)), (x+k*49-k*e, y-p*233-p*e, 2*p*e, 2*p*e), 2)

nebo(NEBO)
rainbow (-400, 0)
trava(sc, TRAVA, (0, 300, 600, 500))
sun()
flowers(60)
edinorog(300,350,1,0,0.6,10)
edinorog(250,570,1,0,1,40)

edinorog(550,450,-1,1,0.8,63)
edinorog(550,300,-1,1, 0.5,35)


derevo(100, 350, 1, 1, 100)
derevo(175, 400, 0.8, 0.5, 70)
derevo(0, 500, 0.9, 0.9, 30)
derevo(133, 590, 0.8, 0.7, 140)
derevo(50, 700, 0.7, 0.7, 50)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
