#this program calculates the factorial of a number

num = int(input("Enter a number: "))
def factorial (num):
    if num < 0:
        return None
    elif num < 2:
        return 1
    else:
        result = 1
        for i in range (2, num + 1):
            result = result * i
    return result
print(factorial(num))  