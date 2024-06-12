# def minimumTotal(triangle):
#         """
#         :type triangle: List[List[int]]
#         :rtype: int
#         """
# 优化前时间复杂度o(n^2), 空间O(2n),已经挺好的了。
import copy
triangle = [[-10]]
n = len(triangle)
dp = [float("inf")] * n
dp2 = [0] * n
dp[0] = triangle[0][0]
dp2 = copy.deepcopy(dp)
# print(dp2)
for i in range(1, n):
    for j in range(i + 1):
        if j != 0:
            dp[j] = min(dp2[j - 1] + triangle[i][j], dp2[j] + triangle[i][j])
            # print(j, dp2[j - 1], dp2[j], triangle[i][j])
        else:
            dp[j] = dp2[j] + triangle[i][j]
    # print(dp)
    dp2 = copy.deepcopy(dp)
print(min(dp))

# 虽然优化后空间还是0(2n),但是少了赋值的一步，更快一点，利用奇偶性，用prev计算curr,i加一。则curr变成prev，则可以利用上一行curr计算当前行的curr
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         n = len(triangle)
#         f = [[0] * n for _ in range(2)]
#         f[0][0] = triangle[0][0]
#
#         for i in range(1, n):
#             curr, prev = i % 2, 1 - i % 2
#             f[curr][0] = f[prev][0] + triangle[i][0] # 最左
#             for j in range(1, i):
#                 f[curr][j] = min(f[prev][j - 1], f[prev][j]) + triangle[i][j]
#             f[curr][i] = f[prev][i - 1] + triangle[i][i] # 最右
#
#         return min(f[(n - 1) % 2])

# 从 i到 0 递减地枚举 j，这样我们只需要一个长度为 n 的一维数组 f，就可以完成状态转移，空间复杂度为O(n)
# 什么只有在递减地枚举 j 时，才能省去一个一维数组？
# 当我们在计算位置 (i,j)，f[j+1]到 f[i] 已经是第 i行的值，而 f[0] 到 f[j] 仍然是第 i−1行的值。此时我们直接通过
# f[j]=min(f[j−1],f[j])+c[i][j],当时想了一下可以这样，但是没仔细往下想
#
# class Solution:
# def minimumTotal(self, triangle: List[List[int]]) -> int:
#     n = len(triangle)
#     f = [0] * n
#     f[0] = triangle[0][0]
#
#     for i in range(1, n):
#         f[i] = f[i - 1] + triangle[i][i]
#         for j in range(i - 1, 0, -1):    #最重要的一步
#             f[j] = min(f[j - 1], f[j]) + triangle[i][j]
#         f[0] += triangle[i][0]
#
#     return min(f)



