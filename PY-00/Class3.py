from time import sleep

#===============================================================================
# Class3:
# Roupen Kaloustian
# July 2025
# Learning Objectives: Teaching string methods, 
#===============================================================================

#===============================================================================
# Group exercise:
# Making Abbreviated Usernames:
#===============================================================================

firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
birthYear = input("Please enter your birth year: ")

firstName = firstName.lower()

print(firstName)
firstName = firstName.capitalize()
print(firstName)

lastName = lastName.lower()
print(firstName)
lastName = lastName.capitalize()
print(firstName)

print()

print("Your username will be: ")
print(firstName + lastName[0] + "-" + birthYear[2:])

#===============================================================================
# Basic individual task:
#===============================================================================

question1 = "What is my name?"
question2 = "What is the name of the country you're in?"
question3 = "if x = 4, and y = 5x - 2: y = ?"

answer1 = "a"
answer2 = "b"
answer3 = "c"

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
print("a) Canada")
print("b) USA")
print("c) Mexico")

playerAnswer = input("guess: ")
playerAnswer = playerAnswer.lower()

if playerAnswer == answer2:
    print("Nicely done!!")
else:
    print("Incorrect...")

print(question3)
print("a) 16")
print("a) 20")
print("a) 18")

playerAnswer = input("guess: ")
playerAnswer = playerAnswer.lower()

if playerAnswer == answer3:
    print("Nicely done!!")
else:
    print("Incorrect...")

#===============================================================================
# Bonus Task:
# Adding a game over menu with a summary
#===============================================================================

question1 = "What is my name?"
question2 = "What is the name of the country we're in?"
question3 = "if x = 4, and y = 5x - 2: y = ?"

answer1 = "a"
answer2 = "b"
answer3 = "c"

print("============================================================================")
print("Welcome to the Quiz Game!")
print("============================================================================")
print()

print(question1)
print("a) Instructor's real name")
print("b) Incorrect Name")
print("c) Incorrect Name")

playerAnswer1 = input("guess: ")
playerAnswer1 = playerAnswer1.lower()

if playerAnswer1 == answer1:
    print("Nicely done!!")
else:
    print("Incorrect...")

print(question2)
print("a) Canada")
print("b) USA")
print("c) Mexico")

playerAnswer2 = input("guess: ")
playerAnswer2 = playerAnswer2.lower()

if playerAnswer2 == answer2:
    print("Nicely done!!")
else:
    print("Incorrect...")

print(question3)
print("a) 16")
print("a) 20")
print("a) 18")

playerAnswer3 = input("guess: ")
playerAnswer3 = playerAnswer3.lower()

if playerAnswer3 == answer3:
    print("Nicely done!!")
else:
    print("Incorrect...")

print()
print()
print("============================================================================")
print("                                Game Over")
print("                              Quiz Summary:")
print("                            Question 1: " + str(playerAnswer1 == answer1))
print("                            Question 2: " + str(playerAnswer2 == answer2))
print("                            Question 3: " + str(playerAnswer3 == answer3))
print("============================================================================")