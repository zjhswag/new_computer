# 返回多个返回值，多个接受
# def test_return():
#     return 4,2,3

# x,y,z=test_return()
# print(x,y,z)


def use_info(name,age=22,gender='男'):#缺省参数，定义了一个默认值
    print(f"name is:{name}，age is:{age},gender is:{gender}")

# use_info(22)  
# use_info('zz',22,gender='男')
# #关键字参数，可以打乱顺序，，通过‘键=值’-+9形式传递参数但是位置参数必须在关键字参数的前面
# use_info('zz',22,'女')
# # 正常参数，默认的方式，位置参数，根据参数位置来传递参数

# 传递的所有参数都会被args传递，都会被传进tuple()，一个*
# def user_tuple(*args):
#     print(args)

# user_tuple('tom',19)
# user_tuple('tom')

# 关键词不定长，两个**，接受key：value类型
def user_dict(**dict):
    print(dict)
    for key in dict:
        print('**',key,dict[key],'**')
    dict['add']='change'
    return dict#

dict12=user_dict(name='tom',age=18,id=110)
print(dict12)
#result: {'name': 'tom', 'age': 18, 'id': 110}


def greet(name, msg="早上好!"):
    """
    此函数向提供消息的人打招呼。
    如果没有提供消息，
    则默认为“早上好!”
    """
    print("你好", name + ', ' + msg)

# 2个关键词参数
greet(name = "Bruce",msg = "How do you do?")

# 2个关键词参数，参数顺序调换
greet(msg = "How do you do?",name = "Bruce") 

#1 个位置参数, 1 个关键词参数，这个对
greet("Bruce", msg = "How do you do?")

# 这个错，关键词参数必须跟在位置参数之后
# greet(name="Bruce","How do you do?")