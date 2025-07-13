import pygame as pg

pg.init()

screen  = pg.display.set_mode((1200,800))
clock = pg.time.Clock()

playerSize = 100
player = pg.Rect(550, 350, playerSize, playerSize)
speed = 5

while True:
    pg.event.pump()

    pg.display.flip()
    clock.tick(60)

