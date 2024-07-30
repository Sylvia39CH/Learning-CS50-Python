def main():
    fuel =  percentage()
    
    if 0 <= fuel <= 0.01:
        print("E")
    elif 0.01 <= fuel < 0.99:
        print (f"{(fuel*100):.0f}%")
    elif  0.99 <= fuel <= 1:
        print ("F")
    elif  fuel > 1:
        print ("Error: Wrong input (more than 100%)")
    else:
        print ("Error: Wrong input (negative)")

def percentage():
    while True:
        try:
            p =  str(input("Input a fraction: "))
            q = p.split("/")
            return float (int(q[0]) / int(q[1]))
        except ValueError:
            print("Error:  Wrong input (not a fraction)")
        except ZeroDivisionError:
            print("Error : Wrong input (devision by zero)")
        except TypeError:
            print("Error : Wrong input (not a fraction)")
        
    

main()