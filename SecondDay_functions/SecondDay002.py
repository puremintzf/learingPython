#函数进阶学习

#定义一个求绝对值的函数
def absolute(a):
    if a>=0:
        return a;
    else:
        return  -a;

num=input("请输入一个数字：");
num=float(num);
print("绝对值是：",absolute(num));

#导入某个文件的某个函数
#from SecondDay002 import abslute来导入my_abs()函数，SecondDay002是文件名，不带拓展名

def nothing():
    pass;#里面用到了pass表示什么也不做 缺少了pass，代码运行就会有语法错误。

print(nothing());