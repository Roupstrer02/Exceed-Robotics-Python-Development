#===============================================================================
# Class8:
# Roupen Kaloustian
# July 2025
#===============================================================================

#===============================================================================
# Basic individual task:
# Treasure Hunting Game
#===============================================================================

ocean = [['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~']]
row = 2
column = 2

treasureRow = 4
treasureColumn = 4


movesLeft = 10
while True:

    ocean[row][column] = 'X'

    # DO NOT REUSE THE NAME "row" FOR THIS VARIABLE
    for mapRow in ocean:
        print(mapRow)
    print("your current position is:")
    print("row: " + str(row))
    print("column: " + str(column))
    print("moves left: " + str(movesLeft))
    Movement = input("Where do you want to go? ")

    ocean[row][column] = '~'

    if Movement == "w":
        column = column - 1
    elif Movement == "e":
        column = column + 1
    elif Movement == "n":
        row = row - 1
    elif Movement == "s":
        row = row + 1

    movesLeft = movesLeft - 1

    if row == treasureRow and column == treasureColumn:
        print("!!! You Win !!!")

    elif movesLeft == 0:
        print("... You Lose ...")

    print()
    print()

#===============================================================================
# Bonus Tasks:
# - the while loop ends when the player wins
# - print player's position before every move
# - print moves left before every move
#===============================================================================

ocean = [['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~']]
row = 2
column = 2

treasureRow = 4
treasureColumn = 4
gameover = False

movesLeft = 10
while gameover == False:

    ocean[row][column] = 'X'

    # DO NOT REUSE THE NAME "row" FOR THIS VARIABLE
    for mapRow in ocean:
        print(mapRow)
    print("your current position is:")
    print("row: " + str(row))
    print("column: " + str(column))
    print("moves left: " + str(movesLeft))
    Movement = input("Where do you want to go? ")

    ocean[row][column] = '~'

    if Movement == "w":
        column = column - 1
    elif Movement == "e":
        column = column + 1
    elif Movement == "n":
        row = row - 1
    elif Movement == "s":
        row = row + 1

    if Movement == "nw":
        column = column - 1
        row = row - 1
    elif Movement == "ne":
        column = column + 1
        row = row - 1
    elif Movement == "sw":
        column = column - 1
        row = row + 1
    elif Movement == "se":
        column = column + 1
        row = row + 1

    movesLeft = movesLeft - 1

    if row == treasureRow and column == treasureColumn:
        print("!!! You Win !!!")
        gameover = True
    elif movesLeft == 0:
        print("... You Lose ...")
        gameover = True

    print()
    print()
