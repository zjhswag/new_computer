# 集合是项目的 无序 集合。每个元素都是唯一的（没有重复项）

# 并且元素必须是不可变的（不能更改）。
# 但是，集合本身是可变的。我们可以在其中添加或删除元素
# set={1,2,3,2,4,3,'asdasd',[1,2,3]}#自动去掉重复,以及不能含可变元素的列表
set1={1,2,3,(1,2,3),'sadad'}
nu=()#列表和元组可这样初始化，集合不行，一定要用set()，因为字典的初始化是{}
print(set1,type(set1),type(nu),nu)
# 增加移除元素，add,update,clear,remove,discard,pop
set1.add('cnm')
set1.update([8,100])
set1.remove(2)
num=set1.pop()#随即删除一个元素，并返回
print(set1,num)
set2={-1,-2,0}
set3=set1.union(set2)
print(set3)

# 支持for循环 不支持while循环 因为不支持下标索引

list1=['geima','ssss','asd','geima','ssss','asd']
setnew=set()
setnew.update(list1)
print(setnew|set1)

# 集合的各种运算，交并集差等