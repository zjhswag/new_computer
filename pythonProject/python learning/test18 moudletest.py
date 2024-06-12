import sys
sys.path.append('../')#./当前目录 ../上一级目录
for i in sys.path:
    print(i)
import mypackage.moudle as m
m.helloinfo()