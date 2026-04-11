import pygame as pg
import random as rd

pg.init()

#======================================================
# Class definitions

class platform:
    def __init__(self, platformType, x, y):
        self.hitbox = pg.Rect(x,y,PLATFORMWIDTH, PLATFORMHEIGHT)
        self.pT = platformType
        if self.pT == "normal":
            self.colour = "gray"
        elif self.pT == "water":
            self.colour = "blue"
        elif self.pT == "lava":
            self.colour = "orange"


    def checkCollisions(self, otherObject):
        global gravity
        if self.hitbox.colliderect(otherObject):
            if self.pT == "normal":
                otherObject.bottom = self.hitbox.top
                gravity = 0

    def draw(self):
        pg.draw.rect(screen, self.colour, self.hitbox)
#====================================================
# Global Variables
screen = pg.display.set_mode((1200,600))
clock = pg.time.Clock()
state = 2

player = pg.Rect(50,550,50,50)
PLAYERSPEED = 7
PLAYERJUMPHEIGHT = 20
gravity = 0
isJumping = False


PLATFORMWIDTH = 200
PLATFORMHEIGHT = 50

camera = (0,0)

platforms = [platform("normal", 200, 400)]
#======================================================
# Main Menu Functions

def mainMenu():
    global state

#======================================================
# Main Game Functions

def addPlatform():
    platforms.append()

def keyboardInputs():
    pg.event.pump()
    k = pg.key.get_pressed()
    return k

def gameLogic(inputs):
    global gravity, isJumping
    if inputs[pg.K_d]:
        player.x += PLAYERSPEED
    if inputs[pg.K_a]:
        player.x -= PLAYERSPEED
    if inputs[pg.K_w] and isJumping == False:
        gravity = -PLAYERJUMPHEIGHT
        isJumping = True

    if player.y > 550:
        player.y = 550
        gravity = 0
        isJumping = False

    for p in platforms:
        p.checkCollisions(player)

def updates():
    global gravity
    player.y += gravity
    gravity += 1

def drawing():
    screen.fill("black")
    for p in platforms:
        p.draw()
    pg.draw.rect(screen, 'red', player)

def game():
    global state

    #INPUTS
    keys = keyboardInputs()

    #GAME LOGIC
    gameLogic(keys)

    #UPDATES
    updates()

    #DRAWING
    drawing()

    #UPDATE
    pg.display.flip()
    clock.tick(60)

#======================================================
# End Screen Functions

def endScreen():
    global state







while True:
    if state == 1:
        mainMenu()
    elif state == 2:
        game()
    elif state == 3:
        endScreen()
