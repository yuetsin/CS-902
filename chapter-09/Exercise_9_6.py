# Exercise 9.6

from random import random

def throwOneDice():
    return int(random() * 6) + 1

def throwSixDices():
    currNum = throwOneDice()
    for i in range(5):
        prevNum = currNum
        currNum = throwOneDice()
        if prevNum != currNum:
            return False
    return True

def main():
    times = input("How many times do you want to throw? >>> ")
    Win = 0.0
    for i in range(times):
        if throwSixDices():
            Win += 1
    print "Possibility is approximately", (Win / times)

if __name__ == '__main__':
    main()
