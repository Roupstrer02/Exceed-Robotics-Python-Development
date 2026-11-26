import pygame as pg
import random as rd

pg.init()
screen = pg.display.set_mode([800,800])
clock = pg.time.Clock()

def randomColour():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    colour = [r,g,b]
    return colour

black = [0,0,0]

r1 = pg.Rect(10,10,100,100)
r2 = pg.Rect(690,10,100,100)
r3 = pg.Rect(350,350,100,100)
r5 = pg.Rect(10,690,100,100)
r4 = pg.Rect(690,690,100,100)
colourTimer = 0
while True:
    pg.event.pump()
    screen.fill(black)
    mousePos = pg.mouse.get_pos()

    if colourTimer == 0:
        c1 = randomColour()
        c2 = randomColour()
        c3 = randomColour()
        c4 = randomColour()
        c5 = randomColour()
        colourTimer = 10

    if colourTimer != 0:
        colourTimer = colourTimer - 1

    r3.x = mousePos[0] - 50
    r3.y = mousePos[1] - 50

    pg.draw.rect(screen, c1, r1)
    pg.draw.rect(screen, c2, r2)
    pg.draw.rect(screen, c3, r3)
    pg.draw.rect(screen, c4, r4)
    pg.draw.rect(screen, c5, r5)
    pg.display.flip()
    clock.tick(60)