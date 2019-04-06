# Exercise 13

daysInMonthInCommonYears = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysInMonthInLeapYears = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthsName = ['January', 'February', 'March', 'April', 'May',' June', 'July', 'August', 'September', 'October', 'November',' December']
def isLeapYear(yearIndex):
    if yearIndex % 4 == 0:
        if yearIndex % 100 == 0:
            if yearIndex % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def getDate(year, day, daysList):
    for i in range(12):
        day -= daysList[i]
        if day <= 0:
            day += daysList[i]
            return i + 1, day

def getYearAndMonth():
    y = int(input("Please input the year number: >>>"))
    d = int(input("Please input the day number: >>>"))
    if y in range(1000, 3000) and d in range(1, 367):
        return y, d
    else:
        return

def main():
    year, day = getYearAndMonth()
    if isLeapYear(year):
        daysList = daysInMonthInLeapYears
    else:
        daysList = daysInMonthInCommonYears
    month, day = getDate(year, day, daysList)
    if day % 10 == 1:
        suffix = 'st'
    elif day % 10 == 2:
        suffix = 'nd'
    elif day % 10 == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print monthsName[month - 1], str(day) + suffix

if __name__ == '__main__':
    main()
