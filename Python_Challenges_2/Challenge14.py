#this program is a random number guessing game

import random

user = input("Hello there. What's your name? ")
agree= input(f"Welcome, {user}! Wanna play a game: (yes/ no) ")

chances = 3
correct = random.randint(0, 1000)

if agree == "no":
    print("Okay. Thank you for your time!")
else:
    print("You have 3 chances to guess the right number")
    

    while chances != 0:
        guess =int(input("Guess a rondom number between 0 and 1000: "))
        chances -= 1
    
    if guess == correct:
       print(f"Yeey! You guessed the correct number: {correct}")
        
    else:
       print(f"Yikes! Better luck next time. The correct number: {correct}")
    
    
       