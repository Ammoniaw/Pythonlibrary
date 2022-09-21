# -*- coding: utf-8 -*-
# @Time : 2022/9/22 2:43
# @Author : AmmoniaW
# @File : 003 将widget的常用属性relief列出来.py
"""
relief:
    表示控件的边框样式
使用pack()方法和side参数
"""
from tkinter import *

root = Tk()
Reliefs = ['flat', 'groove', 'raised', 'ridge', 'solid', 'sunken']
for Relief in Reliefs:
    label = Label(root, text=Relief, relief=Relief,fg="blue", font="Times 20 bold")
    label.pack(side=LEFT, padx=5)


root.mainloop()