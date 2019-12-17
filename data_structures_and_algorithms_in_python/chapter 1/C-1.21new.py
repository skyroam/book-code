message = []
try:
    while True:
        line = input()
        if line = 'ctrl-D'
            raise EOFError
        else:
            message.append(line)
except EOFError:
    for i in range(len(message)-1,-1,-1):
        print(message[i])