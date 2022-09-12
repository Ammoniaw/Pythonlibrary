# -*- coding: utf-8 -*-
# @Time : 2022/9/13 2:31
# @Author : AmmoniaW
# @File : 6-01 建立控件的边框.py
"""
flat: 无效果-平坦
groove: 凹槽
raised: 文本凸显
ridge: 边框凸显
solid: 边框加粗
sunken: 凹陷
"""

from tkinter import *

root = Tk()
root.title("6-01 relief属性设置控件的边框")
label = Label(root,text="raised", relief="raised").pack()

root.mainloop()