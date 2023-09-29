import random


def main():
    level = get_level()
    sum =0
    for _ in range(10):
        n1 =generate_integer(level)
        n2 =generate_integer(level)
        answer =int(input(f"{n1} + {n2} ="))
        i =0
        for i in range(3):    
            if answer == n1+n2:
                sum +=1
                break
            else:
                i+=1
                print("EEE")
                if i ==2:
                    print(f"{n1} + {n2} = {n2+n1}")
                else:
                    answer =int(input(f"{n1} + {n2} ="))

    print("Score: ", sum)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
                break
        except ValueError:
            pass 


def generate_integer(level):
    if level ==1:
        return random.randint(0,9)
    elif level==2:
        return random.randint(10,99)
    elif level ==3:
        return random.randint(100,999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()