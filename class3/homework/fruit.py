fruit = input("Fruit: ")

fruits = {
    "Apple":"130",
    "Avocado": "50",
    "Banana":"110",
    "Cantaloupe":"50",
    "Grapefruit":"60",
    "Grapes":"90",
    "Honeydew Melon": "50"
}

if fruit in fruits:
    print(fruits[fruit])