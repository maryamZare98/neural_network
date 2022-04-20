import time
import math


def weight(yIn, target, toleranceE, learningRate, nodesValue, weights, error):
    weights[-1] += (learningRate * (target - yIn))
    for i in range(len(nodesValue)):
        weights[i] += (target - yIn) * nodesValue[i] * learningRate
        error[i] = round((target - yIn) ** 2, 3)

    return weights


def data(inputTable, target, toleranseE=0.38, learningRate=0.1):
    print("*---------------------------------*")
    trainingSetLenght = len(inputTable)
    inputNodeLenght = len(inputTable[0])
    print("NodesVal:", trainingSetLenght)
    print("sample training:", inputNodeLenght)
    weights = [0.1, 0.1, 0.1]
    error = [0, 0, 0]
    print("*---------------------------------*")
    print("initW", weights)
    print("*---------------------------------*")

    k = 0
    repeat = True
    while repeat:
        k += 1

        logicW = [[], [], [], []]
        for i in range(trainingSetLenght):

            yIn = weights[-1]
            for j in range(inputNodeLenght):
                yIn += (inputTable[i][j] * weights[j])

            a = weight(yIn, target[i], toleranseE, learningRate, inputTable[i], weights, error)
            logicW[i].extend(a)
        print(f"Weights {k}: ", logicW)
        print("E:", error[1])
        print("*---------------------------------*")

        time.sleep(1)

        count = 0
        if toleranseE < error[1]:
            count += 1

        else:
            repeat = False


data(
    [
        [1, 1], [1, -1], [-1, 1], [-1, -1]
    ],

    [
        1, 1, 1, -1
    ]
)
