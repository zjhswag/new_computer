import json
#  json 为字符串类型，可以无缝转换
list_1 = [{"name": "周jh", "age": 11}, {"name": "zsh", 'age': 22}]
# 转换列表
jsons_str = json.dumps(list_1, ensure_ascii=False)
print(type(jsons_str), jsons_str)
# 转换字典
d = {"name": "zjh", "addr": "taiwan"}
jsons_str2 = json.dumps(d)
print(type(jsons_str2), jsons_str2)
# 转换回来列表
s = '[{"name": "周jh", "age": 11}, {"name": "zsh", "age": 22}]'
l = json.loads(s)
print(type(l), l)
# 转换回来字典
s2 = '{"name": "zjh", "addr": "taiwan"}'
d = json.loads(s2)
print(d, type(d))
