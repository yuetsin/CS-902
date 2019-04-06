# Exercise 6

length = input("Please input a number... >>>")
oppositeFlag = False
initialNumber = 1
resultNumber = 0.0
exprString = ""
if length > 2:
    for i in range(1, length + 1):
        if oppositeFlag:
            resultNumber -= 1.0 / i
            exprString += ('-1/' + str(i))
        else:
            resultNumber += 1.0 / i
            if i != 1:
                exprString += ('+1/' + str(i))
            else:
                exprString += '1'
        oppositeFlag = not oppositeFlag
print exprString, '=', ("%.6f" % (resultNumber))