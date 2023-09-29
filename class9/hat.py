import random

class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff","Ranvenclaw","Slytherin"]
    
    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

def main():
    hat = Hat()
    hat.sort("Harry")

main()