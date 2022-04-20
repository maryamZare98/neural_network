import numpy as np


def weights(zIn, z, yIn, target, inputTable, learningRate, inputNodeLenght, weightsZ):
    if yIn >= 0:
        yIn = 1
    else:
        yIn = -1
    if target == yIn:
        print("no weight updates are performed.")
        print("*---------------------------------*")

    elif target == -1:
        for s in range(len(z)):
            weightsZ[s][-1] += (learningRate * (-1 - zIn[s]))
            for b in range(inputNodeLenght):
                if z[s] > 0:
                    weightsZ[s][b] += (learningRate * (-1 - zIn[s])) * inputTable[b]
        print(np.round(weightsZ, 4))
        print("*---------------------------------*")
    else:
        if abs(zIn[0]) < abs(zIn[1]):
            weightsZ[0][-1] += (learningRate * (1 - zIn[0]))
            for h in range(inputNodeLenght):
                weightsZ[0][h] += (learningRate * (1 - zIn[0])) * inputTable[h]
        else:
            weightsZ[1][-1] += (learningRate * (1 - zIn[1]))
            for h in range(inputNodeLenght):
                weightsZ[1][h] += (learningRate * (1 - zIn[1])) * inputTable[h]

        print(np.round(weightsZ, 4))
        print("*---------------------------------*")


def data(inputTable, target, learningRate=0.5):
    trainingSetLenght = len(inputTable)
    inputNodeLenght = len(inputTable[0])
    weightsY = [0.5, 0.5, 0.5]
    weightsZ = [
        [0.05, 0.2, 0.3],
        [0.1, 0.2, 0.15]
    ]
    print("*---------------------------------*")

    z = [[0], [0]]
    for i in range(trainingSetLenght):
        zIn = [
                weightsZ[0][-1],
                weightsZ[1][-1]
               ]

        for j in range(inputNodeLenght):
            for k in range(len(zIn)):
                zIn[j] += (inputTable[i][k] * weightsZ[j][k])

        for d in range(len(z)):
            if zIn[d] >= 0:
                z[d] = 1
            else:
                z[d] = -1

        yIn = weightsY[-1] + (z[0] * weightsY[0]) + (z[1] * weightsY[1])
        print(f"Epoch{i + 1}:")
        weights(zIn, z, yIn, target[i], inputTable[i], learningRate, inputNodeLenght, weightsZ)


data(
    [
        [1, 1], [1, -1], [-1, 1], [-1, -1]
    ],

    [
        -1, 1, 1, -1
    ]
)
