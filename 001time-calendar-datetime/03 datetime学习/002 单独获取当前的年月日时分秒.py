# -*- coding: utf-8 -*-
# @Time : 2022/8/31 9:48
# @Author : AmmoniaW
# @File : 002 单独获取当前的年月日时分秒.py
import datetime

# 获取到今天的时间信息
now_time = datetime.datetime.now()
print(type(now_time))  # <class 'datetime.datetime'>

print(now_time)
# 分别获取其中的年月日时分秒信息
year = now_time.year
month = now_time.month
day = now_time.day
hour = now_time.hour
minute = now_time.minute
second = now_time.second
print(year, month, day, hour, minute, second)  # 2022 8 31 9 52 12