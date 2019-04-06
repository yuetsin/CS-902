# Exercise 10

# Yang Hui Triangle

from math import factorial, log

def getInteger():
    num = int(eval(raw_input("Please input a integer: >>> ")))
    if num > 1:
        return num
    else:
        return 0;

def comb(m, n):
    return factorial(m) / (factorial(n) * factorial(m - n))

def printEndLine():
    print

def printOneLine(lineIndex, fixedSize = '__default__'):
    if fixedSize == '__default__':
        maxSize = int(log(comb(lineIndex, int(round(lineIndex / 2.0))), 10) + 1)
    else:
        maxSize = fixedSize
    for i in range(lineIndex + 1):
        currNum = comb(lineIndex, i)
        currSize = int(log(currNum, 10)) + 1
        print currNum, ' ' * (maxSize - currSize),

def printSpaces(spaceAmount):
    print ' ' * spaceAmount,

def main():
    lines = getInteger()
    realMaxSize = int(log(comb(lines, int(round(lines / 2.0))), 10) + 1)
    if realMaxSize % 2 == 0:
        realMaxSize += 1
    for i in range(lines):
        printSpaces((realMaxSize) * (lines - i - 1) - (lines - i - 1) / 2)
        printOneLine(i, realMaxSize)
        printEndLine()

if __name__ == '__main__':
    main()
