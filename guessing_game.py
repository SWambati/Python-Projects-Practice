#the program is a guessing game where the player is supposed to guess a secret randomly generated number in 3 tries

import random

secret_number = random.randint(1, 500)
attempts = 3

player = input("Hello, player! Please enter your name: ")

for i in range (attempts):
    while True:
        try:
            guess = int(input(f"{player}, I'm thinking of a number, between 1 and 500. You have {attempts} attempts. Take a guess? "))

            if 1 <= guess <= 500:
                break
            else:
                print(f"Your number is out of range, {player}! Enter another number: ")

        except ValueError:
            print(f"Enter a number {player}: ")
    
    if guess == secret_number:
        print(f"Congratulations, {player}! You won. The secret number is {secret_number}")
        break
    elif i < attempts - 1:
        print("That's not right. Try again")
    else:
        print(f"Sorry, {player}. You're out of attempts. The secrete number was {secret_number}")
       


    

    

