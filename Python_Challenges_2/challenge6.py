#this program converts temperature between Fahrenheit and Celsius

temp = input("Choose one: (a)Fahrenheit or (b)Celcius: ")

if temp == "a":
    fahrenheit = float(input("Enter the temperature: "))
    celcius = (fahrenheit - 32) * 5/9
    celcius = celcius.__round__(2)

    print(f"It is {celcius} degree celcius")

else:
    celcius2 = float(input("Enter the temperature: "))
    fahrenheit2 =(celcius2 * 9/5) + 32
    fahrenheit2= fahrenheit2.__round__(2)

    print(f"It is {fahrenheit2} degree celcius")