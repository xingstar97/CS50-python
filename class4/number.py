while True:
# try statement
    try:
        x = int(input("X: "))
    except ValueError:
        print("X should be an integer!")
    else:
        break
# when there is ValueError, it will immediately go to except, otherwise it will break

    

while True:
    try:
        x = int(input("X: "))
        break
    except ValueError:
        print("X should be an integer!")




while True:
    try:
        x = int(input("X: "))
        break
    except ValueError:
        pass


print(x)