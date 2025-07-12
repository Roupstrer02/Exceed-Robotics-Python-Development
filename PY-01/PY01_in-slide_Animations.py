import pygame as pg

#PY01 - Class2
pg.init()
screen = pg.display.set_mode((800,800))
clock = pg.time.Clock()
myRect = pg.Rect(50,50,15,15)

black = (0,0,0)
green = (0,255,0)

font = pg.font.Font('freesansbold.ttf', 32)
Xdirection = 1
Ydirection = 1

while True:
    myRect.x += Xdirection
    myRect.y += Ydirection

    if myRect.x <= 0 or myRect.x >= 785:
        Xdirection = -Xdirection
    if myRect.y <= 0 or myRect.y >= 785:
        Ydirection = -Ydirection
    text = font.render("myRect.x = " + str(myRect.x), True, "white")
    text2 = font.render("myRect.y = " + str(myRect.y), True, "white")
    screen.fill(black)
    pg.draw.rect(screen, green, myRect)
    screen.blit(text, (0,0))
    screen.blit(text2, (0,32))
    pg.display.flip()
    clock.tick(60)