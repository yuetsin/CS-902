# Exercise 3.19

dataAmount = int(input("Please input the amount of the data: "))
dataBase = range(1, dataAmount + 1)
sumUp = 0
passAmount = 0
for i in range(1, dataAmount):
    print "Please input number", i, ": ",
    currentScore = int(input())
    dataBase[i] = currentScore
    if currentScore >= 60:
        sumUp += currentScore
        passAmount += 1
print "Total pass number sum up:", sumUp
if passAmount != 1 and passAmount != 0:
    print passAmount, "students passed the exam"
elif passAmount == 1:
    print passAmount, "student passed the exam"
else:
    print "No student passed the exam"
