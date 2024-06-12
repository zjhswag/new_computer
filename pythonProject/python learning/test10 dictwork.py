dict={'wlh':{'department':'kjb','salary':3000,'grade':1},
      'zjl':{'department':'scb','salary':5000,'grade':2},
      'ljj':{'department':'scb','salary':7000,'grade':3},
      'zxy':{'department':'kjb','salary':4000,'grade':1},
      'ldh':{'department':'scb','salary':6000,'grade':2}}
# print(dict)

for key in dict:
    # print(dict[key]['grade'])
    if dict[key]['grade']==1:
        dict[key]['grade']+=1
        dict[key]['salary']+=1000

for key in dict:
    print(key,':',dict[key])#dict[key]输出的是其对应的值
    changedict=dict[key]#对应的value值
    print('change\n',changedict)


# 支持下标索引 ：列表[] 元组() 字符串
# 不支持下标索引：字典{key：value} 集合{} 用set()初始化

# 支持重复元素： 列表，元组，字符串， 
# 不支持重复元素：字典{key：value} 集合{} 

# 是否可以修改 是：列表，集合，字典
# 不可以:字符串，元组

# 集合：去重合适，字典适合key检索value
