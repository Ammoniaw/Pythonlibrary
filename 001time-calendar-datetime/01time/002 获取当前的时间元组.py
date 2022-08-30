"""
@author: AmmoniaL
@software: PyCharm
@file: 002 获取当前的时间元组.py
@time: 2022/8/30 22:18
"""

import time
"""
time 
def localtime(secs: float | None = ...)  -- 参数就是时间戳，浮点值
-> struct_time - 返回时间元组
localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
tm_sec,tm_wday,tm_yday,tm_isdst)
Convert seconds since the Epoch to a time tuple expressing local time. When 'seconds' is not passed in, convert the current time instead.
不提供参数时，默认转换当前的时间戳
"""
# 获取当前的时间元组信息
now_time = time.localtime()
print(type(now_time))  # <class 'time.struct_time'>
print(now_time)
"""
# time.struct_time(tm_year=2022, tm_mon=8, tm_mday=30, tm_hour=22, tm_min=20, tm_sec=38, tm_wday=1, tm_yday=242, tm_isdst=0)
对时间元组的解读：
    2022-8-30-22-20-38-Tuesday-242
"""

# 示例 将当前时间戳的前一天，转换为时间元组
yesterday_time = time.time() - 24 * 60 * 60

# 使用time.localtime()转化为昨天的时间元组
yesterday_struct = time.localtime(yesterday_time)
print(yesterday_struct)
"""
time.struct_time(tm_year=2022, tm_mon=8, tm_mday=29, tm_hour=22, tm_min=27, tm_sec=8, tm_wday=0, tm_yday=241, tm_isdst=0)
"""
