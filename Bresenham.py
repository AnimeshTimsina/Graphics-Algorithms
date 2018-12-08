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
x_inc = 1 if (dx*1)==dx else -1
y_inc = 1 if (dy*1)==dy else -1
x=int(a)
y=int(b)
print('{} , {}'.format(x,y))
gfxdraw.pixel(win,int(a),int(b),color)
if (fabs(dx)>fabs(dy)):
    p=2*dy-dx
   
    for k in range (0,dx,1):
        if p<0:
            x=x+x_inc
            p=p+2*(int(d)-y)
        else:
            x=x+x_inc
            y=y+y_inc
            p=p+2*(int(d)-y)-2*(int(c)-x)
        print('{} , {} , {}'.format(x,y,p))
        gfxdraw.pixel(win,x,y,color)
else:
    p=2*dx-dy
 
    for k in range (0,dy,1):
        if p<0:
            y=y+y_inc
            p=p+2*(int(c)-x)
        else:
            x=x+x_inc
            y=y+y_inc
            p=p-2*(int(d)-y)+2*(int(c)-x)
        print('{} , {}, {}'.format(x,y,p))
        gfxdraw.pixel(win,x,y,color)
    
pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
