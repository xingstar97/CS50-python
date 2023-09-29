students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

gryffindors2 = {student : "Gryffindor" for student in students}

print(gryffindors)
print(gryffindors2)