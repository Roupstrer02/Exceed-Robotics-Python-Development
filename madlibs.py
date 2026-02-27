numberToGuess = 5

playerGuess = input("Guess my number, it's between 1 and 10: ")

playerGuess = int(playerGuess)

if playerGuess < numberToGuess:
    print("Too low")

elif playerGuess > numberToGuess:
    print("Too high")

else:
    print("Well Done!")
