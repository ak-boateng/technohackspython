import time

print("This is a calculator to perform basic arithmetic operations")

time.sleep(0.5)

print("Shall we begin...")

# ask user for input for operation
opr = int(input("What operation do you want to perform?\n"
                "1. Addition\n"
                "2. Substraction\n"
                "3. Multiplication\n"
                "4. Division\n"
                "5. Modulo\n"
                "Enter operation: "))

# ask user for input for operands
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))


# Functions to perform the variuos operations
# Addition
def add(x, y):
    return x + y


# Substraction
def substract(x, y):
    return x - y


# Multiplication
def multiply(x, y):
    return x * y


# Division
def division(x, y):
    return x/y

# Modulo


def modulo(x, y):
    return x % y


if opr == 1:
    print(f"The result is: {add(x, y)}")
elif opr == 2:
    print(f"The result is: {substract(x, y)}")
elif opr == 3:
    print(f"The result is: {multiply(x, y)}")
elif opr == 4:
    print(f"The result is: {division(x, y)}")
elif opr == 5:
    print(f"The result is: {modulo(x, y)}")
