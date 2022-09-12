# -*- coding: utf-8 -*-
# @Time : 2022/9/13 1:14
# @Author : AmmoniaW
# @File : 001 设置窗口的标题及大小.py
from tkinter import *
root = Tk()
root.title("My First Tkinter Window")

root.geometry("300x160")  # 设置窗口大小

"""
tkinter.Wm
def wm_geometry(self, newGeometry: Any = None) -> Any
Set geometry to NEWGEOMETRY of the form =widthxheight+x+y. Return current value if None is given.
注意特殊的使用形式
"""
root.configure(bg="yellow")  # 设置窗口背景颜色

root.mainloop()

