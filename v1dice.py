'''
Sandra Dögg Kristmundsdóttir
28.01.2018
'''
import pygame
from random import *
pygame.init()

window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)  # makes screen resizable

pygame.display.set_caption('Teningakast')

LEFT_BUTTON = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#næ í myndir fyrir teningana
ten1png = pygame.image.load('ten1.png')
ten2png = pygame.image.load('ten2.png')
ten3png = pygame.image.load('ten3.png')
ten4png = pygame.image.load('ten4.png')
ten5png = pygame.image.load('ten5.png')
ten6png = pygame.image.load('ten6.png')

# Myndir færðar inn í lista
teningalisti = [[ten1png, 1], [ten2png, 2], [ten3png, 3], [ten4png, 4], [ten5png, 5], [ten6png, 6]]


running = True  # loop control variable(for the game loop)
a = window.blit(teningalisti[randint(0, 5)][0], (0, 0))
b = window.blit(teningalisti[randint(0, 5)][0], (200, 0))
c = window.blit(teningalisti[randint(0, 5)][0], (0, 200))
d = window.blit(teningalisti[randint(0, 5)][0], (200, 200))
e = window.blit(teningalisti[randint(0, 5)][0], (400, 200))
pygame.display.flip()
#myndalisti
imagelisti=[a,b,c,d,e]
#teljari fyrir köst
rollcounter=0
#listi til að fylgjast með völdum reitum
clickedreitir=[]
while running:
    #birti texta í reroll reit eftir hve oft hefur verið kastað
    my_font = pygame.font.SysFont("", 30)
    rollcheck = pygame.draw.rect(window, WHITE, pygame.Rect(170, 330, 260, 50))
    if rollcounter <= 1:
        label = my_font.render('Ýttu til að kasta aftur ', 1, BLACK)
        window.blit(label, (180, 340))
        pygame.display.flip()
    else:
        label = my_font.render('Ekki hægt að kasta aftur ', 1, RED)
        window.blit(label, (180, 340))
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #lokar leiknum ef það er ýtt á escape
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        #athuga hvort það var klikkað
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
            #fæ hnit hvar var klikkað
            x , y = event.pos
            #fer í gegnum alla teninga til að vita hvort það hafi verið ýtt á þá
            for img in imagelisti:
                if img.collidepoint(event.pos):
                    #ef þeir eru valdnir þá er þeim bætt við clickedreitir
                    #ef að þeir voru nú þegar í listanum þá eru þeir fjarlægðir
                    if img not in clickedreitir:
                        clickedreitir.append(img)
                        print("Selected dice")
                        print(len(clickedreitir),"dice selected")
                    else:
                        clickedreitir.remove(img)
                        print("Unselected dice")
                        print(len(clickedreitir),"dice selected")
            #ef það var klikkað á kasta aftur reitinn
            if rollcheck.collidepoint(event.pos):
                #athuga ef notandi má kasta aftur eða ekki
                if rollcounter<=1 and len(clickedreitir)>0:
                    rollcounter+=1
                    #fer í gegnum listan af völdum reitum og kastar þeim aftur
                    for image in imagelisti:
                        if image in clickedreitir:
                            clickedreitir.remove(image)
                            image=window.blit(teningalisti[randint(0,5)][0],(image[0],image[1]))
                            pygame.display.flip()
                            print("kastað")
                #prentar að enginn reitur var valinn
                elif rollcounter<=1 and len(clickedreitir)==0:
                    print("Þú hefur ekki valið neina teninga til að kasta aftur!")
pygame.quit()
