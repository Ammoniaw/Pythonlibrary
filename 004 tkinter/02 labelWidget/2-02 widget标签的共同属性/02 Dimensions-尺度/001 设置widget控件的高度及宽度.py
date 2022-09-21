# -*- coding: utf-8 -*-
# @Time : 2022/9/13 1:56
# @Author : AmmoniaW
# @File : 001 设置widget控件的高度及宽度.py
from tkinter import *

root = Tk()
root.title("Say Hello")

# LabelWidget输出文本
label = Label(root, text="Hello World!",
              fg="blue", bg="yellow",
              height=3,width=15)  # height:控制控件(这里是指Label)的高度，单位为字符的高度，width同理,单位为字符的宽度, 即3个字符的高度，15个字符的宽度
label.pack()  # 包装和定位组件
print(type(label))  # <class 'tkinter.Label'>

root.mainloop()
