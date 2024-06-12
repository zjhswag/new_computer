# https://www.baidu.com/s?ie=UTF-8&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
import urllib.request
import urllib.parse

key = urllib.parse.quote('周杰伦')
print("http://www.baidu.com/s?wd=" + key)

# 使用parse.urlencode对多个数据进行编码成Unicode
print("\u8be5\u6b7b\u7684")
data = urllib.parse.urlencode({
    "wd": "周杰伦",
    "sex": "男"
})
print("http://www.baidu.com/s?wd=" + data)
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 "
                  "Safari/537.36",
    "Cookie":
        "BIDUPSID=7E138E0E5C0C87CD4B04FBA0AD58C3E7; PSTM=1693997361; "
        "BAIDUID=7E138E0E5C0C87CDBEE55520B81ACD99:SL=0:NR=10:FG=1; "
        "BDUSS"
        "=dXQWotMnpXejd2Z2lidFlPSmV1YWI3MGNuYTZpNGtRbElOVXNwYy1OOEZsaXhsRVFBQUFBJCQAAAAAAAAAAAEAAAAOLqL1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUJBWUFCQVlRk; BDUSS_BFESS=dXQWotMnpXejd2Z2lidFlPSmV1YWI3MGNuYTZpNGtRbElOVXNwYy1OOEZsaXhsRVFBQUFBJCQAAAAAAAAAAAEAAAAOLqL1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUJBWUFCQVlRk; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=39319_39530_39419_39437_39494_39497_39233_38831_26350_22158; BAIDUID_BFESS=7E138E0E5C0C87CDBEE55520B81ACD99:SL=0:NR=10:FG=1; delPer=0; PSINO=6; BA_HECTOR=8la5al8l8525248g24a52h8n1ijf3p71o; ZFY=zA2jYFBKkF6t3ddlDT:A4IQWuU1eU45:BGRuFN0bG2ruw:C"
}
url = urllib.request.Request("http://www.baidu.com/s?wd=" + data, headers=headers)

# 模拟浏览器向服务器访问请求
file = urllib.request.urlopen(url)
# read方法 返回的是字节形式的二进制数据
content = file.read().decode("utf-8")
print(content)
