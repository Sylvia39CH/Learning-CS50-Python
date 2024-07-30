import random
import sys

while True:
    try:
        n = int(input("Input a level: "))
        level = range(0,(n+1),1)
        
        break
    except IndexError:
        print("Input an integer, larger than 1")
    except ValueError:
        print("Input an integer, larger than 1")
    
x = random.choice(level)

while True:
    try:
        y = int(input("Input a number: "))
        if 0 <= y < x:
            print("Too small!")
        elif y <  0:
            print(f"Input an integer between 0 and {n}")
        elif n >= y > x:
            print("Too large!")
        elif y > n:
            print(f"Input an integer between 0 and {n}")
        else:
            sys.exit("Just right!")
    except IndexError:
        print(f"Input an integer between 0 and {n}")
    except ValueError:
        print(f"Input an integer between 0 and {n}")