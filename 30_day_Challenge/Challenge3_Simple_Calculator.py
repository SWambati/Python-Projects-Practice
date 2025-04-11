#this is a simple calculator that performs basic mathematical operations and redo calculations without running the program again

def calculator():
     while True:
          try:
               num1 = float(input("Enter a number: "))
               operation = input("Choose an operation: /, *, +, -: ")
               num2 = float(input("Enter another number: "))

               if operation == "/":
                    if num2 == 0:
                         print("Zero division error")
                    else:
                         result = num1 / num2

               elif operation == "*":
                    result = num1 * num2
               elif operation == "+":
                    result = num1 + num2
               elif operation == "-":
                    result = num1 - num2
               else:
                    print("Invalid operation")

               print(f"{num1} {operation} {num2} ={result}")
            
          except ValueError:
               print("Incorrect values entered")
          
          redo = input("Would you like to perform another calculation?(Type yes or no): ").lower()
          if redo != "yes":
               print("End of calculations")
               break


calculator()

                
                    

