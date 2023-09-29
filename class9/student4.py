class Student:
    ...
# ... is a valid placeholder

def main():
    student = get_student()
    # s1 = Student()
    # s2 = Student()
    # s3 = s2
    # if s1 is s2:
    #     print("Same")
    # else:
    #     print("not the same")
    
    # if s2 is s3:
    #     print("Same")
    # else:
    #     print("not the same")
    # if s1 == s3:
    #     print("Same")
    # else:
    #     print("not the same")


    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()