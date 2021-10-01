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

#Tip Calculator

print("Welcome to Tip Calculator!\n")

total_bill = input ("What was the total bill? $")
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15: ")
no_of_people = input("How many people to split the bill? ")

percentage_formula = int(percentage_tip)/100 #tip in percentage
total_tip = int(total_bill)*float(percentage_formula) #total tip amount

final_bill = int(total_bill) + float(total_tip) #final bill
split_formula =float(final_bill)/int(no_of_people) #bill split w/ no of people

split_bill = round(split_formula, 2) #biil each person

print(f"Each person should pay ${split_bill}")

#Day 3 Control Flow and Logical Operators
number = int(input("Which number do you want to check? "))

input_number = number % 2

if input_number == 0:
  print("You have entered an even number")
else:
  print("You have entered an odd number")
  
#BMI 

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = int(weight / (height ** 2))

if bmi <= 18.5:
  print(f"Your bmi is {bmi}. You are underweight")
elif bmi <= 25:
  print(f"Your bmi is {bmi}. You have a normal weight")
elif bmi <= 30:
  print(f"Your bmi is {bmi}. You are slightly overweight")
elif bmi <= 35:
  print(f"Your bmi is {bmi}. You are obese.")
else:
  print(f"Your bmi is {bmi}. You are clinically obese") 
  
#Leap year
year = int(input("Which year do you want to check? "))

if year % 4  == 0:
  if year % 100 == 0:
    if year % 400 == 0:
        print("Leap year")
    else:
      print("Not a leap year")
  else:
    print("Leap year")
else:
  print("Not a leap year")

#Pizza Order
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
add_cheese = input("Do you want extra cheese? Y or N ")

bill = 0 

if size == "S":
  bill += 15
  if add_pepperoni == "Y":
    bill +=2
    if add_cheese == "Y":
      bill +=1
      print(f"Your total bill is ${bill}")
    else:
      print(f"Your total bill is ${bill}")
  else:
    print(f"Your total bill is ${bill}")
elif size == "M":
  bill += 20
  if add_pepperoni == "Y":
    bill +=3
    if add_cheese == "Y":
      bill +=1
      print(f"Your total bill is ${bill}")
    else:
      print(f"Your total bill is ${bill}")
  else:
    print(f"Your total bill is ${bill}")
elif size == "L":
  bill += 25
  if add_pepperoni == "Y":
    bill +=3
    if add_cheese == "Y":
      bill +=1
      print(f"Your total bill is ${bill}")
    else:
      print(f"Your total bill is ${bill}")
  else:
    print(f"Your total bill is ${bill}")


