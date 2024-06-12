tuple2=(1,2,3,4,5,6,7)

# 空元组 ,放在（）里
tuple1=()        #kong
tuple12=tuple()  #kong
tuple22=tuple2[:] #赋值, 切片法
tuple22=tuple2    #赋值，直接法
print(tuple12)
print(tuple22)

t1=tuple2[::-1]
print(t1)
print(tuple2[5::-1],'!!')
print(tuple2[-5:-3])
# 只有一个元素的元组，仅包含一个元素是不够的。
# 需要一个逗号结尾来表明它实际上是一个元组。
my_tuple = ("hello")
print(type(my_tuple))  # <class 'str'>

# 创建一个只有一个元素的元组
my_tuple = ("hello",)  
print(type(my_tuple))  # <class 'tuple'> 


# 嵌套元组
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# 嵌套索引
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4

# index 索引，count计数，len统计长度 for循环

for element in n_tuple:
    print(element)

# 元组的元素就无法更改。
# 元素本身是可变的数据类型（如列表），则可以更改其嵌套项目。
# n_tuple[0]='asd'  #失败


#嵌套列表可修改
n_tuple[1][2]="6change"
for element in n_tuple:
    print(element)

testnuple=('zjh',11,['football','music'])

indexnum=testnuple.index(11)
print(indexnum)

del testnuple[2][0]  
testnuple[2].append('coding')
for element in testnuple:
    print(element)