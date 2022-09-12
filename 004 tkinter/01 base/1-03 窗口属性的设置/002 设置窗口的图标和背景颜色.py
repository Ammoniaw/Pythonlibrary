# -*- coding: utf-8 -*-
# @Time : 2022/9/13 1:20
# @Author : AmmoniaW
# @File : 002 设置窗口的图标和背景颜色.py
from tkinter import *
root = Tk()
root.configure(bg="#00ff00")  # 16进制的颜色表示方式

# 更改tkinter的默认窗口图标
root.iconbitmap(r"C:\Users\Ammonia\Desktop\My CS Study\Pythonlibrary\Instagram.ico")

root.mainloop()