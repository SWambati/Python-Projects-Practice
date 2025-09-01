#this program identifies the largest of three numbers

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
num3 = float(input("Enter the last number: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is the largest of the three numbers")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the largest of the three numbers")
else:
    print(f"{num3} is the largest of the three numbers")
    