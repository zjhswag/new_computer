f=open(r"C:\Users\14601\Desktop\wordcount.txt",'r',encoding='UTF-8')
count=0
 
for line in f:
    # print(line,type(line))  #str class

    # line=line.strip()
    # linelist=line.split(' ')     #get a list without '\n'

    linelist=line.split()
    # print(linelist)
    for num in linelist:
        if num=='itheima':
            count+=1
           

num=f.read().count('itheima')
print(num)
