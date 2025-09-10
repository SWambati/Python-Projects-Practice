#this program checks if a string is a palindrome

string = input("Enter a word: ")

reverse = string[:: -1]

if string == reverse:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")