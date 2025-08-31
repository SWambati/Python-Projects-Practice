#the program checks if a number is even or odd

num = int(input("Enter a number: "))
result = num % 2

if result == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")