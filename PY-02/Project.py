import pygame as pg
import random as rd
platforms = []
heights = (100,200,300)
screen = pg.display.set_mode((1200,400))
clock = pg.time.Clock()

player = pg.Rect(50,100,50,50)

black = (0,0,0)
green = (0,255,0)
red = (255,0,0)

gameover = False

def addRandomPlatform():
    global platforms
    x = len(platforms * 300) + 300
    randindex = rd.randint(0,2)
    platforms.append(pg.Rect(x, heights[randindex], 100, 50))

def playerInputs():
    keys = pg.key.get_pressed()

    if keys[pg.K_w] == True:
        player.y = 100
    elif keys[pg.K_s] == True:
        player.y = 200
    elif keys[pg.K_x] == True:
        player.y = 300

def drawGame():
    screen.fill(black)
    pg.draw.rect(screen, green, player)
    for platform in platforms:
        pg.draw.rect(screen, red, platform)

def nextFrame():
    pg.display.flip()
    clock.tick(60)
# start of game =======================================================
pg.init()

for i in range(0,100):
    addRandomPlatform()

while not gameover:
    #inputs
    pg.event.pump()
    playerInputs()
    #game logic

    for platform in platforms:
        if player.colliderect(platform):
            gameover = True

    #updates
    for platform in platforms:
        platform.x -= 5
        if platform.x < -100:
            platforms.remove(platform)

    #drawing
    drawGame()

    #clock
    nextFrame()

