
coin=[0,0,0,0,0,0,0,0,0,0]
n = 0

while True:
    coin[n] = int(input("Please put in coin one by one: "))
    s = 0
    for i in coin:
        s += i

    if s < 50 : 
        print(f"Total: ${s}")
        n = n + 1
        continue

    else:
        break
    
print(f"Total: ${s}")
print(f"Charge:{s - 50}")

#提示投币

#投币一次，做一次加法，没有到达50之前就循环

    

#达到50之后就循环，并找零