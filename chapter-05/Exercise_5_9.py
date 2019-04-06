# Exercise 5.9
from math import *
from Tkinter import *

windowWidth = 550
windowHeight = 400
margin = 100

funcType = ''


def getValue(x, width, height):
    global funcType
    if funcType == 'sin':
        return height / 2.0 - sin((x * 1.0 / width) * 2 * pi) * (height / 2.0)
    elif funcType == 'cos':
        return height / 2.0 - cos((x * 1.0 / width) * 2 * pi) * (height / 2.0)
    elif funcType == 'tan':
        return height / 2.0 - tan((x * 1.0 / width) * 2 * pi) * (height / 2.0)
    elif funcType == 'sinh':
        return height / 2.0 - sinh((x * 1.0 / width) * 2 * pi) * (height / 2.0)
    elif funcType == 'cosh':
        return height / 2.0 - cosh((x * 1.0 / width) * 2 * pi) * (height / 2.0)
    elif funcType == 'tanh':
        return height / 2.0 - tanh((x * 1.0 / width) * 2 * pi) * (height / 2.0)
    else:
        return height / 2.0


funcType = raw_input(
    "Please input the type of the funcion: 'sin', 'cos' or 'tan': >>> ")
root = Tk()
c = Canvas(root,
           width=windowWidth + 2 * margin,
           height=windowHeight + 2 * margin,
           bg='gray')
c.pack()
i = 0
while i < 10 * windowWidth:
    c.create_rectangle(i / 10.0 + margin,
                       getValue(i / 10.0, windowWidth,
                                windowHeight) + margin,
                       i / 10.0 + 1 + margin,
                       getValue(i / 10.0, windowWidth,
                                windowHeight) + 1 + margin,
                       outline='black', width=1, fill='')
    i += 1
root.mainloop()
