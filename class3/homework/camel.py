camel = input("Camelname: ")

for c in camel:
    if c.isupper():
        c = c.lower()
        print(f"_{c}", end="")
    else:
        print(c, end = "")

print()
