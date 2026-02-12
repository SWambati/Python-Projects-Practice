#this program converts plain text to cipher text using a cipher key of 5

plain_text =input("Enter a  message: ")
cipher_text =""

for char in plain_text:
    if not char.isalpha():
        continue

    char = char.upper()
    char_code = ord(char)
    cipher_code = char_code +5
    

    if  cipher_code >ord('Z'):
        cipher_code = ord('A') + (cipher_code - ord('Z') - 1)
    
    cipher_text += chr(cipher_code)
    



print(f"Message cipher text: {cipher_text}")
    
