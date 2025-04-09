#the program tests the use of import function and aliases
from math import pow as power
base = int(input("Enter the base number: "))
exponent_num = int(input("Enter the exponent: "))
result = power(base, exponent_num)

print(f"The power of {base} to {exponent_num} is {result}")