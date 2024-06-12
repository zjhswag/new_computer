import urllib.request
import urllib.parse
import json

url = "https://fanyi.baidu.com/sug"
data = urllib.parse.urlencode({
    'kw': 'plot'
}).encode('utf-8')

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 "
                  "Safari/537.36",
    "Cookie":
        "BIDUPSID=7E138E0E5C0C87CD4B04FBA0AD58C3E7; PSTM=1693997361; "
        "BAIDUID=7E138E0E5C0C87CDBEE55520B81ACD99:SL=0:NR=10:FG=1; "
        "BDUSS"
        "=dXQWotMnpXejd2Z2lidFlPSmV1YWI3MGNuYTZpNGtRbElOVXNwYy1OOEZsaXhsRVFBQUFBJCQAAAAAAAAAAAEAAAAOLqL1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUJBWUFCQVlRk; BDUSS_BFESS=dXQWotMnpXejd2Z2lidFlPSmV1YWI3MGNuYTZpNGtRbElOVXNwYy1OOEZsaXhsRVFBQUFBJCQAAAAAAAAAAAEAAAAOLqL1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUJBWUFCQVlRk; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=39319_39530_39419_39437_39494_39497_39233_38831_26350_22158; BAIDUID_BFESS=7E138E0E5C0C87CDBEE55520B81ACD99:SL=0:NR=10:FG=1; delPer=0; PSINO=6; BA_HECTOR=8la5al8l8525248g24a52h8n1ijf3p71o; ZFY=zA2jYFBKkF6t3ddlDT:A4IQWuU1eU45:BGRuFN0bG2ruw:C"
}

# post不可以拼接,需要放在data位置参数处,且必须进行编码
file_1 = urllib.request.Request(url, data=data, headers=headers)
print(json.loads(urllib.request.urlopen(file_1).read())['data'])
# print(json.loads(urllib.request.urlopen(file_1).read())['data'][0]['k'])
