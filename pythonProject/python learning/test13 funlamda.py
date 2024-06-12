def compute(x,y):
    return x+y

def test_fun(compute2):#当内部调用的函数名固定，可以不传入参数名，当调用lambda函数时，需定义名字
    result=compute2(1,2)
    print(result)

def test_fun2():
    result=compute(1,2)
    print(result)   


# def recursor():
#     recursor()
# recursor()
# 递归深度为1080层
# lambda arguments: expression
# Lambda函数可以具有任意数量的参数arguments，
# expression逻辑表达式，表示执行逻辑。表达式被求值并{返回}，只能有一行代码。
# Lambda函数可在需要函数对象的任何地方使用。

#compare??
# test_fun(lambda x,y:x+y)#lambad被当做为compute2作为函数参数传入test_fun
# test_fun2()

# double2 = lambda x: x * 2#等价double2作为一个普通函数

# print(double2(5),type(double2))#<class 'function'>
# print(double2(10))

#map返回一个新列表包含该函数为每个项返回的项。
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list =list(map(lambda x: x+2 , my_list))
print(new_list)

# 这是使用filter()函数从列表中仅滤除偶数的示例
# 使用列表中的所有项调用该函数，并返回一个新列表，
# 其中包含函数计算结果为{True}的项。
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: x%2 == 0 , my_list))
print(new_list)