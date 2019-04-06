# -*- coding: cp936 -*-
# Exercise 5.5

from Tkinter import *
root = Tk()
c = Canvas(root, width=550, height=400, bg='gray')
c.pack()
c.create_text(300, 200, text="�Ӵ����İ���ҹ")
c.create_text(300, 300, text="������������¥")
c.create_text(300, 300, text="\u4efb\u4ed6\u660e\u6708\u4e0b\u897f\u697c")
root.mainloop()
