#this program checks if a number is a prime number

def prime_num(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))    
if (prime_num(num)):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")




