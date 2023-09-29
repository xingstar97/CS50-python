import re

name = input("What's your name? ").strip()
match = re.search(r"^(.+), *(.+)$", name)
#()caputure anything in the () and re.search return it
#(?:)not caputure, just group
# if match:
#     last, first = match.groups()
#     name = f"{first} {last}"

# if match:
#     last = match.group(1)
#     first = match.group(2)
#     name = f"{first} {last}"

# if match:
#     name = match.group(2)+" "+match.group(1)
    
if match := re.search(r"^(.+), *(.+)$", name):
# := assign value and also ask if True or False
    name = match.group(2)+" "+match.group(1)
print(name)