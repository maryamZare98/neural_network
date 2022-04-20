import numpy as np


def weight(yIn, target, threshold, learningRate, nodesValue, weights):
    if yIn < -threshold:
        yIn = -1

    elif yIn > threshold:
        yIn = 1

    else:
        yIn = 0

    if yIn != target:
        weights[-1] += (learningRate * target)
        for i in range(len(nodesValue)):
            weights[i] += target * nodesValue[i]

    return weights


def data(inputTable, target, threshold=0.2, learningRate=1):
    print("*---------------------------------*")
    trainingSetLenght = len(inputTable)
    inputNodeLenght = len(inputTable[0])
    print("NodesVal:", trainingSetLenght)
    print("sample training:", inputNodeLenght)
    weights = np.zeros(len(inputTable[0]) + 1)
    print("*---------------------------------*")
    print("initW", weights)
    print("*---------------------------------*")


    repeat = True
    while repeat:

        logicW = [[], [], [], []]
        for i in range(trainingSetLenght):

            yIn = weights[-1]
            for j in range(inputNodeLenght):
                yIn += (inputTable[i][j] * weights[j])

            a = weight(yIn, target[i], threshold, learningRate, inputTable[i], weights)
            logicW[i].extend(a)
        print("Weights: ", logicW)
        print("*---------------------------------*")

        count = 0
        for k in range(len(logicW)):
            if round(np.linalg.norm(logicW[0])**2) == round(np.linalg.norm(logicW[k])**2):
                count += 1

        if count == trainingSetLenght:
            repeat = False



data(
    [
        [1, 1], [1, -1], [-1, 1], [-1, -1]
    ],

    [
        1, -1, -1, -1
    ]
)

