text = input("Text: ")

for c in text:
    if c.lower() in ["a", "e", "i", "o", "u"]:
        print("", end = "")
    else:
        print(c, end = "")

print()