#===============================================================================
# Class2:
# Roupen Kaloustian
# July 2025
#===============================================================================

#===============================================================================
# Group exercise:
#===============================================================================

"""
Task: Guess a number between 1 and 10 and have the computer give you hints to help
"""

numberToGuess = 5

playerGuess = input("Guess my number, it's between 1 and 10: ")
playerGuess = int(playerGuess)

if playerGuess < numberToGuess:
    print("Too low")
elif playerGuess > numberToGuess:
    print("Too high")
else:
    print("Well Done!")

#===============================================================================
# Basic individual task:
#===============================================================================

"""
Task description:

Write a program to solve this logic puzzle:

I want to buy a breakfast wrap from Tim Horton's. 

I have 5.50$. 
It is currently 11AM on a Friday. 
A breakfast wrap usually costs 7.50$. 
*if* it's the weekend, breakfast wraps are 50% off. 
I can buy a breakfast wrap *if* it's still morning 
I can buy a breakfast wrap *if* I have enough money.  
"""

money = 5.50
cost = 7.50
weekend = False
Time = 11
if weekend == True:
    cost = cost / 2

if Time < 12:
    Morning = True
else:
    Morning = False

if Morning and money >= cost:
    print("I can buy a wrap!")
else:
    print("no breakfast wrap for me... :(")

#===============================================================================
# Bonus Task:
# Increasing difficulty of certain logic statements
#===============================================================================

"""
two people argue about who they think is the best football player in the world... or rather who isn't...

person A says that Mbappe is NOT the best player in the world, and that Haaland is also NOT the best player in the world
person B says that the best player in the world is NOT Mbappe or Haaland

They seem to be yelling over eachother instead of listening to one another...

Are they even disagreeing?...
"""
#innocence list
Mbappe = True
Haaland = True
A = not Mbappe and not Haaland
B = not (Mbappe or Haaland)

Answer = A == B
print(Answer)