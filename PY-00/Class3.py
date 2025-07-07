from time import sleep

#===============================================================================
# Class3:
# Roupen Kaloustian
# July 2025
#===============================================================================

#===============================================================================
# Group exercise:
# Making Abbreviated Usernames:
#===============================================================================

firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
birthYear = input("Please enter your birth year: ")

firstName = firstName.lower()
firstName = firstName.capitalize()

lastName = lastName.lower()
lastName = lastName.capitalize()

print("Your username will be: ")
print(firstName + lastName[0] + "-" + birthYear[2:])

#===============================================================================
# Basic individual task:
#===============================================================================

# """
# There is a coded message on the board, make a program to decrypt it and put it together,
# go up to the instructor computer and try to enter your code in their "unhackable system"
# """

# #for instructor ===============================================================
# messageOnBoard = "The 4nswer works b3tter when you look clo5er"

# # code below generates a valid code from the message given above
# codeOnBoard = ""
# for letter in messageOnBoard:
#     codeOnBoard += str(ord(letter)) + " "

# print(codeOnBoard)
# #end of instructor resource ====================================================
codeOnBoard = """
84 104 101 32 52 110 115 119 101 114 32 119 111 114 107 115 32 98 51 116 116 101 114 32
119 104 101 110 32 121 111 117 32 108 111 111 107 32 99 108 111 53 101 114
"""

#use chr() of a number in the list to get the letter, then replace it in the string

codeOnBoard = codeOnBoard.replace("84", "T")
codeOnBoard = codeOnBoard.replace("104", "h")
codeOnBoard = codeOnBoard.replace("101", "e")
codeOnBoard = codeOnBoard.replace("32", " ")

codeOnBoard = codeOnBoard.replace("97", "a")
codeOnBoard = codeOnBoard.replace("110", "n")
codeOnBoard = codeOnBoard.replace("115", "s")
codeOnBoard = codeOnBoard.replace("119", "w")

codeOnBoard = codeOnBoard.replace("114", "r")
codeOnBoard = codeOnBoard.replace("111", "o")
codeOnBoard = codeOnBoard.replace("107", "k")
codeOnBoard = codeOnBoard.replace("98", "b")
codeOnBoard = codeOnBoard.replace("116", "t")

codeOnBoard = codeOnBoard.replace("121", "y")
codeOnBoard = codeOnBoard.replace("117", "u")
codeOnBoard = codeOnBoard.replace("99", "c")
codeOnBoard = codeOnBoard.replace("108", "l")
codeOnBoard = codeOnBoard.replace("46", ".")

codeOnBoard = codeOnBoard.replace("52", "4")
codeOnBoard = codeOnBoard.replace("51", "3")
codeOnBoard = codeOnBoard.replace("53", "5")

print(codeOnBoard)
#===============================================================================
# Bonus Task:
# Increasing difficulty of certain logic statements
#===============================================================================

"""
see the responses given by the computer using the code in the instructor resources
"""



#===============================================================================
# Instructor Resources:
# Run this code on the instructor PC and have students come input their discovered codes in
#===============================================================================

realCode = "435"
secondMessage = "Off by 1: "
secondCode = "725"
while True:
    code = input("\n\nEnter secret password: ")

    if code == realCode:
        print("First Authentication step complete:")
        print("Loading . ", end = "")
        for i in range(0,3):
            sleep(1)
            print(".", end = " ")
        sleep(1)
        print()

        print(secondMessage)

        for letter in secondCode:
            sleep(1)
            print(str(ord(letter)+1) + " ", end = " ")

        sleep(1)

        secondCodeGuess = input("What is the real code: ")

        if secondCodeGuess == secondCode:
            print("Welcome!")
            sleep(1)
            print("Congratulations!\n\n")
        else:
            print("IMPOSTOR!")
            sleep(1)
            print("LEAVE AT ONCE!")

    else:
        print("Incorrect!")