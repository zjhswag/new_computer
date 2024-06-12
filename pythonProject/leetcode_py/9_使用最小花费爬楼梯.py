def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    # 1
    n = len(cost)
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])  # 要到当前台阶，只可能是从上一个或者上上个台阶跳过来，取代价最小者
    print(dp)
    return min(dp[n - 1], dp[n - 2])

    # 2
    # n = len(cost)
    # prev = cost[0]
    # curr = cost[1]
    # for i in range(2, n):
    #     prev, curr = curr, min(prev+cost[i], curr+cost[i])
    # return min(curr, prev)


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost))

# 自己独立做出两种方法，第一种里面的dp保留的是跳到该楼梯时的最小花费，第二种优化了空间复杂度
