"""
@author: AmmoniaL
@software: PyCharm
@file: 005 时间元组-格式化时间字符串.py
@time: 2022/8/30 23:39
"""
import time

# 将格式化字符串转化为时间元组 time.strptime()
"""
time 
def strptime(string: str,
             format: str = ...) -> struct_time
strptime(string, format) -> struct_time
"""
time_str = "2022-08-30 22:30:53"
struct_time1 = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
print(struct_time1)
"""
time.struct_time(tm_year=2022, tm_mon=8, tm_mday=30, tm_hour=22, tm_min=30, tm_sec=53, tm_wday=1, tm_yday=242, tm_isdst=-1)
"""
# 将时间元组-》为时间戳
"""
time def mktime(t: Tuple[int, int, int, int, int, int, int, int, int] | struct_time)
  -> float
mktime(tuple) -> floating point numbe  -  将时间元组-》为时间戳
"""
now_seconds = time.mktime(struct_time1)
print(now_seconds)  # 1661869853.0

# 编程实现01：将"09-02-2018 02:06:00" 转换为 "2018-09-02 02:06:00"
old_time_str = "09-02-2018 02:06:00"
# 首先转化为时间元组
old_struct_time = time.strptime(old_time_str, "%m-%d-%Y %H:%M:%S")
print(old_struct_time)
# 时间元组转化为时间格式字符串
new_time_str = time.strftime("%Y-%m-%d %H:%M:%S", old_struct_time)
print(new_time_str)  # 2018-09-02 02:06:00
