# def 函数名(传入参数):
def len(str):
    count=0
    for i in str:
        count+=1
    print(f"字符串{str}的长度是{count}")

str1="asdasedas是吧"
str2="asda"

len(str1)
len(str2)
def max(a,b):
    """
    """
    if(a>b): 
     print(f"max1")
     return a
    else: 
     print("max2");   
     return b
     
a1=200**10;
a2=2**200
print(f"max is{max(a1,a2),type(max(a1,a2))}")