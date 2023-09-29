import re

email = input("Email: ")

# if re.search("@",email):

# re.search return a corresponding match object

# if re.search("..*@..*", email):
#1st . means any characters, 2nd .*means any characters 0 or more times
# if re.search(".+@.+", email):
# if re.search(".{1}@.+", email):

    
# if re.search(r".+@.+\.edu", email):
#r means raw

# if re.search(r"^.+@.+\.edu$", email):
#^ match the beginning of the input, $ matching the end of the input

# if re.search(r"^.+@.+\.(edu|com|net)$", email):
#|: or

# if re.search(r"^[^@]+@[^@]+\.edu$", email):
#+ means 1 or more things of the left
#[^@] means any characters except @

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#[]means any characters in the square bracket


# if re.search(r"^[a-zA-Z0-9_ ]+@[a-zA-Z0-9_]+\.edu$", email):
# allow whitespace
#or (\w|\s)

#if re.search(r"^\w+@\w+\.edu$", email):
#\w any word character: number, words, and _

# if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
# flag = re.IGNORECASE

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email):
# (\w+\.) group together, ? means 0 or 1 repitition
    print("Valid")
else:
    print("Invalid")
