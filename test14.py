#the program determines if a year is a leap year and returns the number of days in the month entered
year = int(input("Enter a year: "))  
month = input("Enter a month: ")
day = int(input("Enter a day in the month: "))

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else: 
        return False
    
def days_in_month(year, month):
    if is_year_leap (year):
        if month == "February":
             return 29
        elif month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
            return 31
        else:
            return 30
        
    else:
        if month == "February":
             return 28
        elif month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
            return 31
        else:
            return 30

result = is_year_leap(year)
if result:
    print (year, " is a leap year")
else:
    print(year, " is not a leap year")

days = days_in_month(year, month)
print(month, " in ", year," has ", days, " days")