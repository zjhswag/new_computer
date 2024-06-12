# 这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。
#
# 给定三个整数 n ,  k 和 target ，返回可能的方式(从总共 k**n 种方式中)滚动骰子的数量，使正面朝上的数字之和等于 target 。
#
# 答案可能很大，你需要对 10**9 + 7 取模 。  动态规划

# 1 <= n, k <= 30
# 1 <= target <= 1000


# 这题较难，目前还没看太懂

def numRollsToTarget(n, k, target):
    """
    :type n: int
    :type k: int
    :type target: int
    :rtype: int
    """
    mod = 10 ** 9 + 7
    f = [[0] * (target + 1) for _ in range(n + 1)]
    f[0][0] = 1
    for i in range(1, n + 1):  # n个骰子
        for j in range(target + 1):  # j目标值
            for x in range(1, k + 1):  # k个面
                if j - x >= 0:
                    print("i:", i, "j:", j, "f[i-1][j-x]:", f[i-1][j-x])
                    f[i][j] = (f[i][j] + f[i - 1][j - x]) % mod
                    print(f, f[i][j])
    return f[n][target]



print(numRollsToTarget(n = 4, k = 6, target = 7))

