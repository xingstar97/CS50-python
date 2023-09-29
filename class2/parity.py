def main():
    x = int(input("Number: "))
    if even(x):
        print("Even")
    else:
        print("Odd")
    
def even(x):
    return True if x%2 == 0 else False

# x%2 == 0 is a bool, it has two values true or false
# def even(x):
#     return x%2==0

main()