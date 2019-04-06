from random import random
from math import log
maxSize = 100
leftPossibility = 0.7
boardSize = int(input("输入钉板的栅格数目："))
ballCount = int(input("输入倒入的小球数目："))
resultList = [0] * boardSize
if boardSize < maxSize:
    for i in range(ballCount):
        currLoc = 0;
        for j in range(boardSize - 1):
            if random() > leftPossibility:
                currLoc += 1
        resultList[currLoc] += 1
    for i in resultList:
        # print(str(i) + '\t' + "*" * int((i / (log(ballCount) ** 2))))
        print(str(i))
    sumUp = 0
    for i in resultList:
        sumUp += i
    average = sumUp * 1.0 / boardSize
    sSquare = 0.0
    for i in resultList:
        sSquare += (i - average) ** 2
    sSquare /= (boardSize - 1)
    print("平均值是：", average)
    print("方差是：", sSquare)