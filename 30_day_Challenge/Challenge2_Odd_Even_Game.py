#the program determines if a value is odd or even

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input\n")
    num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

