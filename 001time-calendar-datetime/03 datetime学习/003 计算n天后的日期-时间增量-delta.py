# -*- coding: utf-8 -*-
# @Time : 2022/8/31 9:53
# @Author : AmmoniaW
# @File : 003 计算n天后的日期-时间增量-delta.py
import datetime

# 计算指定时间增量（间隔）后的时间
feature_time = datetime.datetime.today() + datetime.timedelta(days=2)
print(type(feature_time))
print(feature_time)  # 2022-09-02 09:54:48.409620

# datetime.timedelta() 使用
"""
datetime.timedelta def __init__(self,
             days: float = ...,
             seconds: float = ...,
             microseconds: float = ..., - 毫秒
             milliseconds: float = ..., - 毫秒
             minutes: float = ...,
             hours: float = ...,
             weeks: float = ...,
             *,
             fold: int = ...) -> None
Represent the difference between two datetime objects.
表示两个时间之间的差异
Supported operators:
add, subtract timedelta
unary plus, minus, abs
compare to timedelta
multiply, divide by int
In addition, datetime supports subtraction of two datetime objects returning a timedelta, and addition or subtraction of a datetime and a timedelta giving a datetime.
此外，日期时间支持两个返回时间增量的日期时间对象相减，以及一个日期时间和一个时间增量的加法或减法给出一个日期时间
Representation: (days, seconds, microseconds). Why? Because I felt like it.
不要你觉得，而是我觉得 - 好家伙，黄晓明是吧
"""

# 示例说明 - 还是使用关键字参数保险一些
time1 = datetime.timedelta(days=1, hours=12, minutes=56, seconds=13)
time2 = datetime.timedelta(days=1, hours=10, minutes=45)
difference_time = time1 - time2
print(difference_time)  # 2:11:13
