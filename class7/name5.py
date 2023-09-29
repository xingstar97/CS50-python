names=[]

with open("name.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # student = {}
        # student["name"] = name
        # student["house"] = house
        student = {"name": name, "house":house}
        names.append(student)

def get_name(student):
    return student["name"]

#get name is called by sorted function on each of the dictionary in the list
for name in sorted(names, key = get_name):
    print(f"{name['name']} is in {name['house']}")    


#labmda x, y, z: value 1, value 2, value3
for name in sorted(names, key = lambda student:student["name"]):
    print(f"{name['name']} is in {name['house']}")    