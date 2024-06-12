import time
# 读文件
# f=open(r"C:\Users\14601\Desktop\草稿.txt","r",encoding='UTF-8')
# print(f.read(1))
# print(f.read())  #文件读取会从上一次读取完的地方继续读

# 读取每一列作为列表的内容
# lines=f.readlines()
# print(lines,type(lines))

# 一次读取一行，返回的是字符串
# lines=f.readline()
# print(lines,type(lines))

# for 循环读取每一行
# for line in f:
#     print(f'每一行数据是： {line}')

# 文件读取关闭 close()  with open() as f 自动关闭文件

# 写文件 flush写入内存，write缓冲区,close内置flush，w模式覆盖写
# f=open(r"C:\Users\14601\Desktop\test.txt","w",encoding='UTF-8')
# f.write('fuck2 you')
# time.sleep(100)
# f.flush()

# 追加写入a模式，
f=open(r"C:\Users\14601\Desktop\test.txt","a",encoding='UTF-8')
f.write('fuck you')
f.flush()
time.sleep(20)
f.write('\ncnmsb')