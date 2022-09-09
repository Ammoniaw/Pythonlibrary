# -*- coding: utf-8 -*-
# @Time : 2022/9/10 2:24
# @Author : AmmoniaW
# @File : 001draw_circle.py
import pgzrun


def draw():
    screen.fill('green')
    screen.draw.filled_circle((400, 300), 50, 'yellow')


pgzrun.go()
