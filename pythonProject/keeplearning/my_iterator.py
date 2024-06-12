# 迭代器协议 iter()和next()

my_list = [4, 7, 0, 3]
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())
print(my_iter.__next__())
# next(my_iter)  # 会报错 StopIteration 已经没有元素可以出来

# for循环是用迭代器实现
# for element in iterable:
# iter_obj = iter(iterable)
#
# # 无限循环
# while True:
#     try:
#         # 获取下一项
#         element = next(iter_obj)
#         # 对元素做点什么
#     except StopIteration:
#         # 如果引发StopIteration，则从循环中断
#         break
