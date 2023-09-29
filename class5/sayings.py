#have main to test if the functions work

def main():
    hello("ting")
    goodbye("ting")


def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")


#when import this library. it will be read from the beginning to the end
#main function will be called
#instead of using main(), use the following

if __name__=="__main__":
    main()

#__name__is a variable whose value is automatically set to be main when running a file from the command line
#main will be called when running from the command line
#but main won't be called when importing as a library