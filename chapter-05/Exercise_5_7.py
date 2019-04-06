# Exercise 5.7

from Tkinter import *
root = Tk()
radius = 50
c = Canvas(root, width=400, height=265, bg='gray')
c.pack()


def myDrawOval(x, y, color):
    c.create_oval(x, y, x + radius, y + radius,
                  fill="", outline=color, width=5)


myDrawOval(50, 58, 'blue')
myDrawOval(116, 58, 'black')
myDrawOval(182, 58, 'red')
myDrawOval(84, 90, 'yellow')
myDrawOval(151, 90, 'green')
root.mainloop()
