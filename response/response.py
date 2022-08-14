from validator_collection import validators, errors

try:
    email = validators.email(input("What's your email address? "))
except (errors.EmptyValueError, errors.InvalidEmailError):
    print("Invalid")
else:
    print("Valid")




