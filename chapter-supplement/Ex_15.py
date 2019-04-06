# Exercise 15

debugMode = True
upperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerLetters = "abcdefghijklmnopqrstuvwxyz"
def log(info):
    if debugMode:
        print "Log:", info
def smartTimes(occurTimes):
    if occurTimes == 0 or occurTimes == 1:
        return 'time'
    else:
        return 'times'
log("Initializing Data List...")
rawWordList = []
rawLineList = []
dictList = []
countList = []
givenList = []
givenCountList = []
f = file("Ex_15.txt")
poem = ""
log("Reading File Stream...")
rawLineList = f.readlines()
for i in rawLineList:
    poem += i
f.close()
log("Formatting Text... (Step 1)")
poem = poem.replace("\n", " ")
log("Formatting Text... (Step 2)")
for i in range(26):
    poem = poem.replace(upperLetters[i], lowerLetters[i])
currWord = ""
log("Parsing Words...")
for i in poem:
    if i in lowerLetters or i == "'":
        currWord += i
    else:
        if currWord != "":
            rawWordList.append(currWord)
            currWord = ""
log("Analysing Word Frequency...")
for rawWord in rawWordList:
    if rawWord in dictList:
        countList[dictList.index(rawWord)] += 1
    else:
        dictList.append(rawWord)
        countList.append(1)
log("Correctness Checking...")
if len(dictList) != len(countList):
    log("ERROR!")
    exit()
log("Sorting Dictionary...")
for i in range(len(countList)):
    swapFlag = True
    for j in range(len(countList) - i - 1):
        if countList[j] < countList[j + 1]:
            countList[j], countList[j + 1] = countList[j + 1], countList[j]
            dictList[j], dictList[j + 1] = dictList[j + 1], dictList[j]
            swapFlag = False
    if swapFlag:
        break
print 'Analysing Complete!'
for i in range(10):
    print 'No.', (i + 1), 'most frequent:', dictList[i], '(' + str(countList[i]) , smartTimes(countList[i]) + ')'
print '--------------------------'
for i in range(10):
    print 'No.', (i + 1), 'least frequent:', dictList[len(countList) - 10 + i], '(' + str(countList[len(countList) - 10 + i]) , smartTimes(countList[len(countList) - 10 + i]) + ')'
print '--------------------------'
givenLength = input("Please input a length of word that you want to search: >>>")
for i in dictList:
    if len(i) == givenLength:
        givenList.append(i)
if givenList == []:
    print 'No matched result.'
else:
    for i in givenList:
        givenCountList.append(countList[dictList.index(i)])
    for i in range(len(givenList)):
        swapFlag = True
        for j in range(len(givenList) - i - 1):
            if givenCountList[j] < givenCountList[j + 1]:
                givenList[j], givenList[j + 1] = givenList[j + 1], givenList[j]
                givenCountList[j], givenCountList[j + 1] = givenCountList[j + 1], givenCountList[j]
                swapFlag = False
        if swapFlag:
            break
    print 'Among', givenLength, 'length words,'
    print 'The most frequent word is "' + givenList[0] + '", occured', givenCountList[0], smartTimes(givenCountList[0]) + '.'
    print 'The least frequent word is "' + givenList[-1] + '", occured', givenCountList[-1], smartTimes(givenCountList[-1]) + '.'
print '--------------------------'
index = int(input("Input 1 to 10 and check in which lines these words occured. >>>"))
for i in range(len(rawLineList)):
    rawLineList[i] = ' ' + rawLineList[i].replace(',', '').replace('.', '') + ' '
if index in range(1, 11):
    print 'You selected the word "' + dictList[index - 1] + '".'
    searchWord = ' ' + dictList[index - 1] + ' '
    count = 0
    for i in range(len(rawLineList)):
        if searchWord in rawLineList[i]:
            count += 1
            print 'Occured', count, 'time in line', i + 1
else:
    print 'Invalid input.'
