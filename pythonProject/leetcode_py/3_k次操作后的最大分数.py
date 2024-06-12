import math
import heapq



def maxKelements(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    for i in range(k):
        max_k, count = max_num1(nums)
        nums[count] = math.ceil(nums[count]/3)
        global sum1
        sum1 += max_k
        print(count, nums, sum1)
    return sum1


num1 = [10,3,10,10,10]
sum1 = 0


def max_num1(nums):
    max1 = num1[0]
    j = 0
    for i in range(1, len(num1)):
        if max1 < num1[i]:
            max1 = num1[i]
            j = i
    return max1, j


print(maxKelements(num1, 5))

heapq.heapify(num1)
print(heapq.heappop(num1))
# 使用python内置小堆
# q = [-x for x in nums]
# heapify(q)
#
# ans = 0
# for _ in range(k):
#     x = heappop(q)
#     ans += -x
#     heappush(q, -((-x + 2) // 3))
# return ans