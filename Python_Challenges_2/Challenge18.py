#this program checks if 2 strings are anagrams

word1 = input("Enter a word: ")
word2 = input("Enter another word: ")

word1 = word1.lower()
word2 = word2.lower()

def are_anagrams(word1, word2):
    if sorted(word1) == sorted(word2):
        print(f"{word1} and {word2} are anagrams")
    else:
        print(f"{word1} and {word2} are not anagrams")


are_anagrams(word1, word2)