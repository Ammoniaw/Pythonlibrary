# -*- coding: utf-8 -*-
# @Time : 2022/9/13 3:05
# @Author : AmmoniaW
# @File : 002 标签内显示jpg文件.py

"""
如果想要在标签内显示jpg文件，需要借助PIL模块的Image和ImageTk模块

"""

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("jpg显示")

image = Image.open("./wolf.jpeg")
jpgTest = ImageTk.PhotoImage(image)

# 使用Label方法
label = Label(root, image=jpgTest)
label.pack()

root.mainloop()
