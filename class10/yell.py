def main():
    yell("This", "is", "Cs50")

def yell(*words):
    uppercased = list()
    for word in words:
        word = word.upper()
        uppercased.append(word)
    print(*uppercased)
    print(uppercased)

if __name__ == "__main__":
    main()