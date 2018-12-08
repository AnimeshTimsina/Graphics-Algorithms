import pygame
from pygame import gfxdraw
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('Mid-Point Circle Drawing Program')
win.fill((0,0,0))
color=(255,255,255)


def drawPoints(x,y):
    gfxdraw.pixel(win,x+a+250,y+b+250,color)
def MidPointCircle():
    p=1-r
    x=0
    y=r
    drawPoints(x,y)
    while (x<y):
        if (p>=0):
            x=x+1
            y=y-1
            p=p+2*x+1-2*y
        else:
            x=x+1
            y=y
            p=p+2*x+1
        drawPoints(x,y)
        drawPoints(y,x)
        drawPoints(-x,y)
        drawPoints(x,-y)
        drawPoints(-x,-y)
        drawPoints(-y,x)
        drawPoints(y,-x)
        drawPoints(-y,-x)

a,b,c = input('Enter center and radius of the circle').split()
a = int(a)
b = int(b)
r = int(c)
MidPointCircle()
r=int(c)-50
MidPointCircle()
pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
