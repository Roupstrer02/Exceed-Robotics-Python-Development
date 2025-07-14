#===============================================================================
# Class6:
# Roupen Kaloustian
# July 2025
#===============================================================================

#===============================================================================
# Group exercise:
#===============================================================================

num = 0

while num < 10:
    action = input("write 'up' to increase num or 'down' to decrease num: ")
    action = action.lower()
    action = action.strip()
    if action == "up":
        num += 1
    elif action == "down":
        num -= 1

    print(num)

#===============================================================================
# Basic individual task:
#===============================================================================
import random as rd

playerHealth = 10

level = 1

enemyHealth = 3

print("================================================================")
print("Welcome Adventurer")
print("================================================================")
print()
print("How to play:")
print(" - 'a' to Attack")
print(" - 'h' to recover Health")
print()

while playerHealth > 0:
    print("================================================================")
    print("Level " + str(level))
    print("================================================================")
    print("Player Health: " + str(playerHealth))
    print("Enemy Health: " + str(enemyHealth))

    playerChoice = input("What would you like to do?\n-->")
    playerChoice = playerChoice.lower()
    playerChoice = playerChoice.strip()
    if playerChoice == "a":
        enemyHealth = enemyHealth - 1
        
    elif playerChoice == "h":
        playerHealth = playerHealth + 1

    if enemyHealth == 0:
        level = level + 1
        enemyHealth = level * 3



print("================================================================")
print("You won!")
print("Congratulations!")


#===============================================================================
# Bonus Task:
# Have the enemy also take random actions against the player (Attack or Heal)
#===============================================================================

playerHealth = 10

level = 1

enemyHealth = 3

print("================================================================")
print("Welcome Adventurer")
print("================================================================")
print()
print("How to play:")
print(" - 'A' to Attack")
print(" - 'H' to recover Health")
print()
while playerHealth > 0 and level <= 3:
    print("================================================================")
    print("Level " + str(level))
    print("================================================================")

    print("Player Health: " + str(playerHealth))
    print("Enemy Health: " + str(enemyHealth))
    print()

    enemyChoice = rd.randint(0,2)
    if enemyChoice == 0:
        playerHealth -= 1
        print("The enemy attacks!")
    elif enemyChoice == 0:
        enemyHealth += 1
        print("The enemy heals!")
    else:
        print("The enemy does nothing...")
    print()

    playerChoice = input("What would you like to do?\n-->")
    

    if playerChoice == "a":
        enemyHealth = enemyHealth - 1
        
    elif playerChoice == "h":
        playerHealth = playerHealth + 1

    if enemyHealth == 0:
        level = level + 1
        enemyHealth = level * 3
    