# Exercise 4.15

def slope(pA, pB):
    slp = (pA[1] - pB[1]) * 1.0 / (pA[0] - pB[0])
    return slp
def intercept(pA, pB):
    intcpt = pA[1] - slope(pA, pB) * pA[0]
    return intcpt
pointA = input("Please input the coordinate of the point A as (0, 0): >>>")
pointB = input("Please input the coordinate of the point B as (0, 0): >>>")
try:
    print "Slope is", slope(pointA, pointB)
    print "Intercept is", intercept(pointA, pointB)
except TypeError:
    print "\nType Error!"
except ZeroDivisionError:
    print "\nCan't be divided by Zero!"
except:
    print "\nSomething went wrong!"
