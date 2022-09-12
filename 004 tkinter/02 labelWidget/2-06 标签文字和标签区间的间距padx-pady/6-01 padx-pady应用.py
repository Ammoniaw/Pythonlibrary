# -*- coding: utf-8 -*-
# @Time : 2022/9/13 2:39
# @Author : AmmoniaW
# @File : 6-01 padx-pady应用.py
"""
在设计标签或其他Widget控件时，若是不设置Widget的大小，系统将使用最适空间作为此Widget的大小,
可以使用width & height 自动设置Widget的大小
其实也可以通过设置标签文字与标签区间的间距，达到更改标签区间的目的。padx可以设置标签文字左右边界与标签区间的x轴间距，pady可以设置标签文字上下边界与标签区间的y轴间距。
"""

from tkinter import *

root = Tk()
root.title("6-01 padx-pady标签内间距的设置")
label = Label(root, text="raised", relief="raised",
              bg="lightyellow",
              padx=5, pady=10)  # 在自适应控件大小的基础之上，设置控件内部的左右及上下的间距
label.pack()
root.mainloop()
