#this program calculates BMI for metric and imperial systems
 
def bmi_metric(mass, height):
    height = height ** 2
    result1 = mass / height
    return result1
def bmi_imperial(mass, height):
    mass = mass * 703
    height = height ** 2
    result2 = mass / height
    return result2

option = input("Choose an option: metric_system or imperial_system...")

if option == "metric_system":
    mass = float(input("Enter your body mass in kilograms:"))
    height = float(input("Enter your height in metres: "))
    bmi = bmi_metric(mass, height)
else:
    mass = float(input("Enter your body mass in pounds:"))
    height = float(input("Enter your height inches: "))
    bmi = bmi_imperial(mass, height)

if bmi <= 18.5:
    print (bmi)
    print("You are underweight")
elif bmi > 18.5 and bmi <= 24.9:
    print (bmi)
    print("You are of healthy weight")
elif bmi >=25.0 and bmi <= 29.9:
    print (bmi)
    print("You are overweight")
else:
    print (bmi)
    print("You are obese")
