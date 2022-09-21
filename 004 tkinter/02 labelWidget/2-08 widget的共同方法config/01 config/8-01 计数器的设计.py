# -*- coding: utf-8 -*-
# @Time : 2022/9/22 1:27
# @Author : AmmoniaW
# @File : 8-01 计数器的设计.py
from tkinter import *

counter = -60


def run_counter(digit):
    def counting():
        global counter                      # 定义全局变量，在局部修改变量时，全局变量counter就会发生改变
        counter += 1
        digit.config(text=str(counter))     # 更改控件的中的文本内容列出数字内容
        digit.after(1000, counting)         # 间隔一秒后，调用counting-表示隔一秒会调用第二个参数注明的方法

    counting()                              # 持续调用


root = Tk()
root.title('计数器设置')
digit = Label(root, bg='yellow', fg='blue',
              height=3, width=10,
              font="Helvetic 20 bold")
digit.pack()
run_counter(digit)

root.mainloop()
