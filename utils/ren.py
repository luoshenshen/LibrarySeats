import time
import requests

requests.urllib3.verify=False


a = []
for i in range(1,500):
    h = {
        'Cookie': 'zh_choose=n; a22e7_ol_offset=215049; a22e7_lastpos=F57; a22e7_threadlog=%2C57%2C; a22e7_lastvisit=520%091698201172%09%2F2048%2Fthread.php%3Ffid-57-page-'+str(i)+'.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',

    }
    t = requests.get(url='https://pt46app.com/2048/thread.php?fid-57-page-'+str(i)+'.html', headers=h ,verify=False).text

    if '师范' in t:
        a.append(i)
    print(t)
    time.sleep(3)

print(a)