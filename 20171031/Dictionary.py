#字典结构 类似于map的key-value
#定义一个集合
fruits=['apple','bnanna','vatermalen','orange','apple','orange']
#定义一个集合
static={}

for fruit in fruits:
    if fruit in static:
        static[fruit]+=1
    else:
        static[fruit]=1

print(static)