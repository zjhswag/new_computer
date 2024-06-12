# def longestPalindrome(s):
#     """
#     :type s: str
#     :rtype: str
#     """

s = "acacacacacacacacaecacacacacacacacbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbacacacacacacacacaacacacacacacacac"
# rst = s[0]
# n = len(s)
# out = 0
# for i in range(n-1):
#     for j in range(i+1, n):
#         st = s[i:j+1]
#         print(st)
#         ed = st[::-1]
#         if st == ed and len(st) > out:
#             out = len(st)
#             rst = st
# print(out,rst)


#         n = len(s)
#         if n < 2:
#             return s
#
#         max_len = 1
#         begin = 0
#         # dp[i][j] 表示 s[i..j] 是否是回文串
#         dp = [[False] * n for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = True

#         # 递推开始
#         # 先枚举子串长度
#         for L in range(2, n + 1):
#             # 枚举左边界，左边界的上限设置可以宽松一些
#             for i in range(n):

#                 # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
#                 j = L + i - 1
#                 # 如果右边界越界，就可以退出当前循环
#                 if j >= n:
#                     break
#
#                 if s[i] != s[j]:
#                     dp[i][j] = False
#                 else:
#                     if j - i < 3:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i + 1][j - 1]
#
#                 # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
#                 if dp[i][j] and j - i + 1 > max_len:
#                     max_len = j - i + 1
#                     begin = i
#         return s[begin:begin + max_len]


# def longestPalindrome2(s):
#     """
#     思路二:中心扩展法
#     回文串:如果是奇数串 则分为 left center right三个部分
#           如果是偶数串 则分为 left center1 center2 right  四个部分
#           本次选择的中心为center 和 center1
#     从中心开始向左向右扩展,直至不能扩展,此时就是回文子串最长的长度
#     在下面代码中通过函数确认回文中心和回文长度来确认整个子串
#     """
# print(s)
# n = len(s)
# if s == None or n < 1:
#     print('NONE')


# def aroundcenter(s, left, right):
#     while (left >= 0 and right < n and s[left] == s[right]):
#         # left 和 right分别向左向右扩展
#         left = left - 1
#         right = right + 1
#     # 注意前一个左右相等条件满足时 left和right已经向左向右移动了 长度需要end-start+1 但这里还需要-2
#     return right - left - 1
#
#
# end = 0
# start = 0
# for i in range(n):
#     print(s[i])
#     # 奇数回文子串的长度 循环结束时i代表center 此时既确定了中心i又确定了长度len
#     len1 = aroundcenter(s, i, i)
#     # 偶数回文子串的长度 循环结束时i代表center1
#     len2 = aroundcenter(s, i, i + 1)
#     # 取奇数最长子串和偶数最长子串中更长的
#     len3 = max(len1, len2)
#
#     # 通过中心和长度判断子串的开始和结束
#     # len3代表不断变化回文子串长度 end-start代表上一个回文子串的长度 只有现在的回文子串大于前一个 end-start才会更新
#     # 类似于打擂台
#     if len3 > (end - start):
#         start = i - (len3 - 1) // 2
#         end = i + len3 // 2
#         print(s[start:end + 1])
# 字符串切片是左闭右开型 所以end+1
# print(s[start:end + 1])
