#===============================================================================
# Class8:
# Roupen Kaloustian
# July 2025
#===============================================================================

#===============================================================================
# Basic individual task:
# 5x5 Battleship
#===============================================================================

# ocean = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
# ships = [[0,0], [1,1], [2,2], [3,3], [4,4]]

# while True:
#     for row in ocean:
#         for tile in row:
#             print(tile, end=" ")
#         print("")

#     playerAttackX = input("What row do you want to hit? ")
#     playerAttackY = input("What column do you want to hit? ")

#     playerAttackX = int(playerAttackX)
#     playerAttackY = int(playerAttackY)
#     playerAttack = [playerAttackX, playerAttackY]

#     if playerAttack in ships:
#         print("Hit!")
#         ocean[playerAttackX][playerAttackY] = "H"
#     else:
#         print("Miss...")
#         ocean[playerAttackX][playerAttackY] = "M"

#===============================================================================
# Bonus Tasks:
# - detect duplicate moves (hitting tiles already hit)
# - detecting game victory

#===============================================================================

maze = [['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~']]
row = 2
column = 2

treasureRow = 4
treasureColumn = 4
while True:

    maze[row][column] = 'X'

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

    if row > 4:
        row = 0
    elif row < 0:
        row = 4

    if column > 4:
        column = 0
    elif column < 0:
        column = 4

    #treasure finding
    #==================================================================
    if row == treasureRow and column == treasureColumn:
        break

print("=====================================")
print("     ! Treasure has been Found !")
print("          !!! You Win !!!")
print("=====================================")