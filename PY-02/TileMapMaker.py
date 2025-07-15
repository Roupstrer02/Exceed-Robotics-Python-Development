import pygame as pg
"""
TileMapMaker.py

This tool helps create a tile map for any projects students may want to make.
The tool explains to the user how to use it every step of the way

features:
    1) user inputs:
        - screen width
        - screen height
        - tile size

    2) tool outputs to:
        - console/terminal
        - file ("output.txt" in same directory)

    3) can modify already made maps by editing the 'tileMap' variable
    
Created July 2025
Roupen Kaloustian
"""


#if you want to modify an existing map, input your list of Rect objects here
# ====================================================================================================
tileMap = []
# ====================================================================================================






# functions ==========================================================================
digits = ['0','1','2','3','4','5','6','7','8','9']
def isValidDigit(input_str):

    if input_str == "":
        return True
    for letter in input_str:
        if letter not in digits:
            return False
    x = int(input_str)
    return x > 0

def PrintRetryInstructions():
    print("===============================================================")
    print("invalid width: please enter an integer number greater than 0")
    print()

def getScreenSizeFromUser():
    screen_x = input("Input the width of your screen (press ENTER for standard size of 1000): ")

    while isValidDigit(screen_x) == False:
        PrintRetryInstructions()
        screen_x = input("Input the width of your screen (press ENTER for standard size of 1000): ")

    screen_y = input("Input the height of your screen (press ENTER for standard size of 1000): ")

    while isValidDigit(screen_y) == False:
        PrintRetryInstructions()
        screen_y = input("Input the height of your screen (press ENTER for standard size of 1000): ")

    if screen_x != "":
        screen_x = int(screen_x)
    else:
        screen_x = 1000
    if screen_y != "":
        screen_y = int(screen_y)
    else:
        screen_y = 1000
    size = (screen_x, screen_y)
    
    tileSize = input("Input the size of each tile (press ENTER for standard size of 20): ")

    while isValidDigit(tileSize) == False:
        PrintRetryInstructions()
        tileSize = input("Input the size of each tile (press ENTER for standard size of 20): ")

    print("screen size: " + str(size))
    
    if tileSize != "":
        tileSize = int(tileSize)
    else:
        tileSize = 20

    return size, tileSize

def printTileMap(tileMap):
    tileMapString = ""
    for tile in tileMap:
        tileMapString += f"pg.Rect({tile.x},{tile.y},{tile.w},{tile.h}),"
    
    tileMapString = "[" + tileMapString[:-1] + "]"

    with open("output.txt", 'w+') as f:
        f.write(tileMapString)

    print("=========================================================================")
    print(tileMapString)
    print("=========================================================================")
# tool ===============================================================================

pg.init()
user_input = getScreenSizeFromUser()
screensize = user_input[0]
screen = pg.display.set_mode(screensize)
clk = pg.time.Clock()
font = pg.font.Font('freesansbold.ttf', 30)

TutorialText1 = font.render("Hold left-click to add tiles to the maze", True, "white")
TutorialText2 = font.render("Hold right-click to remove tiles to the maze", True, "white")
TutorialText3 = font.render("Press ENTER to exit", True, "white")
TutorialText4 = font.render("You'll see your map written in the terminal and in the output.txt file", True, "white")

tileSize = user_input[1]
Done = False

while not Done:
    pg.event.pump()

    mx, my = pg.mouse.get_pos()
    L, M, R = pg.mouse.get_pressed()
    keys = pg.key.get_pressed()

    tileSelectedX = int(mx // tileSize)
    tileSelectedY = int(my // tileSize)
    if L or R:
        newRect = pg.Rect(tileSelectedX * tileSize, tileSelectedY * tileSize, tileSize, tileSize)
        if L and newRect not in tileMap:
            tileMap.append(newRect)
        elif R and newRect in tileMap:
            tileMap.remove(newRect)
    
    if keys[pg.K_RETURN]:
        printTileMap(tileMap)    
        break

    # drawing
    screen.fill("black")
    if len(tileMap) > 0:
        for tile in tileMap:
            pg.draw.rect(screen, "green", tile)
    else:
        screen.blit(TutorialText1, (0,0))
        screen.blit(TutorialText2, (0,32))
        screen.blit(TutorialText3, (0,96))
        screen.blit(TutorialText4, (0,128))
    pg.display.flip()
    clk.tick(60)



