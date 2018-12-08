from math import fabs


import pygame
from pygame import gfxdraw
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('DDA')
win.fill((0,0,0))
color=(255,255,255)



a,b,c,d=input('Enter 2 endpoints of a line').split()
dx=int(c)-int(a)
dy=int(d)-int(b)

step = int(fabs(dx)) if (fabs(dx)>fabs(dy)) else int(fabs(dy))
x=int(a)
y=int(b)
k=0
x_inc = (dx/step)
y_inc = (dy/step)

for i in range(0,step+1,1):
    print('{0},{1}'.format(round(x),round(y)))
    gfxdraw.pixel(win,round(x),round(y),color)
    x=x+x_inc
    y=y+y_inc

pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
