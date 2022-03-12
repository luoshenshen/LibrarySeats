"""
@ project: LibrarySeats
@ file: window
@ user: ShenshenLuo
@ email: luoshenshen@buaa.edu.cn
@ tool: PyCharm
@ time: 2022/1/5 21:27
"""
import time
import tkinter as tk
from tkinter import ttk
import api
from function import seat_time

cookie = ''
floor = ''
seat = ''

warning_cookie = "Cookie 不能为空 :"
warning_floor = "楼层不能为空 :"
warning_seat = "座位不能为空 :"

root = tk.Tk()
label1 = tk.Label(root, text='输入微信来选座系统Cookie:')
label2 = tk.Label(root, text='输入微信来选座系统楼层:')
label3 = tk.Label(root, text='输入微信来选座系统座位号:')
label4 = tk.Label(root, text='默认明日选座,输入值则预选明日座位:')
label5 = tk.Label(root, text='输入选座时间（24小时格式 eg: 19:30）:')
label6 = tk.Label(root, text='选座结果:')

comboxlist1 = ttk.Combobox(root)
comboxlist2 = ttk.Combobox(root)


def window():
    root.title('微信来选座系统 LibrarySeats beta v0.1'+str(time.time()))
    root.geometry('900x600')
    # 设置标签信息

    label1.grid(row=0, column=0)

    label2.grid(row=1, column=0)

    label3.grid(row=2, column=0)

    label4.grid(row=3, column=0)

    label5.grid(row=4, column=0)

    label6.grid(row=8, column=0)

    # 创建输入框
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=2, padx=5, pady=5)
    # entry2 = tk.Entry(root)
    comboxlist1.grid(row=1, column=2, padx=5, pady=5)
    # entry3 = tk.Entry(root)
    # entry3.grid(row=2, column=2, padx=5, pady=5)
    comboxlist2.grid(row=2, column=2, padx=5, pady=5)

    entry2 = tk.Entry(root)
    entry2.grid(row=3, column=2, padx=5, pady=5)

    entry3 = tk.Entry(root)
    entry3.grid(row=4, column=2, padx=5, pady=5)

    # 创建按键
    def show():
        print('Cookie: %s' % entry1.get())
        cookie = entry1.get()
        if cookie == '':
            label1.config(text=warning_cookie)
            return
        else:
            label1.config(text="输入微信来选座系统Cookie:")
        # print('Floor：%s' % entry2.get())
        print(cookie)
        floor = comboxlist1.get()
        if floor == '':
            label2.config(text=warning_floor)
            return
        else:
            label2.config(text="输入微信来选座系统楼层:")
        print(floor)
        seat = comboxlist2.get()
        if seat == '':
            label3.config(text=warning_seat)
            return
        else:
            label3.config(text="输入微信来选座系统座位号:")
        print(seat)

        flag = entry2.get()

        if flag == '':
            label3.config(text="默认明天:")
        else:
            label3.config(text="今天选座:")

        seat_time = entry3.get()

        if seat_time == '':
            label5.config(text="请输入开始选作时间:")
            return
        else:
            label5.config(text="输入选座时间（24小时格式 eg: 19:30）:")
            if(":" not in seat_time):
                label5.config(text="时间格式不正确:")
        print(seat_time)


        if (flag == ''):
            flag = True
        else:
            flag = False

        label6.config(text="选座结果: " + api.run(cookie, floor, seat, flag),
                      font = ('黑体',12),relief = tk.FLAT)

    def exit_sys():
        exit()

    tk.Button(root, text='开始选座', command=show).grid(row=5, column=0, sticky=tk.W, padx=30, pady=5)
    tk.Button(root, text='退出系统', command=exit_sys).grid(row=5, column=1, sticky=tk.E, padx=30, pady=5)
    tk.mainloop()
