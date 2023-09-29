students = [
    {"name":"Hermione", "house":"Gryffindor"},
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Ron","house":"Gryffindor"},
    {"name":"Draco","house":"Slytherin"},
    {"name":"Padma","house":"Ravenclaw"}
]

houses = list()
# or houses = []

for student in students:
    if not student["house"] in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)