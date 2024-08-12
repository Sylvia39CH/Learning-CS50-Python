import csv
import sys


try: 
    before = sys.argv[1]
    after = sys.argv[2]  
    
    students = []

    with open(before,"r") as file:
        reader = csv.DictReader(file)
        n = []
        for row in reader:
            n = row["name"].split(", ")
            student = [n[1],n[0],row["house"]]
            students.append(student)

    with open(after,"w",newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["first","last","house"])
        writer.writerows(students)

except FileNotFoundError:
    sys.exit("The original file is not found.")

except IndexError:
    sys.exit("Lack of argument.")


"""
第17行，将读取出来的信息（同时转化了first和last name）存进students这个列表中
在19-22行，直接将整个students列表写入新文件。
由于students列表没有表头，通过21行，在存入students列表前，先写入一个header（"first","last","house）。

"""