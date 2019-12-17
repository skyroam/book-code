
def countLines(name):
    f1 = open(name, 'r').readlines()
    print(len(f1))

def countChars(name):
    f1 = open(name, 'r').read()
    print(len(f1))

def test(name):
    countLines(name)
    countChars(name)
    
if __name__ == '__main__':
    print(test(name))
    
    