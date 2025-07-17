# Making Calculator using Match Case.

a = int(input("Enter The Value of a: "))
b = int(input("Enter The Value of b: "))

operation = int(input("Enter 1 for Addition\nEnter 2 for Subtraction\nEnter 3 for Multiplication\nEnter 4 for Division\n"))
try:
    match operation:
        case 1:
            print(f"The Addtion of a and b is {a+b}")
        case 2:
            print(f"The Subtraction of a and b is {a-b}")
        case 3:
            print(f"The Multiplication of a and b is {a*b}")
        case 4:
            print(f"The Division of a and b is {a/b}")
        case default:
            print("Unknown Error Occured!!")
except ZeroDivisionError:
    print("Division by Zero is not possible!!")