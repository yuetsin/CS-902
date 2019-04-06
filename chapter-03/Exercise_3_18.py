# Exercise 3.18

goodPrice = float(input("Please enter the price of the goods... >>> "))
goodPrice = int(goodPrice % 1.0 * 100)
coinNumber = 0
def getChanges(denomination):
    global goodPrice, coinNumber
    coinNumber += int(goodPrice / denomination)
    goodPrice = goodPrice % denomination
    if goodPrice == 0:
        return False
    else:
        return True

for i in [50, 20, 10, 5, 2, 1]:
    if not getChanges(i):
        break
print "The total coin number is", coinNumber
