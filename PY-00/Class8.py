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

ocean = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
ships = [[0,0], [1,1], [2,2], [3,3], [4,4]]
previousAttacks = []
while True:
    for row in ocean:
        for tile in row:
            print(tile, end=" ")
        print("")

    playerAttackX = input("What row do you want to hit? ")
    playerAttackY = input("What column do you want to hit? ")

    playerAttackX = int(playerAttackX)
    playerAttackY = int(playerAttackY)
    playerAttack = [playerAttackX, playerAttackY]
    
    if playerAttack not in previousAttacks:
        previousAttacks.append(playerAttack)
        if playerAttack in ships:
            print("Hit!")
            ocean[playerAttackX][playerAttackY] = "H"
        else:
            print("Miss...")
            ocean[playerAttackX][playerAttackY] = "M"
    else:
        print("!!! Tile already hit, pick a new tile !!!")
    
    print()
    print()