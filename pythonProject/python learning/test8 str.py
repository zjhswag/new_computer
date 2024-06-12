# 字符串是不可变的。
# 这意味着字符串的元素不可更改或删除

str1 = 'i am so handsome'
print(str1[2:3], type(str1[::-1]))

# del str[0]  #will fail
# del str1
print(str1)

local=str1.index('am')
print(local)

#replace 替换字符转变为新字符串
str2=str1.replace('i am','you are')
print(str2)
print(str1) #str1未更改

# split 分割函数得到新列表<class 'list'>
# 不改变之前的字符串 
    # string='i love xi dian'
    # str_list=string.split(" ")
    # str_list.append('University')
    # print(str_list,type(str_list))

#strip方法，不传参数去除首尾空格，传参去参,首尾都去
    # string='i love xi dian '
    # new_str=string.strip()
    # new_str1=string.strip('i o')
    # print(new_str,'\n',string,'\n',new_str1)
    # print(new_str1)

# count 统计字符串中某个的次数
string='i love xi dian'
num=len(string)
print(num) 