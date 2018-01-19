from __future__ import division
import pygame
from pygame.locals import*
from math import sin,cos,pi

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
VIOLET = (148,0,211)

WIDTH = 600
HEIGHT = 600
size = (WIDTH, HEIGHT)
XMIN = -7
XMAX = 7
YMIN = -7
YMAX = 7

fmatrix = [[-4,-4,2],
           [-1,-4,2],
           [0,-1,2],
           [1,-4,2],
           [4,-4,2],
           [1,4,2],
           [-1,4,2],
           [-4,-4,2],
           [-4,-4,-2],
           [-1,-4,-2],
           [0,-1,-2],
           [1,-4,-2],
           [4,-4,-2],
           [1,4,-2],
           [-1,4,-2],
           [-4,-4,-2],
           [-1,0,2],
           [1,0,2],
           [0,2,2],
           [-1,0,2],
           [-1,0,-2],
           [1,0,-2],
           [0,2,-2],
           [-1,0,-2]]

edges = [[0,1],
         [1,2],
         [2,3],
         [3,4],
         [4,5],
         [5,6],
         [6,7],
         [7,8],
         [8,9],
         [9,10],
         [10,11],
         [11,12],
         [12,13],
         [13,14],
         [14,15],
         [16,17],
         [17,18],
         [18,19],
         [20,21],
         [21,22],
         [22,23],
         [0,8],
         [1,9],
         [2,10],
         [3,11],
         [4,12],
         [5,13],
         [6,14],
         [7,15],
         [16,20],
         [17,21],
         [18,22],
         [19,23]]

Xc = 0
Yc = 3.0
Zc = 6.0

zoom = 10

def screenXY(point):
    return [point[0]*(WIDTH/(XMAX-XMIN)) + WIDTH/2,
            -point[1]*HEIGHT/(YMAX-YMIN) + HEIGHT/2]

def grid():
    for i in range(XMAX - XMIN + 1):
        pygame.draw.line(screen,CYAN,screenXY([XMIN+i,YMIN]),
                                    screenXY([XMIN+i,YMAX]),2)

    for i in range(YMAX - YMIN + 1):
         pygame.draw.line(screen, CYAN, screenXY([XMIN, YMIN+i]),
                                       screenXY([XMAX, YMIN+i]), 2)
    pygame.draw.line(screen, BLACK, screenXY([XMIN,0]),
                                    screenXY([XMAX,0]), 2)
    pygame.draw.line(screen, BLACK, screenXY([0,YMIN]),
                                    screenXY([0,YMAX]), 2)
def draw(f,color):
    for e in edges :
        pygame.draw.line(screen, color ,screenXY(f[e[0]]),
                                       screenXY(f[e[1]]),2)

def matMult(a,b):
    newmatrix = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            sum1 = 0
            for k in range(len(b)):
                sum1 += a[i][k] * b[k][j]
            row.append(sum1)
        newmatrix.append(row)
    return newmatrix

def rotate(rot,tilt):
    rotmatrix_Y = [[cos(rot),0,sin(rot)],
                   [0,1,0],
                 [-sin(rot),0,cos(rot)]]
    rotmatrix_X = [[1,0,0],
                   [0,cos(tilt),sin(tilt)],
                 [0,-sin(tilt),cos(tilt)]]
    return matMult(rotmatrix_Y,rotmatrix_X)

def collapse(point):
    screenx = ((point[0] - Xc) / (point[2] + Zc) * zoom) + Xc
    screeny = ((point[0] - Yc) / (point[2] + Zc) * zoom) + Xc
    return [screenXY([screenx,screeny])]

#setup display
pygame.init()
w,h = 600,600
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('Grafika Komputer')

done = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    key = pygame.key.get_pressed()
    dx = 0
    dy = 0
    if key[pygame.K_UP]:
        dy =+ 1/1000
    if key[pygame.K_DOWN]:
        dy =- 1/1000
    if key[pygame.K_RIGHT]:
        dx =+ 1/1000
    if key[pygame.K_LEFT]:
        dx =- 1/1000
    screen.fill(WHITE)

    screen_point = []
    for i in fmatrix:
        screen_point.append(collapse(i))

    #grid()
    fmatrix = matMult(fmatrix,rotate(dx,dy))
    draw(fmatrix,BLACK)

    pygame.display.update()

pygame.quit()
