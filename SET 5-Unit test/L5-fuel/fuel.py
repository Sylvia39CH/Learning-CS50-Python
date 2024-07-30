import sys



def main():
    fraction = input("X/Y = ").strip().replace(" ","")
    percentage = convert(fraction)
    print(gauge(percentage))              
  
  
def convert(fraction):
    fraction_1 = str(fraction).split("/")

    try:
        x, y = int(fraction_1[0]),int(fraction_1[1])
        if 0 <= x <= y:
            return float(x/y) 
        else:
            sys.exit("Wrong input (X and Y should be positive integers, and X should not be larger than Y)") 
    except TypeError:
        sys.exit("Wrong input (X and Y should be positive integers3)")   
    except ValueError:
        sys.exit("Wrong input (X and Y should be positive integers2)")
    except ZeroDivisionError:
        sys.exit("Wrong input (devision by zero)")    
    
  
def gauge(percentage):
    if percentage == 1:
        return f"F"
    elif percentage == 0:
        return f"E"
    else:
        return f"{(percentage * 100):.0f}%"
          
  
  
if __name__ == "__main__":
    main()