#===============================================================================
# Class7:
# Roupen Kaloustian
# July 2025
#===============================================================================

#===============================================================================
# Group exercise:
# printing a 2D matrix and use it as a map
#===============================================================================

#explain how a matrix is just a list where each element is itself a list
map = [[1,2,3],[4,5,6],[7,8,9]]

#try printing each element in the list
#we can think of each element of the map as one row, and each element of those rows as a single tile
for row in map:
    print(row)

#print it a little nicer:
for row in map:
    for tile in row:
        #explain how the print command automatically goes to the next line, but that we can turn it off by using the 'end' parameter
        print(tile, end=" ")
    print("")

#===============================================================================
# Basic individual task:
# Hide and Seek
#===============================================================================

# maze = [['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~']]
# row = 2
# column = 2
# while True:

#     maze[row][column] = 'X'

#     for i in range(0,5):
#         print(maze[i])

#     maze[row][column] = '~' # <-- this line will almost definitely be confusing to students

#     move = input("where do you want to go? ")

#     if move == "left":
#         column = column - 1
#     elif move == "right":
#         column = column + 1
#     elif move == "up":
#         row = row - 1
#     elif move == "down":
#         row = row + 1


#===============================================================================
# Bonus Task(s):
# - if the player tries to go out of bounds, keep them where they are
# - let the player move diagonally
# - (VERY HARD) draw the path left by the player of all the tiles they've already visited [W.I.P might not teach foreach loop]
#===============================================================================

maze = [['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~'], ['~','~','~','~','~']]
row = 2
column = 2
while True:

    maze[row][column] = 'X'

    for i in range(0,5):
        print(maze[i])

    maze[row][column] = '~'

    move = input("where do you want to go? ")

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
