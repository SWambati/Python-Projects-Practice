#this program assists a user to create a strong password

import random
import string


def generate_strong_password(length=12):

    if length < 8:
        length = 8

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    password =[
            random.choice(upper),
            random.choice(lower),
            random.choice(digits),
            random.choice(special_chars)
        ]

    all_chars = upper + lower + digits + special_chars

    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return "".join(password)

def validate_password(password):
    if len(password) < 8:
        return "Password length must be at least 8 characters long."
    if not any(char.islower() for char in password):
        return "Password must contain at least 1 lowercase character."
    if not any(char.isupper() for char in password):
        return "Password must contain at least 1 uppercase character."
    if not any(char.isdigit() for char in password):
        return "Password must contain at least 1 number."
    if not any(char in string.punctuation for char in password):
        return "Password must contain at least 1 special character."
    
    return "Your password is strong"

def main_program():
    print("Welcome to the Strong Password Generator and Validator!")
    print("Please choose either of the 2 options below:")

    print("1. Generate a random password: ")
    print("2. Create your own password: ")

    option = input("Choose any of the options above (1 or 2): ")

    if option == "1":
        length = int(input("Ebter your desired password length, minimum is 8 characters: "))
        password = generate_strong_password(length)

        print(f"Your new password is: {password}. Please keep it safe and hidden")
    
    elif option == "2":
        password = input("Enter your password: ")

        validate = validate_password(password)

        print(validate)

        while validate != "Your password is strong":
            password = input("Enter another password:")
            validate = validate_password(password)
            print(validate)
    
    else:
        print("Please enter a valid option between 1 and 2")


main_program()


    
