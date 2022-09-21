# -*- coding: utf-8 -*-
# @Time : 2022/9/22 2:03
# @Author : AmmoniaW
# @File : 9-01 在标签间建立分割线.py
"""
Separator(父对象,options)
父对象：
    表示这个分割线建立在哪一个父对象内
options:
    HORIZONTAL: 水平分割线
    VERTICAL: 垂直分割线
"""
from tkinter import *
from tkinter.ttk import Separator

root = Tk()
root.title('在标签内建立分割线')
myTitle = '一个人的旅行'
myContent = """野兽先辈也就是田所浩二，你是一个一个一个。。。。。。"""

label = Label(root, text=myTitle, font="Helvetic 20 bold")
label.pack(padx=10, pady=10)

sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X, padx=5)                # 表示此分割线填满X轴，它与窗口边界左右相距5像素

lab2 = Label(root, text=myContent)
lab2.pack(padx=10, pady=10)

root.mainloop()