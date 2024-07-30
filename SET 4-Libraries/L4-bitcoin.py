"""
作业要求：
Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. 
If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
注意抓取exceptions
"""

import sys
import requests


if len(sys.argv) < 2:
    sys.exit("Lack of command-line argument.Please input a number.")

elif len(sys.argv) == 2:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    usdrate = float(str(o["bpi"]["USD"]["rate"]).replace(",",""))
    #这里用连续的方括号，获取嵌套的字典内容
    #查了一下，这里的汇率数字是会用“,”来作分隔的，运算之前先去掉逗号，然后转化为浮点数

    try:
        n = sys.argv[1]
        print(f"${(n * usdrate):,.2f}")
    except requests.RequestException:
        pass
    except ValueError:
        sys.exit("command-line argument is ot a number.Please input a number.")

else:
    sys.exit("Wrong command-line argument.Please input a number.")

#-Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator.