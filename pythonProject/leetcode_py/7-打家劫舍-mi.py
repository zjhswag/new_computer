# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0:
        return 0
    f = [0] * (n + 1)
    # print(f)
    # f[0] = nums[0]
    f[1] = nums[0]
    for i in range(2, n + 1):  # 1.  2. 3.  4...
        f[i] = max((f[i - 2] + nums[i - 1]), f[i - 1])
        print(f[i], f[i - 2] + nums[i - 1], f[i - 1], i)
    return f


nums = [1, 100, 1, 1, 0, -3, -2]
print(rob(nums))
# print(f)
# f[i]存储的是偷前面n个房子能偷到的最大值
# 假设要在n个房子的要偷到最大值（在这n个房子里面任意偷几个房子，只要不相隔），要不要偷第n个房子，取决于
# 偷这个房子加前面的不偷倒数第二个的房子（最大值）的财富之和，与之前偷到倒数第二个房子的（最大值之和）财富，两个比大小，按照这个递推


# def rob(self, nums: List[int]) -> int:
#     prev = 0
#     curr = 0
#
#     # 每次循环，计算“偷到当前房子为止的最大金额”
#     for i in nums:
#         # 循环开始时，curr 表示 dp[k-1]，prev 表示 dp[k-2]
#         # dp[k] = max{ dp[k-1], dp[k-2] + i }
#         prev, curr = curr, max(curr, prev + i)
#         # 循环结束时，curr 表示 dp[k]，prev 表示 dp[k-1]
#
#     return curr

# 空间优化 用两个变量来代替f,prev表示前n-2个房子最大值， curr代表前n-1个， max(curr, prev + i)表示f[i] = max((f[i - 2] + nums[i - 1]), f[i - 1])


