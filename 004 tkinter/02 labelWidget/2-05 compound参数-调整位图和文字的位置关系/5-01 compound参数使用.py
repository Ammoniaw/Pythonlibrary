# -*- coding: utf-8 -*-
# @Time : 2022/9/13 2:24
# @Author : AmmoniaW
# @File : 5-01 compound参数使用.py
"""
图像与文字共存时，可以使用此参数定义文字与图像的位置关系。compound参数可以是下列值。
left        图像在左
right       图像在右
center      图像在文字下方
top         图像在文字的上方
bottom      图像在文字的下方
"""
from tkinter import *

root = Tk()
root.title("bitmaps")

# label显示位图
label = Label(root, bitmap="hourglass",
              compound="left", text="沙漏")

label.pack()

root.mainloop()
