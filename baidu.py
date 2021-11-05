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
# 被人恶意刷欠费了，现在欠费中，如果能帮你请打赏点还债
APP_ID = '你的APP_ID: 25040399'
API_KEY = '你的API_KEY: 4U9f0wxFKzI9c3Phvju8T4VH'
SECRET_KEY = 'SECRET_KEY: IH7Y2nTpjuuSAIHMl9YyN8buV2kQmFmW'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
