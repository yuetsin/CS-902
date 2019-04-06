# Exercise 7.10

from random import *

suits = ['♠', '♦', '♥', '♣', 'Black', 'Red']

# suits.size = 6
# suits[4]/[5] should only be used with the 'Joker'

points = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'Joker']

# points.size = 14
# points[13] should only be used with 'Black'/'Red'

class Card:
    def __init__(self, suitIndex, pointIndex):
        self.suit = suits[suitIndex]
        self.point = points[pointIndex]
    def getSuit(self):
        return self.suit
    def setSuit(self,suitIndex):
        self.suit = suits[suitIndex]
    def getPoint(self):
        return self.point
    def setPoint(self,point):
        self.point = points[pointIndex]
    def printCard(self):
        print self.suit, self.point

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(13):
            for j in range(4):
                self.cards.append(Card(j, i))
        self.cards.append(Card(4, 13))
        # Add Black Joker
        self.cards.append(Card(5, 13))
        # Add Red Joker
    def shuffle(self):
        shuffle(self.cards)
    def getNextCard(self):
        return self.cards.pop()
    def moreCards(self):
        if len(self.cards) == 3:
            return self.cards
    def getRestCards(self):
        cardsOut = []
        for i in range(3):
            cardsOut.append(self.cards.pop())
        return cardsOut
    def setCards(self, cards):
        self.cards = cards
    def addCard(self, card):
        self.cards.append(card)

class Player:
    def __init__(self, id = 'John Smith'):
        self.id = id
        self.hand = []
        self.score = 0
    def addToHand(self, card):
        self.hand.append(card)
    def playCards(self, suitIndex, pointIndex):
        if Card(suits[suitIndex], points[pointIndex]) in self.hand:
            self.hand.remove(Card(suits[suitIndex], points[pointIndex]))
        else:
            print """
            -----------------------------HELP-----------------------------
            suits = ['Spade', 'Diamond', 'Heart', 'Club', 'Black', 'Red']

            # suits.size = 6
            # suits[4]/[5] should only be used with the 'Joker'

            points = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'Joker']

            # points.size = 14
            # points[13] should only be used with 'Black'/'Red'
            """
    def getID(self):
        return self.id
    def setID(self, id):
        self.id = id
    def getHand(self):
        return self.hand
    def setHand(self, hand):
        self.hand = hand
    def getScore(self):
        return self.score
    def setScore(self, score):
        self.score = score

def main():
    # A Sample Game
    d = Deck()
    d.shuffle()
    p1, p2, p3 = Player("Kyle"), Player("Kenny"), Player("Cartman")
    for i in range(17):
        p1.hand.append(d.getNextCard())
        p2.hand.append(d.getNextCard())
        p3.hand.append(d.getNextCard())
    print 'Now there are still 3 cards... Who will take them?'
    print p1.getID(), '?'
    print p2.getID(), '?'
    print p3.getID(), '?'
    for j in d.cards:
        j.printCard()
    p1.hand.append(d.getRestCards())
    print p1.getID(), 'takes them!'

if __name__ == '__main__':
    main()
else:
    print """
    -----------------------------HELP-----------------------------
    suits = ['Spade', 'Diamond', 'Heart', 'Club', 'Black', 'Red']

    # suits.size = 6
    # suits[4]/[5] should only be used with the 'Joker'

    points = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'Joker']

    # points.size = 14
    # points[13] should only be used with 'Black'/'Red'
    """
