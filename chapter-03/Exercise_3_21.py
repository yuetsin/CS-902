# Exercise 3.21

def Calculate():
    M = int(input("Please enter number M: "))
    N = int(input("Please enter number N: "))
    Sum = 0
    if M > N:
        temp = M
        M = N
        N = temp
    Index = M
    if Index % 2 == 0:
        Index += 1
    while Index <= N:
        Sum += Index
        Index += 2
    print "The result is: ", Sum

while True:
    Calculate()
    print "----------ONCE---AGAIN----------"
