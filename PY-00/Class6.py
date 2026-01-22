#===============================================================================
# Class6:
# Roupen Kaloustian
# July 2025
#===============================================================================

testBonus = True
testGroupExercise = False
#===============================================================================
# Group exercise:
#===============================================================================

num = 0
if testGroupExercise:
    while num < 10:
        action = input("write 'up' to increase num or 'down' to decrease num: ")
        action = action.lower()
        action = action.strip()
        if action == "up":
            num += 1
        elif action == "down":
            num -= 1

        print(num)

#===============================================================================
# Basic individual task:
#===============================================================================

import random as rd

score = 0

level = 1

print("================================================================")
print("Welcome Idler")
print("================================================================")

print()

# in their games, this would just be a while True,
# I've just done this here to let you test the normal and bonus versions of the task by changing the variable at the top of the code
while not testBonus:
    print("You have " + str(score))

    playerChoice = input("What would you like to do?\n-->")
    playerChoice = playerChoice.lower()
    playerChoice = playerChoice.strip()

    if playerChoice == "w":
        score = score + level

    elif playerChoice == "b" and score >= 10:
        score = score - 10
        level = level + 1

#===============================================================================
# Bonus Task:
# Have the enemy also take random actions against the player (Attack or Heal)
#===============================================================================

import random as rd

score = 0

level = 1

print("================================================================")
print("Welcome Idler")
print("================================================================")

print()

# in their games, this would just be a while True,
# I've just done this here to let you test the normal and bonus versions of the task by changing the variable at the top of the code
while testBonus:

    print("================================================================")
    print("You have " + str(score) + "$")
    print("================================================================")
    print("How to play:")
    print(" - press and hold ENTER to work")
    print(" - 'b' to buy an upgrade for 100$")

    playerChoice = input("What would you like to do?\n-->")
    playerChoice = playerChoice.lower()
    playerChoice = playerChoice.strip()

    if playerChoice == "":
        score = score + level

    elif playerChoice == "b" and score >= 100:
        score = score - 100
        level = level + 1
