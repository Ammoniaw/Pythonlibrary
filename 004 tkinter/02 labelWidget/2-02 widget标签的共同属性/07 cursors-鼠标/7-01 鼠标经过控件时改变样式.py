# -*- coding: utf-8 -*-
# @Time : 2022/9/22 1:52
# @Author : AmmoniaW
# @File : 7-01 鼠标经过控件时改变样式.py
from tkinter import *

root = Tk()
root.title("改变鼠标的样式")
label = Label(root, text="\n\n\nraised\n\n\n", relief="raised",
              bg="lightyellow",
              cursor="heart")           # 光标形状
label.pack()



root.mainloop()