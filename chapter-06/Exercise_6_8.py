# Exercise 6.8

def getPrimeNumber(limitNumber):
    rawList = range(2, limitNumber + 1)
    primeList = []
    while rawList != []:
        currItem = rawList[0]
        maxTimes = int((limitNumber) * 1.0 / currItem) + 1
        primeList.append(currItem)
        for i in range(1, maxTimes + 1):
            try:
                rawList.remove(i * currItem)
            except:
                pass
    return primeList
        


def main():
    print "This program can find all prime numbers in a certain range."
    limitNumber = int(input("Please input a integer as an upper limit of the search: >>> "))
    if limitNumber >= 2 and limitNumber <= 2 ** 31:
        print getPrimeNumber(limitNumber)
    else:
        print "What a STRANGE number..."

main()
