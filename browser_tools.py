'''
@ project: LibrarySeats
@ file: browser_tools
@ user: 罗申申
@ email: luoshenshen@buaa.edu.cn
@ tool: PyCharm
@ time: 2021/5/24 1:19
'''
import time

input_time = str(int(time.time()))
input_session = input("请输入cookie：")

index_url = 'https://wechat.laixuanzuo.com/index.php/reserve/index.html'
prereserve_url = 'https://wechat.laixuanzuo.com/index.php/prereserve/index.html'
center_url = 'https://wechat.laixuanzuo.com/index.php/center.html'
floor_url = 'https://wechat.laixuanzuo.com/index.php/reserve/layout/libid='
today_url = 'https://wechat.laixuanzuo.com/index.php/reserve/get/libid='

index_header = {
    'Host':'wechat.laixuanzuo.com',
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0',
    'Upgrade-Insecure':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer':'https://wechat.laixuanzuo.com/index.php/prereserve/index.html',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
    'Cookie':'wechatSESS_ID='+str(input_session)+'; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098='+input_time+'; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098='+input_time,
    'If-Modified':'Thu, 01 Jan 1970 00:00:00GMT',
}
layout_header = {
    'Host':'wechat.laixuanzuo.com',
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0',
    'Upgrade-Insecure':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer':'https://wechat.laixuanzuo.com/index.php/prereserve/index.html',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
    'Cookie':'wechatSESS_ID='+str(input_session)+'; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098='+input_time+','+str(int(input_time)+20)+'; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098='+input_time,
    'If-Modified':'Thu, 01 Jan 1970 00:00:00GMT',
}


prereserve_header = {
    'Host':'wechat.laixuanzuo.com',
    'Connection': 'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer':'https://wechat.laixuanzuo.com/index.php/reserve/index.html',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
    'Cookie':'wechatSESS_ID='+str(input_session)+'; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098='+str((int(input_time)+10))+'; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098='+str((int(input_time)+20)),
}

center_header = {
    'Host': 'wechat.laixuanzuo.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://wechat.laixuanzuo.com/index.php/reserve/index.html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
    'Cookie': 'wechatSESS_ID=' + str(
        input_session) + '; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098=' + str(
        (int(input_time) - 10)) + '; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=' + input_time,
}

today_header = {
    'Host': 'wechat.laixuanzuo.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)',
    'Referer': 'https://wechat.laixuanzuo.com/index.php/reserve/index.html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4',
    'Cookie': 'wechatSESS_ID=' + str(
        input_session) + '; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098=' + str(
        (int(input_time) - 10)) + '; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=' + input_time,
}

js_header = {
    'authority': 'static.wechat.laixuanzuo.com',
    'method':'GET',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1326.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63010200)',
    'Accept-Encoding': 'gzip, deflate,br',
    'scheme':'https',
    'if-none-match':'"5d5f8357-6da"',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site':'none',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}
