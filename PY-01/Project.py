import pygame as pg
from random import randint
pg.init()

#pygame variables
screen = pg.display.set_mode((800,600))
clock = pg.time.Clock()
font = pg.font.Font('freesansbold.ttf', 32)
text = font.render("Game Over", False, "white")
text2 = font.render("Click anywhere to close the game", False, "white")
moleImage = pg.image.load(r"mole.png")
hammerUp = pg.image.load(r"hammerNotClicked.png")
hammerDown = pg.image.load(r"hammerClicked.png")

#game variables
previousClick = False
justClicked = False
moleDelay = 60
moleCooldown = 60
moleSize = 100
moles = []
gameover = False
while not gameover:

    #input processing
    pg.event.pump()

    L, M, R = pg.mouse.get_pressed()
    mousePos = pg.mouse.get_pos()
    mx, my = mousePos
    #this is insanely extra, but you get the idea
    justClicked = L and not previousClick

    for mole in moles:
        if mole.collidepoint(mousePos) and justClicked:
            moles.remove(mole)
            moleDelay -= 1

    previousClick = L

    #continuous game events
    if moleCooldown == 0:
        moleCooldown = moleDelay
        moles.append(pg.Rect(randint(0,screen.get_width()-moleSize),randint(0,screen.get_height()-moleSize), moleSize, moleSize))
    else:
        moleCooldown -= 1

    #general logic
    if len(moles) > 5:
        gameover = True

    screen.fill("black")

    #I understand this is inefficient, but repeating this for loop makes it easier to understand 
    for mole in moles:

        #I'd rather teach getting attributes by name rather than by indexing, it's used nowhere else
        screen.blit(moleImage, (mole.x, mole.y))

    # >>> BONUS <<< #
    if L == False:
        screen.blit(hammerUp, (mx - 25, my - 25))
    else:
        screen.blit(hammerDown, (mx - 25, my - 25))
    

    clock.tick(60)
    pg.display.flip()

while True:
    pg.event.pump()

    L, M, R = pg.mouse.get_pressed()

    if L == True:
        break

    screen.fill("black")
    screen.blit(text, (300,200))
    screen.blit(text2, (135,250))
    pg.display.flip()
