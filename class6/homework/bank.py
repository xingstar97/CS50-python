def main():
    greet = input("Hello! ")
    print(f"${value(greet)}")

def value(greet):
    greet = greet.lstrip().upper()
    if greet.startswith("HELLO"):
        return 0
    elif greet.startswith("H"):
        return 20
    else:
        return 100

if __name__=="__main__":
    main()
