def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    for c in s[:2]:
        if c.isnumeric():
            return False
    for c in s[-1:]:
        if c.isalpha():
            return False
    for c in s:
        if c.isalnum()==False:
            return False
    for c in s:
        if c.isnumeric():
            if c == "0":
                return False
            else:
                break
    return True

main()