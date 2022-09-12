# -*- coding: utf-8 -*-
# @Time : 2022/9/13 2:00
# @Author : AmmoniaW
# @File : 001 anchor输出位置设置.py
from tkinter import *

root = Tk()
root.title("Say Hello")

# LabelWidget输出文本
label = Label(root, text="Hello World!",
              fg="blue", bg="yellow",
              height=3, width=15,
              anchor="sw")  # 此处就是控制标签的位置在西南即左下角处
"""
也可以使用常量 SW，因为在导入tkinter模块的时候就使用全部导入的方式
"""

label.pack()
print(type(label))

root.mainloop()
