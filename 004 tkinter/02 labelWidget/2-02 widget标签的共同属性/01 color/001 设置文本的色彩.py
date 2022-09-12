# -*- coding: utf-8 -*-
# @Time : 2022/9/13 1:53
# @Author : AmmoniaW
# @File : 001 设置文本的色彩.py
"""
fg/foreground : 设置前置色彩
bg/background : 设置背景色彩
"""
from tkinter import *

root = Tk()
root.title("Say Hello")

# LabelWidget输出文本
label = Label(root, text="Hello World!",
              fg="blue", bg="yellow")
label.pack()  # 包装和定位组件
print(type(label))  # <class 'tkinter.Label'>

root.mainloop()
