import urllib.request
import json
url = "https://syks.xidian.edu.cn/redir.php?catalog_id=6&cmd=dati&moni=0"

# 模拟浏览器向服务器访问请求
# response = urllib.request.urlopen(url)
# # read方法 返回的是字节形式的二进制数据
# content = response.read().decode("utf-8")
# 将二进制转换为字符串 解码 decode
# print(content)

# response 是httpResponse类型 这一块介绍它的方法

# print(response.getheaders())
# .getheaders()获取一个状态信息

# print(response.getcode())
# getcode() 返回200 则逻辑正确

# .readline()  读取一行
# .readlines() 读取一行行
# .read(5)  不加数字为读取全部内容，否则为读取几个字节
# .geturl  获取url

# print(response.info())
# print(content)
# #  将百度首页的内容转成utf-8的形式，存取到本地的html文件
# f = open(r"C:\Users\14601\PycharmProjects\pythonProject\爬虫\1.html", "w", encoding='utf-8')
# f2 = open("2.html", "w", encoding='utf-8')
# f2.write(content)
# f2.close()
# 或者直接用如下的方法
# urllib.request.urlretrieve(url_1,"bilibili.mp4")
# url_1 = "blob:https://haokan.baidu.com/e4d3fde8-2bb7-441f-abe1-44c0f917f7f2"
headers = {
    'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 "
                  "Safari/537.36 Edg/118.0.2088.61",
    'Cookie': "PHPSESSID=ST-1227915-aWzjwH7FVY9LQOfXZSoOVdXyKbsauthserver2; UqZBpD3n3iPIDwJU=v1Aa1bQwSDKCl"
}
file_1 = urllib.request.Request(url, headers=headers)
print(urllib.request.urlopen(file_1).read().decode("utf-8"))


