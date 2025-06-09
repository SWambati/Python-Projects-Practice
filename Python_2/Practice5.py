#this program mimics a lottery game by utilizing the random module

import random

def generate_winning_numbers():
    return [random.randint(1, 100) for _ in range(4)]

def get_player_guesses():
    guesses = []
    while(len(guesses) < 4):
        try:
            guess = int(input(f"Guess a number between 1 and 100. Enter your {len(guesses)+1}: "))
            if 1<= guess <= 100:
                guesses.append(guess)
            else:
                print("Your guess should be a number between 1 and 20")
        except ValueError:
            print("Invalid input")
    return guesses

def check_guesses(player_guesses, winning_numbers):
    if player_guesses == winning_numbers:
        result = print("Congratulations! You win!")
    else:
        result = print("Better luck next time")
    return result

def play_lottery():
    result = input("Hello there! Do you wanna play a game?{yes/no}: ")
    if result == "no":
        print("Okay. Thank you for your time")
    else:
        print("Welcom to our lottery game. You have 4 turns to guess a series of numbers. You win if your guesses are similar to the winning numbers")
        winning_numbers = generate_winning_numbers()
        player_guesses = get_player_guesses()

        print(f"Your guesses are: {player_guesses}")
        print(f"The lucky numbers are: {winning_numbers}")

        check_guesses(player_guesses, winning_numbers)

play_lottery()



