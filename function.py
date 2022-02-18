'''
@ project: LibrarySeats
@ file: function
@ user: 罗申申
@ email: luoshenshen@buaa.edu.cn
@ tool: PyCharm
@ time: 2021/5/24 1:44
'''
import requests
import time
import browser_tools
import re
import js_code
import baidu
import timer
import random
from aip import AipOcr
from utils import get_seat_time

requests.packages.urllib3.disable_warnings()
requests_with_session = requests.Session()

seat_time = ':'
seat_hour, seat_minute = get_seat_time(seat_time)

def session_get(url, header):
    requests.adapters.DEFAULT_RETRIES = 30
    return requests_with_session.get(url=url, headers=header, allow_redirects=False, verify=False, timeout=300)


def floors(floor):
    floor = str(floor)
    if floor == "21":
        floor = str(10073)
    elif floor == "22":
        floor = str(10065)
    elif floor == "23":
        floor = str(10071)
    elif floor == "24":
        floor = str(10072)
    elif floor == "31":
        floor = str(10080)
    elif floor == "32":
        floor = str(10081)
    elif floor == "33":
        floor = str(10082)
    elif floor == "34":
        floor = str(10083)
    elif floor == "35":
        floor = str(10084)
    elif floor == "41":
        floor = str(10085)
    elif floor == "42":
        floor = str(10086)
    elif floor == "43":
        floor = str(10087)
    elif floor == "44":
        floor = str(10088)
    elif floor == "45":
        floor = str(10089)
    elif floor == "51":
        floor = str(10090)
    elif floor == "52":
        floor = str(10091)
    elif floor == "53":
        floor = str(10092)
    elif floor == "61":
        floor = str(11019)
    elif floor == "62":
        floor = str(11033)
    elif floor == "63":
        floor = str(11040)
    elif floor == "64":
        floor = str(11300)
    elif floor == "71":
        floor = str(11054)
    elif floor == "72":
        floor = str(11061)
    elif floor == "73":
        floor = str(11068)
    elif floor == "81":
        floor = str(11075)
    elif floor == "82":
        floor = str(11096)
    elif floor == "83":
        floor = str(11117)
    elif floor == "84":
        floor = str(11131)
    elif floor == "85":
        floor = str(11138)
    elif floor == "91":
        floor = str(11082)
    elif floor == "92":
        floor = str(11103)
    elif floor == "93":
        floor = str(11124)

    return str(floor)


def get_floor_url(url, floor):
    return url + str(floor) + ".html&"


def get_tomorrow_floor_url(url, floor):
    return url + str(floor)


def get_seat(html):
    xys = re.findall('<div class="grid_cell grid_1" data-key="(\d+,\d+)" style="left:', html)
    return xys


def get_my_seat(html):
    xys = re.findall('data-key="(.*)" style="left:', html)
    seats = re.findall('<em>(.*)</em>', html)
    return xys, seats


def today_img_download(url, header, nick):
    r = requests.get(url, stream=True, headers=header, verify=False)
    with open(nick + '.png', 'wb') as f:
        f.write(r.content)


def img_download(url, nick):
    r = requests.get(url, stream=True, verify=False)
    with open(nick + '.png', 'wb') as f:
        f.write(r.content)


def fecth(cookie, floor, k, flag, nick):
    floor = floors(floor)
    # 定义进入楼层的时间
    times = str(int(time.time()))
    # 定义浏览器时间记录
    lvt = str(int(times) - 1)
    lptv = str(int(times) + 1)

    hour, min, sec = timer.times()
    if str(hour) == str(6):
        flag = False
    else:
        flag = True

    if flag == False:

        url = get_floor_url(browser_tools.floor_url_api, floor)
        url += str(times)
        alive = 0
        hour, min, sec = timer.times()
        # 时间控制：小时：eg 阁下学校开始抢座时间 如：19：50 ，控制小时 19
        while int(hour) < int(seat_hour):
            time.sleep(0.2)
            alive += 1
            if alive == 360:
                session_get(url, browser_tools.get_tomorrow_layout_header(cookie, lvt, lptv))
                alive = 0
                print("需要再等" + str((int(seat_hour) - int(hour))) + "小时")
            hour, min, sec = timer.times()
        # 时间控制：小时：eg 阁下学校开始抢座时间 如：19：50 ，控制分钟 50
        while int(min) < int(seat_minute):
            time.sleep(0.2)
            alive += 1
            if alive == 360:
                session_get(url, browser_tools.get_tomorrow_layout_header(cookie, lvt, lptv))
                alive = 0
                print("需要再等" + str((int(seat_minute) - 1 - int(min))) + "分")
            hour, min, sec = timer.times()

        # 进入楼层链接
        url = get_floor_url(browser_tools.floor_url_api, floor)
        url += str(times)
        # 正式进入楼层
        result = session_get(url, browser_tools.get_layout_header(cookie, lvt, lptv))
        js_result = js_code.obtain_js(result.text)
        print(js_result)
        if len(js_result) <= 1:
            return "已选中座位或者不在选座时间!"
        request_js = js_result[1]
        need_js = re.findall(r"layout/(.+?).js", request_js)
        print("选座js已获取：" + need_js[0])
        verify_code = js_code.verify_code_get(need_js[0], cookie, times)
        js = str(verify_code)
        print("选座js匹配验证码:" + verify_code)
        xys = get_seat(result.text)

        # 支持自定义抢座
        xy, se = get_my_seat(result.text)
        ke = {}
        for i, j in zip(xy, se):
            ke.update({str(j): str(i)})
        for i in ke.keys():
            if i != '' and i != '柱' and i != '窗':
                print('可选座位：', i)
        keys = []
        for i in xys:
            keys.append(i)
        print(keys)
        if (k == ''):
            seats = random.choice(keys)
        else:
            seats = ke.pop(k)
        if len(keys) == 0:
            return "来晚了！没位置了！"
        result = ''
        # 初始化百度验证码识别
        client = AipOcr(baidu.APP_ID, baidu.API_KEY, baidu.SECRET_KEY)
        options = {}
        options["detect_language"] = "true"
        # 开始选座
        while '成功' not in result or '失败' not in result or '满' not in result:
            # 获取验证码
            img_url = browser_tools.img_url + "?" + str(int(time.time()))
            hr = requests.get(img_url, stream=True,
                              headers=browser_tools.img_header_today(cookie, floor, lvt, lptv, times),
                              verify=False, allow_redirects=False).headers
            if 'Location' in hr.keys():
                print("重定向")
                img_url = hr.pop('Location')
                print(img_url)
                img_download(img_url, nick)
                img = baidu.get_file_content(nick + '.png')
                word = client.basicAccurate(img)
            else:
                print("未重定向")
                print(img_url)
                today_img_download(img_url, browser_tools.img_header_today(cookie, floor, lvt, lptv, times), nick)
                img = baidu.get_file_content(nick + '.png')
                word = client.basicAccurate(img)
            # 判断识别图片合法性
            if len(word.get('words_result')) == 0:
                continue
            li = word.get('words_result')
            if len(li[0]["words"]) != 4:
                continue
            code = li[0]["words"]
            # 各种安全已经验证，开始抢座
            print('(o゜▽゜)o☆[BINGO!]', "\tCNN卷积神经网络自动判别验证码为：", code)
            # 抢座url
            # 如果准备预定某一个位子，把下面# 注释去掉即可（失败概率极大）,x 与 y值改成对应坐标
            # seats = 'x,y'
            target_url = browser_tools.today_url + str(floor) + '&' + str(js) + '=' + str(seats) + '&yzm=' + str(code)
            print(target_url)
            result = str(session_get(target_url, browser_tools.get_today_header(cookie, lvt, lptv, times, floor)).text)
            if ('预定' in result) or ('退选' in result) or ('释放' in result) or ('成功' in result):
                return result
            print("选座失败: 随即座位 " + seats + result + " 继续重试!")
            if ("不存在" in result or "抢掉" in result):
                seats = random.choice(keys)

    else:
        url = get_tomorrow_floor_url(browser_tools.floor_tomorrow_url_api, floor)
        print(url)
        alive = 0
        hour, min, sec = timer.times()
        # 时间控制：小时：eg 阁下学校开始抢座时间 如：19：50 ，控制小时 19
        while int(hour) < int(seat_hour):
            time.sleep(0.2)
            alive += 1
            if alive == 360:
                session_get(url, browser_tools.get_tomorrow_layout_header(cookie, lvt, lptv))
                alive = 0
                print("需要再等" + str((int(seat_hour) - int(hour))) + "小时")
            hour, min, sec = timer.times()
        # 时间控制：小时：eg 阁下学校开始抢座时间 如：19：50 ，控制分钟 50
        while int(min) < int(seat_minute):
            time.sleep(0.2)
            alive += 1
            if alive == 360:
                session_get(url, browser_tools.get_tomorrow_layout_header(cookie, lvt, lptv))
                alive = 0
                print("需要再等" + str((int(seat_minute) - 1 - int(min))) + "分" + str((59 - int(sec))) + "秒")
            hour, min, sec = timer.times()

        # 最后一次刷新
        result = session_get(url, browser_tools.get_tomorrow_layout_header(cookie, lvt, lptv))
        xys = get_seat(result.text)
        keys = []
        for i in xys:
            keys.append(i)
        if len(keys) == 0:
            return "来晚了！没位置了！"

        # 支持自定义抢座
        xy, se = get_my_seat(result.text)
        ke = {}
        for i, j in zip(xy, se):
            ke.update({str(j): str(i)})
        for i in ke.keys():
            if i != '' and i != '柱' and i != '窗':
                print('可选座位：', i)
        if (k == ''):
            seats = random.choice(keys)
        else:
            seats = ke.pop(k)
        seats = str(seats)
        # 获取js验证
        js_result = js_code.obtain_js(result.text)
        print("提前发起主动锁定...")
        while len(js_result) == 1:
            result = session_get(url, browser_tools.get_tomorrow_layout_header(cookie, lvt, lptv))
            # 获取js验证
            js_result = js_code.obtain_js(result.text)

        request_js = js_result[1]
        need_js = re.findall(r"layout/(.+?).js", request_js)
        print(need_js)
        verify_code = js_code.verify_code_get(need_js[0], cookie, time)
        js = str(verify_code)
        client = AipOcr(baidu.APP_ID, baidu.API_KEY, baidu.SECRET_KEY)
        options = {}
        options["detect_language"] = "true"
        result = ''
        while '成功' not in result or '失败' not in result or '满' not in result:
            # 获取验证码链接
            img_url = browser_tools.img_url
            hr = session_get(img_url, header=browser_tools.tomorrow_imgs_header(cookie, lvt, lptv, floor)).headers
            if 'Location' in hr.keys():
                print("重定向")
                img_url = hr.pop('Location')
                print(img_url)
                img_download(img_url, nick)
                img = baidu.get_file_content(nick + '.png')
                word = client.basicAccurate(img)
            else:
                print("未重定向")
                today_img_download(img_url, browser_tools.tomorrow_imgs_header(cookie, floor, lvt, lptv), nick)
                img = baidu.get_file_content(nick + '.png')
                word = client.basicAccurate(img)
            # 判断合法性
            print("验证码识别为：" + str(word))
            if len(word.get('words_result')) == 0:
                continue
            li = word.get('words_result')
            if len(li[0]["words"]) != 4:
                continue
            code = li[0]["words"]
            print('(o゜▽゜)o☆[BINGO!]', "\tCNN卷积神经网络自动判别验证码为：", code)
            # 各种安全已经验证，开始抢座
            # 如果准备预定某一个位子，把下面# 注释去掉即可（失败概率极大）,x 与 y值改成对应坐标
            # seats = 'x,y'
            seats = str(seats)
            target_url = browser_tools.tomorrow_url + str(floor) + '&' + str(js) + '=' + str(seats) + '&yzm=' + code
            print(target_url)
            print(keys)
            result = session_get(target_url, browser_tools.get_today_header(cookie, lvt, lptv, times, floor)).text
            print("选座结果:", result)
            if '成功' in result or '失败' in result or '满' in result or '已经预定' in result:
                return result
            if ("不存在" in result or "抢掉" in result):
                seats = random.choice(keys)
