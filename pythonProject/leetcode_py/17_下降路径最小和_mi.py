# def minFallingPathSum(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: int
#         """
matrix = [[-48]]
m = len(matrix)
n = len(matrix[0])
dp = [[0] * n for _ in range(2)]
dp[0] = list(matrix[0])
for i in range(1, m):
    curr, prev = i % 2, i % 2 - 1
    dp[curr][0] = min(dp[prev][0], dp[prev][1]) + matrix[i][0]
    for j in range(1, n - 1):
        dp[curr][j] = min(dp[prev][j], dp[prev][j - 1], dp[prev][j + 1]) + matrix[i][j]
    dp[curr][n - 1] = min(dp[prev][n - 1], dp[prev][n - 2]) + matrix[i][n - 1]
print(min(dp[(m - 1) % 2]))
# 空间0(n),时间O(n^2)
