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
if __name__ == '__main__':
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
    print(Fore.RED+Back.WHITE+"请输抢座标记(可选，不输入预约明天座位,按回车继续!) \n")
    flag = str(input(""))
    if(flag == ''):
        flag = True
    else:
        flag = False
    print(Fore.GREEN+Back.WHITE+api.run(cookie,floor,seat,flag))
    print(Fore.RED+Back.WHITE+"回车退出!\n")
    exit = str(input(""))

