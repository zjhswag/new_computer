s = "acabeedbaa"

# n = len(s)
# dp = [[False] * n for _ in range(n)]
# # print(dp)
# begin = 0
# max_len = 1
# for l in range(2, n + 1):
#     for i in range(n - 1):
#         j = l + i - 1
#         if j > n - 1:
#             break
#         if s[i] != s[j]:
#             continue
#         else:
#             if j - i < 3:
#                 dp[i][j] = True
#             else:
#                 dp[i][j] = dp[i + 1][j - 1]
#         if dp[i][j] and j - i + 1 > max_len:
#             max_len = j - i + 1
#             begin = i
# acaa
# 0123
# 1. a
# 2. a a dp[2][3] = 2
# 3. c a dp[1][2] = dp[2][2] and dp[1][1] 1
#    c a dp[1][3] = dp[2][3] and dp[1][2] 2
# 4. a c dp[0][1] = dp[1][1] and dp[0][0] 1
#    a a dp[0][2] = dp[1][1]+2 = 3
#    a a dp[0][3] = dp[1][2]+2 = 3

n = len(s)
dp = [[0] * n for _ in range(n)]
for i in range(n - 1, -1, -1):
    dp[i][i] = 1
    for j in range(i + 1, n):
        if s[i] == s[j]:
            dp[i][j] = dp[i + 1][j - 1] + 2
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
print(dp[0][n - 1])

