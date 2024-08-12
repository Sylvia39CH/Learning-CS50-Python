import csv
import sys

try: 
    before = sys.argv[1]
    after = sys.argv[2] 

    with open(after,"a",newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["first","last","house"])
    
    with open(before,"r") as file:
        reader = csv.DictReader(file)
        n = []
        for row in reader:
            n = row["name"].split(", ")
            student = [n[1],n[0],row["house"]]
        
            with open(after,"a",newline='') as file:
                writer = csv.DictWriter(file,fieldnames=["first","last","house"])
                writer.writerow({"first":student[0],"last":student[1],"house":student[2]})


except FileNotFoundError:
    sys.exit("The original file is not found.")

except IndexError:
    sys.exit("Lack of argument.")   



"""
第21-23行，采用逐行读取——将新行循环写入新文件的方式
在此之前，通过8-10行，先增加了header

注意，如果19-21行写成如下形式来增加header，则会出现一行header、一行内容的形式，是有误的：
writer = csv.DictWriter(file,fieldnames=["first","last","house"])
    writer.writeheader()
    writer.writerow({"first":student[0],"last":student[1],"house":student[2]})


另一解法见L6-sourgify1.py

"""
