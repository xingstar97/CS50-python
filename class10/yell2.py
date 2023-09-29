# functional programming
   
def main():
    yell("This", "is", "Cs50")

def yell(*words):
    uppercased = map(str.upper, words)
    # map applied the function to every element of some sequence, e.g., list
    # pass str.upper to map function, map can add () to call it
    # map returns a list
    print(*uppercased)

if __name__ == "__main__":
    main()