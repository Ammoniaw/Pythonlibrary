"""
@author: AmmoniaL
@software: PyCharm
@file: 001 获取当前的时间戳.py
@time: 2022/8/30 22:08
"""
import time

# 获取当前的时间戳
now_time = time.time()

# 进行验证一下-现在是2022年 - 一年大概365天，每天都是24小时每小时60分钟每分钟60秒
years = now_time / (24 * 60 * 60 * 365) + 1970
print(years)  # 2022.6975097291415  -- 还是听准确的
