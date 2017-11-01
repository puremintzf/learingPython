#迭代
for i in [1,3,5,7,9,11]:
    print(i)
for s in ('abc'):
    print(s)
#判断该类型是否可以迭代
from collections import  Iterable
flag=isinstance(['sfjkasfnkaf','123dkfkkf'], Iterable)
print(flag)