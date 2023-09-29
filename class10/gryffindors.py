students = [
    {"name":"Hermione", "house":"Gryffindor"},
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Ron","house":"Gryffindor"},
    {"name":"Draco","house":"Slytherin"},
    {"name":"Padma","house":"Ravenclaw"}
]

Gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

# for student in sorted(Gryffindors):
#     print(student)

print(Gryffindors)