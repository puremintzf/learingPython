#Python读取文件
file=open('d:\\test.txt','r')#打开文件
g=file.read();
print(g)
file.close();#关闭文件

#Python写文件
file_new=open('d:\\test_new.txt','w');#w表示写文件
file_new.write('123\n456\t789\nqwe');#换行写文件
file_new.close();