students = [
    {"name":"Hermione", "house":"Gryffindor"},
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Ron","house":"Gryffindor"},
    {"name":"Draco","house":"Slytherin"},
    {"name":"Padma","house":"Ravenclaw"}
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"


Gryffindors = filter(is_gryffindor, students)
# filter pass the function to every element to the sequence
# the function returns True or False, telling me whether I should include or not include the current element in the final sequence
# Gryffindors = filter(lambda s:s["house"] == "Gryffindor", students)

for student in sorted(Gryffindors, key = lambda s:s["name"]):
    print(student)
