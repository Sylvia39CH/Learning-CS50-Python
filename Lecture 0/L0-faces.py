#  In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 😄and any :( converted to 😢.
#  All other text should be returned unchanged.
#Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.
# Be sure to call main at the bottom of your file.

def main ():
    get_str = str(input("Say something with emoticons: "))
    print(f"{convert(get_str)}")

def convert(s):
    s = s.replace(":)","😄").replace(":(","😢")
    return s

main ()

#按题目要求，需要定义一个convert函数
#注意def conver（s）需要一个return值