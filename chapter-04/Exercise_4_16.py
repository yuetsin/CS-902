# calendar.py
rawListAlign = []
listIterator = 0
for i in range(96):
    rawListAlign.append("")
# print rawListAlign

def getYear():
    global listIterator
    print "This program prints the calendar of a given year."
    year = input("Please enter a year (after 1900): ")
    return year
def firstDay(year):
    global listIterator
    k = leapyears(year)
    n = (year - 1900) * 365 + k
    return (n + 1) % 7
def leapyears(year):
    global listIterator
    count = 0
    for y in range(1900,year):
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            count = count + 1
    return count
def printCalendar(year,w):
    global listIterator
    print
    print "=========== " + str(year) + " =========="
    first = w
    for month in range(12):
        heading(month)
        first = oneMonth(year,month,first)
def heading(m):
    global listIterator
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
    rawListAlign[listIterator] += "            %s             " % (months[m])
    listIterator += 1
    rawListAlign[listIterator] += "Mon Tue Wed Thu Fri Sat Sun "
    listIterator += 1
def oneMonth(year,month,first):
    global listIterator
    d = days(year,month)
    frame = layout(first,d)
    printMonth(frame)
    return (first + d) % 7
def days(y,m):
    global listIterator
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    d = month_days[m]
    if (m == 1) and (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)):
        d = d + 1
    return d
def layout(first,d):
    global listIterator
    frame = 42 * [""]
    if first == 0:
        first = 7
    j = first - 1
    for i in range(1,d+1):
        frame[j] = i
        j = j + 1
    return frame
def printMonth(frame):
    global listIterator
    for i in range(42):
        rawListAlign[listIterator] += "%3s " % (frame[i])
        if (i+1) % 7 == 0:
            listIterator += 1
def printFixedCalendar():
    for i in range(4):
        for j in range(8):
            print rawListAlign[i * 24 + j], "  ", rawListAlign[i * 24 + j + 8], "  ", rawListAlign[i * 24 + j + 16]
def main():
    global listIterator
    year = getYear()
    w = firstDay(year)
    printCalendar(year,w)
    printFixedCalendar()
main()
