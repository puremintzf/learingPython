#Cyclic Structure 循环结构
weeks=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
#for day in weeks:
    #print (day)

i=0;
while i<7:
    print(weeks[i]+'\t'+str(i));
    if '星期一' == weeks[i]:
        print('是星期1')
    i = i + 1

