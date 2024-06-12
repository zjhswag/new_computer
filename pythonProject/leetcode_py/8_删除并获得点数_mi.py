# def deleteAndEarn(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
nums = [3,4,2,4,4,5,5,5,5]
n = max(nums)+1
suma = [0]*n
for i in nums:
    # print(i)
    suma[i] += i
print(suma)
# suma[i+1]+prev>now?
prev = suma[0]
now = suma[1]
for i in range(2, n):
    print(prev, now)
    prev, now = now, max(now, prev+suma[i])

print(now)



#     new_list = sorted(nums)
#     if len(new_list) == 0:
#         return 0
#     # dp = [0] * len(new_list)+1
#     n = len(new_list)
#     dp = [0] * (n+1)
#     i = 0
#     while i < n - 1 and (new_list[i]+1) != (new_list[i+1]):
#         dp[1] += new_list[i]
#         i = i+1
#
#     # m = new_list[i+1]
#     # b = new_list[i]
#     # dp[1]+=new_list[i]
#     # count_b = new_list.count(b)
#     # count_m = new_list.count(m)
#     # print(i, new_list[i],m,b)
#     # dp[2] = dp[1] - count_b*b
#     # print(dp[2], dp[1])
#     # j = i+1
#     # while j < n - 1 and (new_list[j]+1) != (new_list[j+1]):
#     #     dp[2] += new_list[j]
#     #     j = j+1
#     # dp[2]+=new_list[j]
#     # print(dp[2])
#     # i = i+count_m+1
#     # print(i)
#     # while  (new_list[i]+1) != (new_list[i+1]):
#     #     dp[1] += new_list[i]
#     #     print(i)
#     #     i = i+1
#     # return max(dp[1], dp[2])
#
#
# nums =[1,1,1,1,1,2,2,2,2,3,3,3]
# print(deleteAndEarn(nums))
#
# nums = [1, 2, 3, 4, 1, 2, 3, 5]
# maxVal = max(nums)
# total = [0] * (maxVal + 1)
# for val in nums:
#     total[val] += val
#
# print(total)  # 输出：[0, 2, 4, 6, 4, 5]


