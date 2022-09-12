# -*- coding: utf-8 -*-
# @Time : 2022/9/13 2:05
# @Author : AmmoniaW
# @File : 3-01 使得标签中的文字达到指定像素宽度后自动换行.py
from tkinter import *

root = Tk()
root.title("Say Hello")

# LabelWidget输出文本
label = Label(root, text="Hello World!",
              fg="blue", bg="yellow",
              height=3, width=15,
              anchor="sw",
              wraplength=40)  # 标签中的文字达到40像素宽度后自动换行
label.pack()
print(type(label))

root.mainloop()
