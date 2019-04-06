# Exercise 6.5

def getInputs():
    d = []
    x = raw_input("Enter a number now, or press <Enter> to stop. >>> ")
    while x != "":
        d.append(eval(x))
        x = raw_input("Enter a number now, or press <Enter> to stop. >>> ")
    return d

def sumUp(numberList):
    totalSum = 0.0
    for item in numberList:
        totalSum += item
    return totalSum

def meanNum(numberList):
    return sumUp(numberList) / len(numberList)

def medianNum(numberList):
    numberList.sort()
    listSize = len(numberList)
    if listSize % 2 == 0:
        return (numberList[listSize / 2 - 1] + numberList[listSize / 2]) / 2.0
    else:
        return numberList[(listSize - 1) / 2]

def stdDeviation(numberList):
    listSize = len(numberList)
    stdDvi = 0.0
    avgNum = meanNum(numberList)
    for item in numberList:
        stdDvi += (item - avgNum) ** 2
    return stdDvi ** (0.5)

def main():
    print "This program can calculate sum, mean, median and standard deviation."
    data = getInputs()
    print "Sum: ", sumUp(data)
    print "Mean: ", meanNum(data)
    print "Median: ", medianNum(data)
    print "Standard Deviation: ", stdDeviation(data)

if __name__ == '__main__':
    main()
