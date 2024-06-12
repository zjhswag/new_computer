def minPathSum(grid):
    """
        :type grid: List[List[int]]
        :rtype: int
        """
    # 2 空间优化后
    m, n = len(grid), len(grid[0])
    r = [grid[0][0]] + [0] * (n - 1)
    c = [grid[0][0]] + [0] * (m - 1)

    for i in range(1, n):
        r[i] = grid[0][i] + r[i - 1]
    for i in range(1, m):
        c[i] = grid[i][0] + c[i - 1]
    # print(r, c)
    for i in range(1, m):
        for j in range(1, n):
            if j != 1:
                r[j] = min(r[j] + grid[i][j], r[j - 1] + grid[i][j])
                # print(r[j],"22")
            else:
                r[j] = min(r[j] + grid[i][j], c[i] + grid[i][j])
                # print(r[j])
    return r[n - 1]

    # 1 优化前
    # 当 i>0 且 j=0时，dp[i][0]=dp[i−1][0]+grid[i][0]
    # 当 i=0且 j>0时，dp[0][j]=dp[0][j−1]+grid[0][j]
    # 当 i>0 且 j>0 时，dp[i][j]=mib(dp[i−1][j],dp[i][j−1])+grid[i][j]

    # dp = [[0 for _ in range(n)] for _ in range(m)]
    # # print(dp)
    # dp[0][0] = grid[0][0]
    # for i in range(1, n):
    #     dp[0][i] = grid[0][i] + dp[0][i - 1]
    # for i in range(1, m):
    #     dp[i][0] = grid[i][0] + dp[i - 1][0]
    # # print([row[0] for row in dp])
    # for i in range(1, m):
    #     for j in range(1, n):
    #         dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])
    # return dp[m - 1][n - 1]


grid = [[1, 2, 3], [4, 5, 6]]
# print(len(grid))
print(minPathSum(grid))

# 空间优化是因为每一行的值取决于上一行和当前行的前一个数据
