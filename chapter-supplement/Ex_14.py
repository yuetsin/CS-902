# Exercise 14

prefetchList = []
def Fibonacci(n):
    if n <= len(prefetchList) and prefetchList[n] != 0:
        return prefetchList[n]
    else:
        for i in range(n - len(prefetchList)):
            prefetchList.append(0)
    if n >= 3:
        i = prefetchList[n - 2] = Fibonacci(n - 2)
        j = prefetchList[n - 1] = Fibonacci(n - 1)
        return i + j
    else:
        return 1

def main():
    print Fibonacci(input("Please input a integer: >>>"))

if __name__ == '__main__':
    main()
