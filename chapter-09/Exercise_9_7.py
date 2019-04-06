# Exercise 9.7

from random import random

def oneStep():
    if random() > 0.5:
        return True
    else:
        return False

def goHiking(steps):
    Pos = 0
    for i in range(steps):
        if oneStep():
            Pos += 1
        else:
            Pos -= 1
    return Pos

def main():
    times = input("How many times do you want to go hiking? >>> ")
    steps = input("How many steps do you want to go hiking? >>> ")
    totalNum = 0.0
    for i in range(times):
        totalNum += goHiking(steps)
    print "Final destination will be about", (totalNum / times)

if __name__ == '__main__':
    main()
