list = []
i = 0 
while True:
    try: 
        item = str(input("Input items, one per line; or input control + d to finish: ")).upper()
        list.append(item)
        
    except EOFError:
        break
  
list.sort()   
#以上步骤，定义空白列表，要求一个个输入清单，转化为大写，然后按字母表顺序整理


items = [] 
for i in range(0,len(list)-1):
    if list[i] != list[i+1]:
        items.append(list[i])
if list[len(list)-1] not in items:
    items.append(list[len(list)-1])
#以上步骤，由于list已经是按顺序整理好的，就直接比较list里面的前后项，如有不同，就列入新的列表items中
#由于list的最后一项总是没有办法进行跟后项的比较，所以补充了一个if


numbers = []
for n in range(0,len(items)):
    number = 0
    for i in range(0,len(list)-1):    
        if list[i] == items[n]:
            number += 1
        else:
            number += 0
    numbers.append(str(number))
#以上步骤，比对item和list中的每一项，如有相同项则+1，由此统计item中的每一项
#统计出来的每一个number，都存入numbers列表中



for i in range(0,len(items)):
    print(f"{items[i]} : {numbers[i]}")
#由于item列表和numbers列表是一一对应的，只需要按顺序打印出来就行了