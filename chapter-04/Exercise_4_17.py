# Exercise 4.17

from math import *
# 40 Lines, 100 Columns
Lines = 30
Columns = 100
SineSheet = []
for i in range(Columns + 1):
    SineSheet.append([])
    for j in range(Lines + 1): 
        SineSheet[i].append(" ")
# print SineSheet
def getValue(i):
    if i >= 0 and i <= 100:
        return sin(i * 2 * pi / 100)
for x in range(Columns):
    y = Lines / 2 - int(getValue(x) * (Lines / 2))
#   print x, y
    SineSheet[x][y] = "*"

for j in range(Lines + 1):
    line = ""
    for i in range(Columns + 1):
        line += SineSheet[i][j]
    print line
