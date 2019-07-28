def divide(x, y):
    if y == 0:
        print("can not divide by 0")
        return 
    else: return x/y

command = input()
while '#' not in command:
    for i in range(len(command)):
        if command[i] in ['-', '+', '*', '/']
            choice = command[i]
            num1 = float(command[:i])
            num2 = float(command[i+1:])
    if choice is '+':
        print(num1 + num2)
    elif choice is '-':
        print(num1 - num2)
    elif choice is '*':
        print(num1 * num2)
    elif choice is '/':
        print(num1 / num2)
    else:
        print('wrong operator')
    command = input()