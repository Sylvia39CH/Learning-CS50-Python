while True:
#用循环，当除数为零的时候重新询问用户输入正确的表达式
    f = str(input("Input an arithmetic expression: "))
    l = list(f.split(" "))
    #假设用户输入的表达式有空格，将用户输入的字符串转换成列表（用空格来划分），来检查除数不能为零
    if l[1] == "/" and l[2] == "0":
        print("The divisor cannot be 0. Please try again.")
        continue
    else:
        break

print(f"{eval(f):.1f}")
        # eval函数，是将字符串转换为数值的函数，可以处理整数和浮点数，并且可以执行一些简单的数学表达式。

    