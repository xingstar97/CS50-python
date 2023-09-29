with open("name.txt", "r") as file:

#readlines reads all lines in the file and return them as a list   
    lines = file.readlines()

for line in lines:
    print(line.rstrip())



with open("name.txt", "r") as file:
    for line in file:
        print(line.rstrip())


with open("name.txt", "r") as file:
    for line in sorted(file):
        print(line.rstrip())