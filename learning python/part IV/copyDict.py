def copyDict(dict):
    copdict = {}
    for item in dict.keys():
        copdict[item] = dict[item]
    return copdict


print(copyDict({1: 'a', 2: 'b'}))