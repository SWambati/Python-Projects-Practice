#this program talkes user inputs in the form of strings and performs simple mathematic operations on them

input_string = input("Enter a line of numbers to be operated on, separated by spaces:   ")
operation = input("Please select an operation (enter the operation number): \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n ")
nums = input_string.split()



try:
    if operation not in ['1', '2', '3', '4']:
        raise ValueError("Invalid operation selected. Please choose a number between 1 and 4.") 
    
    nums = [float(n) for n in nums]

    if operation == '1':
        result = sum(nums)
    
    elif operation == '2':
        result = nums[0]
        for n in nums[1:]:
            result = result - n
    
    elif operation == "3":
        result = 1
        for n in nums:
            result *= n
    
    elif operation == "4":
        result = nums[0]
        for n in nums[1:]:
            if n == 0:
                raise ZeroDivisionError("You cannnot divide a number by zero")
            result = result/ n

        

    print(f"Result: {result}")
    

except ValueError as ve:
    print(f"Error: {ve}") 

except ZeroDivisionError as zde:
    print(f"Error: {zde}")