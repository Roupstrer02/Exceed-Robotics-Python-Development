#===============================================================================
# Class5:
# Roupen Kaloustian
# July 2025
#===============================================================================

#===============================================================================
# Basic individual task: Real Mastermind
#===============================================================================

answer = ["red", "red", "blue", "green"]
playerAnswer = []

print("===========================")
print("Welcome to Mastermind")
print("===========================")
print()

print("guess the first color:") # BONUS
playerInput1 = input()
playerInput1 = playerInput1.lower() # BONUS
playerAnswer.append(playerInput1)

print("guess the second color:") # BONUS
playerInput2 = input()
playerInput2 = playerInput2.lower() # BONUS
playerAnswer.append(playerInput2)

print("guess the third color:") # BONUS
playerInput3 = input()
playerInput3 = playerInput3.lower() # BONUS
playerAnswer.append(playerInput3)

print("guess the fourth color:") # BONUS
playerInput4 = input()
playerInput4 = playerInput4.lower() # BONUS
playerAnswer.append(playerInput4)

print("Results:")
for i in range(0,4):
    if answer[i] == playerAnswer[i]:
        print(" - Correct!")
    else:
        print(" - Wrong...")
