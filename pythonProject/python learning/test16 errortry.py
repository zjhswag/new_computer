#
# try:
#     f=open(r"C:\Users\14601\Desktop\tes2t.txt","r",encoding='UTF-8')
# except:
#     print('读取异常')
#     f=open(r"C:\Users\14601\Desktop\tes2t.txt","w",encoding='UTF-8')

# 捕获指定异常
# try:
#     print(name)
# except NameError as e:
#     print(e)


# 捕获多个指定异常
# try:
#     print(name)
# except (NameError,ZeroDivisionError) as e:
#     print(e)

# 捕获所有异常
# try:
#     print('cnm')
# except Exception as e:
#     print('出现异常:',e)
# else:
#     print('很高兴，没有异常')
# finally:
#     print("我是finally,有没有异常我都要执行")

# else 和 finally 可选.


import sys
# randomList = ['a',4,0, 2]

# for entry in randomList:
#     try:
#         print("The entry is", entry)
#         r = 1/int(entry)
#         break

#     except Exception as e:
#         print("Oops!",sys.exc_info()[0],"occured.")
#         print("Next entry.")
#         print()
# print("The reciprocal of",entry,"is",r)

# try:
#     a = int(input("输入一个正整数: "))
#     if a <= 0:
#         raise ValueError("这不是一个正数!")
# except ValueError as ve:
#     print(ve)

print("**")

print(sys.path)
