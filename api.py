'''
@ project: LibrarySeats
@ file: api
@ user: 罗申申
@ email: luoshenshen@buaa.edu.cn
@ tool: PyCharm
@ time: 2021/6/14 10:27
'''
#-*- coding:utf-8 -*-
import time
import tornado.web
import tornado.ioloop
import app
from threading import Thread
import browser_tools
import requests

cookies = []

requests.packages.urllib3.disable_warnings()
requests_with_session = requests.Session()

def keep_alive():

    while 1:
        for i in cookies:
            print(requests_with_session.get(url='https://wechat.laixuanzuo.com/index.php/reserve/index.html',
                                  headers=browser_tools.get_index_header(i,time.time()), allow_redirects=False, verify=False).text)
        time.sleep(300)

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("seat.html")

    def post(self):
        cookie = self.get_body_argument('cookie', '')
        floor = self.get_body_argument('floor', '')
        seat = self.get_body_argument('seat', '')
        flag = self.get_body_argument('flag', '')
        if flag == '':
            goal = True
        else:
            goal = False
        result = "未订阅或不符合选座要求"
        if cookie == '' or floor == '' or seat == '':
            return result
        result = app.run(cookie, floor, seat,goal)
        print(result)
        cookies.append(cookie)
        Thread(target=keep_alive).start()
        self.write(result)

if __name__ == '__main__':

    api = tornado.web.Application([(r'/api/seat',IndexHandler)])
    api.listen(port=8081)
    tornado.ioloop.IOLoop.current().start()