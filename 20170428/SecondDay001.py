#开始学习函数
def functionadd(a,b):
    return a+b;

def summany(n):
    i=1;
    sum=0;
    while i<n:
        sum+=n*n+1;
        i+=1;
    return sum;
print(functionadd(1,5));
print(summany(100));
#调用现有的函数
print(abs(-99));
print(max(1,2,4,5,6,78,998));
print(min(-1,-2,-100,99))
print(int(11.12));#使用int函数转化为整数
print(float(123.1231));
# a=input("plz　input a Intenger number:")
n1 = 255;
print(hex(255));#hex函数将十进制数值转化为十六进制的数值