import pygame as pg
import random as rd

pg.init()
pg.mixer.init()

screen = pg.display.set_mode((800,600))
clock = pg.time.Clock()

state = "Main Menu"

font = pg.font.Font(None, 40)

#colours
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
purple = (255,0,255)
teal = (0,255,255)
white = (255,255,255)

#Main Menu global vars
startButton = pg.Rect(300,200,200,75)
startButtonText = font.render("Start Game", True, white)

#Game global vars
bricks = []

def makeRowOfBricks(y):
    for i in range(10):
        bricks.append(pg.Rect(80*i+1, y, 78, 48))

def makeGridOfBricks(rowCount):
    for j in range(rowCount):
        makeRowOfBricks(50*j)

makeGridOfBricks(5)

player = pg.Rect(325,500,150,25)

#GameOver global vars

while True:
    pg.event.pump()

    #inputs
    keys = pg.key.get_pressed()

    #game logic
    if keys[pg.K_a]:
        player.x -= 10
    if keys[pg.K_d]:
        player.x += 10

    #drawing
    screen.fill(black)
    for brick in bricks:
        pg.draw.rect(screen, red, brick)

    pg.draw.rect(screen, green, player)
    pg.display.flip()
    clock.tick(60)