for i in [0,1,2]:
    print("Meow")

# start at 0, go up to but not through the number specify (0,1,2)
for i in range(3):
    print("Meow")

# need a variable for counting or updating, but don't care about its name and don't use it later
for _ in range(3):
    print("Meow")


print("Meow\n" *3, end = "")