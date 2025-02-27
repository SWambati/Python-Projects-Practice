#this program is a guessing game using while loops
answer = "duckies"
your_name = input("Hello! Enter your name: ")
guess = input("Hi "+your_name+ ", we are going to play a guessing game. Enter a random word: ")
while guess != answer:
    print("Yikes! Wrong guess!")
    guess  = input("Guess again: ")
print("Yipee! Congratulations, you guessed right!")