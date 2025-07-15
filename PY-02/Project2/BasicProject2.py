import pygame as pg

#the essentials
pg.init()
screen = pg.display.set_mode((1000,1000))
clock = pg.time.Clock()
font = pg.font.Font('freesansbold.ttf', 32)

#vars used everywhere
black = (0,0,0)
lightblue = (150,180,255)
green = (0,255,0)
red = (255,0,0)
white = (0,0,0)

state = 0

#vars for main menu
startGameButton = pg.Rect(400,450,200,100)
startGameText = font.render("Start Game", True, white)

#vars for main game
maze = [
    pg.Rect(0,0,50,1000),
    pg.Rect(0,0,1000,50),
    pg.Rect(950,0,50,1000),
    pg.Rect(0,950,1000,50),
    pg.Rect(0,950,1000,50)
    ]

def mainMenu():
    # global vars
    global state

    # inputs
    pg.event.pump()
    mousePos = pg.mouse.get_pos()
    L, M, R = pg.mouse.get_pressed()

    # logic
    if L == True and startGameButton.collidepoint(mousePos):
        state = 1

    # drawing
    screen.fill(black)
    pg.draw.rect(screen, green, startGameButton)
    screen.blit(startGameText, (412,484))
    
    #clock
    pg.display.flip()
    clock.tick(60)

def playGame():
    # global vars
    global state

    # inputs
    pg.event.pump()
    keys = pg.key.get_pressed()
    
    # logic
    if keys[pg.K_ESCAPE]:
        state = 3
    
    # drawing
    screen.fill(black)
    for wall in maze:
        pg.draw.rect(screen, lightblue, wall)
    # clock
    pg.display.flip()
    clock.tick(60)

def gameOver():
    global state
    pass

while True:
    if state == 0:
        mainMenu()
    elif state == 1:
        playGame()
    elif state == 2:
        gameOver()
    else:
        break