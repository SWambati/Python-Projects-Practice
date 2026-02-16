#this program deciphers cipher text using ceaser cipher with a key of 5

cipher_text = input("Enter a cipher text: ")
plain_text = ""

for char in cipher_text:
    if not char.isalpha():
        continue

    char = char.upper()
    decipher_code = ord(char) - 5
    
    if decipher_code < ord('A'):

        decipher_code = ord("Z") - (ord('A') - decipher_code - 1)

    plain_text += chr(decipher_code)



print(f"The cipher text for {cipher_text} is: {plain_text}")

