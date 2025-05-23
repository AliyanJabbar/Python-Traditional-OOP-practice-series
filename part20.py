# Creating a Custom Exception 
# Assignment: Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.


class InvalidAgeError(Exception):
    def __init__(self):
        print("Invalid Age Error: Age must be 18 or older.")

def check_age(age):
    if age < 18: 
        raise InvalidAgeError()
    else : 
        print("valid age")
        
try :
    check_age(9)  # This will raise the InvalidAgeError
except InvalidAgeError as e: 
    print(e)