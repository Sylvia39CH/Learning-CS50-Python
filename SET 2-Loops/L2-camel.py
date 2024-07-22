c = list(input("Please input your name in camel case: "))

for i in range(len(c)):
    if c[i].isupper():#找出字符串里面的大写字母
        c[i] = "_" + c[i]#在这个字符前面增加下划线

c_out = ''.join(c)#把刚才拆散的list重新拼合起来成为str

print(f"{c_out.lower()}")#打印之前全部转化为小写