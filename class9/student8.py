
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        # passing house via init method will call setter function as well

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    @property
    def house(self):
        return self._house
    #when getting a value, call getter function
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff","Ranvenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
        # when setting a value, call setter function
        # if self.house, self.house will call setter function and iterate setter function forever

    def __str__(self):
        return f"{self.name} from {self.house}"
    
def main():
    student = get_student()
    # student.house = "123"
    # passing value here will call setter function

    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()
