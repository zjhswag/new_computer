import urllib.request

url = "https://www.baidu.com"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 "
                  "Safari/537.36"}

req_1 = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器访问请求
file = urllib.request.urlopen(req_1)
# read方法 返回的是字节形式的二进制数据
content = file.read().decode("utf-8")
# 将二进制转换为字符串 解码 decode


print(content)

#
# for i in range(100):
#     try:
#         url = "http://www.baidu.com"
#         # 模拟浏览器向服务器访问请求
#          response = urllib.request.urlopen(url, timeout=0.05)
#         # read方法 返回的是字节形式的二进制数据
#         content = response.read().decode("utf-8")
#         # 将二进制转换为字符串 解码 decode
#         print(len(content))
#     except Exception as e:
#         print("异常为：", e)
