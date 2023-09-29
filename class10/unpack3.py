def f(*args, **kwargs):
    # *args: the function takes variable number of positional arguments and returns a tuple
    # **kwargs: the function takes variable number of keyword arguments and return a dictionary
    # print("Positional: ", args)
    print("Named: ", kwargs)

# f(100, 50, 25)
f(galleons = 100, sickles = 50, knuts = 25)