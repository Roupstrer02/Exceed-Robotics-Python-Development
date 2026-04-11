import pygame as pg
import random as rd

pg.init()

screen = pg.display.set_mode((1200,600))
clock = pg.time.Clock()
state = 2

player = pg.Rect(50,550,50,50)

platforms = []

camera = (0,0)

def mainMenu():
    global state


def game():
    global state

    #INPUTS
    pg.event.pump()
    keys = pg.key.get_pressed()

    #GAME LOGIC
    

    #UPDATES


    #DRAWING
    screen.fill('black')
    pg.draw.rect(screen, 'red', player)
    pg.display.flip()
    clock.tick(60)
    #UPDATE


def endScreen():
    global state







while True:
    if state == 1:
        mainMenu()
    elif state == 2:
        game()
    elif state == 3:
        endScreen()
