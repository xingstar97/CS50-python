def main():
    n = int(input("How many sheeps? "))
    for i in sheep(n):
        print(i)

def sheep(n):
    for i in range(n):
        yield "🐏"*i
    # return one value at a time, and the loop continues working
    # yield returns an iterator to allow your own for loop to iterate over generated values

if __name__ =="__main__":
    main()