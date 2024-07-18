#LECTURE 0 作业2
# It’s customary to leave a tip for your server after dining in a restaurant,
# typically an amount equal to 15% or more of your meal’s cost.
# Not to worry, though, we’ve written a tip calculator for you, below!

i = float(input("How much is your bill? "))

n = input("How much do you want to tip? ")

def percent(p):
    if "%" in str(p):
        p = float(p.replace("%",""))/100
    else:
        p = float(p)
    return p



print("Total with Tips: $", i + i * percent(n))

#反思：考虑到有人会输入小数点，有人会输入百分数，增加了这个法则：如果有百分数的话去掉百分号再除以100.
#！！！记得要return，不然percent（p）就没有结果！