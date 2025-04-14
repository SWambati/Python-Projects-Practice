#the program calculates the area of circle, rectangle, square and triangle
from math import pi, sqrt
shape = input("Choose a shape: circle, rectangle, square or triangle: ")

def circle():
    area = pi * radius * radius
    return area

def rectangle():
    area = length * width
    return area

def square():
    area = pow(side, 2)
    return area

def triangle():
    s = (length1 + length2 + length3)/2
    area = sqrt(s * (s-length1) * (s-length2) * (s - length3))
    return area

if shape == "circle":
    radius = int(input("Enter the radius of the circle: "))
    result = circle()
    
elif shape == "rectangle":
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    result = rectangle()

elif shape == "square":
    side = int(input("Enter the length of a side of the square: "))
    result= square()

elif shape == "triangle":
    length1 = int(input("Enter the length of the first side: "))
    length2 = int(input("Enter the length of the second side: "))
    length3 = int(input("Enter the length of the third side: "))
    result = triangle()

else:
    print("Invalid shape. Choose either rectangle, circle, square or triangle")

print(f"The area of {shape} is {result}")

