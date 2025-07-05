#===============================================================================
# Class2:
# Roupen Kaloustian
# July 2025
#===============================================================================

#===============================================================================
# Group exercise:
#===============================================================================

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
There are 4 people in a room accused of robbing a bank,
it's your job to figure out who's guilty without a shadow of a doubt. (No guessing at all)
One person, the criminal, is lying, everyone else is telling the truth

person A says: "I didn't do it!"
person B says: "I know A and C didn't do it!"
person C says: "D robbed the bank!"
person D says: "C robbed the bank!"
"""
#innocence list
A = True
B = True
C = True
D = True

#accusations against A
accusationsA = not A and not A and A

#accusations against B (none)
accusationsB = False
#accusations against C
accusationsC = not C and C

#accusations against D
accusationsD = D

print(accusationsA)
print(accusationsB)
print(accusationsC)
print(accusationsD)

