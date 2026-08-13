import keyboard
import random

money = 0
moneyGain = 1
luck = 0.01 # can also be 1 if the student wants to use random.randint(1,100) instead of using float values
actions = 0 # BONUS (1)
while money < 1000000: # player wins at a million points

    key = keyboard.read_key()
    print()
    #action 1 (a)
    if key == "a":
        actions = actions + 1 # BONUS (1)
        randomChance = random.random()
        if randomChance < luck:
            money = money + moneyGain * 100
            print("LUCKY!")
            print("money ($CAD)")
            print(money)
            
        if randomChance >= luck:
            money = money + moneyGain
            print("money ($CAD)")
            print(money)

    #action 2 (b)
    if key == 'b':
        actions = actions + 1 # BONUS (1)
        if money >= 10:
            print("upgrade bought: -10$")
            moneyGain = moneyGain + 1
            money = money - 10

    #action 3 (c)
    if key == 'c':
        actions = actions + 1 # BONUS (1)
        if money >= 25:
            luck += 0.01
            money = money - 25
            print("upgrade bought: -25$")
            print("luck:")
            print(luck)

print("=========================================")
print("=              ! Victory !")
print("You have won in") # BONUS (1)
print(actions) # BONUS (1)
print("actions") # BONUS (1)
print("=========================================")