import sys
import csv
from tabulate import tabulate

headers = []
full = []
table = []

if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) >2:
    sys.exit("Too many command-line arguments ")
else:
    ext = sys.argv[1].split(".")
    if ext[1] != "csv":
        sys.exit("Not a CSV file")
    else:
        try:
            file = open(sys.argv[1], "r")
            reader = csv.reader(file)
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            for row in reader:
                full.append(row)
            headers = (full[0])
            table = (full[1:])
            print(tabulate(table, headers, tablefmt="grid"))




