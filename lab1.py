import random

print("Hello world!")

ADD = "add"
SUB = "sub"
MUL = "mul"
DIV = "div"


def math_operations(num1, num2, op):
    if op == ADD:
        return num1 + num2
    elif op == SUB:
        return num1 - num2
    elif op == MUL:
        return num1 * num2
    elif op == DIV:
        return num1 / num2
    else:
        return None


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operation = input("Enter operation: ")

print("Result: ", math_operations(number1, number2, operation))

numbers = []
even_numbers = []

for i in range(10):
    numbers.append(random.randint(0, 100))

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])

print("List of 10 numbers: ", numbers)
print("Even numbers of this list: ", even_numbers)
