# Exercise 5.10

from Tkinter import *

capitalAmount = input("Please input the capital money: >>> ")
interestRate = input("Please input the interest rate (%): >>> ")
totalFee = capitalAmount * 1.0
interestRate /= 100.0
layout = 30
rectWidth = 40

root = Tk()
c = Canvas(root, width = 800, height = 500, bg = "white")
c.pack()
for i in range(10):
    totalFee += round(totalFee * interestRate, 2)
#   print "year", i + 1, totalFee
    c.create_rectangle(layout * 3 + (layout + rectWidth) * i, 400 - layout - totalFee / 5, layout * 2 + (layout + rectWidth) * i + 1, 400 - layout, fill = 'pink')
    c.create_text(layout * 2.3 + (layout + rectWidth) * i + 1, 400 - layout + 30, text = ("%0.2f" % totalFee))
root.mainloop()
