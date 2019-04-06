# Exercise 10.2

from random import random

numberList = [1, 5, 2, 4, 7, 26, 7, 4, 2, 78, 3, 2, 284, 276, -1]

def generateRandom():
    a = int(len(numberList) * random())
    b = int(len(numberList) * random())
    c = int(len(numberList) * random())
    return a, b, c

def getMaxMinNum(numberList):
    if len(numberList) == 2:
        print 'ends with', numberList
        return
    a, b, c = generateRandom()
    while a == b or b == c or a == c:
        a, b, c = generateRandom()
    # print 'generated', a, b, c
    if numberList[a] < numberList[b] and numberList[b] < numberList[c]:
        numberList.pop(b)
    getMaxMinNum(numberList)


def main():
     getMaxMinNum(numberList)

main()
