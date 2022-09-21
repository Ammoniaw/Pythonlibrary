# -*- coding: utf-8 -*-
# @Time : 2022/9/22 2:33
# @Author : AmmoniaW
# @File : 002 修改pack()方法side参数.py
"""
options:
    TOP:默认由上往下
    BOTTOM:由下往上
    LEFT: 由左往右排列
    RIGHT:由右往左排列

pack(side="")
"""
from tkinter import *

root = Tk()
root.title('pack()方法默认设置')
colors = ['lightyellow', 'lightblue', 'lightgreen']
universities = ['明志科技大学', '长庚大学', '天下第一大学']
labs = []

for i in range(3):
    label = Label(root, text=universities[i], bg=colors[i])
    labs.append(label)
sides = [TOP, RIGHT, LEFT]
for i in range(len(labs)):
    labs[i].pack(side=sides[i])

root.mainloop()