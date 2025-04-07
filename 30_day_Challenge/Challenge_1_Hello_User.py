#this is a simple program that displays a user's name and their age in days
import datetime

today = datetime.date.today()

name = input("Hello. Kindly enter your name: ")
yob = int(input("Which year were you born: "))
month =int(input("Enter the number of the month you were born: "))
day = int(input("Enter the day you were born: "))

birthday = datetime.date(yob, month, day)
age_in_years = today.year - yob

if (today.month, today.day) < (month, day):
    age_in_years -= 1

age_in_days = (today - birthday).days


print(f"Hello {name}!\n")
print(f"You are {age_in_years} years old. That's somewhere close to {age_in_days} days old!")