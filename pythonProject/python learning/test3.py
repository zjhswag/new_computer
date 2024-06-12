# for i in range(1,6):
#     print("sb")
#     if i<3:
#         continue
#     if i>4:
#        print("over"); break
#     print(i)
import random as rd   
money=10000
for num in range(1,21):
    n=rd.randint(1,10)
    if n>5 and money!=0 :
        money=money-1000
        print("员工",num,"号得到1000")
        
print("over",num,money)
