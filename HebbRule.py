import numpy as np

inputTable = [
    [1, 1, 1],
    [1, -1, 1],
    [-1, 1, 1],
    [-1, -1, 1]
]

andTable = [
    [1],
    [-1],
    [-1],
    [-1]
]

orTable = [
    [1],
    [1],
    [1],
    [-1]
]

notANDtable = [
    [1],
    [1],
    [-1],
    [1]
]


def hebbRule(var):
    initWeights = np.array([0, 0, 0])
    for i in range(0, 4):
        a = var[i][0]
        newInput = [i * a for i in inputTable[i]]
        initWeights += newInput
    return (initWeights)


print(hebbRule(andTable))
print(hebbRule(orTable))
print(hebbRule(notANDtable))
