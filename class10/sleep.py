def main():
    n = int(input("How many sheeps? "))
    for i in sheep(n):
        print(i)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐏"*i)
    return flock

if __name__ =="__main__":
    main()