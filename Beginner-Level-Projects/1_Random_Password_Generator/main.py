# Importing all required libraries
import random
import string
import sys
import pyperclip

# Taking Input from the user
print("Welcome to the Random Password Generator!\n")
while True:
    try:
        length = int(input("Enter the length of the password(in integers), which you want to generate : "))
        if (length>0):
                print("\nWhat things you want in your password? Answer below👇\n")

                choice_Number = str(input("Do you want that your password contains number? Enter Y/N: "))
                choice_UpperCase = str(input("Do you want that your password contains UpperCase character? Enter Y/N: "))
                choice_LowerCase = str(input("Do you want that your password contains LowerCase character? Enter Y/N: "))
                choice_Symbol = str(input("Do you want that your password contains Symbols? Enter Y/N: "))
                choice_Special_Symbol = str(input("Do you want that your password contains Special Symbols Enter Y/N: "))
                break
        else:
             print("Password length must be greater than zero")
    except ValueError:
        print("Please enter a vaild Natural Number!")
    
# Storing the choices in form of boolean variables
a=choice_Number.lowercase()
print(a)
print(b)
print(c)