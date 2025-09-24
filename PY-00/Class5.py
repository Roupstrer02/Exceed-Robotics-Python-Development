#===============================================================================
# Class5:
# Roupen Kaloustian
# July 2025
#===============================================================================

#===============================================================================
# Group exercise:
#===============================================================================

# tuples and lists can hold any number of any type of data
myNewTuple = (1, 3.14, True, "Exceed")
print(myNewTuple)

myNewList = [False, "Robotics", 100, 9.99]
print(myNewList)

# we use tuples in cases we know the amount of data won't change
profile = ("Adventurer01", "supersecretpassword123")

print("Username: " + profile[0])
print("password: " + profile[1])

# we use lists in cases we know the amount of data can change
handOfCards = ["7 of diamonds", "Queen of hearts", "9 of clubs", "King of spades", "Joker"]
# this is just an example, we'll look at MUCH better ways to implement this kind of feature in the future


# Using lists
# Very often, we need to go through every element of a list and perform some action.
# There are two ways to do this:

# element x in [y]
print("Player hand:")
for card in handOfCards:
    print(" - " + card)

# i in range(a,b)
print("Player hand:")
for i in  range(0,5):
    print(" - " + handOfCards[i])

# both methods get the same job done, but sometimes, it's easier to use one than the other

#===============================================================================
# Basic individual task: Real Mastermind
#===============================================================================

answer = ["red", "red", "blue", "green"]
playerAnswer = []

print("first color:")
playerInput1 = input()
playerInput1 = playerInput1.lower()
playerAnswer.append(playerInput1)

print("second color:")
playerInput2 = input()
playerInput2 = playerInput2.lower()
playerAnswer.append(playerInput2)

print("third color:")
playerInput3 = input()
playerInput3 = playerInput3.lower()
playerAnswer.append(playerInput3)

print("fourth color:")
playerInput4 = input()
playerInput4 = playerInput4.lower()
playerAnswer.append(playerInput4)

print("Results:")
for i in range(0,4):
    if answer[i] == playerAnswer[i]:
        print(" - Correct!")
    else:
        print(" - Wrong...")


#===============================================================================
# Bonus Task 1: Game Over Message
# Make a Game Over message telling the player that they won *ONLY IF* the player guessed all 4 colours correctly
# Otherwise, tell the player how many answers are **completely** wrong (guesses that never appear in the answer even once)
#===============================================================================

#Add this code to the previous code

print("==========================================")
if playerAnswer == answer:
    print("Victory!")
else:
    for pA in playerAnswer:
        if pA not in answer:
            print(pA + " is not part of the answer!")
    