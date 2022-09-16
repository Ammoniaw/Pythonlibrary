# -*- coding: utf-8 -*-
# @Time : 2022/9/15 18:11
# @Author : AmmoniaW
# @File : 01 Python中文件路径的简单操作.py
import os
result = os.path.join('demo', 'test.txt')
print(result)  # demo\test.txt

# 1. 将文件名列表中的名称添加到文件夹路径的后面

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    # 实现路径和文件的路径拼接 \\ 表示转义符号
    print(os.path.join('C:\\demo\\exercise', filename))


