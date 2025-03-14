#the program calculates the factorial of a number using recursion
num = int(input("Enter a number: "))
def factorial (num):
    if num < 0:
        return None
    elif num < 2:
        return 1
    else:
        result = factorial(num-1) * num
        return result

print("The factorial of the ",num, " is: ", factorial(num))
