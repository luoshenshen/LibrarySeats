'''
@ project: LibrarySeats
@ file: baidu
@ user: 罗申申
@ email: luoshenshen@buaa.edu.cn
@ tool: PyCharm
@ time: 2021/5/24 20:48
'''
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = 'your app_id: '
API_KEY = 'your api_key: '
SECRET_KEY = 'SECRET_KEY: '

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()