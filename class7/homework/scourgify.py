import csv
import sys

if len(sys.argv)!=3:
    sys.exit("Wrong command line arguments!")
else:
    name1 = sys.argv[1]
    name2 = sys.argv[2]
    if not name1.endswith(".csv") or not name2.endswith("csv"):
        sys.exit("Wrong file format!")

newfile =[]
try:
    with open(name1, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for name, house in reader:
            last, first = name.split(",")
            newfile.append({"first":first, "last":last, "house":house})
except FileNotFoundError:
    sys.exit("File not found!")

with open(name2, "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first","last","house"])
    writer.writeheader()
    for person in newfile:
        writer.writerow(person)