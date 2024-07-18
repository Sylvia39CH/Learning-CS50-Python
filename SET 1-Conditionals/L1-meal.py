def main():
    time = input("What time is it now? ")

    if 7.0<=convert(time)<=8.0:
        print("It's time for breakfast.")
    elif 12.0<=convert(time)<=13.0:
        print("It's time for lunch.")
    elif 18.0<=convert(time)<=19.0:
        print("It's time for dinner.")
    else:
        return 0

def convert(time):
    t = list(str(time).split(":"))
    m = float(t[0]) + (float(t[1]) / 60)

    return m

if __name__ == "__main__":
    main()



"""
一、
题目假设了用户会输入24小时制的带有冒号的时间，所以靠冒号转化为列表。

二、
return不能忘！
列表里的数位用方括号[]!
这两点我真的很容易错v😂

三、
题目给了代码框架，要求完成两个def的内容
查了一下，__name__ == "__main__"相当于把后文打了个包，并这样使用：
“if __name__ == "__main__":”下面的内容，在原本的.py文件中直接执行；
但是如果原.py文件是作为一个模块，导入其他.py文件中执行的话，这个包里面的内容不执行。

在这个现在这个.py文件，就当是直接运行main就可以了。

四、
一个容易有bug的地方：中文输入很容易输入全角字符的冒号，这样程序会报错。不过我就不解决这个问题啦，反正题目里没有要求v🤣
"""
