"""
@ project: LibrarySeats
@ file: utils
@ user: ShenshenLuo
@ email: luoshenshen@buaa.edu.cn
@ tool: PyCharm
@ time: 2022/1/10 21:49
"""
import requests

# 避免新手半角输入有问题
def get_seat_time(time):
    if "：" in time:
        return time.split("：")
    if ":" in time:
        return time.split(":")
