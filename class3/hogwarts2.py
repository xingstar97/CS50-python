students = {"Hermione":"Gryffinfor", 
            "Harry":"Gryffindor",
            "Ron":"Gryffindor",
            "Draco":"Slytherin"}

# list use number as index, dict just use the key word as the index
print(students["Hermione"])

# use a for loop to iterate a dict, it iterate the keys
for student in students:
    print(student, students[student])