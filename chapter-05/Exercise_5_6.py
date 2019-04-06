# Exercise 5.6

from Tkinter import *
root = Tk()
c = Canvas(root, width=550, height=400, bg='gray')
c.pack()
centralPoint = (300, 175)
colors = ['yellow', 'red', 'blue', 'black', 'white']
i = 0
while i < 5:
    c.create_oval(275 - i * 20, 275 - i * 20, 200 +
                  i * 20, 200 + i * 20, fill='', outline=colors[i], width=8)
    i += 1
root.mainloop()
