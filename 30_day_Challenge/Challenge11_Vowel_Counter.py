#the program counts the number of vowels in a sentence

vowels = "aeiou"
counter = 0

sentence = input("Please enter a sentence: ")
letters = sentence.lower()

for letters in sentence:
    if letters in vowels:
        counter += 1

print(f"The number of vowels in your sentence is {counter}")








