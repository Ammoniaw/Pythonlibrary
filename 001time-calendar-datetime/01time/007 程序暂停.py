"""
@author: AmmoniaL
@software: PyCharm
@file: 007 程序暂停.py
@time: 2022/8/31 0:11
"""
import time

# time.sleep()
"""
time 
def sleep(secs: float) - 可以是浮点数
 -> None  - 没有返回值
sleep(seconds)
Delay execution for a given number of seconds. The argument may be a floating point number for subsecond precis
延迟运行
"""
for i in range(1,10):
    print(f'{i}秒经过')
    time.sleep(1)