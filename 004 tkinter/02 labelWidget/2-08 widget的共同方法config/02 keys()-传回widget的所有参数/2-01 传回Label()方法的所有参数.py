# -*- coding: utf-8 -*-
# @Time : 2022/9/22 1:58
# @Author : AmmoniaW
# @File : 2-01 传回Label()方法的所有参数.py
from tkinter import *
root = Tk()
root.title("使用keys()方法传回widget的所有参数")
label=Label(root, text='I like Tkinter!')
label.pack()
print(label.keys())
"""
['activebackground', 'activeforeground', 'anchor', 'background', 'bd', 'bg', 'bitmap', 'borderwidth', 'compound', 'cursor', 'disabledforeground', 'fg', 'font', 'foreground', 'height', 'highlightbackground', 'highlightcolor', 'highlightthickness', 'image', 'justify', 'padx', 'pady', 'relief', 'state', 'takefocus', 'text', 'textvariable', 'underline', 'width', 'wraplength']

"""

root.mainloop()