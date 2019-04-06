# Exercise 9.3

from random import random
class Player:
    def __init__(self, scorePossibility):
        self.scorePos = scorePossibility
        self.isServeBall = False
        self.matches = 0
    def oneScore(self):
        self.score += 1
    def clearMatches(self):
        self.matches = 0

p1, p2 = Player(0.6), Player(0.5)

def changeServe():
    p1.isServeBall = not p1.isServeBall
    p2.isServeBall = not p2.isServeBall
    if p1.isServeBall == p2.isServeBall:
        if random() > 0.5:
            p1.isServeBall = not p1.isServeBall
        else:
            p2.isServeBall = not p2.isServeBall

def oneGame(isNewRule):
    changeServe()
    scoreA = scoreB = 0
    while scoreA != 21 and scoreB != 21:
        if p1.isServeBall == True:
            if random() < p1.scorePos:
                scoreA += 1
            else:
                if isNewRule:
                    scoreB += 1
            changeServe()
        elif p2.isServeBall == True:
            if random() < p2.scorePos:
                scoreB += 1
            else:
                if isNewRule:
                    scoreA += 1
            changeServe()
        else:
            print "Error! Nobody Serves the Ball!"
            return
    return scoreA, scoreB

def oneMatch(isNewRule):
    gameOver = [(3, 0), (0, 3), (3, 1), (1, 3), (3, 2), (2, 3)]
    gameA = gameB = 0
    while not(gameA, gameB) in gameOver:
        pointA, pointB = oneGame(isNewRule)
        if pointA > pointB:
            gameA += 1
        else:
            gameB += 1
    return gameA, gameB

def manyMatches(times, isNewRule):
    for i in range(times):
        gameA, gameB = oneMatch(isNewRule)
        if gameA > gameB:
            p1.matches += 1
        else:
            p2.matches += 1
    if isNewRule:
        print "New Rule, ", p1.matches, p2.matches
    else:
        print "Old Rule, ", p1.matches, p2.matches
manyMatches(1000, True)
p1.clearMatches()
p2.clearMatches()
manyMatches(1000, False)
