import numpy


def checkValid(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """


matrix = [[1, 3, 2, 4], [1, 2, 3, 4], [4, 1, 2, 3], [4, 1, 2, 3]]
np1 = numpy.array(matrix)
# print(np1.transpose())
n = np1.shape[0]
flag = True
# 我的：开始判断从1到n是否在每前n行，后面判断每n列
for i in range(2 * n):
    if flag:
        if i < n:
            for j in range(1, n + 1):
                if j in np1[i]:
                    # print(j, "11")
                    continue
                else:
                    # print(i, "1")
                    flag = False
                    break
        else:
            for j in range(1, n + 1):
                if j in np1[:, i - n]:
                    # print(j, "22")
                    continue
                else:
                    # print(j, "2")
                    flag = False
                    break
    else:
        break
print(flag)

# for i in zip(*matrix):
#     print(i)
# print(tuple(zip(*matrix))[0])
# print(*matrix)  # * 号用于解压列表， zip函数返回的是一个迭代器，该迭代器生成元组，其中每个元组包括来自每个可迭代对象的相同索引位置的元素

# best idea 利用集合去重
# n=len(matrix)
#         for row in matrix:
#             if len(set(row))!=n: # 强制转换为集合，然后用集合去重
#                 return False
#         for col in zip(matrix):
#             if len(set(col))!=n:
#                 return False
#         return True

# another idea BETTER THAN MY 利用集合，判断是否有重复的整数即可判断不全是，对立思想
# class Solution:
#     def checkValid(self, matrix: List[List[int]]) -> bool:
#         n = len(matrix)
#         occur = set()   # 每一行/列出现过的整数
#         # 判断每一行是否符合要求
#         for i in range(n):
#             occur.clear()   # 确保统计前哈希表为空
#             for j in range(n):
#                 if matrix[i][j] in occur:
#                     # 出现重复整数，该行不符合要求
#                     return False
#                 occur.add(matrix[i][j])
#         # 判断每一列是否符合要求
#         for i in range(n):
#             occur.clear()   # 确保统计前哈希表为空
#             for j in range(n):
#                 if matrix[j][i] in occur:
#                     # 出现重复整数，该列不符合要求
#                     return False
#                 occur.add(matrix[j][i])
#         return True
