import argparse

parser = argparse.ArgumentParser(description = "Meow like a cat")
parser.add_argument("-n", default = 1, help = "number of time to meow", type = int)
# add a help parameter to the -n argument, explaining what -n means
# set the default value of -n
args = parser.parse_args()

for _ in range(args.n):
    # access the property called n
    # args.n contains the int human type after -n space
    print("meow")

# command line arguments "meows5.py -h/--help" will show usage information about the program
# [-h] []in documentation means optional