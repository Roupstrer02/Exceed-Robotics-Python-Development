#===============================================================================
# Class2:
# Roupen Kaloustian
# July 2025
# 
#===============================================================================

#===============================================================================
# Group exercise:
#===============================================================================

"""
Task: Guess a number between 1 and 10 and have the computer give you hints to help
"""

# explain the flow of if elif else -> what happens when two ifs can occur (if - if - if vs if - elif - else)

# try with num = 5 | num = 15 | num = 10 << this final one would make both if statements occur 
num = 5
if num <= 10:
    print("Hi, i'm A")
# try the above code on its own

if num >= 10:
    print("Hi, i'm B")

# try the above code again but including the second "if" statement, with the same values for num

# afterwards, add an "el" in front of the second if statement above and run it with num = 10.

if num <= 10:
    print("Hi, i'm A")
elif num >= 10:
    print("Hi, i'm B")


# this second example shows how booleans can be stored in variables and used
x = input("pick a number, any number: ")
x = int(x)
isInNumberRange = x > 10 and x < 100

# what will get printed here?...
if isInNumberRange:
    print("Your number is between 10 and 100")
else:
    print("Your number is NOT between 10 and 100")



#===============================================================================
# Basic individual task: Number guesser
# Player guesses a given number between 1 to 10
#===============================================================================

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
# Bonus Task:
# Single unit Mastermind
# Give the player multiple chances to guess a larger, harder to guess number.
#===============================================================================

numberToGuess = 72
print("============= Welcome to Mastermind =============")
print("Guess my number, it's between 1 and 100, good luck!")
playerGuess = input("Your first guess: ")
playerGuess = int(playerGuess)

if playerGuess < numberToGuess:
    print("Too low")
elif playerGuess > numberToGuess:
    print("Too high")
else:
    print("Well Done!")

playerGuess = input("Your second guess: ")
playerGuess = int(playerGuess)

if playerGuess < numberToGuess:
    print("Too low")
elif playerGuess > numberToGuess:
    print("Too high")
else:
    print("Well Done!")

playerGuess = input("Your third guess: ")
playerGuess = int(playerGuess)

if playerGuess < numberToGuess:
    print("Too low")
elif playerGuess > numberToGuess:
    print("Too high")
else:
    print("Well Done!")

# An extra bonus could be to get them to force the game to stop when the right number is reached