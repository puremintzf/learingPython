#函数的参数说明
#写一个求n次方的函数
# def power(a,b):
#     result=1;
#     while b>0:
#         result=result*a;
#         b=b-1;
#     return result;
# print(power(2,8));

#如果没有定义某个函数可以设置某个是个默认值
def power2(a,b=2):
    s=1;
    while b>0:
        b = b - 1;
        s=s*a;
    return s;
print(power2(5,3));