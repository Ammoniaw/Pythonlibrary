# -*- coding: utf-8 -*-
# @Time : 2022/8/31 10:09
# @Author : AmmoniaW
# @File : 004 获取连个日期时间的时间差.py
import datetime
"""

"""
first_time = datetime.datetime(2022,8,31,12,0,0)
print(type(first_time))  # <class 'datetime.datetime'>
now_time = datetime.datetime(2022,8,31,10,0,0)
difference_time = first_time - now_time
print(difference_time)  # 2:00:00

# 使用这个total_seconds()方法查看一下
print(difference_time.total_seconds())  # 7200.0