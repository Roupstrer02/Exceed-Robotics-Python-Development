import keyboard
import random

money = 0
moneyGain = 1
luck = 0.01 # can also be 1 if the student wants to use random.randint(1,100) instead of using float values

while money < 1000000: # player wins at a million points

    key = keyboard.read_key()
    print()
    #action 1 (a)
    if key == "a":

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


    #action 2 (m)
    if key == 'm':
        print("money ($):")
        print(money)

    #action 3 (b)
    if key == 'b':
        if money >= 10:
            print("upgrade bought: -10$")
            moneyGain = moneyGain + 1
            money = money - 10

    #action 4 (c)
    if key == 'c':
        if money >= 25:
            luck += 0.01
            money = money - 25
            print("upgrade bought: -25$")
            print("luck:")
            print(luck)

print("=========================================")
print("=              ! Victory !              =")
print("=========================================")