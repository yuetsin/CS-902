# Exercise 9.5

from random import random

def throwOneTime():
    x = 2 * random() - 1
    y = 2 * random() - 1
    if x ** 2 + y ** 2 <= 1:
        return True
    else:
        return False

def main():
    times = input("How many times do you want to throw? >>> ")
    n = h = 0
    for i in range(times):
        if throwOneTime():
            h += 1
        n += 1
    print "Pi is approximately", (4.0 * h / n)

if __name__ == '__main__':
    main()
