import random

guess = input("pick 'rock', 'paper', or 'scissors': ")

#1 means rock, 2 means paper, 3 means scissors
CPU = random.randint(1,3)

#The results for guessing "rock"
if guess == "rock":
    if CPU == 1:
        print("tie")
    if CPU == 2:
        print("You Lose...")
    if CPU == 3:
        print("You Win!")

#The results for guessing "paper"
if guess == "paper":
    if CPU == 1:
        print("You Win!")
    if CPU == 2:
        print("tie")
    if CPU == 3:
        print("You Lose...")

#The results for guessing "scissors"
if guess == "scissors":
    if CPU == 1:
        print("You Lose...")
    if CPU == 2:
        print("You Win!")
    if CPU == 3:
        print("tie")

#===========================================================================
# Bonus: coin flip
#===========================================================================

import random

guess = input("what will the coin land on ('heads' or 'tails')? ")

coin = random.randint(1,2) #students can also use random.random() if they want and check if the value is (> or <) 0.5

if guess == 'heads':
    if coin == 1:
        print("You got it!")
    if coin == 2:
        print("Nope... try again!")

if guess == 'tails':
    if coin == 1:
        print("Nope... try again!")
    if coin == 2:
        print("You got it!")