# Exercise 9

def isSelfInverseNumber(number):
    strType = str(number)
    if strType == strType[::-1]:
        return True
    else:
        return False

for i in range(100, 1000):
    if isSelfInverseNumber(i):
        print i, 'is a self inverse number.'
