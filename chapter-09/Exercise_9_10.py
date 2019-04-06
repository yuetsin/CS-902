# Exercise 9.10

import thread

def isPrime(n):
    print "Judging", n, "..."
    for i in range(1, int(n / 2) + 1):
        if n % i == 0 and n / i != 0:
            return False
    return True

def CalculatePrimes(start, end):
    amount = 0
    for i in range(start, end + 1):
        if isPrime(i):
            amount += 1
    print start, '-', end, 'there are', amount, 'prime numbers'

thread.start_new_thread(CalculatePrimes, (2, 10000000))
thread.start_new_thread(CalculatePrimes, (10000000, 20000000))
