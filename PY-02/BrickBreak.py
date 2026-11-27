import pygame as pg
import random as rd

pg.init()
pg.mixer.init()

screen = pg.display.set_mode((800,600))
clock = pg.time.Clock()

state = "Main Menu"

font = pg.font.Font(None, 40)

#colours
black = [0,0,0]
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
aqua = [100,100,255]
yellow = [255,255,0]
purple = [255,0,255]
teal = [0,255,255]
white = [255,255,255]

#Main Menu global vars
startButton = pg.Rect(300,200,200,75)
startButtonText = font.render("Start Game", True, white)

player = pg.Rect(325,500,150,25)
playerspeed = 8

ball = pg.Rect(395,470,10,10)
ballXSpeed = 5
ballYSpeed = 5


#Game global vars
bricks = []
for i in range(10):
    for j in range(3):
        bricks.append(pg.Rect(80*i+1, 50*j+1, 78, 48))

player = pg.Rect(325,500,150,25)

#GameOver global vars
<<<<<<< Updated upstream
def control():
    keys = pg.key.get_pressed()

    if keys[pg.K_a] == True:
        player.x -= playerspeed
    if keys[pg.K_d] == True:
        player.x += playerspeed

def drawEverything():
=======

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

    #game logic
    if keys[pg.K_a]:
        player.x -= 10
    if keys[pg.K_d]:
        player.x += 10

    #drawing
>>>>>>> Stashed changes
    screen.fill(black)

    for brick in bricks:
        pg.draw.rect(screen, red, brick)
<<<<<<< Updated upstream
    
    pg.draw.rect(screen, green, player)
    pg.draw.rect(screen, aqua, ball)
    pg.display.flip()

=======

    pg.draw.rect(screen, green, player)
    pg.display.flip()

def GameOver():
    pass

>>>>>>> Stashed changes
while True:
    #player inputs
    pg.event.pump()
    control()

    #game logic
    if player.colliderect(ball):
        ballYSpeed = -ballYSpeed

    for r in bricks:
        if ball.colliderect(r):
            bricks.remove(r)

    if ball.x < -10 or ball.x > 800:
        ballXSpeed = -ballXSpeed

    if ball.y < -10:
        ballYSpeed = -ballYSpeed

    #updates
    ball.x += ballXSpeed
    ball.y += ballYSpeed

    #drawing
    drawEverything()



    clock.tick(60)