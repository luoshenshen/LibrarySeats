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


def run():
    result = function.session_get(browser_tools.index_url, browser_tools.index_header)
    if '来选座' in result.text:
        print('(o゜▽゜)o☆')
        print('尝试进入选座系统')
        print('成功进入来选座系统')
        print('(￣▽￣)～■干杯□～(￣▽￣)')
    else:
        print(result.text)
        print('进入来选座系统失败，请联系开发者email:luoshenshen@buaa.edu.cn或者重试！')

    result = function.session_get(browser_tools.center_url, browser_tools.center_header)
    nick = re.findall('<div class="nick">(.*)</div>', result.text)[0]
    print('(๑•̀ㅂ•́)و✧' + '你好呀：--------------------------' + nick)
    result = function.session_get(browser_tools.prereserve_url, browser_tools.prereserve_header)
    if nick in result.text or "预约明天的座位" in result.text:
        print('成功进入明日预约选座')
        print('开始准备抢座')
        print('<(￣︶￣)↗[GO!]')
        function.fecth(nick + '.jpg')
    else:
        print('进入明日预约选座失败，请联系开发者email:luoshenshen@buaa.edu.cn或者重试！')


if __name__ == "__main__":
    run()
