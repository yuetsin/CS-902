# Exercise 2

inputStr = raw_input("Please input a string... >>>")
if len(inputStr) < 2:
    print 'Split result:', inputStr
else:
    splitPoint = len(inputStr) / 2
    print 'Split result:'
    print inputStr[:splitPoint]
    print inputStr[splitPoint:]