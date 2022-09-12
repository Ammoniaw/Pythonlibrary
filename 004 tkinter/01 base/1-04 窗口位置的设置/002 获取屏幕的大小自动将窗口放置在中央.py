# -*- coding: utf-8 -*-
# @Time : 2022/9/13 1:37
# @Author : AmmoniaW
# @File : 002 获取屏幕的大小自动将窗口放置在中央.py
from tkinter import *
root = Tk()
root.title("Say Hello")

# 获取屏幕的长宽
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

height = 600  # 所要绘制的窗口的高度
width = 800   # 所要绘制窗口的宽度

# 调用geometry()方法 使得绘制的窗口自动居于屏幕的中间
x = (screenWidth - width) // 2
y = (screenHeight - height) // 2


root.geometry(f"{width}x{height}+{x}+{y}")

root.configure(bg="green")



root.mainloop()