# -*- coding: utf-8 -*-
# @Time : 2022/9/13 2:48
# @Author : AmmoniaW
# @File : 001 设置gif图像到控件中.py
"""
图片可以应用在许多地方，例如标签、功能按钮、选项按钮、文字区域等。在使用前可以用PhotoImage( )方法建立图像对象，然后再将此对象应用在其他窗口组件上
imageObj = PhotoImage(file="xxx.gif")   # 传回图像对象
Label( )方法内使用“image=imageObj”参数设置此图像对象。
"""
from tkinter import *

root = Tk()
root.title("gif显示")

gifTest = PhotoImage(file=r"./gif_test.gif")

# 使用Label方法
label = Label(root, image=gifTest)
label.pack()

root.mainloop()
