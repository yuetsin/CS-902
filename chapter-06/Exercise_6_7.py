def shuffleList(aList, shuffleTimes):
    listSize = len(aList)
    for i in range(shuffleTimes):
        itemA = int(random() * listSize)
        itemB = int(random() * listSize)
        aList[itemA], aList[itemB] = aList[itemB], aList[itemA]
    return aList

def main():
    print "Use 'shuffleList(<list>, <int>Shuffle times) to shuffle the list."
    print "E.g. shuffleList(range(100), 100)"

main()
