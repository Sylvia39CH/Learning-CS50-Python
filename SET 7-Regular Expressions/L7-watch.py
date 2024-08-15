import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"^https?://(?:www\.)?youtube\.com/embed/(.+)$",s)
    if matches: 
        return ("https://youtu.be/")+matches.group(1)
    else:
        return None


if __name__ == "__main__":
    main()


"""
题目及测试用：
<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
- http://youtube.com/embed/xvFZjo5PgG0
- https://youtube.com/embed/xvFZjo5PgG0
- https://www.youtube.com/embed/xvFZjo5PgG0
"""
"""
re.removeprefix()可以用于去掉括号中的前缀
re.sub()可以用于替换，例如attribute = re.sub(r"^https?://(www\.)?youtube\.com\.embed/","https://youtu.be/",s)
这样直接替换前缀。但是由于本题涉及替换，所以换用re.search.
(www.)的括号，是用于表示这个www.这一组可以没有，但并不需要作为一个group捕获，所以www前面加了“?:”表示不捕获。
这样，group就可以用（1）而不是（2）了

如果没有:?,并且写的是group(2)，就会在用户的输入没有包含www.的时候报错，因为这时候group（1）才是要捕获的内容，而group（2）为空。


"""
