import keyboard


money = 0
moneyGain = 1


while True:

    key = keyboard.read_key()
    print()
    #action 1 (a)
    if key == "a":
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