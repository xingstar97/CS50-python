# lists of dict
students = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Draco", "house":"Slytherin", "patronus":None}
]

# None reprents the absense of value

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=",")