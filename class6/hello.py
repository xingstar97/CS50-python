# define main
def main():
    name = input("What's your name? ")
    print(hello(name))


# define the default value to to as world
def hello(to = "world"):
    # print(f"hello, {to}")
    return f"hello, {to}"

# call main
if __name__ == "__main__":
    main()
