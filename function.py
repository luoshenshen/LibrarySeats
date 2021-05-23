'''
@ project: LibrarySeats
@ file: function
@ user: 罗申申
@ email: luoshenshen@buaa.edu.cn
@ tool: PyCharm
@ time: 2021/5/24 1:44
'''
import requests

def session_get(url,header):
    requests.packages.urllib3.disable_warnings()
    return requests.session().get(url=url,headers=header,allow_redirects=True,verify=False)
