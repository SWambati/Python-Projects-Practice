#this program determines if an year is a leap year or not

year= int(input("Enter a year: "))

def is_leap_year(year):
    if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
    
result = is_leap_year(year)
if result == True:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
