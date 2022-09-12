# -*- coding: utf-8 -*-
# @Time : 2022/9/13 2:14
# @Author : AmmoniaW
# @File : 4-01justify参数使用.py
"""
标签的输出中，如果是多行的输出，在最后一行输出时可以使用
justify参数设置所输出的标签内容是left/center/right
（靠左/居中/靠右），默认是居中输出。

"""
from tkinter import *

root = Tk()
root.title("Say Hello")

# LabelWidget输出文本
label = Label(root, text="abcdefghijklmnopqrsyuvwxyz",
              fg="blue", bg="yellow",
              wraplength='40',  # 达到40像素自动换行 不指定justify参数时，默认最后一行居中对齐进行输出
              justify="left")  # 左对齐输出最后一行
label.pack()
print(type(label))

root.mainloop()
