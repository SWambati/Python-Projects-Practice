#this program checks if a number num is prime or not and generates all the prime numbers upto num
import math

num = int(input("Enter a number: "))

def is_prime_number(num):
    if num <= 1:
        return False
    
    for n in range(2, int(math.sqrt(num)) +1):
            if num % n ==0:
                return False
    return True

def prime_numbers_before(num):
     prime= []
     for i in range(2, num):
          if is_prime_number(i):
               prime.append(i)
                
     return prime
   

result = is_prime_number(num) 
result2=prime_numbers_before(num)

if result == False:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number\n")
    print(f"Prime numbers before {num}: {result2}")






