# Exercise 7

from math import factorial
epsilon = 10e-15
result = 0
calcIndex = 0
while True:
    pieceAdded = 1.0 / factorial(calcIndex)
    result += pieceAdded
    calcIndex += 1
    if pieceAdded < epsilon:
        break
print 'e is approximately', result
