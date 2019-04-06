# Exercise 3.22

approximatePi = 0.0
calculateIndex = 1
currentItem = 0.0
previousItem = 0.0
while True:
    previousItem = currentItem
    currentItem = 1.0 / (2 * calculateIndex - 1)
    if calculateIndex % 2 == 1:
        approximatePi += currentItem
        # print "+", currentItem
    else:
        approximatePi -= currentItem
        # print "-", currentItem
    if calculateIndex != 1 and abs(currentItem - previousItem) < 0.000000001:
        approximatePi *= 4
        break
    # print "                       = ", approximatePi
    calculateIndex += 1
print "Pi is approximately", approximatePi
