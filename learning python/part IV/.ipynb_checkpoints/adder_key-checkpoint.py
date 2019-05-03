def adder(good = 1, bad = 2, ugly = 3):
    result = good + bad + ugly
    return result

print(adder())
print(adder(4))
print(adder(4, 5))
print(adder(4, 5, 6))
#print(adder(4, 5, 6, 7))
print(adder(ugly = 1, good = 2))


def new_adder(good = 1, bad = 2, ugly = 3, **others):
    result = good + bad + ugly
    for item in others.keys():
        result += others[item]
    return result

print(new_adder(wose = 4))