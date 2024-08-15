import re
import sys


def main():
    msg = input("Your message: ").lower().strip()
    print(count(msg))


def count(s):
    n = 0
    words = re.split(r"[^\w]",s)
    
    for i in words:
        if i == 'um':
            n += 1
        else:
            n += 0
    return n


if __name__ == "__main__":
    main()