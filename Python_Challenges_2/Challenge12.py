#this program reverses digits in a number using loops

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = (reverse * 10) + digit

    num //= 10


print(f"{num} reversed is {reverse}")

