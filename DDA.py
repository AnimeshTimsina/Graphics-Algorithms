from math import fabs
import pygame
from pygame import gfxdraw
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('DDA')
win.fill((0,0,0))
color=(255,255,255)




def lineDDA(a,b,c,d):
    dx=int(c)-int(a)
    dy=int(d)-int(b)
    step = int(fabs(dx)) if (fabs(dx)>fabs(dy)) else int(fabs(dy))
    x=int(a)
    y=int(b)
    k=0
    x_inc = (dx/step)
    y_inc = (dy/step)

    for i in range(0,step+1,1):
        gfxdraw.pixel(win,round(x),round(y),color)
        x=x+x_inc
        y=y+y_inc
    return

a,b,c,d=input('Enter 2 endpoints of a line').split()

lineDDA(a,b,c,d)
pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
