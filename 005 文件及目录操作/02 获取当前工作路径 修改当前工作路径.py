# -*- coding: utf-8 -*-
# @Time : 2022/9/15 18:25
# @Author : AmmoniaW
# @File : 02 keys()-传回widget的所有参数 获取当前工作路径 修改当前工作路径.py
import os

# 1. 获取当前的工作目录
workDir = os.getcwd()
print(workDir)  # C:\Users\Ammonia\Desktop\My CS Study\Pythonlibrary\005 文件及目录操作

# 2. 修改当前的工作路径-跳转到别的路径下
os.chdir('D:\\chrome_download')
workDir = os.getcwd()
print(workDir)              # D:\chrome_download

# 3.当要跳转的目录并不存在的时候 会抛出FileNotFoundError
os.chdir('error')

