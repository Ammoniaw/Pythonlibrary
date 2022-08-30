"""
@author: AmmoniaL
@software: PyCharm
@file: 006 获取当前的程序运行的时间.py
@time: 2022/8/31 0:04
"""
import time

# time.process_time()
"""
time 
def process_time() -> float
process_time() -> float
Process time for profiling: sum of the kernel and user-space CPU time.
"""
start = time.process_time()
for i in range(1, 1000000):
    print(i)
end = time.process_time()

run_time = end - start
print(run_time)  # 4.796875
