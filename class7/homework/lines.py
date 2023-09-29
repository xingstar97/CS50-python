import sys

if len(sys.argv)>2:
    sys.exit("Too many command line arguments!")
elif len(sys.argv)<2:
    sys.exit("Too few command line arguments!")
else:
    name = sys.argv[1]
    if not name.endswith(".py"):
        sys.exit("Wrong file name!")

try:
    with open(name, "r") as file:
        sum=0
        for line in file:
            if line.isspace():
                continue
            elif line.strip().startswith("#"):
                continue
            else:
                sum +=1
        print(sum)
except FileNotFoundError:
    sys.exit("File not found!")