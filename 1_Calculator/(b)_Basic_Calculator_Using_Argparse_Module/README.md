# 🧮 Basic Calculator Using argparse

### 🤝Project Type: Made with Help

This is a simple command-line calculator built using Python's built-in argparse module. It allows you to perform basic arithmetic operations—addition, subtraction, multiplication, and division—by passing arguments directly from the terminal.

---

## 🚀 How to Use

Run the script from your terminal like this:


python calculator.py <num1> <num2> <operation>


- <num1> – First number (int or float)
- <num2> – Second number (int or float)
- <operation> – One of the following:
  - add → Addition
  - sub → Subtraction
  - mul → Multiplication
  - div → Division

---

## 🧪 Examples


python calculator.py 12 4 add


Output:

Namespace(num1=12.0, num2=4.0, operation='add')
The Adition of num1 and num2 is 16.0



python calculator.py 10 0 div


Output:

Namespace(num1=10.0, num2=0.0, operation='div')
Division by Zero is not possible!


---

## 📄 License

This project is open for educational and personal use. Feel free to fork and modify it as you like.