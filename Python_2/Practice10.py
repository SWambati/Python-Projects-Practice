#this program illustrates number-string and string-number conversions

num1 = 89
num2 = 78.89

str1  = str(num1)
str2 = str(num2)

print(str1 + " " + str2)

num3 = int(str1)
num4 = float(str2)

print(num3 - num4)

num5 = float(str1)
print(num5 - num4)

num6 = int(str2)
print(num6 - num5)