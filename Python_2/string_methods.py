string1 = " sCHOOL IS COOL"

print(string1.capitalize())

print(string1.center(30, '*'))

result= string1.endswith("zedk")
if result == True:
    print(f"{string1} ends with 'zedk'")
else:
   print(f"{string1} does not end with 'zedk'")


print(string1.find("ool", 3))

print(string1.isalnum())

print(string1.isalpha())

print(string1.isdigit())

print(string1.islower())
print(string1.isupper())
print(string1.isspace())

print(":".join(["bananas", "tangerines", "grapes", "kiwis"]))


print(" sCHOOL is COOL".strip())
