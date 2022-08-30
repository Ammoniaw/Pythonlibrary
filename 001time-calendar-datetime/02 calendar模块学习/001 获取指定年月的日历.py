"""
@author: AmmoniaL
@software: PyCharm
@file: 001 获取指定年月的日历.py
@time: 2022/8/31 0:19
"""
import calendar

# calendar.month(year, month)

now_calendar = calendar.month(2022,8)
print(now_calendar)
"""
    August 2022
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
"""

# 案例实现：获取当年的每一个月份的日历
for i in range(1,13):
    month = calendar.month(2022, i)
    print(month)