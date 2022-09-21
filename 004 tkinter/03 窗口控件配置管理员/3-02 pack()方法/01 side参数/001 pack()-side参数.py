# -*- coding: utf-8 -*-
# @Time : 2022/9/22 2:18
# @Author : AmmoniaW
# @File : 001 pack()-side参数.py
"""
最常用的控件配置管理方法，使用相对位置的概念处理widget控件配置，至于控件的正确位置则是由pack()方法自动完成
语法格式：
    pack(options,...)
options:
    side:可以垂直或水平配置控件
"""

# 当有多个组件时，可以让组件由上往下排列显示

from tkinter import *


root = Tk()
root.title('pack()方法默认设置')
colors = ['lightyellow', 'lightblue', 'lightgreen']
universities = ['明志科技大学', '长庚大学', '天下第一大学']
labs = []

for i in range(3):
    label = Label(root, text=universities[i], bg=colors[i])
    labs.append(label)

for i in labs:
    i.pack()


root.mainloop()