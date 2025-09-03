#this program generates the multiplication table for a given numbe

num = int(input("Enter a number: "))

print(f"Multiplication Table for {num}: ")
for i in range(1, 16):
    result = num * i
    print(f"{num} x {i} = {result}")



