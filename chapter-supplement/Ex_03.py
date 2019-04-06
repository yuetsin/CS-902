# Exercise 3

def encryptChar(ch):
    code = ord(ch) + 20
    if code > 126:
        code -= 95
        # Avoid Overflow
        # ASCII Code's visible characters range between 32 and 126
        # So minus 95
    return chr(code)

inputStr = raw_input("Please input the string you want to encrypt... >>>")

encryptedStr = ''
for i in range(len(inputStr)):
    encryptedStr += encryptChar(inputStr[i])
print encryptedStr
