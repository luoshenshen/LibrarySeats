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
APP_ID = '24367773'
API_KEY = 'dtmPtFqc6fLY1LWGcHmbevEU'
SECRET_KEY = '63htlbBIMrofo4ANtQkh0zOSm8d6FIsz'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
