#this program generates the Fibonacci sequence up to n terms

n= int(input("Enter a number: "))

print(f"The Fibonacci Sequence for {n} terms: ")

num1, num2 = 0, 1

for _ in range (n):
    print(num1)
    num1, num2 = num2, num1 + num2