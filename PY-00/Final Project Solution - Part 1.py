#=========================================================================
# A note about the extensions for this project
#
# There are 3 files of solution code for this final project.
# Each week's slides will list more bonuses for students to try and complete.
# Each of the 3 solutions showcase only the bonuses newly added in their respective week's slides:
#   - part 1 contains the bonuses of week 6
#   - part 2 contains the bonuses of week 7
#   - part 3 contains the bonuses of week 8
# 
# Any line of code that is relevant to a bonus will have the comment "# BONUS (x)" next to it that indicates for which bonus it is relevant.
# If a whole block of code is relevant to a bonus, you will clearly see where the bonus code starts and ends 
# 
# Of course, students are welcome to complete all the bonuses of every week. I've simply opted to separate them for the sake of readability.
# 
# Roupen, August 2026  
#=========================================================================
import keyboard
import random # BONUS (3)


money = 0
moneyGain = 1


while True:

    key = keyboard.read_key()
    print()
    #action 1 (a)
    if key == "a":
        money = money + moneyGain
        
        print("money ($CAD)") # BONUS (1)
        print(money)

    #action 2 (b)
    if key == 'b':
        if money >= 10:
            print("upgrade bought: -10$") # BONUS (1)
            moneyGain = moneyGain + 1
            money = money - 10

    #============================================= Start of BONUS (2)
    #action 3 (m)
    if key == 'm':
        print("money ($):") # BONUS (1)
        print(money)
    #============================================= End of BONUS (2)

    #============================================= Start of BONUS (3)
    #action 4 (t)
    if key == 't':
        print("Tossing a coin!") # BONUS (1)
        randomness = random.randint(1,2)
        if randomness == 1:
            money = money + moneyGain * 100 
        if randomness == 2:
            money = money - moneyGain * 100
    #============================================= End of BONUS (3)