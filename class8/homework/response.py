from validator_collection import validators
from sys import exit

email = input("Email: ")

try:
    validate = validators.email(email)
    exit("Valid!")
except ValueError:
    exit("Invalid!")