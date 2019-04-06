# Exercise 9.4

from random import random

def throwOneDice():
    return int(random() * 6) + 1

def throwTwoDices():
    return throwOneDice() + throwOneDice()

def oneGame():
    d = throwTwoDices()
    if d == 2 or d == 3 or d == 12:
        return False
    if d == 7 or d == 11:
        return True
    numberP = d
    while True:
        d = throwTwoDices()
        if d == numberP:
            return True
        if d == 7:
            return False

def manyGames(times):
    winGame = loseGame = 0
    for i in range(times):
        if oneGame():
            winGame += 1
        else:
            loseGame += 1
    print "Win", winGame, "Lose", loseGame

def main():
    times = input("Please input the times you want to play: >>> ")
    manyGames(times)

if __name__ == '__main__':
    main()
