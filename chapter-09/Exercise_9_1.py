# Exercise 9.1
from random import random
from random import randrange
def getShootingResult():
    return int(random() * 11)

def getFloatRandom():
    return random() - 0.5

def getDiceResult():
    return int(random() * 6) + 1

def getTwoDiceResult():
    return (getDiceResult(), getDiceResult())

def main():
    print "You may use these functions: "
    print "getShootingResult() ... 0 arguments, returns an integer between 0 and 10"
    print "getFloatRandom() ... 0 arguments, returns a float number between -0.5 and 0.5"
    print "getDiceResult() ... 0 arguments, returns an integer between 1 and 6"
    print "getTwoDiceResult() ... 0 arguments, returns a tuple contains two integers between 1 and 6"

if __name__ == '__main__':
    main()
