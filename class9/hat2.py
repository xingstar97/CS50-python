import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff","Ranvenclaw","Slytherin"]
    
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

def main():
    Hat.sort("Harry")

main()