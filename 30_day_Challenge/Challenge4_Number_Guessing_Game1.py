import random

secret_number = random.randint(1, 500)
attempts = 3

option = input("Hello there! Would you like to play a game? (yes/no): ").lower()
if option == "yes":
    for i in range(attempts):
        while True:
            try:
                guess = int(input("We are gonna play a simple game. Guess a the secret number, a number between 1 and 500. You have 3 attempts. Enter your guess: "))

                if 1<= guess <= 500:
                    break
                else:
                    print("Your guess is out of range")
            except ValueError:
                print("Your guess has to be a number")
        
        if guess == secret_number:
            print(f"Congratulations! You've guess the correct number: {secret_number}")
        elif i < attempts - 1:
            print("That's not right. Try again")
        else:
            print(f"Better luck next time. The secret number was {secret_number}")

    

else:
    print("Okay, thank you for your time")
        




    



