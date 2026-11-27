import pygame as pg
import random as rd

#Obviously the contents of this function could be rewritten as: return [rd.randint(0,255), rd.randint(0,255), rd.randint(0,255)]
#Both answers are fine.
def getRandomColour():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    
    newColour = [r,g,b]
    
    return newColour

pg.init()
screen = pg.display.set_mode([800,800])
clock = pg.time.Clock()

black = [0,0,0]
r1 = pg.Rect(20,20,100,100)
r2 = pg.Rect(680,20,100,100)
r3 = pg.Rect(20,680,100,100)
r4 = pg.Rect(680,680,100,100)
r5 = pg.Rect(350,350,100,100)

while True:
    screen.fill(black)
    pg.draw.rect(screen, getRandomColour(), r1)
    pg.draw.rect(screen, getRandomColour(), r2)
    pg.draw.rect(screen, getRandomColour(), r3)
    pg.draw.rect(screen, getRandomColour(), r4)
    pg.draw.rect(screen, getRandomColour(), r5)
    pg.display.flip()
    clock.tick(3)