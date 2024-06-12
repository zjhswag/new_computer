# # 数据容器 list tuple set dictionary
# # 将所有项目（元素）放在方括号[]中并用逗号分隔来创建列表。
# # 支持嵌套
list = [1, 'ab', [3, 2], -1, True, 5,(1,2,3)]
print(type(list[6]),type(list[4]))
# list[6][0]=3  #不支持修改单个元组元素里面的小元素,可全部替换整个元组
# list[1][0]='b' #不支持修改单个字符串里面的某个字母，可全部替换整个字符串
list[2][0]='cc'  #list 单个的整个元素可修改
print(list)
# # print(list[2][1])
# # print(list[-3][0])
# # print(list[2:4])
# # print(list[:-2])
# # print(list[-4:-2])

# # append()方法将一个项目添加到列表中，
# # 使用extend()方法将多个项目添加到列表中。
# # list.append('zjh')
# # list.extend(['hand', 'some',[1,2,3,5]])
# # print(list)

# # 使用+运算符组合两个列表。这也称为串联。
# # list+=[1,2,3]#区别于嵌套
# # print(list)
# # *运算符重复给定次数的列表。
# # list*=2**10
# # print(list)

# # 查找元素的索引值,index
# opp = list.index(5)
# print(f"True is locatated at {opp}")

# # 插入insert
# list.insert(0, 'sb')
# print(list)


# # 删除del,pop,指定位置,pop会返回值
# del list[0]
# print(list)
# delnum = list.pop(0)
# print(delnum)

# 删除元素，通过名称 remove
# list.remove(True)
# print(list)

# 清空列表，clear
# list.clear()
# print(list)

# 指定元素数量 count
# # COUTA=list.count(True)
# # print(COUTA)

# num = len(list[2:4])
# num2 = len(list)
# print(num, num2)
# # 容乃2**63-1

# # 循环 for while


# def list1hulie():
#     index = 0
#     list1 = ['a', 'b', 'c', 'd', 'e']
#     while index < len(list1):
#         element = list1[index]
#         index += 1
#         print(element)


# list1 = ['a', 'b', 'c', 'd', 'e']
# for i in list1:
#     print(f"**{i}")


# list1hulie()

list2=[1,2,3,4,5,6,7,8,9,10]
list=[]

for i in list2:
    if i%2==0:
        print(i)
        list.append(i)
      

print(list)