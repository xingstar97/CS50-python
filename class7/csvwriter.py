import csv

name = input("Name: ")
house = input("House: ")

# with open("name2.csv", "a") as file:
#     writer = csv.writer(file)
#     # WRONG: writer.writerow(name, house)
#     writer.writerow([name, house])


with open("name2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "house"])
    # WRONG: writer.writerow(name, house)
    writer.writerow({"name":name, "house":house})