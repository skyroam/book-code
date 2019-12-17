def addDict(dictA, dictB):
    if type(dictA) == list:
        dictC = dictA[:]
        for item in dictB:
            if not item in dictA:
                dictC.append(item)
    else:     
        dictC = {}
        for item in dictA.keys():
            dictC[item] = dictA[item]
        for item in dictB.keys():
            if not item in dictA.keys():
                dictC[item] = dictB[item]
    return dictC

A = {1: 'a', 2: 'b', 3: 'c'}
B = {1: 'c', 4: 'e'}
print(addDict(A, B))
C = [1, 2, 3]
D = [4, 5, 6]
print(addDict(C, D))