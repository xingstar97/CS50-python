def main():
 fraction = input("Fuel: ")
 while True:
    try:
         percentage = convert(fraction)
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

 gauge(percentage)


def convert(fraction):    
    x,y = fraction.split("/")
    result = int(x)/int(y)*100
    if result>100:
        raise ValueError
    else:
        return result

def gauge(result):
    if result<=1:
        return "E"
    elif result>=99:
        return "F"
    else:
        return f"{int(result)}%"

if __name__=="__main__":
    main()