#day03 005 dict键值对
dic={'A':1,'B':2,'C':3,'D':4};
dic['E']=5;#添加一个元素
if ('A' in dic) is False:
    print('元素不在里面！');
else:
    print('元素在里面！');

# dic.pop('E');#pop方法将去掉某个键值对
print(dic['E']);
print(dic.get("A2",-1));
print('E' in dic);


#day03 006 set  set中不允许含有相同改得元素
set11=set([1,2,2,3,4,5,5,6,7]);
print(set11);