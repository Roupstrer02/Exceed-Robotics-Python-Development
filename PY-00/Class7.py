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
map = ((0,1,2),(3,4,5),(6,7,8))

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
# 5x5 Battleship
#===============================================================================

ocean = ((0,0,0,0,0),(0,0,0,0,0),(0,0,0,0,0),(0,0,0,0,0),(0,0,0,0,0))

for row in ocean:
    for tile in row:
        print(tile, end=" ")
    print("")




#===============================================================================
# Bonus Task:
#===============================================================================
