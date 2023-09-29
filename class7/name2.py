name =input("What's your name? ")


# open returns a file handle, a value that allows people to access the file subsequently
#"w"open the file and recreate it with brand-new contents
#"a" append new contents to the file
#"r" is the default 
file = open("name.txt", "a")
file.write(f"{name}\n")
file.close()


# this statement will automatically close file after file.write is executed
with open("name.txt", "a") as file:
    file.write(f"{name}\n")