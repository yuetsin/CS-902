# Exercise 10.1

num = 0
while True:
    if num % 3 == 2:
        if num % 5 == 3:
            if num % 7 == 4:
                break
    num += 1
print num
