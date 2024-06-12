# 法1，取代，分割，分割，取出黑马程序员
str='月薪过万，员序程马黑来，nohtyp学'
str1=str.replace('来','')
str1_list=str1.split('，')
print(str1_list[1][::-1])

str11=str.replace('来','').split('，')[1][::-1]#链式编程
print(str11)


# 法2 倒序，取位置
str2=str1[::-1]
# print(str2.index('，'),str2.index('，',9,15))
print(str2[str2.index('黑'):str2.index('，',9,15)])

# 法三
str3=str[::-1][9:14]
print(str3)