import pygame as pg
import random as rd

pg.init()
screen = pg.display.set_mode([800,800])
clock = pg.time.Clock()

black = [0,0,0]
green = [0,255,0]

def rectRow(y, w, h, numberOfRects):
    rects = []
    for i in range(numberOfRects):
        newRect = pg.Rect(w*i, y, w, h)
        rects.append(newRect)
    return rects

def drawRectRow(RectList, colour):
    Tgreen = [0,255,0]
    for i in range(len(RectList)):
        pg.draw.rect(screen, Tgreen, RectList[i], 10)
        Tgreen[1] -= 30
        Tgreen[0] += 30

r1 = rectRow(3, 100, 50, 8)

while True:

    screen.fill(black)
    drawRectRow(r1, green)
    pg.display.flip()