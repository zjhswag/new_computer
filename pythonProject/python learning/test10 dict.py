# key:value,key不可以重复，相同值会直接被覆盖，key不能为字典，value可以

dict1 = {}  # define dictionary
# print(type(dict1))

dict2 = {1: 1, 2: 2, 3: 3, '4': 41, 4: 4}
# print(dict2,dict1)

print(dict2['4'], dict2[4])  # use [key] to find value

# dictionary = {key: value "for vars in iterable"}
# value=num*num 字典理解
# 列一
square_dict = {}
square_dict = {num: num * num for num in range(1, 11)}
# print(square_dict)
print(square_dict.items())
# ([(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)])

# 列二
old_price = {'milk': 1.02, 'coffee': 3.5, 'bread': 2.5}
dollar_to_pound = 0.76
new_price = {k: v * dollar_to_pound for (k, v) in old_price.items() if v < 3}  # 注意v<3
print(new_price)

# 列二
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict_1 = {k: ('old' if v > 40 else 'young')
              for (k, v) in original_dict.items()}
print(new_dict_1)

# same as
# for num in range(1, 11):
#     square_dict[num] = num*num
# print(square_dict)


# dict3 = {'zjh': {'chinese': 100, 'english': 100}, 'zdh': {'chinese': 99, 'english': 99}}  # 嵌套使用
# print(dict3['zjh']['chinese'])

# operate
# dict3 = {'zjh': {'chinese': 100, 'english': 100}, 'zdh': {'chinese': 99, 'english': 99}}  # 嵌套使用

# change
# dict3['zdh']['english']=0
# print(dict3)

# # add
# dict3['zzz'] = 99  # 直接添加，但是只能添加一维键值对
# dict3add = {'zsh': {'english': 100}}  # 利用创建新字典，增加多层嵌套元素
# dict3.update(dict3add)
# print(dict3)

# pop
# score = dict3.pop('zzz')
# score=dict3.pop['zzz']  error
# print(score,dict3)

# 1.获取全部的keys,利用key来遍历字典
# print(dict3)
# keys=dict3.keys()
# print(keys)
# for key in keys:
#     print(f'1key值是：{key},value值是：{dict3[key]}')

# 2.不获取，直接掉用，原理类似1
# for key in dict3:
#     print(f'2key值是：{key},value值是：{dict3[key]}')

# 元素数量 利用len(),有多少个键值对
# num = len(dict3)
# print(num, dict3)
