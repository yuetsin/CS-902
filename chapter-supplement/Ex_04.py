# Exercise 4

def convertToChar(rawNum):
    ordNum = int(rawNum)
    if ordNum <= 255 and ordNum >= 0:
        return chr(ordNum)
    else:
        return '--ERR--'

inputStr = raw_input("Please input a series of numbers.\nLength must be 3x.\n>>>")
resultStr = ''
correctness = True
if len(inputStr) % 3 != 0:
    print 'Invalid input!'
    correctness = False
else:
    for i in range(len(inputStr) / 3):
        stepCon = convertToChar(inputStr[i * 3 : i * 3 + 3])
        if stepCon != '--ERR--':
            resultStr += stepCon
        else:
            correctness = False
            break
if correctness:
    print 'Convert Result is:', resultStr
else:
    print 'Something went wrong during the convert progress.'
    print 'Check your number range and length.'
