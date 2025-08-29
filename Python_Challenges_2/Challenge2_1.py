#variable swapping using addition and subtraction

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1- num2

print("Here are your numbers after swapping: ")
print(f"First number: {num1}; Second number: {num2}")