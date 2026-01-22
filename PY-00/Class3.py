#===============================================================================
# Class3:
# Roupen Kaloustian
# January 2026
# Learning Objectives: Teaching string methods,
#===============================================================================

# !!! #
# This file contains both the normal and extended versions of the task.
# Comment out one of the versions to test the other if needed.
# !!! #

#===============================================================================
# Basic individual task:
#===============================================================================

question1 = "What is my name?"
question2 = "What is the name of the country you're in?"
question3 = "if x = 4, and y = 5x - 2: y = ?"

answer1 = "a"
answer2 = "b"
answer3 = 18

print("============================================================================")
print("Welcome to the Quiz Game!")
print("============================================================================")
print()

print(question1)
print("a) Instructor's real name")
print("b) Incorrect Name")
print("c) Incorrect Name")

playerAnswer = input("guess: ")
playerAnswer = playerAnswer.lower()

if playerAnswer == answer1:
    print("Nicely done!!")
else:
    print("Incorrect...")

print(question2)
print("a) USA")
print("b) Canada")
print("c) Mexico")

playerAnswer = input("guess: ")
playerAnswer = playerAnswer.lower()

if playerAnswer == answer2:
    print("Nicely done!!")
else:
    print("Incorrect...")

print(question3)
print()

playerAnswer = input("input the answer directly: ")
playerAnswer = int(playerAnswer)

if playerAnswer == answer3:
    print("Nicely done!!")
else:
    print("Incorrect...")

#===============================================================================
# Bonus Task:
# Adding a game over menu with a summary
#===============================================================================

username = "Instructor"
password = "in123"

usernameInput = input("Enter username: ")
passwordInput = input("Enter password: ")

caseCorrectedPassword = passwordInput.lower()

if usernameInput == username and passwordInput == password:
    print("Logging in...")
elif usernameInput == username and caseCorrectedPassword == password:
    print("Invalid password (double check your capitalization)")
else:
    print("Invalid Login")



