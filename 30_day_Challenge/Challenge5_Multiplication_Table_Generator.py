#the program generates the multiplication table of number entered by a user

num = int(input("Hello user. Kindly enter a number to get it's multiplication table: "))

print(f"Multiplication table for {num} \n")
for i in range(1, 21):
    result = num * i
    print(f"{num} x {i} = {result}")




