import re


def main():
    print(convert(input("Hours: ")))


def convert(s): #timelist(s)函数生成的列表，是包含了两个带着AM或者PM的str，在这里转化后存入新的列表timelist_trans，再输出
    timelist_trans = []
    
    for time in timelist(s):#将timelist(s)函数生成的列表中的内容进行拆解。用户输入9：00 AM和 9 AM两种方式，将转化为具有3个或者2个元素的列表。
        n = re.split(r":| ",time)

        #当n为3个元素（带有：00的输入）或2个元素（不带：00的输入），有不同的转化方式；转化之后存入新的列表timelist_trans中：          
        if len(n) == 3 and 0 <= int(n[1]) < 60:
            if n[2] == "AM":
                n[0] = am(int(n[0]))
            elif n[2] == "PM":
                n[0] = pm(int(n[0]))
            time_trans = f"{n[0]}:{n[1]}"
            timelist_trans.append(time_trans)  
            
        elif len(n) == 2 :    
            if n[1] == "AM":
                n[0] = am(int(n[0]))
            elif n[1] == "PM":
                n[0] = pm(int(n[0]))
            time_trans = f"{n[0]}:00"
            timelist_trans.append(time_trans)  
        else:
            raise ValueError
    # 将转化后的列表按标准格式打印出来
    return (f"{timelist_trans[0]} to {timelist_trans[1]}")
        
def timelist(s): #识别带有AM/PM的字段并将它们用存入一个列表
    pattern = r'(\d+(?:\:(?:\d+))?\s(?:AM|PM))\sto\s(\d+(?:\:(?:\d+))?\s(?:AM|PM))' 
    msg = re.findall(pattern,s)
    if len(msg) == 0:
        raise ValueError
    else:
        for m in list(msg):                  
            timelist = list(m)
            return timelist

def am(t):#对于AM的转化函数
    if int(t) == 12:
        return f"00"
    elif 10 <= int(t) < 12:
        return f"{t}"
    elif 0 < int(t) < 10:
        return f"0{t}"
    else:
        raise ValueError
    
def pm(t):#对于PM的转化函数
    if int(t) == 12:
        return f"{t}"
    elif 0 < int(t) < 12:
        return f"{t+12}"       
    else:
        raise ValueError
        

    

if __name__ == "__main__":
    main()