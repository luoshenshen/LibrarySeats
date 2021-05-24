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
APP_ID = '23483161'
API_KEY = 'ydyGUiAQg8Q5operuXlfz4sC'
SECRET_KEY = 'B3lDlGvjZR1F43xu0GW8G3LiGVc6PkQB'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
