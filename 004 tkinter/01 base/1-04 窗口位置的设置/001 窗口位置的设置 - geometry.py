# -*- coding: utf-8 -*-
# @Time : 2022/9/13 1:30
# @Author : AmmoniaW
# @File : 001 窗口位置的设置 - geometry.py
from tkinter import *
root = Tk()
root.title("Say Hello")
# root.geometry("300x160+20+20")  # 修改参数体验不同的位置
# 使用另外一种方式体会参数的不同之处会对绘制窗口的大小和位置带来何种改变

height = 600  # 所要绘制的窗口的高度
width = 800   # 所要绘制窗口的宽度
x = 200       # 窗口左上角的距离屏幕左边框的距离（左上角的横坐标）
y = 100       # 窗口左上角的距离屏幕上边框的距离（左上角的纵坐标）

root.geometry(f"{width}x{height}+{x}+{y}")

root.configure(bg="green")



root.mainloop()