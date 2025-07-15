import pygame as pg
import random as rd

pg.init()
screen = pg.display.set_mode((1200,400))

heights = (100,200,300)
platforms = []
clock = pg.time.Clock()

player = pg.Rect(50,100,50,50)

black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
white = (255,255,255)

gameover = False

rocketImg = pg.image.load(r"Rocket.png")
rocketSpeed = 5
score = 0
font = pg.font.Font('freesansbold.ttf', 32)

def addRandomPlatform():
    global platforms
    x = len(platforms * 300) + 500
    randindex = rd.randint(0,2)
    platforms.append(pg.Rect(x, heights[randindex], 100, 50))

def playerInputs():
    keys = pg.key.get_pressed()

    if keys[pg.K_w] == True:
        player.y = heights[0]
    elif keys[pg.K_s] == True:
        player.y = heights[1]
    elif keys[pg.K_x] == True:
        player.y = heights[2]

def drawGame():
    screen.fill(black)
    pg.draw.rect(screen, green, player)
    for platform in platforms:
        screen.blit(rocketImg, (platform.x, platform.y))
    
    scoreText = font.render("score: " + str(score), True, (white))
    screen.blit(scoreText, (0,0))

def nextFrame():
    pg.display.flip()
    clock.tick(60)

# start of game =======================================================

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
        platform.x -= rocketSpeed
        if platform.x < -100:
            platforms.remove(platform)
            rocketSpeed += 1
            score += 1

    

    #drawing
    drawGame()

    #clock
    nextFrame()

