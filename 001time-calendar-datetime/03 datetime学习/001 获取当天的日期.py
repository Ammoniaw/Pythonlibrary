# -*- coding: utf-8 -*-
# @Time : 2022/8/31 9:40
# @Author : AmmoniaW
# @File : 001 获取当天的日期.py

import datetime

# 1. datetime.datetime.now()

print(datetime.datetime.now())  # 2022-08-31 09:46:54.151470

# 2. datetime.datetime.today()
now_time = datetime.datetime.today()
print(now_time)  # 2022-08-31 09:47:35.573102
