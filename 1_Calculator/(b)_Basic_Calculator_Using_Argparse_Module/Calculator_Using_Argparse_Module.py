import argparse

parser = argparse.ArgumentParser(description="Basic Calculator")

parser.add_argument("num1", type=float, help="Argument for num1")
parser.add_argument("num2", type=float, help="Argument for num2")
parser.add_argument("operation" ,choices=['add','sub','mul','div'], help="Argument for performing operation")

args = parser.parse_args()
print(args)
try:
    if args.operation == 'add':
        print(f"The Adition of num1 and num2 is {args.num1 + args.num2}")
    elif args.operation == 'sub':
        print(f"The Subtraction of num1 and num2 is {args.num1 - args.num2}")
    elif args.operation == 'mul':
        print(f"The Multiplication of num1 and num2 is {args.num1 * args.num2}")
    elif args.operation == 'div':
        print(f"The Divsion of num1 and num2 is {args.num1 / args.num2}")
    else:
        print("Something Went Wrong!!")
except ZeroDivisionError:
    print("Division by Zero is not possible!")

# python 2_Calculator_Command_Line.py 5 10 add  = 15
# python 2_Calculator_Command_Line.py 5 2 sub   = 3
# python 2_Calculator_Command_Line.py 5 9 mul   = 45
# python 2_Calculator_Command_Line.py 10 5 div  = 2