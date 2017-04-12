
#day3 001 ranges函数可以指定循环的次数  多数还是用  xx in XX 的方式来表示循环 这个和java中是有点相似的
names={'tom','ammy','alice','julic'};
for name in names:
    print(name);
print('--------');
j=0;
a=list(range(100));
for i in a:
    j+=i;
print(j);

while j<=100:
    j+=j;
print('j is:',j);


#day3 002 测试循环功能
L = ['Bart', 'Lisa', 'Adam'];
for ll in L:
    str='hello,'+ll;
    print('Hello,',ll);
    print(str);
    str='';

#day3 003  测试continue结束本次循环
n=0;
while n<10:
    n+=1;
    if n%2==0:
        continue;
    print(n);

#day03 004测试breark
n=0;
while n<100:
    if n>10:
        break;
    n=n+1;
    print(n);