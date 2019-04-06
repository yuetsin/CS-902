# Exercise 5.8
print "Please input the number r and y: "
r = input("r >>> ")
y = input("y >>> ")
from math import *
from Tkinter import *
root = Tk()
c = Canvas(root, width=550, height=400, bg='gray')
c.pack()

c.create_oval(275 - r, 200 - r, 275 + r, 200 + r, fill='', outline='black')
c.create_line(0, y, 550, y, fill='black')
iteratorX = 0
while iteratorX < 550:
    if (iteratorX <= 275 + r) and (iteratorX >= 275 - r):
        ovalYA = 200.0 + sqrt(pow(r, 2) - pow((275 - iteratorX), 2))
        ovalYB = 200.0 - sqrt(pow(r, 2) - pow((275 - iteratorX), 2))
        if (abs(y - ovalYA) < 1) or (abs(y - ovalYB) < 1):
            print '(', iteratorX, ',', y, ')'
    iteratorX += 1
print 'END'
root.mainloop()
