import random


#主程序：设定level，运算10次，得到分数
def main():
    level = get_level()
    
    score = 0

    for i in range(0,10):#出10次题，每次都重新获得随机数X和Y，然后在函数caculate中比较答案是否正确    
        X = generate_integer(level)
        Y = generate_integer(level)
        z = X + Y
        print(f"{X} + {Y} = ",end="")
        
        if caculate(z) is True:
            score += 1        
        else:
            print(f"The answer is {z}")
            score += 0
        
        print(f"Total Score: {score}")        


#设定level的函数：需要判定用户输入的值，应该是1，2或者3。同时也排除非数字的输入。
def get_level():
    while True:
        n = input("Level: ")
        try:
            if int(n) in [1,2,3]:
                return int(n) 
            else:
                print("Please input 1, 2 or 3.")
                continue
        except ValueError:
            print("Please input 1, 2 or 3.")



#设定生成随机数的函数。我把获取X和Y的函数放在main中了，因为这里除了要获得X和Y，还要进行X+Y的计算，放在main中比较方便。
#根据level的值，来得到随机数的取值范围。
def generate_integer(level):
    integer = range(((level - 1) * 10),(level * 10)) 
    return random.choice(integer)

#设定一个比较x+y与用户答案的函数。注意是有3次回答机会（3轮循环）。回答错了就继续这个3轮循环，回答正确就返回true到main之中。
def caculate(z):
    for i in range(0,3):
        answer = input()
        try:
            if int(answer) != z:
                print("EEE")
                continue
            else:
                print("Correct!")
                return True
        except ValueError:
            print("EEE")
    

if __name__ == "__main__":
    main()
    