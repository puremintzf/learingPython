#定义的函数可以返回多个参数
def getMany(x,y):
    return x*10,y*10;
a,b=getMany(2,3);#返回的两个结果分别赋值给了a和b 很实用，返回的仍然是单一值，返回了一个元组tuple
print(a,b)

c=getMany(2,3);
print(c[0],c[1]);#可以认为是返回了一个集合

# 小结
#
# 定义函数时，需要确定函数名和参数个数；
#
# 如果有必要，可以先对参数的数据类型做检查；
#
# 函数体内部可以用return随时返回函数结果；
#
# 函数执行完毕也没有return语句时，自动return None。
#
# 函数可以同时返回多个值，但其实就是一个tuple。