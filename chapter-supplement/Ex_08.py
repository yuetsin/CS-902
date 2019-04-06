# Exercise 8

def isLilyNum(number):
    if number >= 100 and number <= 999:
        numA = number / 100
        numB = (number - numA * 100) / 10
        numC = number - numA * 100 - numB * 10
        if numA ** 3 + numB ** 3 + numC ** 3 == number:
            return True
    return False

for i in range(100, 1000):
    if isLilyNum(i):
        print i, 'is a Lily Number.'
