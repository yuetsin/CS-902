# Exercise 3.20

numberAmount = 0
for i in range(1, 1001):
    if i % 3 == 0 and i % 5 != 0:
        # print i
        numberAmount += 1
print "There are", numberAmount, "numbers in total."
