
while True:
    try:
        x,y = input("Fuel: ").split("/")
        result = int(x)/int(y)
        if result>1:
            pass
        else:
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

if result<=1/100:
    print("E")
elif result>=99/100:
    print("F")
else:
    print(f"{int(result*100)}%")