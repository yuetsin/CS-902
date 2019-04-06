# Exercise 3.13

scores = int(input("Please enter your score: >>> "))
if scores > 100 or scores < 0:
    ranking = "???"
elif scores >= 90 and scores <= 100:
    ranking = "A"
elif scores >= 80 and scores < 90:
    ranking = "B"
elif scores >= 70 and scores < 80:
    ranking = "C"
elif scores >= 60 and scores < 70:
    ranking = "D"
else:
    ranking = "F"
print "Your ranking is", ranking
