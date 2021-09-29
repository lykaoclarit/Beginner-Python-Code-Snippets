#Day 1 of 100 - Python Challenge
#Band Name Generator -  printing, string manipulation and variable declaring in python
print("Welcome to the Band Name Generator")

city = input("Which City did you grew up in?\n")
pet = input("What is the name of your pet?\n")

band_name = city + " " + pet
print("Your Band Name is: \n" + band_name)

#Day 2 0f 100
#Learning about Data Types, subscripting, conversion of data types
#Mathematical Operations in Python

two_digit_number = input("Type a two digit number: ")
output = (int(two_digit_number[0]) + int(two_digit_number[1])) 
print(output)

#BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

h = float(height)
w = float(weight)

bmi = (w / (h ** 2))
print(int(bmi))

#Life in Weeks - with using F string
age = input("What is your current age?\n")
remaining_years = (90 - int(age)) 
x = 365
y = 52
z = 12

days = remaining_years * x
weeks = remaining_years * y
months = remaining_years * z

print(f"You have {days} days, {weeks}, and {months} months left.")
