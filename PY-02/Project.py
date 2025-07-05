"""

Perhaps we focus more on making a game look much more professional:
- tilemap (grid of Rect objects, )
- animations
- music
- main menu
- basic options settings as bonus?

Project: Basic Role Playing Game?
"""

#The project here is only a feasability test

import pygame as pg

pg.init()

screen  = pg.display.set_mode((1200,800))
clock = pg.time.Clock()

playerSize = 100
player = pg.Rect(550, 350, playerSize, playerSize)
speed = 5

while True:
    pg.event.pump()

    keys = pg.key.get_pressed()

    if keys[pg.K_w] == True:
        player.y -= speed
    if keys[pg.K_a] == True:
        player.x -= speed
    if keys[pg.K_s] == True:
        player.y += speed
    if keys[pg.K_d] == True:
        player.x += speed
    


    screen.fill("black")
    pg.draw.rect(screen, "white", player)
    pg.display.flip()
    clock.tick(60)

