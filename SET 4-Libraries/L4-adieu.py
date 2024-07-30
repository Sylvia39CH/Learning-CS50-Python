#提示用户输入一串名字并存在列表中
list = []
i = 0 
while True:
    try: 
        name = str(input("Input names, one per line; or input control + d to finish: ")).title()
        list.append(name)
        
    except EOFError:
        break

#将列表转化成带有“， ”的格式，存入新的列表
list_1 = [str(i) + ", "  for i in list]

#分三种情况打印
if len(list) > 2:
    names = ''.join(str(i) for i in list_1[0:-2])
    print(f"Adieu, adieu, to {names}{list[len(list)-2]} and {list[len(list)-1]}")
elif len(list) < 2:
    print(f"Adieu, adieu, to {list[0]}") 
else:
    print(f"Adieu, adieu, to {list[0]} and {list[1]}")   