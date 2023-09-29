
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    # being able to call a get without having a student object already
    # cls(name, house) == Student(name, house): instantiate a student object
    
def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()
