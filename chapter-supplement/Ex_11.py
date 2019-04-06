# Exercise 11

def getString():
    inputStr = raw_input("Please input a string... >>>")
    return inputStr

def getChar():
    inputChar = raw_input("Please input a character to be replaced... >>>")
    if len(inputChar) == 1:
        return inputChar
    else:
        return

def replaceString(replacedString, replacingChar):
    counter = 0
#   print 'Length: ', len(replacedString)
    newString = ""
    for i in range(len(replacedString)):
        if replacedString[i] != replacingChar:
            newString += replacedString[i]
        else:
            counter += 1
    return newString, counter

def main():
    replacedString = getString()
    replacingChar = getChar()
    print 'Result:', replaceString(replacedString, replacingChar)

if __name__ == '__main__':
    main()
