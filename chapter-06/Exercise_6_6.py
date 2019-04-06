# Exercise 6.6
from random import random
def count(aList, x):
    countTimes = 0
    for item in aList:
        if item == x:
            countTimes += 1
    return countTimes

def isIn(aList, x):
    for item in aList:
        if item == x:
            return True
    return False

def getIndex(aList, x):
    iterIndex = 0
    for item in aList:
        if item == x:
            return iterIndex
        iterIndex += 1
    return -1

def reverseList(aList):
    listSize = len(aList)
    iterIndex = listSize - 1
    reversedList = listSize * [""]
    for item in aList:
        reversedList[iterIndex] = item
        iterIndex -= 1
    return reversedList

def main():
    print "You may use count(aList, x)"
    print "You may use isIn(aList, x)"
    print "You may use getIndex(aList, x)"
    print "You may use reverseList(aList)"

main()
