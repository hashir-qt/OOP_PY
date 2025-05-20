class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    return age

# Test
try:
    check_age(15)
except InvalidAgeError as e:
    print(e)  # Output: Age must be 18 or older