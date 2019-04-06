# Exercise 5.11

from Tkinter import *
from random import *
root = Tk()
c = Canvas(root, width = 550, height = 400, bg = 'lightblue')
c.pack()
c.create_polygon((0,200), (550, 300), (550,400), (0,400), outline = '', fill = 'gray')
c.create_oval(75, 83, 75 + 75, 83 + 75, fill = 'white', outline = '')
c.create_oval(57, 146, 57 + 116, 146 + 116, fill = 'white', outline = '')
for i in range(500):
    x = random() * 550
    y = random() * 400
    c.create_rectangle(x, y, x + 1, y + 1, fill = 'white', outline = 'white')
root.mainloop()
