def main():
    message = list(input("Message: ").lower())
    print(f"{''.join(msg(message))}")

def msg(t):
    for i in range(len(t)):
        if t[i] in ["a","e","i","o","u"]:
            t[i] =  ""
        else:
            t[i] = t[i]
    return t

main()

"""
我之前在第七行错误使用了for循环，这使得最后打印的结果是空值
如果这里用的是for，意思就变成：不断在第7、8行循环，
令列表t里的每个字母都轮番变成"a""(空格)"e""(空格)"i""(空格)"o""(空格)"u""(空格)"
所以最后列表t会变成一个全部都是空格的列表

另外：这里可以用if-else语法，也可以把if-else整个换成while语法，更省字数
"""