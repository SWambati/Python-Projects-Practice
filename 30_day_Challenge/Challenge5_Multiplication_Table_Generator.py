#the program generates the multiplication table of number entered by a user

num = int(input("Hello user. Kindly enter a number to get it's multiplication table: "))

print(f"Multiplication table for {num} \n")
for n in range(1, 21):
    result = num * n
    print(f"{num} x {n} = {result}")





