# Exercsie 5.12

from time import sleep
from math import sin
from math import cos
from math import sqrt
from Tkinter import *
dividedParts = int(input("Please input the parts you want to divide: >>> "))
lastX = 275
lastY = 50
currRotateAngle = 0
Pi = 3.141592653589
lineLength = 50

if dividedParts > 20 or dividedParts < 10:
    print "Too big or small"
    sleep(1.0)
    exit()

root = Tk()
c = Canvas(root, width = 550, height = 400, bg = 'white')
c.pack()

for i in range(dividedParts):
    currRotateAngle += 2 * Pi * 1 / dividedParts
    c.create_line(lastX, lastY, lastX + lineLength * cos(currRotateAngle), lastY + lineLength * sin(currRotateAngle))
    lastX += lineLength * cos(currRotateAngle)
    lastY += lineLength * sin(currRotateAngle)
#   print lastX, lastY, currRotateAngle
root.mainloop()
