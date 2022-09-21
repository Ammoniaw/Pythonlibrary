"""
@author: AmmoniaL
@software: PyCharm
@file: 003 格式化时间.py
@time: 2022/8/30 22:53
"""
import time

# 1. 将时间戳格式化时间  ctime()
"""
time 
def ctime(secs: float | None = ...) -> str 
ctime(seconds) -> string - 返回一个字符串
Convert a time in seconds since the Epoch to a string in local time. This is equivalent to asctime(localtime(seconds)). When the time tuple is not present, current time as returned by localtime() is used
当没有时间元组时，这相当于 asctime(localtime(seconds))。
"""
now_time = time.time()

now = time.ctime(now_time)
print(now)  # Tue Aug 30 22:54:51 2022
# 不提供参数给ctime()
now = time.ctime()
print(now)  # Tue Aug 30 22:54:51 2022

# 2. 将struct_time-时间元组格式化时间 - asctime()
"""
time def asctime(t: Tuple[int, int, int, int, int, int, int, int, int] | struct_time = ...)
  -> str - 返回一个字符串格式
asctime([tuple]) -> string
Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'. 
When the time tuple is not present, current time as returned by localtime() is used
默认使用localtime()提供的当前的时间元组信息
"""
now_struct_time = time.localtime()
now = time.asctime(now_struct_time)
print(now)  # Tue Aug 30 22:56:33 2022

# 不提供任何参数给asctime()
now_time = time.asctime()
print(now_time)  # Tue Aug 30 23:02 keys()-传回widget的所有参数:28 2022
