#this program counts the vowels and consonants in a statement

vowels = "aeiou"
vowel_counter = 0
consonant_counter = 0

statement = input("Enter a sentence: ")
letters = statement.lower()

for letters in statement:
    if letters in vowels:
        vowel_counter += 1
    
    elif letters.isalpha() and letters not in vowels:
        consonant_counter +=1
    

print(f" Number of vowels in the sentence: {vowel_counter}")
print(f" Number of consonants in the sentence: {consonant_counter}")    

