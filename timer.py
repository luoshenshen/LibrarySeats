'''
@ project: LibrarySeats
@ file: timer
@ user: 罗申申
@ email: luoshenshen@buaa.edu.cn
@ tool: PyCharm
@ time: 2021/5/27 11:15
'''
import time

def times():
    localtime = time.localtime(time.time())
    hour = localtime.tm_hour
    min = localtime.tm_min
    sec = localtime.tm_sec
    return hour,min,sec