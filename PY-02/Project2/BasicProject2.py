import pygame as pg

#the essentials
pg.init()
screensize = (1050,1050)
screen = pg.display.set_mode(screensize)
clock = pg.time.Clock()
font = pg.font.Font('freesansbold.ttf', 32)

#vars used everywhere
black = (0,0,0)
lightblue = (150,180,255)
green = (0,255,0)
red = (255,0,0)
white = (255,255,255)
yellow = (255,255,0)

state = 2

#vars for main menu
startGameButton = pg.Rect(400,450,200,100)
startGameText = font.render("Start Game", True, white)

#vars for main game
maze = [pg.Rect(0,0,500,50),pg.Rect(550,0,500,50),pg.Rect(0,50,50,50),pg.Rect(450,50,50,50),pg.Rect(550,50,50,50),pg.Rect(1000,50,50,50),pg.Rect(0,100,50,50),pg.Rect(100,100,50,50),pg.Rect(200,100,100,50),pg.Rect(350,100,50,50),pg.Rect(450,100,50,50),pg.Rect(550,100,50,50),pg.Rect(650,100,50,50),pg.Rect(750,100,100,50),pg.Rect(900,100,50,50),pg.Rect(1000,100,50,50),pg.Rect(0,150,50,50),pg.Rect(100,150,50,50),pg.Rect(200,150,100,50),pg.Rect(350,150,50,50),pg.Rect(650,150,50,50),pg.Rect(750,150,100,50),pg.Rect(900,150,50,50),pg.Rect(1000,150,50,50),pg.Rect(0,200,50,50),pg.Rect(1000,200,50,50),pg.Rect(0,250,100,50),pg.Rect(150,250,750,50),pg.Rect(950,250,100,50),pg.Rect(0,300,100,50),pg.Rect(950,300,100,50),pg.Rect(0,350,100,50),pg.Rect(150,350,350,50),pg.Rect(550,350,350,50),pg.Rect(950,350,100,50),pg.Rect(0,400,100,50),pg.Rect(150,400,50,50),pg.Rect(450,400,50,50),pg.Rect(550,400,50,50),pg.Rect(850,400,50,50),pg.Rect(950,400,100,50),pg.Rect(0,450,100,50),pg.Rect(150,450,50,50),pg.Rect(250,450,250,50),pg.Rect(550,450,250,50),pg.Rect(850,450,50,50),pg.Rect(950,450,100,50),pg.Rect(150,500,50,50),pg.Rect(0,550,100,50),pg.Rect(150,550,50,50),pg.Rect(250,550,250,50),pg.Rect(550,550,250,50),pg.Rect(850,550,50,50),pg.Rect(950,550,100,50),pg.Rect(0,600,100,50),pg.Rect(150,600,50,50),pg.Rect(450,600,50,50),pg.Rect(550,600,50,50),pg.Rect(850,600,50,50),pg.Rect(950,600,100,50),pg.Rect(0,650,100,50),pg.Rect(150,650,350,50),pg.Rect(550,650,350,50),pg.Rect(950,650,100,50),pg.Rect(0,700,100,50),pg.Rect(950,700,100,50),pg.Rect(0,750,300,50),pg.Rect(350,750,150,50),pg.Rect(550,750,150,50),pg.Rect(750,750,300,50),pg.Rect(0,800,100,50),pg.Rect(250,800,50,50),pg.Rect(350,800,150,50),pg.Rect(550,800,150,50),pg.Rect(750,800,50,50),pg.Rect(950,800,100,50),pg.Rect(0,850,100,50),pg.Rect(150,850,150,50),pg.Rect(350,850,150,50),pg.Rect(550,850,150,50),pg.Rect(750,850,150,50),pg.Rect(950,850,100,50),pg.Rect(0,900,100,50),pg.Rect(350,900,150,50),pg.Rect(550,900,150,50),pg.Rect(950,900,100,50),pg.Rect(0,950,500,50),pg.Rect(550,950,500,50),pg.Rect(0,1000,500,50),pg.Rect(550,1000,500,50)]
collectables = [pg.Rect(60,60,30,30), pg.Rect(960,60,30,30), pg.Rect(510,510,30,30), pg.Rect(810,810,30,30), pg.Rect(210,810,30,30)]
player = pg.Rect(500,0,50,50)
playerSpeed = 5
coinsCollected = 0

#vars for game over
gameOverText1 = font.render("Congratulations!", True, white)
gameOverText2 = font.render("Press 'Esc' to exit the game", True, white)

def isPlayerHittingWall():
    global maze, player
    for wall in maze:
        if player.colliderect(wall):
            return True
    return False

def collectCoins():
    global collectables, coinsCollected, player
    for coin in collectables:
        if player.colliderect(coin):
            collectables.remove(coin)
            coinsCollected += 1
            break

def checkForGameOver():
    global collectables, state
    if len(collectables) == 0:
        state = 2

def movePlayer():
    global player
    keys = pg.key.get_pressed()

    if keys[pg.K_w] == True:
        player.y -= playerSpeed
        if isPlayerHittingWall():
            player.y += playerSpeed

    if keys[pg.K_a] == True:
        player.x -= playerSpeed
        if isPlayerHittingWall():
            player.x += playerSpeed

    if keys[pg.K_s] == True:
        player.y += playerSpeed
        if isPlayerHittingWall():
            player.y -= playerSpeed

    if keys[pg.K_d] == True:
        player.x += playerSpeed
        if isPlayerHittingWall():
            player.x -= playerSpeed

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

    # inputs ===============================================================
    pg.event.pump()
    keys = pg.key.get_pressed()
    
    # logic ================================================================
    collectCoins()
    checkForGameOver()
    
    # updates ==============================================================
    movePlayer()
    text = font.render("coins: " + str(coinsCollected), True, black)
    # drawing ==============================================================
    screen.fill(black)
    for wall in maze:
        pg.draw.rect(screen, lightblue, wall)
    
    for coin in collectables:
        pg.draw.rect(screen, yellow, coin)
    
    pg.draw.rect(screen, green, player)
    screen.blit(text, (0,5))

    # clock ==============================================================
    pg.display.flip()
    clock.tick(60)

def gameOver():
    global state
    pg.event.pump()
    keys = pg.key.get_pressed()

    if keys[pg.K_ESCAPE] == True:
        exit()
    
    screen.blit(gameOverText1, (375,400))
    screen.blit(gameOverText2, (300,440))
    pg.display.flip()

while True:
    if state == 0:
        mainMenu()
    elif state == 1:
        playGame()
    elif state == 2:
        gameOver()
    else:
        break


# possible bonuses (second opinion first):
# - "Game Over" can loops back to main menu instead of closing
# - enemies that move in a pattern that make you instantly lose
# - animations in the Main Menu and Game Over menus
# - going outside the boundaries loops your character to the other side