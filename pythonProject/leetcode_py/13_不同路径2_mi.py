def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    # 优化前
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    # dp = [[0] * n for _ in range(m)]  # or [[0 for _ in range(n)] for _ in range(m)]
    #
    # # dp[0][0] = 1
    # i = 0
    # while i < n and obstacleGrid[0][i] != 1:
    #     dp[0][i] = 1
    #     i = i + 1
    # i = 0
    # while i < m and obstacleGrid[i][0] != 1:
    #     dp[i][0] = 1
    #     i = i + 1
    # print(dp)
    # for i in range(1, m):
    #     for j in range(1, n):
    #         if obstacleGrid[i][j] != 1:
    #             dp[i][j] = dp[i][j-1]+dp[i-1][j]
    #         else:
    #             dp[i][j] = 0
    # return dp[m-1][n-1]

    i = 0
    # 优化后
    dp = [0] * n
    clow = [0] * m
    # print(dp)
    while i < n and obstacleGrid[0][i] != 1:
        dp[i] = 1
        i = i + 1
    i = 0
    while i < m and obstacleGrid[i][0] != 1:
        clow[i] = 1
        i = i + 1
    print(dp, clow)
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] != 1 and j != 1:
                dp[j] = dp[j] + dp[j - 1]
            elif obstacleGrid[i][j] != 1:
                dp[j] = clow[i] + dp[j]
            else:
                dp[j] = 0
        # print(dp)
    # print(dp)
    if n == 1:
        return clow[m - 1]
    return dp[n - 1]


# 继续优化之后，只需要一个数组就行了，很巧妙的地方就是第一列通过将dp[0],直接全赋值为1，若是遇到不同的地方，就将dp[0]赋值为0
#  n = len(obstacleGrid)
#  m = len(obstacleGrid[0])
#  dp = [0] * m
#  # 起点可能有障碍物
#  dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
#  for i in range(n):
#      for j in range(m):
#          # 有障碍物的格子直接赋0
#          if obstacleGrid[i][j] == 1:
#              dp[j] = 0
#          # 否则dp[j]的值由左方和上一次迭代的dp[j]累加而来
#          elif obstacleGrid[i][j] == 0 and j - 1 >= 0:
#              dp[j] = dp[j] + dp[j - 1]
#  return dp[-1]


obstacleGrid = [[0], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [0], [0], [0], [0], [1], [0], [0], [0],
                [0], [0], [0], [0], [0], [0], [0], [1], [1], [0], [1], [0], [0], [1], [0], [0], [0], [0], [1]]
ans = uniquePathsWithObstacles(obstacleGrid)
print(ans)
