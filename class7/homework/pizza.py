import sys
from tabulate import tabulate
import csv

if len(sys.argv) !=2:
    sys.exit("Incorrect command line arguments!")
else:
    name = sys.argv[1]
    if not name.endswith(".csv"):
        sys.exit("Wrong file format!")

try: 
    with open(name, "r") as file:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers = "keys", tablefmt="grid"))
        #tabular data iteratable
except FileNotFoundError:
    sys.exit("File not found!")
