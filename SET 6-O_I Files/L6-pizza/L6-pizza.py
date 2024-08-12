import sys
from tabulate import tabulate

def main():
    n = str(sys.argv[1])
    if n.endswith(".csv"):
        make_table(n)
    else:
        sys.exit(f'Input a files name ended with ".csv"')


def make_table(n):
    with open(n,"r") as file:
        table = []
        lines = file.readlines()
        for line in lines:
            l = line.split(",")
            table.append(l)
    
    print(tabulate(table[1:],headers=table[0],tablefmt="grid"))

if __name__ == "__main__":
    main()