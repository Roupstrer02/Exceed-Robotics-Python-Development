import pygame as pg

#PY01 - Class2
pg.init()
screen = pg.display.set_mode((800,400))
clock = pg.time.Clock()
myRect = pg.Rect(50,100,150,200)
black = (0,0,0)
green = (0,255,0)
Xdirection = 1
while True:
    myRect.x += Xdirection
    if myRect.x <= 0 or myRect.x >= 650:
        Xdirection = -Xdirection
    screen.fill(black)
    pg.draw.rect(screen, green, myRect)
    pg.display.flip()
    clock.tick(60)