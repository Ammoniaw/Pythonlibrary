# -*- coding: utf-8 -*-
# @Time : 2022/9/13 1:46
# @Author : AmmoniaW
# @File : 001 在窗口内输出文本.py
from tkinter import *
root = Tk()
root.title("Say Hello")

# 使得屏幕自动居中
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
height = 600
width = 800
x = (screenWidth - width) // 2
y = (screenHeight - height) // 2
root.geometry(f"{width}x{height}+{x}+{y}")
# 屏幕的背景颜色
root.configure(bg="green")

# LabelWidget输出文本
label = Label(root, text="I like Tkinter!")
label.pack()  # 包装和定位组件
print(type(label))  # <class 'tkinter.Label'>

root.mainloop()