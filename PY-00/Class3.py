#===============================================================================
# Class3:
# Roupen Kaloustian
# July 2025
#===============================================================================

#===============================================================================
# Group exercise:
#===============================================================================

#===============================================================================

# """
# Making Abbreviated Uuernames:
# """

# firstName = input("Please enter your first name: ")
# lastName = input("Please enter your last name: ")
# birthYear = input("Please enter your birth year: ")

# firstName = firstName.lower()
# firstName = firstName.capitalize()

# lastName = lastName.lower()
# lastName = lastName.capitalize()

# print("Your username will be: ")
# print(firstName + lastName[0] + "-" + birthYear[2:])

#===============================================================================
# Basic individual task:
#===============================================================================

"""
There is a coded message on the board, make a program to decrypt it and put it together, give the real message to the instructor to finish
(or possibly give each student a few words of the message to decrypt)
"""
#for instructor ===============================================================
# messageOnBoard = "whatever you want here"

# codeOnBoard = ""
# for letter in messageOnBoard:
#     codeOnBoard += str(ord(letter)) + " "

# print(codeOnBoard)
#end of instructor resource ====================================================
codeOnBoard = """
84 104 101 32 97 110 115 119 101 114 32 119 111 114 107 115 32 98 101 116 116 101 114
32 119 104 101 110 32 121 111 117 32 97 108 108 32 119 111 114 107
32 116 111 103 101 116 104 101 114 46 46 46
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
codeOnBoard = codeOnBoard.replace("108", "l")
codeOnBoard = codeOnBoard.replace("103", "g")
codeOnBoard = codeOnBoard.replace("46", ".")


print(codeOnBoard)
#===============================================================================
# Bonus Task:
# Increasing difficulty of certain logic statements
#===============================================================================

"""

"""
