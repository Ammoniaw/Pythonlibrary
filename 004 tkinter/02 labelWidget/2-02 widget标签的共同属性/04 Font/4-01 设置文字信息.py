# -*- coding: utf-8 -*-
# @Time : 2022/9/13 2:08
# @Author : AmmoniaW
# @File : 4-01 设置文字信息.py
from tkinter import *

root = Tk()
root.title("Say Hello")

# LabelWidget输出文本
label = Label(root, text="Hello World!",
              fg="blue", bg="yellow",
              height=3, width=15,
              font="Helvetic 20 bold")  # 设置字形为Helvetic 大小为20 粗体显示(也可以使用元组来指定参数)
label.pack()
print(type(label))

root.mainloop()
