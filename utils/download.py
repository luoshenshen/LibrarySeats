import urllib.request
import ssl
from pytube import YouTube

# 设置代理服务器地址和端口
proxy_host = "127.0.0.1"
proxy_port = "7890"

# 创建一个不验证SSL证书的上下文对象
context = ssl._create_unverified_context()
# 创建一个HTTPS处理程序，使用自定义上下文对象
https_handler = urllib.request.HTTPSHandler(context=context)

# 设置代理
hp = {"http": f"http://{proxy_host}:{proxy_port}", "https": f"http://{proxy_host}:{proxy_port}"}
proxy = urllib.request.ProxyHandler(hp)
opener = urllib.request.build_opener(proxy, https_handler)
urllib.request.install_opener(opener)


# 获取YouTube视频对象
url = 'https://www.youtube.com/watch?v=C9h88KTBlY0'
yt = YouTube(url)

# 选择最高分辨率的视频流
stream = yt.streams.get_highest_resolution()

# 下载视频
video_response = urllib.request.urlopen(stream.url)
with open('C://ProgramData//DreamScene//video.mp4', 'wb') as f:
    f.write(video_response.read())