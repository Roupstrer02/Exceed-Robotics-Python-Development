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
for i in range(10):
    for j in range(3):
        bricks.append(pg.Rect(80*i+1, 50*j+1, 78, 48))

#GameOver global vars

def MainMenu():
    global state
    #inputs
    mousePos = pg.mouse.get_pos()
    L, M, R = pg.mouse.get_pressed()

    if startButton.collidepoint(mousePos) and L == True:
        state = "Game"

    #drawing
    screen.fill(black)
    pg.draw.rect(screen, green, startButton)
    screen.blit(startButtonText, (325,225))
    pg.display.flip()


def Game():
    global bricks

    #inputs
    keys = pg.key.get_pressed()

    #drawing
    screen.fill(black)
    for brick in bricks:
        pg.draw.rect(screen, red, brick)
    pg.display.flip()

def GameOver():
    pass


while True:
    pg.event.pump()

    if state == "Main Menu":
        MainMenu()

    if state == "Game":
        Game()

    if state == "Game Over":
        GameOver()

    clock.tick(60)