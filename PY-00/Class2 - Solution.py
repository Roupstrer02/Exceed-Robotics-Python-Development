#user writes the length of the rectangle
userinput = input("Length of the rectangle: ")

#the computer saves the length as a number
length = int(userinput)

#user writes the height of the rectangle
userinput2 = input("Height of the rectangle: ")

#the computer saves the height as a number
height = int(userinput2)

area = length * height

print(area)

#===========================================================================
# Bonus: House Area Calculator
#===========================================================================

#user writes the width of the house walls
userinput = input("Width of the house: ")

#the computer saves the length as a number
width = int(userinput)

#user writes the height of the house
userinput2 = input("Height of the house: ")

#the computer saves the height as a number
height = int(userinput2)

wallArea = width * height

userinput3 = input("height of the roof: ")

roofHeight = int(userinput3)

roofArea = width * roofHeight / 2

totalArea = wallArea + roofArea

print("results:")
print("walls:")
print(wallArea)
print("roof:")
print(roofArea)
print("total:")
print(totalArea)
