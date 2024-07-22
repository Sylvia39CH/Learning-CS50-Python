#这个也是plantes这题的解法。我用了多个def。意思跟plate


def main():#要求用户输入牌号，转化为list，然后进行函数is_valid判别之后输出结果
    plates = list(input("Vanity Plates: "))
    
    if is_valid(plates):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if 2 <= len(s) <= 6: #牌号应该在2-6位之间
        if s[0].isalpha() and s[1].isalpha(): #先判断头两位是不是字母
            if len(s) == 2: #如果只输入了两位字母的牌号，就可以返回true了；
                return True
            else: #如果不止两位，再继续下一步
                is_digit(s)
                
        else: #头两位不是字母就错
            return False
    else: #如果牌号的位数不在2-6的范围内都是错
        return False

def is_digit(s):
    for i in range(2,len(s)): #检查第三位到最后一位
        if s[i].isdigit(): #如果有用到了数字，
            if s[len(s)-1].isdigit(): #就去判断最后一位是不是数字
                 return True
            else: #最后一位是不是数字的话就false
                return False
        else: #如果s[]里面没有数字，纯字母，那就true
            return True

main()

"""
 反思：第18行，这里很容易用“if s[i].isalpha()”判断。
 这样判断的意思是“如果s[]里面有字母”，而非“如果s[]全部都是字母”，这样不好进行下一步判断。
 所以这里我用“如果s[]里面有数字”来判断。
"""

