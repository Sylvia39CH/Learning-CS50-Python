menu = {
"Baja Taco": 4.25,
"Burrito": 7.50,
"Bowl": 8.50,
"Nachos": 11.00,
"Quesadilla": 8.50,
"Super Burrito": 8.50,
"Super Quesadilla": 9.50,
"Taco": 3.00,
"Tortilla Salad": 8.00
}

prices = []
#在循环之外建立一个空白list，用于存放下面item对应的单价
#注意不可以在循环里面简历list，不然会在循环中被反复覆盖

while True:
    try:
        item = input("Input items, one per line; inputs control-d to finish: ").title()
        prices.append(menu[item])
        sum = 0
        for i in range(len(prices)):
            sum += prices[i]
        print(sum) 
    except KeyError:
        pass#忽略输错了的菜名
    except EOFError:
        break#按ctrl+d或者ctrl+z退出

print(f"Total: {sum}")
