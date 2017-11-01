#读取CSV文件
csv_file=open('d:\\111.csv','r')
contents=csv_file.read()
content=contents.split('\n')
print(content)
c=[];
for cc in content:
    c.append(cc.split(','));

print(c)
csv_file.close()