#===============================================================================
# Class8:
# Roupen Kaloustian
# July 2025
#===============================================================================

#===============================================================================
# Basic individual task:
# Treasure Hunting Game
#===============================================================================

maze = [['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~']]
row = 2
column = 2

treasureRow = 4
treasureColumn = 4


movesLeft = 10
while True:

    maze[row][column] = 'X'

    # DO NOT REUSE THE NAME "row" FOR THIS VARIABLE
    for mapRow in maze:
        print(mapRow)
    print("your current position is:")
    print("row: " + str(row))
    print("column: " + str(column))
    print("moves left: " + str(movesLeft))
    Movement = input("Where do you want to go? ")

    for i in range(0,5):
        print(maze[i])

    maze[row][column] = '='

    move = input("where do you want to go? ")

    #movement (class 7)
    #==================================================================
    if move == "w":
        column = column - 1
    elif move == "e":
        column = column + 1
    elif move == "n":
        row = row - 1
    elif move == "s":
        row = row + 1
    elif move == "ne":
        row = row - 1
        column = column + 1
    elif move == "se":
        row = row + 1
        column = column + 1
    elif move == "sw":
        row = row + 1
        column = column - 1
    elif move == "nw":
        row = row - 1
        column = column - 1

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

    #treasure finding
    #==================================================================
    if row == treasureRow and column == treasureColumn:
        break

print("=====================================")
print("     ! Treasure has been Found !")
print("          !!! You Win !!!")
print("=====================================")