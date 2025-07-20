import pygame as pg

# if you want to modify an existing map, input your list of Rect objects here
# if the list beliw is empty, the tool will check the "save.txt" file for the previously saved map
# ====================================================================================================
tileMap = []
# ====================================================================================================

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

def isValidTileSize(input_str, screenX, screenY):
    if input_str == "":
        return True
    if isValidDigit(input_str):
        potentialTileSize = int(input_str)
        return screenX % potentialTileSize == 0 and screenY % potentialTileSize == 0

def PrintRetryInstructions():
    print("===============================================================")
    print("invalid value:")
    print("please enter an integer number greater than 0")

def getDefaultTileSize(x, y):
    DTS = 1
    for i in range(1, max(x//12,y//12)+1):
        if x % i == 0 and y % i == 0:
            DTS = i

    return DTS

def getUserInputs():
    screen_x = input("Input the width of your screen (press ENTER for standard size of 1000): ")

    while isValidDigit(screen_x) == False:
        PrintRetryInstructions()
        print()
        screen_x = input("Input the width of your screen (press ENTER for standard size of 1000): ")

    screen_y = input("Input the height of your screen (press ENTER for standard size of 1000): ")

    while isValidDigit(screen_y) == False:
        PrintRetryInstructions()
        print()
        screen_y = input("Input the height of your screen (press ENTER for standard size of 1000): ")

    if screen_x != "":
        screen_x = int(screen_x)
    else:
        screen_x = 1000
    if screen_y != "":
        screen_y = int(screen_y)
    else:
        screen_y = 1000
    size = (screen_x, screen_y + 30)

    defaultTileSize = getDefaultTileSize(screen_x, screen_y)
    tileSize = input(f"Input the size of each tile (press ENTER for standard size of {defaultTileSize}): ")

    while isValidTileSize(tileSize, screen_x, screen_y) == False:
        PrintRetryInstructions()
        print(f"which divides both {screen_x} and {screen_y} with no remainder")
        tileSize = input(f"Input the size of each tile (press ENTER for standard size of {defaultTileSize}): ")

    print("screen size: " + str(size))

    if tileSize != "":
        tileSize = int(tileSize)
    else:
        tileSize = getDefaultTileSize(screen_x, screen_y)

    print("tile size: " + str(tileSize))

    return size, tileSize

def getCompressedTileMap(tileMap):
    global tileSize, screen
    screen_x = screen.get_width()
    screen_y = screen.get_height()
    # empty matrix
    RectMatrix = [[None for _ in range(0,screen_x // tileSize)] for _ in range(0,screen_y//tileSize)]
    compressedRectList = []
    # matrix of individual tiles
    for tile in tileMap:
        RectMatrix[int((tile.y)//tileSize)][int((tile.x)//tileSize)] = pg.Rect(tile.x, tile.y, tile.w, tile.h)

    # matrix of compressed rows
    for row in RectMatrix:
        compressions = 0
        for i in range(0,len(row)-1):
            index = i-compressions
            if row[index] is not None and row[index+1] is not None:
                 row[index].w += row[index+1].w
                 row.remove(row[index+1])
                 compressions += 1

    for row in RectMatrix:
        for rect in row:
            if rect is not None:
                compressedRectList.append(rect)

    return compressedRectList

def printTileMap(tileMap):
    C_TM = getCompressedTileMap(tileMap)

    tileMapString = ""
    C_TMString = ""
    for tile in tileMap:
        tileMapString += f"pg.Rect({tile.x},{tile.y},{tile.w},{tile.h}),"

    tileMapString = "[" + tileMapString[:-1] + "]"

    for rect in C_TM:
        C_TMString += f"pg.Rect({rect.x},{rect.y},{rect.w},{rect.h}),"

    C_TMString = "[" + C_TMString[:-1] + "]"

    with open("output.txt", 'w+') as f:
        f.write("compressed tile map (Use this in your game):\n\n")
        f.write(C_TMString + '\n\n')
        f.write("======================================================================\n\n")
        f.write("raw tile map (use this if you want to use the tool to modify your map again):\n\n")
        f.write(tileMapString)

    with open("save.txt", 'w+') as f:
        for tile in tileMap:
            f.write(f"{tile.x} {tile.y} {tile.w} {tile.h}\n")
    print("=========================================================================\n")
    print("compressed tile map (Use this in your game):\n")
    print(C_TMString + "\n")
    print("raw tile map (use this if you want to use the tool to modify your map again):\n")
    print(tileMapString + '\n')
    print("=========================================================================\n")

def getSavedMap():
    global tileMap
    if tileMap != []:
        return
    with open("save.txt", "r") as f:
        print("getting saved map...")
        while True:
            line = f.readline()
            line = line.strip('\n')
            line = line.split(' ')
            if len(line) > 1:
                tileMap.append(pg.Rect(int(line[0]), int(line[1]), int(line[2]), int(line[3])))
            else:
                print("Done!")
                break

# tool ===============================================================================
pg.init()

user_input = getUserInputs()
screensize = user_input[0]
screen = pg.display.set_mode(screensize)
clk = pg.time.Clock()
font = pg.font.Font('freesansbold.ttf', screensize[0] // 35)

getSavedMap()

TutorialText1 = font.render("Hold left-click to add tiles to the maze", True, "white")
TutorialText2 = font.render("Hold right-click to remove tiles to the maze", True, "white")
TutorialText3 = font.render("You'll see your map written in the terminal and in the output.txt file", True, "white")
TutorialTextBottom = font.render("Press ENTER to exit", True, "black")
tileSize = user_input[1]
Done = False

while not Done:
    # inputs
    pg.event.pump()

    mx, my = pg.mouse.get_pos()
    L, M, R = pg.mouse.get_pressed()
    keys = pg.key.get_pressed()

    tileSelectedX = int(mx // tileSize)
    tileSelectedY = int(my // tileSize)

    #logic
    if L or R:
        newRect = pg.Rect(tileSelectedX * tileSize, tileSelectedY * tileSize, tileSize, tileSize)
        if L and newRect not in tileMap and mx < screen.get_width() and my < screen.get_height():
            tileMap.append(newRect)
        elif R:
            if newRect in tileMap:
                tileMap.remove(newRect)
            else:
                for tile in tileMap:
                    if tile.collidepoint((mx, my)):
                        tileMap.remove(tile)

    if keys[pg.K_RETURN]:
        getCompressedTileMap(tileMap)
        printTileMap(tileMap)
        pg.quit()
        break

    # drawing
    screen.fill("black")
    pg.draw.rect(screen, "yellow", (0, screen.get_height() - 30, screensize[0], 30))
    screen.blit(TutorialTextBottom, (0,screen.get_height()-30))
    if len(tileMap) > 0:
        for tile in tileMap:
            if tile.w == tileSize and tile.h == tileSize:
                pg.draw.rect(screen, "blue", tile)
            else:
                pg.draw.rect(screen, "orange", tile)
    else:
        screen.blit(TutorialText1, (0,0))
        screen.blit(TutorialText2, (0,32))
        screen.blit(TutorialText3, (0,96))

    pg.display.flip()
    clk.tick(60)



