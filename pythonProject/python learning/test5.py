money=500000
name=input("请您输入您的姓名：")

def check(canshu):
    if canshu:
        print("****查询余额****")
    print(f"您的余额为{money}")

def save(num):
    global money
    print("****存款****")
    money+=num
    print(f"您存款{num}元成功")
    check(False)

def get_money(num):
    global money
    print("****取款****")
    money-=num
    print(f"您取款{num}元成功,当前余额{money}")
    check(False)

def main():
    print(f"欢迎您{name}先生，请选择您的操作：")
    print("1.查询")
    print("2.存款")
    print("3.取钱")
    print("4.退出")
    return input()#input 输入为字符
    

while(True):
    n=int(main())#input 输入为字符
    print(n)
    if n==1:
        check(True)
    elif n==2:
        num=int(input("请输入存款金额"))
        save(num)
    elif n==3:
        num=int(input("请输入取款金额"))
        get_money(num)
    else:
        print('退出')
        break