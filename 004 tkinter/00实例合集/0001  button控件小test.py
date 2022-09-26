# -*- coding: utf-8 -*-
# @Time : 2022/9/25 11:07
# @Author : AmmoniaW
# @File : 0001  button控件小test.py
from tkinter import *

root = Tk()

root.title('模拟button点击生成label控件')


# 创建一个函数 功能是生成一个label_widget
def create_label():
    str1 = '你是一个大砂锅'
    while str1:
        test_label = Label(root, text=str1[0], fg="blue", bg="yellow")
        test_label.pack(side="left")
        str1 = str1[1:]


test_button = Button(root, text="click me! Create a label widget", command=create_label)
test_button.pack()

root.mainloop()
