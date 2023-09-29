import random

number =0
while True:
    try:
        n = int(input("n: "))
        if n>=1:
            number = random.randint(1,n)
            break
    except ValueError:
        pass

while True:
    try:
        answer = int(input("Number: "))
        if answer <1:
            pass
        elif answer > number:
            print("Too large!")
        elif answer < number:
            print("Too small")
        else:
            print("Just right!")
            break
    except ValueError:
        pass