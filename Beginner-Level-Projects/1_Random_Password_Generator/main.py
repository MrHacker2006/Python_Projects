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
                include_punctuation = input("Do you want to include Punctuations ? (Y/N): ").strip().lower() in ['y', 'yes']
                break
        else:
             print("Password length must be greater than zero")
    except ValueError:
        print("Please enter a vaild Natural Number!")
    
# Character Pool Construction
char_pool = ""
if(include_number== True):
      char_pool += string.digits   
if(include_lowercase == True):
      char_pool += string.ascii_lowercase
if(include_uppercase == True):
      char_pool += string.ascii_uppercase
if(include_punctuation == True):
      char_pool += string.punctuation

print(char_pool)

# Password Generation

if(char_pool == ""):
     print("Choose any one choice among the provided")
     sys.exit()

resp = input("\nDo You want one character from each type you have selcted? (Y/N) : ").strip().lower()
for resp in ['y', 'yes', 'n', 'no']:
      print("please enter a valid choie!")
      sys.exit()

enforce = resp in ['y', 'yes']
print(enforce)

guranteed_chars = []
if(enforce== True):
    if(include_number):
            guranteed_chars.append(random.choice(string.digits))
    if(include_lowercase):
            guranteed_chars.append(random.choice(string.ascii_lowercase))
    if(include_uppercase):
            guranteed_chars.append(random.choice(string.ascii_uppercase))
    if(include_punctuation):
            guranteed_chars.append(random.choice(string.punctuation))
    print(guranteed_chars)

    # finding lenght of the remaining password
    required_len = length -len(guranteed_chars)
    print(required_len)
    random_chars= []

    # Selecting remainging password
    for i in range(required_len):
            random_chars.append(random.choice(char_pool))
    print(random_chars)     

    # merging the both the lists
    password_chars = guranteed_chars + random_chars
    print(password_chars)

    #shuffling the list
    random.shuffle(password_chars)
    print(password_chars)

    # Converting list to a string
    final_password = "".join(password_chars)
    print(final_password)

    # copying the password into your clipboard
    pyperclip.copy(final_password)

else:
    random_chars = []
    for i in range(length):
        random_chars.append(random.choice(char_pool))
    print(random_chars)
    
    #shuffling the list
    random.shuffle(random_chars)
    print(random_chars)

    # Converting the list into stirg
    final_password = "".join(random_chars)
    print(final_password)

    # copying the password into your clipboard
    pyperclip.copy(final_password)
        




