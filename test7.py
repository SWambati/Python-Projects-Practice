vowels = "AEIOU"
result = ""

user_word = input("Enter a word: ")
letters = user_word.upper()

for letters in user_word:
    if letters not in vowels:
        result += letters
        print(result)

