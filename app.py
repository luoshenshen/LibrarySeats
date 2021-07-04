'''
@ project: LibrarySeats
@ file: app
@ user: 罗申申
@ email: luoshenshen@buaa.edu.cn
@ tool: PyCharm
@ time: 2021/5/23 18:39
'''
import re
import function
import browser_tools
import time

def run(cookie,floor,key,flag):
    result = function.session_get(browser_tools.index_url, browser_tools.get_index_header(cookie,time.time()))
    if '来选座' not in result.text:
        return "进入来选座系统失败，Cookie不正确"
    result = function.session_get(browser_tools.center_url, browser_tools.get_center_header(cookie,time.time()))
    nick = re.findall('<div class="nick">(.*)</div>', result.text)[0]
    result = function.session_get(browser_tools.prereserve_url, browser_tools.get_prereserve_header(cookie,time.time()))
    if nick in result.text or "预约明天的座位" in result.text:
        return function.fecth(cookie,floor,key,flag)
    else:
        return "进入来选座系统失败，Cookie不正确"