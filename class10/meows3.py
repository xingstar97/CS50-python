def meow(n: int) -> None:
    # n: int is a type hint, python does not enforce it
    # -> hint what the return value of a function is
    
    # document of function, docstrings
    """"
    Meow n times.
    :param n: number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    for _ in range(n):
        print("meow")

number: int = input("Number: ")
meow: str = meow(number)
print(meow)