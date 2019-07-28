def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
while True:
    command = input().split()
    operandA, operator, operandB, equal = command
    if operator == '+':
        print(add(float(operandA), float(operandB)))
    if operator == '-':
        print(subtract(float(operandA), float(operandB)))
    if operator == '*':
        print(multiply(float(operandA), float(operandB)))
    if operator == '/':
        print(divide(float(operandA), float(operandB)))