# -*- coding: utf-8 -*-
# @Time : 2022/9/13 2:19
# @Author : AmmoniaW
# @File : 5-01 在标签放置内置位图.py
from tkinter import *

root = Tk()
root.title("bitmaps")

# label显示位图
label = Label(root, bitmap="hourglass")

label.pack()
print(type(label))

root.mainloop()
