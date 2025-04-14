#the program calculates the tan, cos or sin of an angle
from math import radians, sin, cos, tan
angle1 = int(input("Enter the size of an angle in degrees: "))
angle2 = radians(angle1)

trig = input("Which trigonomotery function do you want to perform: sine, cosine or tangent? ")

if trig == "sine":
    result = sin(angle2)
elif trig == "cosine":
    result = cos(angle2)
else:
    result = tan(angle2)

print(f"{trig}({angle1}) = {result}")