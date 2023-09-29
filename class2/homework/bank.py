greet = input("Hello! ").lstrip().upper()

if greet.startswith("HELLO"):
    print("$0")
elif greet.startswith("H"):
    print("$20")
else:
    print("$100")
