"""
@author: AmmoniaL
@software: PyCharm
@file: 004 格式化时间字符串-时间元组.py
@time: 2022/8/30 23:23
"""
import time
now_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(now_time_str)  # 2022-08-30 23:25:04

# 常用格式符
# %X-表示本地的时间表示
local_time = time.strftime("%X", time.localtime())
print(local_time)  # 23:27:35
#  %x-表示本地的时间表示
local_time = time.strftime("%x", time.localtime())
print(local_time)  # 08/30/22

# %c - 表示本地的相应的日期表示和时间表示 - 类似于 asctime()
local_time = time.strftime("%c", time.localtime())
print(local_time)  # Tue Aug 30 23:30:41 2022
