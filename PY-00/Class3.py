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
question3 = "if x = 4, and y = 5x - 2"

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
print("a) Instructor's real name")
print("b) Incorrect Name")
print("c) Incorrect Name")

playerAnswer = input("guess: ")


if playerAnswer == answer2:
    print("Nicely done!!")
else:
    print("Incorrect...")

print(question3)
playerAnswer = input("guess: ")

if playerAnswer == answer3:
    print("Nicely done!!")
else:
    print("Incorrect...")

#===============================================================================
# Bonus Task:
# Adding a score system, more questions, ?~numerical answers~?
#===============================================================================

print("============================================================================")
print("Welcome to the Quiz Game!")
print("============================================================================")
print()

print(question1)
playerAnswer = input("guess: ")
playerAnswer = playerAnswer.lower()

if playerAnswer == answer1:
    print("Nicely done!!")
else:
    print("Incorrect...")

print(question2)
playerAnswer = input("guess: ")

if playerAnswer == answer2:
    print("Nicely done!!")
else:
    print("Incorrect...")

print(question3)
playerAnswer = input("guess: ")

if playerAnswer == answer3:
    print("Nicely done!!")
else:
    print("Incorrect...")