def sumOfMultiples(n):
    # a = 0
    a = []
    for b in range(1, n + 1):
        if b % 3 == 0 or b % 5 == 0 or b % 7 == 0:
            a.append(b)
    #       a+=b
    return sum(a)

    # 2 sum1 = 0
    # for i in range(3, n + 1):
    #     if i % 3 == 0:
    #         sum1 += i
    #     elif i % 5 == 0:
    #         sum1 += i
    #     elif i % 7 == 0:
    #         sum1 += i
    #     else:
    #         continue
    # return sum1

# 3 return sum(i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0 or i % 7 == 0)


print(sumOfMultiples(7))
n=10
print([i for i in range(1, n+1) if not all((i%3, i%5, i%7))])
print(sum(i for i in range(1, n+1) if not all((i%3, i%5, i%7))))
#  给你一个正整数 n ，请你计算在 [1，n] 范围内能被 3、5、7 整除的所有整数之和。
# 返回一个整数，用于表示给定范围内所有满足约束条件的数字之和
