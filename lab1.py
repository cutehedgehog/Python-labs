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
