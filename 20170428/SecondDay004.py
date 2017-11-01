#函数的参数说明
#写一个求n次方的函数
def power(a,b):
    result=1;
    while b>0:
        result=result*a;
        b=b-1;
    return result;
print(power(2,8));

#如果没有定义某个函数可以设置某个是个默认值
def power2(a,b=2):
    s=1;
    while b>0:
        b = b - 1;
        s=s*a;
    return s;
print(power2(5,3));

# 先定义一个函数，传入一个list，添加一个END再返回：

def add_end(L=[]):
    L.append('END')
    return L;

print(add_end())
print(add_end())
print(add_end())
# 每次输出都会加一个end 并不是想象中的只有一个end
#解决方案

def add_end_improve(L=None):#设置一个默认值
    if L is None:
        L=[];
    L.append('END')
    return L;

print(add_end_improve())
print(add_end_improve())
print(add_end_improve())

