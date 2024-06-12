# def wordBreak(s, wordDict):
#     """
#     :type s: str
#     :type wordDict: List[str]
#     :rtype: bool
#     """

# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "andog", "cat"]
# start = 0
# for i in wordDict:
#     len1 = len(i)
#     print(len1)
#     j = 0
#     for j in range(len1):
#         if i[j] == s[start]:
#             start += 1
#             print('yes')
#         else:
#             break
#     if j != len1-1:
#         start -= j
# if start == len(s):
#     print(True)
# not this way ,比如你虽然cats先对上了，最后结果不对，但是可能通过后面的cat开始才对

s = "catsandog"
wordDict = ["ca","cats", "do", "san", "sand", 'a','ndog','andog', "and", "cat"]
# 初始化dp数组
dp = [False] * (len(s) + 1)
dp[0] = True  # 空字符串总是可以被组成

# 遍历字符串s的每一个子串
for i in range(len(s)):
    if dp[i] == True:
        print(i)
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in wordDict:
                print(i,j, s[i:j])
                dp[j] = True
                # if j == (len(s) + 1):
                    # return (dp[-1])

print(dp[-1])









