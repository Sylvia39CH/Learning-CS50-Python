#通过命令行参数打开一个文件，如果是.py文件就继续，不是的话就退出（sys.exit)
#对于打开的
#对于打开的文件，遍历每一行，统计行数，去除以#开头的行，以及空白的行

import sys

def main():
    name = str(sys.argv[1])
    if name.endswith(".py") :
        count(name)
    else:
        sys.exit(f'Please try a ".py" file')

def count(name):    
    with open (name,"r",encoding='utf-8') as file:
        lines = file.readlines()
        counter= 0
    
        for line in lines:            
            if line.replace(" ","") == "\n":#先排除空白行,去掉所有空格后只剩下换行符的，不计入
                counter += 0
            else:
                if line.startswith("#"):
                    counter += 0               
                else:
                    counter += 1
        
        print(counter)

if __name__ == "__main__":
    main()