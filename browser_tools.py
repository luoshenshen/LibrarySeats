'''
@ project: LibrarySeats
@ file: browser_tools
@ user: 罗申申
@ email: luoshenshen@buaa.edu.cn
@ tool: PyCharm
@ time: 2021/5/24 1:19
'''

index_url = 'https://wechat.laixuanzuo.com/index.php/reserve/index.html'
prereserve_url = 'https://wechat.laixuanzuo.com/index.php/prereserve/index.html'
center_url = 'https://wechat.laixuanzuo.com/index.php/center.html'
floor_url_api = 'https://wechat.laixuanzuo.com/index.php/reserve/layout/libid='
# floor_url = 'https://wechat.laixuanzuo.com/index.php/reserve/layoutApi/action=prereserve_event&libid='
# https://wechat.laixuanzuo.com/index.php/reserve/layout/libid=10073.html&1635064601
today_url = 'https://wechat.laixuanzuo.com/index.php/reserve/get/libid='
# https://wechat.laixuanzuo.com/index.php/reserve/get/libid=10065&ZyhTWrKQkQ=15,15&yzm=4065
floor_tomorrow_url_api = 'https://wechat.laixuanzuo.com/index.php/reserve/layoutApi/action=prereserve_event&libid='
tomorrow = 'https://wechat.laixuanzuo.com/index.php/prereserve/index.html'
tomorrow_url = 'https://wechat.laixuanzuo.com/index.php/prereserve/save/libid='
img_url = 'https://wechat.laixuanzuo.com/index.php/misc/verify.html'


#       = 'https://wechat.laixuanzuo.com/index.php/misc/verify.html'
def get_index_header(cookie, time):
    header = {
        'Host': 'wechat.laixuanzuo.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'https://wechat.laixuanzuo.com/index.php/prereserve/index.html',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
        'Cookie': 'wechatSESS_ID=' + str(cookie) + '; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098='
                  + str(int(time)) + '; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=' + str(int(time)),
        'If-Modified': 'Thu, 01 Jan 1970 00:00:00GMT',
    }
    return header

def get_layout_header(cookie, lvt, lpvt):
    header = {
        'Host': 'wechat.laixuanzuo.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure': '1',
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "document",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63030073)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'https://wechat.laixuanzuo.com/index.php/reserve/index.html?f=wechat',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'wechatSESS_ID=' + str(cookie) +
                  '; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098=' +
                  str(lvt) + '; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=' +
                  str(lpvt),
        'Upgrade-Insecure-Requests': '1',
    }
    return header


def get_tomorrow_layout_header(cookie, lvt, lpvt):
    header = {
        'Host': 'wechat.laixuanzuo.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure': '1',
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63030073)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'https://wechat.laixuanzuo.com/index.php/prereserve/index.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'wechatSESS_ID=' + str(cookie) +
                  '; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098=' +
                  str(lvt) + '; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=' +
                  str(lpvt),
        'Upgrade-Insecure-Requests': '1',
    }
    return header


def get_prereserve_header(cookie, time):
    header = {
        'Host': 'wechat.laixuanzuo.com',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'https://wechat.laixuanzuo.com/index.php/reserve/index.html',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
        'Cookie': 'wechatSESS_ID=' + str(cookie) + '; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098=' + str(
            (int(time) + 10)) + '; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=' + str((int(time) + 20)),
    }
    return header


def get_center_header(cookie, time):
    header = {
        'Host': 'wechat.laixuanzuo.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'https://wechat.laixuanzuo.com/index.php/reserve/index.html',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
        'Cookie': 'wechatSESS_ID=' + str(cookie) + '; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098=' + str(
            (int(time) - 10)) + '; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=' + str(int(time)),
    }
    return header


def get_today_header(cookie, lvt, lptv, times, floor):
    header = {
        'Host': 'wechat.laixuanzuo.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63030073)',
        'Referer': 'https://wechat.laixuanzuo.com/index.php/reserve/layout/libid=' + str(floor) + '.html&' + str(times),
        'Accept-Encoding': 'gzip, deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'wechatSESS_ID=' + str(cookie) + '; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098=' + str(
            lvt) + '; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=' + str(lptv)
    }
    return header


def get_js_header(cookie, time):
    header = {
        'authority': 'static.wechat.laixuanzuo.com',
        'method': 'GET',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)',
        'Accept-Encoding': 'gzip, deflate,br',
        'scheme': 'https',
        'if-none-match': '"5d5f8357-6da"',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }
    return header


def imgs_header(cookie, floor):
    imgs_header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)',
        'Referer': 'https://wechat.laixuanzuo.com/index.php/reserve/layoutApi/action=prereserve_event&libid=' + str(
            floor),
        'Cookie': 'wechatSESS_ID=' + str(cookie),
        'Host': 'wechat.laixuanzuo.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
    }
    return imgs_header


import time

tomorrow_time = str(int(time.time()))
tomorrow_var = str(int(tomorrow_time) - 10)


def get_tomorrow_header(cookie):
    tomorrow_headers = {
        'Host': 'wechat.laixuanzuo.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'https://wechat.laixuanzuo.com/index.php/reserve/index.html',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
        'Cookie': 'wechatSESS_ID=' + str(cookie) + ';'
                                                   ' FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098=' + str(
            tomorrow_var) + ';'
                            ' Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=' + str(tomorrow_time),

    }
    return tomorrow_headers


def tomorrow_imgs_header(cookie, lvt, lpvt, floor):
    tomorrow_img_header = {
        'Host': 'wechat.laixuanzuo.com',
        'Connection': 'keep-alive',
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Dest": "image",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63030073)',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
        'Referer': 'https://wechat.laixuanzuo.com/index.php/reserve/layoutApi/action=prereserve_event&libid=' + str(
            floor),
        'Cookie': 'wechatSESS_ID=' + str(cookie) +
                  '; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098=' +
                  str(lvt) + '; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=' +
                  str(lpvt),
    }
    return tomorrow_img_header


def img_header(cookie, floor):
    iheader = {
        'Host': 'static.wechat.laixuanzuo.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200) ',
        'Accept': 'image/webp,image/*,*/*;q=0.8',
        'Referer': 'https://wechat.laixuanzuo.com/index.php/reserve/layoutApi/action=prereserve_event&libid=' + str(
            floor),
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
        'Cookie': 'wechatSESS_ID=' + str(cookie) +
                  '; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098='
                  + str(tomorrow_var) + '; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098='
                  + str(tomorrow_time),
    }
    return iheader


def img_header_today(cookie, floor, lvt, lpvt, times):
    header = {
        "Host": "wechat.laixuanzuo.com",
        "Connection": "keep-alive",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63030073)',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Cookie': 'wechatSESS_ID=' + str(cookie) +
                  '; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098='
                  + str(int(lvt)) + '; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098='
                  + str(int(lpvt)),
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Dest": "image",
        "Referer": "https://wechat.laixuanzuo.com/index.php/reserve/layout/libid=" + str(floor) + ".html&" + str(
            int(times)),
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    return header
