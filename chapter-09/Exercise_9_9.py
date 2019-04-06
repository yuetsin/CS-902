# Exercise 9.9

from random import random
from math import sin
from math import cos

def oneStep():
    stepAngle = random() * 6.283185307178
    return (cos(stepAngle), sin(stepAngle))

def goHiking(steps):
    Xpos = Ypos = 0
    for i in range(steps):
        Movement = oneStep()
        Xpos += Movement[0]
        Ypos += Movement[1]
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
