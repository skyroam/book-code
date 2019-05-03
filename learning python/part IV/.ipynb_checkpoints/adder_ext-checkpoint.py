def adder(first, *others):
    result = first
    for item in others:
        result += item
    return result

print(adder('abcd', 'edfg', 'hijk'))
print(adder('abcd'))
print(adder([1,2,3], [4,5,6]))
print(adder([1,2,3]))
print(adder(13.5, 23.4, 23.1))
print(adder(13.5))
print(adder(13.5, [4,5,6]))