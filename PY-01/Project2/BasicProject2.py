import pygame as pg
from random import randint
pg.init()

#pygame variables
screen = pg.display.set_mode((800,600))
clock = pg.time.Clock()
font = pg.font.Font('freesansbold.ttf', 32)
moleImage = pg.image.load(r"mole.png")
hammer = pg.image.load(r"hammerNotClicked.png")

#game variables
previousClick = False
justClicked = False
moleTimer = 60
moleCooldown = 60
moleSize = 100
moles = []
white = (255,255,255)
black = (0,0,0)
score = 0

#======================================================================================================
# Game
while True:

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
        # Game Over
        print("Final score: " + str(score))
        break


    #drawing
    screen.fill(black)

    #I understand this is inefficient, but repeating this for loop makes it easier to understand 
    for mole in moles:
        #I'd rather teach getting attributes by name rather than by indexing, it's used nowhere else
        screen.blit(moleImage, (mole.x, mole.y))
    screen.blit(hammer, (mx - 25, my - 25))
    screen.blit(scoreText, (0,0))

    #clock
    clock.tick(60)
    pg.display.flip()