#LECTURE 0 作业2 ——上过Exception之后再来看
# It’s customary to leave a tip for your server after dining in a restaurant,
# typically an amount equal to 15% or more of your meal’s cost.
# Not to worry, though, we’ve written a tip calculator for you, below!

def main():
    i = float(input("How much is your bill? "))
    n = percent ()
    print("Total with Tips: $", i + i * n)


def percent():
    while True:
        try:
            p = float(input("How much do you want to tip? "))
        except  ValueError:
            print("It is not a float")
        else:
            break
    return p

main ()


#反思：这里尝试了用Exception章节提到的 try-except语法。当输入一个百分数或者其他不是浮点数的内容时，提示错误并要求重新输入一个浮点数