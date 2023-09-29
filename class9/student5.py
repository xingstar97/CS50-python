class Student:
    def __init__(self, name, house):
    #  def __init__(self, name, house = None) give house the default value as None, then house argument is optional
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff","Ranvenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    
        

#     def __eq__(self, other):
#         return self.name == other.name and self.house == other.house
    
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
#     student1 = Student("1", "Gryffindor")
#     student2 = Student("1", "Gryffindor")
#     if student1 == student2:
#         print("same")
#     else:
#         print("not the same")
#     print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # try: 
    student = Student(name, house)
    # except ValueError:
    #     ...
    return student

if __name__ == "__main__":
    main()