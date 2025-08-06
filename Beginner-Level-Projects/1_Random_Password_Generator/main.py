# Step-1--> Importing all required libraries
import random
import string
import sys
import pyperclip


# Step-2--> Taking Input from the user and storing it in the form of boolean
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
    

# Step-3--> Character Pool Construction
char_pool = ""
if(include_number):
      char_pool += string.digits   
if(include_lowercase ):
      char_pool += string.ascii_lowercase
if(include_uppercase ):
      char_pool += string.ascii_uppercase
if(include_punctuation ):
      char_pool += string.punctuation
# print(char_pool)


# Step-4-->Password Generation + Printing the Output
if(char_pool == ""):
     print("Choose any one choice among the provided")
     sys.exit()

resp = input("\nDo You want one character from each type you have selcted? (Y/N) : ").strip().lower()

if resp not in ['y', 'yes', 'n', 'no']:  
    print("Please enter a valid choice!")  
    sys.exit()  # or continue to re-prompt  


enforce = resp in ['y', 'yes']
# print(enforce)

guaranteed_chars = []
if(enforce== True):
    if(include_number):
            guaranteed_chars.append(random.choice(string.digits))
    if(include_lowercase):
            guaranteed_chars.append(random.choice(string.ascii_lowercase))
    if(include_uppercase):
            guaranteed_chars.append(random.choice(string.ascii_uppercase))
    if(include_punctuation):
            guaranteed_chars.append(random.choice(string.punctuation))
    # print(guaranteed_chars)

    # finding lenght of the remaining password
    required_len = length -len(guaranteed_chars)
    # print(required_len)
    random_chars= []

    # Selecting remainging password
    for i in range(required_len):
            random_chars.append(random.choice(char_pool))
    # print(random_chars)     

    # merging the both the lists
    password_chars = guaranteed_chars + random_chars
    # print(password_chars)

    #shuffling the list
    random.shuffle(password_chars)
    # print(password_chars)

    # Converting list to a string
    final_password = "".join(password_chars)
    # print(final_password)

    # copying the password into your clipboard
    pyperclip.copy(final_password)
    print(f"The Final Password is : {final_password}")
    print("This password is copied in your clipboard automatically.")
else:
    random_chars = []
    for i in range(length):
        random_chars.append(random.choice(char_pool))
    # print(random_chars)
    
    #shuffling the list
    random.shuffle(random_chars)
    # print(random_chars)

    # Converting the list into stirg
    final_password = "".join(random_chars)
    # print(final_password)

    # copying the password into your clipboard
    pyperclip.copy(final_password)
    print(f"The Final Password is : {final_password}")
    print("This password is copied in your clipboard automatically.")