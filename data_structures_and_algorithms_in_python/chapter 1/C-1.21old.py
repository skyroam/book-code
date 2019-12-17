message = []
try:
    while True:
        line = input()
        message.append(line)
except EOFError:
    for i in range(len(message)-1,-1,-1):
        print(message[i])