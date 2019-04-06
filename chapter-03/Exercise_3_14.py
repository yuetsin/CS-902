# Exercise 3.14

inputYear = int(input("Please enter a year: >>> "))
if inputYear % 400 == 0:
    isLeapYear = True
else:
    if inputYear % 100 == 0:
        isLeapYear = False
    elif inputYear % 4 == 0:
        isLeapYear = True
    else:
        isLeapYear = False

if isLeapYear:
    print inputYear, "is a leap year."
else:
    print inputYear, "is a common year."
