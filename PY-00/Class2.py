#===============================================================================
# Class2:
# Roupen Kaloustian
# January 2026
# Learning Objectives:
#===============================================================================

# !!! #
# This file contains both the normal and extended versions of the task.
# Comment out one of the versions to test the other if needed.
# !!! #

#===============================================================================
# Individual Task: Rock Paper Scissors
#===============================================================================
print("===============================================")
print("        Welcome to Rock Paper Scissors!        ")
print("===============================================")

CPU = "Rock" #pick your favorite

player = input("what do you choose? ")

print("The computer chose: " + CPU)

if CPU == player:
    print("it's a Tie!")

elif CPU == "Rock" and player == "Paper":
    print("You Win!")
elif CPU == "Rock" and player == "Scissors":
    print("You Lose!")

elif CPU == "Paper" and player == "Rock":
    print("You Lose!")
elif CPU == "Paper" and player == "Scissors":
    print("You Win!")

elif CPU == "Scissors" and player == "Rock":
    print("You Win!")
elif CPU == "Scissors" and player == "Paper":
    print("You Lose!")

#===============================================================================
# Bonus Task: Rock Paper Scissors Lizard Spock
#===============================================================================

print("===============================================")
print("        Welcome to Rock Paper Scissors!        ")
print("===============================================")

CPU = "Rock" #pick your favorite

player = input("what do you choose? ")

print("The computer chose: " + CPU)

if CPU == player:
    print("it's a Tie!")

elif CPU == "Rock" and player == "Paper" or player == "Spock":
    print("You Win!")
elif CPU == "Rock" and player == "Scissors" or player == "Lizard":
    print("You Lose!")

elif CPU == "Paper" and player == "Rock" or player == "Spock":
    print("You Lose!")

elif CPU == "Paper" and player == "Scissors" or player == "Lizard":
    print("You Win!")

elif CPU == "Scissors" and player == "Rock" or player == "Spock":
    print("You Win!")
elif CPU == "Scissors" and player == "Paper" or player == "Lizard":
    print("You Lose!")

elif CPU == "Lizard" and player == "Rock" or player == "Scissors":
    print("You Win!")
elif CPU == "Lizard" and player == "Paper" or player == "Spock":
    print("You Lose!")

elif CPU == "Spock" and player == "Paper" or player == "Lizard":
    print("You Win!")
elif CPU == "Spock" and player == "Rock" or player == "Scissors":
    print("You Lose!")
