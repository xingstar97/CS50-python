class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            # Cat.MEOWS MEOWS is associated with class variable
            print("meow")

cat = Cat()
cat.meow()