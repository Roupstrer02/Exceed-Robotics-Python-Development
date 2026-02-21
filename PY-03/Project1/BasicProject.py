import pygame as pg
import random as rd
pg.init()

s_size = (1000,1000)
screen = pg.display.set_mode(s_size)

red = (255,0,0)

laserList = []

def drawLasers():
    for laser in laserList:
        pg.draw.rect(screen, red, laser)

class invader:

    def __init__(self, x, y):
        self.hitbox = pg.Rect(x, y, 80, 80)


    def draw(self):
        for part in self.hitbox:
            pg.draw.rect(screen, self.colour, part)
    

    def shoot(self):
        laserList.append(pg.Rect(self.x + 35, self.y + 80, 10, 60))
    


a = invader(450,450)
while True:
    pg.event.pump()

    a.draw()

    pg.display.flip()
