# -*- coding: utf-8 -*-
 # Exercise 10.3

import time

def oldLinearSearch(aList, anIndex):
    for i in range(len(aList)):
         if aList[i] == anIndex:
             return i
    return -1

def newLinearSearch(aList, anIndex):
    aList.append(anIndex)
    for i in range(len(aList)):
        if aList[i] == anIndex:
            break
    if i == len(aList):
        return -1
    else:
        return i

def main():
    lis = [4,6,1,4,6,3,6,4,3,8,5,3,89,5,3,3,8,4,3,2,6,8]
    ind = 1
    # Not in the list
    jud = raw_input("Input 1 for the older search and 2 for the newer one >>> ")
    if jud == '1':
        time.clock()
        oldLinearSearch(lis, ind)
        print time.clock(), '秒'
    else:
        time.clock()
        newLinearSearch(lis, ind)
        print time.clock(), '秒'

main()
