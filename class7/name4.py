with open("name.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
    
    #split will return all the parts to the seprated by "," as a list


with open("name.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        print(f"{name} is in {house}")
#python can assign values to two variables at once