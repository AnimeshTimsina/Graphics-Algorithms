import pygame
from pygame import gfxdraw
import math
from math import fabs
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('Transformation')
win.fill((0,0,0))
color = (255,255,255)

first_point = [[0],[0],[0]]
second_point = [[0],[0],[0]]
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
        gfxdraw.pixel(win,round(x)+250,round(y)+250,color)
        x=x+x_inc
        y=y+y_inc
    return


def multiply(ctm,mat):
    result = [[0],[0],[0]]
    for i in range(len(ctm)):
       for j in range(len(mat[0])):
           for k in range(len(mat)):
               result[i][j] += ctm[i][k] * mat[k][j]

    return result

def display(mat1,mat2):

    lineDDA(round(mat1[0][0]),round(mat1[1][0]),round(mat2[0][0]),round(mat2[1][0]))

    return

def scaling(mat1,mat2,sX,sY):
    ctm = [[sX,0,0],[0,sY,0],[0,0,1]]
    first_point = multiply(ctm,mat1)
    second_point = multiply(ctm , mat2)
    display(first_point,second_point)
    return

def translation(mat1,mat2,x,y):
    ctm = [[1,0,x],[0,1,y],[0,0,1]]
    #display(multiply(ctm,mat1))
    first_point = multiply(ctm,mat1)
    second_point = multiply(ctm,mat2)
    # print(round(first_point[0][0]),round(first_point[1][0]),round(second_point[0][0]),round(second_point[1][0]))
    display(first_point,second_point)
    return

def rotation(mat1,mat2,angle):
    if (angle>0):
        ctm = [[math.cos(angle),-math.sin(angle),0],[math.sin(angle),math.cos(angle),0],[0,0,1]]
    else:
        ctm = [[math.cos(angle),math.sin(angle),0],[-math.sin(angle),math.cos(angle),0],[0,0,1]]


    first_point = multiply(ctm,mat1)
    second_point = multiply(ctm ,mat2)
    display(first_point,second_point)
    return


a,b,c,d = input('Enter the coordinates of the line to be transformed').split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
lineDDA(a,b,c,d)
matA = [[a],[b],[1]]
matB = [[c],[d],[1]]


print('1: Rotation')
print('2: Scaling')
print('3: Translation')
x = int(input('Enter your choice'))
while (2!=3):
    if (x==1):
        angle = int(input('Enter angle for rotation(-ve for clockwise)'))
        rotation(matA,matB,angle)
        break;
    if (x==2):
        sX,sY = input('Enter scale factors').split()
        sX = float(sX)
        sY = float(sY)
        scaling(matA,matB,sX,sY)

        break;
    if (x==3):
        X,Y = input('Enter translation factors').split()
        X = int(X)
        Y=int(Y)
        translation(matA,matB,X,Y)
        break;


pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
