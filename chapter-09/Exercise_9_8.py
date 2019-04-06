# Exercise 9.8

from random import random

def oneStep():
    randomFact = random()
    if randomFact > 0.75:
        return (1, 0)
    elif randomFact > 0.5:
        return (0, 1)
    elif randomFact > 0.25:
        return (-1, 0)
    else:
        return (0, -1)

def goHiking(steps):
    Xpos = Ypos = 0
    for i in range(steps):
        Movement = oneStep()
        if Movement == (1, 0):
            Xpos += 1
        elif Movement == (0, 1):
            Ypos += 1
        elif Movement == (-1, 0):
            Xpos -= 1
        elif Movement == (0, -1):
            Ypos -= 1
    return (Xpos, Ypos)

def main():
    times = input("How many times do you want to go hiking? >>> ")
    steps = input("How many steps do you want to go hiking? >>> ")
    totalX = totalY = 0.0
    move = goHiking(steps)
    for i in range(times):
        totalX += move[0]
        totalY += move[1]
    print "Final destination will be about", totalX / times, totalY / times

if __name__ == '__main__':
    main()
