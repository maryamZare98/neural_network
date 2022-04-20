import numpy as np

inputTable = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
print(f"input = \n{inputTable}")
print("-------------------------------")


def threshold(dot, T):
    if dot >= T:
        return 1
    else:
        return 0


def AND():
    weights = np.array([1, 1])
    print(f"Weight: {weights}")
    print("-------------------------------")
    dotProducts = np.dot(inputTable, weights)
    T = 2
    for i in range(0, 4):
        activation = threshold(dotProducts[i], T)
        print(f'Activation: {activation}')


def NAND():
    weights = np.array([1, 1])
    print(f"Weight: {weights}")
    print("-------------------------------")
    dotProducts = np.dot(inputTable, weights)
    T = 1
    for i in range(0, 4):
        activation = threshold(dotProducts[i], T)
        print(f'Activation: {activation}')


def NotAND():
    weights = np.array([2, -1])
    print(f"Weight: {weights}")
    print("-------------------------------")
    dotProducts = np.dot(inputTable, weights)
    T = 2
    for i in range(0, 4):
        activation = threshold(dotProducts[i], T)
        print(f'Activation: {activation}')


def OR():
    weights = np.array([1, 1])
    print(f"Weight: {weights}")
    print("-------------------------------")
    dotProducts = np.dot(inputTable, weights)
    T = 1
    for i in range(0, 4):
        activation = threshold(dotProducts[i], T)
        print(f'Activation: {activation}')


def NOR():
    weights = np.array([-1, -1])
    print(f"Weight: {weights}")
    print("-------------------------------")
    dotProducts = np.dot(inputTable, weights)
    T = 0
    for i in range(0, 4):
        activation = threshold(dotProducts[i], T)
        print(f'Activation: {activation}')


def XOR():
    weights = np.array([2, -1])
    dotProducts = np.dot(inputTable, weights)
    firstInput = []
    T = 2
    for i in range(0, 4):
        activation = threshold(dotProducts[i], T)
        firstInput.append(activation)
    weights = np.array([-1, 2])
    dotProducts = np.dot(inputTable, weights)
    secondInput = []
    T = 2
    for i in range(0, 4):
        activation = threshold(dotProducts[i], T)
        secondInput.append(activation)
    newInput = [], [], [], []
    for i in range(0, 4):
        newInput[i].append((firstInput[i], secondInput[i]))

    a = np.array(newInput)
    weights = np.array([2, 2])
    print(f"Weight: {weights}")
    print("-------------------------------")
    dotProducts = np.dot(a, weights)
    T = 2
    for i in range(0, 4):
        activation = threshold(dotProducts[i], T)
        print(f'Activation: {activation}')


AND()
# OR()
# NOR()
# NAND()
# NotAND()
# XOR()
