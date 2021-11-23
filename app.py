'''
@ project: LibrarySeats
@ file: app
@ user: 罗申申
@ email: luoshenshen@buaa.edu.cn
@ tool: PyCharm
@ time: 2021/6/14 10:27
'''
#-*- coding:utf-8 -*-
import api
import os
import ntplib
import time

ntp_server_url = 'ntp5.aliyun.com'

def get_ntp_time(ntp_server_url):
    """
    通过ntp server获取网络时间
    :param ntp_server_url: 传入的服务器的地址
    :return: time.strftime()格式化后的时间和日期
    """

    ntp_client = ntplib.NTPClient()
    ntp_stats = ntp_client.request(ntp_server_url)
    fmt_time = time.strftime('%X', time.localtime(ntp_stats.tx_time))
    fmt_date = time.strftime('%Y-%m-%d', time.localtime(ntp_stats.tx_time))
    return fmt_time, fmt_date


def set_system_time(new_time, new_date):
    """
    通过os.system来设置时间,需要管理员权限
    :param new_time:
    :param new_date
    :return: 无返回值
    """
    os.system('time {}'.format(new_time))
    os.system('date {}'.format(new_date))

if __name__ == '__main__':
    ntp_server_time, ntp_server_date = get_ntp_time(ntp_server_url)
    set_system_time(ntp_server_time, ntp_server_date)
    print('时间已经与{}同步'.format(ntp_server_url))
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
    print("""
    ***************************************************************************************
    *                                                                                     *
    *                                                                                     *
    *                                      来选座V1.0                                      *
    *                                      @author: luoshenshen                           *
    *                                                                                     *
    ***************************************************************************************
    """)
    print(Fore.RED+Back.WHITE+"请输入WeChatID,按回车继续!\n")
    cookie = str(input())
    print(Fore.RED+Back.WHITE+"请输入楼层(五位数字，可以进系统楼复制链接查看libid即楼层五位数字,按回车继续!): \n")
    floor = str(input(""))
    print(Fore.RED+Back.WHITE+"请输座位号(可选，不输入随机安排一个空位置,按回车继续!) \n")
    seat = str(input(""))
    #print(Fore.RED+Back.WHITE+"请输抢座标记(可选，不输入预约明天座位,按回车继续!) \n")
    flag = ''
    if(flag == ''):
        flag = True
    else:
        flag = False
    print(Fore.GREEN+Back.WHITE+api.run(cookie,floor,seat,flag))
    print(Fore.RED+Back.WHITE+"回车退出!\n")
    exit = str(input(""))

