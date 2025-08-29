#this program swaps two variables without introducing a third one using tuple unpacking

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
 
num1, num2 = num2, num1

print("Here are your numbers after swapping: ")
print(f"First number: {num1}; Second number: {num2}")

