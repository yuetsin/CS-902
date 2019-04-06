# Exercise 3.16

def Fibonacci(number):
    if number > 2:
        return (Fibonacci(number - 1) + Fibonacci (number - 2))
    else:
        return 1
    
circulateIndex = 0
while True:
    circulateIndex += 1
    result = Fibonacci(circulateIndex)
    if result > 100:
        print result, "is the smallest fibonacci number beyond 100."
        break

