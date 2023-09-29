import csv

names=[]    

with open("name.csv") as file:
    # file is an instance of the class, it has an instance method which returns an iterator to iterate file
    #reader has handled all the format issues in csv
    # csv.reader(): What you get is an iterable, i.e. an object which will give you a sequence of other objects (in this case, strings). 
    # You can pass it to a for loop, or use list() to get an actual list:
    reader = csv.reader(file)
    #for row in reader, here row is a list
    for name, house in reader:
        names.append({"name": name, "house":house})

        
with open("name.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        names.append(row)
        # row is a dictionary    

for name in sorted(names, key = lambda student:student["name"]):
    print(f"{name['name']} is in {name['house']}")    