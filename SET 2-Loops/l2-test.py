def main():
    message = list(input("Message: ").lower())
    print(f"{''.join(msg(message))}")

def msg(t):
    for i in range(len(t)):
        for t[i] in ["a","e","i","o","u"]:
            t[i] =  ""

    return t

main()

"""
我之前在第七行错误使用了for循环，这使得最后打印的结果是空值
如果这里用的是for，意思就变成，
"""