#===============================================================================
# Class4:
# Roupen Kaloustian
# July 2025
#===============================================================================

#===============================================================================
# Group exercise:
# testing out random numbers and showing how to use them
#===============================================================================
import random as rd

print("=======================================================================")
print("Let's take a look at random numbers!")
print("=======================================================================")

#this is how you get a random number from 0 to 10
x = rd.randint(0,10)

#this is how you get a random decimal number from 0.0 to 1.0
y = rd.random()

# print(x)
# print(y)

print()
print("What did the coin land on?...")

#using random numbers are still just numbers, we use them the same way we would any number
if y >= 0.5:
    print("The coin landed on heads")
else:
    print("The coin landed on tails")

print()

#===============================================================================
# Basic individual task:
# Make a rock paper scissors game where you play against the computer who picks randomly
#===============================================================================
print("=======================================================================")
print("Welcome to Rock Paper Scissors!")
print("=======================================================================")
print()
print("What will you choose? Rock, Paper, or Scissors?")
player_Choice = input("Enter choice here: ")

#0 is rock, 1 is paper, 2 is scissors
CPU_Num = rd.randint(0,2)

if player_Choice == "Rock":
    if CPU_Num == 0:
        print("Tie!")
    elif CPU_Num == 1:
        print("You Lose!")
    elif CPU_Num == 2:
        print("You Win!")

elif player_Choice == "Paper":
    if CPU_Num == 0:
        print("You Win!")
    elif CPU_Num == 1:
        print("Tie!")
    elif CPU_Num == 2:
        print("You Lose!")

elif player_Choice == "Scissors":
    if CPU_Num == 0:
        print("You Lose!")
    elif CPU_Num == 1:
        print("You Win!")
    elif CPU_Num == 2:
        print("Tie!")


#===============================================================================
# Bonus Task:
# Allow the player to pick between two minigames: RPS, and a coin toss game
# Can also suggest to cleanup player input by using string methods like String.lower() to ensure the game works even with typos
#===============================================================================

print("=======================================================================")
print("Welcome to the minigame hub!")
print("=======================================================================")
print()
print(" - type '1' for Rock Paper Scissors")
print(" - type '2' for Coin Toss")
print()
game = input("What would you like to play: ")
game = int(game)
if game == 1:
    print("=======================================================================")
    print("Welcome to Rock Paper Scissors!")
    print("=======================================================================")
    print()
    print("What will you choose? Rock, Paper, or Scissors?")
    player_Choice = input("Enter choice here: ")

    #0 is rock, 1 is paper, 2 is scissors
    CPU_Num = rd.randint(0,2)

    if player_Choice == "Rock":
        if CPU_Num == 0:
            print("Tie!")
        elif CPU_Num == 1:
            print("You Lose!")
        elif CPU_Num == 2:
            print("You Win!")

    elif player_Choice == "Paper":
        if CPU_Num == 0:
            print("You Win!")
        elif CPU_Num == 1:
            print("Tie!")
        elif CPU_Num == 2:
            print("You Lose!")

    elif player_Choice == "Scissors":
        if CPU_Num == 0:
            print("You Lose!")
        elif CPU_Num == 1:
            print("You Win!")
        elif CPU_Num == 2:
            print("Tie!")
elif game == 2:
    print("Where will the coin land?")
    print("Heads or Tails?")
    player_Choice = input("Enter prediction here: ")

    Rand_Num = rd.random()

    if Rand_Num > 0.5 and player_Choice == "Heads":
        print("Correct! The coin landed on Heads!")
    elif Rand_Num <= 0.5 and player_Choice == "Tails":
        print("Correct! The coin landed on Tails!")
    else:
        print("Sorry, but the coin landed on the other side...")