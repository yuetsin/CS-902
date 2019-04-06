# Exercise 2.13
from math import *
x1 = float(input("Now, please enter the x axis of the first point: "))
y1 = float(input("Now, please enter the y axis of the first point: "))
x2 = float(input("Now, please enter the x axis of the second point: "))
y2 = float(input("Now, please enter the y axis of the second point: "))
distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("The distance between (", x1, ",", y1, ") and (", x2, ",", y2,") is", distance, end = "")
