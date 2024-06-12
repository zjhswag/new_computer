import time

start_time = time.perf_counter()
matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]

m = len(matrix)
n = len(matrix[0])
print(m, n)
square = 0
# for h in range(1,2):
#     print(h)
for i in range(m):
    for j in range(n):
        if matrix[i][j] == "1":
            print(i,j)
            square = max(square, 1)
            if i == m - 1 or j == n - 1:
                continue
            j1 = j + 1
            i1 = i + 1
            flag = 1
            while i1 < m and j1 < n and matrix[i1][j] == "1" and matrix[i][j1] == "1":
                for h in range(1, i1 - i + 1):
                    if matrix[i1][j + h] != "1" or matrix[i + h][j1] != "1":
                        flag = 0
                        break
                if flag == 1:
                    j1 += 1
                    i1 += 1
                    square = max(square, (j1 - j) ** 2)
                    # print('ss')
                if flag == 0:
                    break
print(square)

# def maximalSquare(matrix):
#     if len(matrix) == 0 or len(matrix[0]) == 0:
#         return 0
#     maxSide = 0
#     rows, columns = len(matrix), len(matrix[0])
#     for i in range(rows):
#         for j in range(columns):
#             if matrix[i][j] == '1':
#                 print(i, j)
#                 # 遇到一个 1 作为正方形的左上角
#                 maxSide = max(maxSide, 1)
#                 # 计算可能的最大正方形边长
#                 currentMaxSide = min(rows - i, columns - j)
#                 for k in range(1, currentMaxSide):
#                     # 判断新增的一行一列是否均为 1
#                     flag = True
#                     if matrix[i + k][j + k] == '0':
#                         break
#                     for m in range(k):
#                         if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
#                             flag = False
#                             break
#                     if flag:
#                         maxSide = max(maxSide, k + 1)
#                     else:
#                         break
#
#     maxSquare = maxSide * maxSide
#     return maxSquare
# print(maximalSquare(matrix))


def maximalSquare(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    maxSide = 0
    rows, columns = len(matrix), len(matrix[0])
    dp = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                maxSide = max(maxSide, dp[i][j])

    maxSquare = maxSide * maxSide
    return maxSquare

print(maximalSquare(matrix))
end_time = time.perf_counter()
execution_time = (end_time - start_time) * 1000  # 将秒转换为毫秒
print("程序运行时间：", execution_time, "毫秒")
