import pygame as pg
from random import randint
pg.init()

#pygame variables
screen = pg.display.set_mode((800,600))
clock = pg.time.Clock()
font = pg.font.Font('freesansbold.ttf', 32)
moleImage = pg.image.load(r"mole.png")
hammerUp = pg.image.load(r"hammerNotClicked.png")
hammerDown = pg.image.load(r"hammerClicked.png")

startButton = pg.Rect(300,225,200,150)
difficultySlider = pg.Rect(500,550,200,30)
difficultyCursor = pg.Rect(500,540,50,50)

#game variables
previousClick = False
justClicked = False
moleTimer = 200
moleCooldown = 200
moleSize = 100
moles = []
white = (255,255,255)
black = (0,0,0)
inMainMenu = True
gameover = False
score = 0
text = font.render("Game Over", False, white)
text2 = font.render("Middle Click anywhere to close the game", False, white)
green = (0,255,0)
red = (255,0,0)
startGameText = font.render("Start Game", True, white)
DifficultyText = font.render("Difficulty", False, white)

#======================================================================================================
# Main Menu
while inMainMenu:
    #inputs
    pg.event.pump()
    mx, my = pg.mouse.get_pos()
    L, M, R = pg.mouse.get_pressed()
    
    #update
    if startButton.collidepoint((mx, my)) and L == True and previousClick == False:
        inMainMenu = False
    previousClick = L

    if difficultyCursor.collidepoint((mx, my)) and L and mx >= 500 and mx <= 700:
 
        difficultyCursor.x = mx - 25
        moleCooldown = 200 - (mx - 500)
        moleTimer = 200 - (mx - 500)

    #drawing
    screen.fill(black)
    pg.draw.rect(screen, green, startButton)
    screen.blit(startGameText, (312,277))
    screen.blit(DifficultyText, (525,500))
    pg.draw.rect(screen, white, difficultySlider)
    pg.draw.ellipse(screen, red, difficultyCursor)
    
    #clock
    pg.display.flip()
    clock.tick(60)

#======================================================================================================
# Game
while not gameover:

    #inputs
    pg.event.pump()

    L, M, R = pg.mouse.get_pressed()
    mousePos = pg.mouse.get_pos()
    mx, my = mousePos
    #this is insanely extra, but you get the idea
    justClicked = L and not previousClick

    for mole in moles:
        if mole.collidepoint(mousePos) and justClicked:
            moles.remove(mole)
            moleTimer -= 1
            score += 1
            break

    previousClick = L

    #updates
    if moleCooldown == 0:
        moleCooldown = moleTimer
        moles.append(pg.Rect(randint(0,screen.get_width()-moleSize),randint(0,screen.get_height()-moleSize), moleSize, moleSize))
    else:
        moleCooldown -= 1
    
    scoreText = font.render("score: " + str(score), True, white)
    
    #game logic
    if len(moles) > 5:
        gameover = True

    screen.fill(black)

    #drawing

    #I understand this is inefficient, but repeating this for loop makes it easier to understand 
    for mole in moles:
        #I'd rather teach getting attributes by name rather than by indexing, it's used nowhere else
        screen.blit(moleImage, (mole.x, mole.y))

    if L == False:
        screen.blit(hammerUp, (mx - 25, my - 25))
    else:
        screen.blit(hammerDown, (mx - 25, my - 25))
    
    screen.blit(scoreText, (0,0))

    #clock
    clock.tick(60)
    pg.display.flip()

#======================================================================================================
# Game Over

while True:
    pg.event.pump()

    L, M, R = pg.mouse.get_pressed()

    if M == True:
        break

    screen.fill(black)
    screen.blit(text, (300,200))
    screen.blit(text2, (80,250))
    pg.display.flip()