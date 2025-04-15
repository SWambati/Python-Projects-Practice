#the program checks whether a password entered by a user is strong or weak
import string

while True:
    password = input("Enter your password: ")

    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    if len(password) < 8:
        print("Strong passwords have at least 8 characters")

    elif not has_lower:
        print("Strong passwords have least one lowercase letter.")

    elif not has_upper:
        print("Strong passwords have at least one uppercase letter.")

    elif not has_digit:
        print("Strong assword have at least one digit.")

    elif not has_symbol:
        print("Strong passwords have at least one symbol (e.g. ! @ # $ %).")

    elif has_lower and has_upper and has_digit and has_symbol and len(password) >= 8:
        print("Your password is strong")
        break  
    else:
        print(" Your password didn't meet any of the strength criteria. Try again!")

