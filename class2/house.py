name = input("Name: ")

match name:
    case "Harry" | "Herminoe" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")