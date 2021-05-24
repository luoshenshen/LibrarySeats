'''
@ project: LibrarySeats
@ file: test
@ user: 罗申申
@ email: luoshenshen@buaa.edu.cn
@ tool: PyCharm
@ time: 2021/5/24 14:27
'''
import re
import function
import requests
import execjs
import browser_tools

def obtain_js(html):
    js = '<script src="(.*?)"'
    href = re.compile(js, re.S).findall(html)
    return href

def verify_code_get(jsname):
    '''代码不麻烦，主要是分析js花了些时间'''
    url = "https://static.wechat.laixuanzuo.com/template/theme2/cache/layout/" + jsname + ".js"

    pattern_js_bg = 'void 0\=\=\=.\&\&\(.\=""\);'
    pattern_js_end = '.\.ajax_get'
    pattern_js = pattern_js_bg + '.*' + pattern_js_end

    pattern_js_res = '\+"\&".*\+"\&yzm\="'

    exjs = network(url=url)

    funjs = re.search(pattern_js, exjs).group(0)
    funjs = funjs[19:-10]

    resjs = re.search(pattern_js_res, exjs).group(0)
    resultcommond = resjs[5:-14]

    exjs8 = exjs

    docjs = execjs.compile(exjs8 + funjs)

    return docjs.eval(resultcommond)

def network(url):
    return function.session_get(url=url,header=browser_tools.js_header).text