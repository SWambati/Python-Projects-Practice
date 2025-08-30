#this is a simple calculator program for 2 variables

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operator = input("Enter an operator (+, -, /, *): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "/":
    result= num1/ num2
else:
    result = num1 * num2

print(f"{num1} {operator} {num2} = {result}")