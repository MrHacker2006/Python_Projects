# Importing all required libraries
import random
import string
import sys
import pyperclip

# Taking Input from the user and storing it in the form of boolean
print("Welcome to the Random Password Generator!\n")
while True:
    try:
        length = int(input("Enter the length of the password(in integers), which you want to generate : "))
        if (length>0):
                print("\nWhat things you want in your password? Answer below👇\n")

                include_number = input("Do you want to include Numbers ? (Y/N): ").strip().lower() in ['y', 'yes']
                include_lowercase = input("Do you want to include Lowercase Letters ? (Y/N): ").strip().lower() in ['y', 'yes']
                include_uppercase = input("Do you want to include Uppercase letters ? (Y/N): ").strip().lower() in ['y', 'yes']
                include_normal_symbol = input("Do you want to include Normal Symbols ? (Y/N): ").strip().lower() in ['y', 'yes']
                include_special_symbol = input("Do you want to include Special Symbols ? (Y/N): ").strip().lower() in ['y', 'yes']
                break
        else:
             print("Password length must be greater than zero")
    except ValueError:
        print("Please enter a vaild Natural Number!")
    
