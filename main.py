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

#Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_name = name1 + name2

combine_name.lower()
t = combine_name.count("t")
r = combine_name.count("r")
u = combine_name.count("u")
e = combine_name.count("e")

l = combine_name.count("l")
o = combine_name.count("o")
v = combine_name.count("v")
e = combine_name.count("e")

true = int(t) + int(r) + int(u) + int(e) 
love = int(l) + int(o) + int(v) + int(e)

score = int(str(true) + str(love))


if (score < 10) or (score > 90):
  print(f"Your score is {score}%, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}%, you are alright together.")
else:
  print(f"Your score is {score}%.")

  
#Treasure Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("Do you wanna go left or right?\n").lower()

if (direction == "left"):
  print("Game Over, you fell into a hole")
elif (direction == "right"):
  action = input("Do you want to swim or wait?\n").lower()
  if (action == "swim"):
    print("Game over, you were attacked by a trout")
  elif (action == "wait"):
    door = input("Which door do you wanna go? Red, Blue, or Yellow?\n").lower()
    if (door == "blue"):
      print("Game over, you were eaten by beasts!")
    elif (door == "red"):
      print("Game over, you were burned to ashes!")
    elif (door == "yellow"):
      print("Congratulations, you win!")
else:
  print("Game over!")

#Day 4 
#Randomisation and Py Lists
  

import random 

print("Heads or Tails?")

random_integer = random.randint(0, 1)

if (random_integer == 1):
  print("Heads")
else:
  print("Tails")
  
  
#Random Names from a List
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

import random

x = len(names)
random_name = random.randint(0, x - 1)
payer = names[random_name]

print(f"{payer} is going to buy the meal today.")

#Treasure Map - List Indexing Practice

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])


selected = (map[vertical-1])
selected[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

#Rock Paper Scissors Game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors] #list of choices

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n")
player_choice = int(choice) #det if 0-2

# print(rps[player_choice])


import random 

computer = random.randint(0, 2)
# rps[computer]

if (player_choice == 0 and computer == 2):
  print(rps[player_choice])
  print("vs\n")
  print("Computer\n")
  print(rps[computer]) 
  print("You win!")
elif (player_choice > computer):
  print(rps[player_choice])
  print("vs\n")
  print("Computer\n")
  print(rps[computer]) 
  print("You win!")
elif (player_choice == computer):
  print(rps[player_choice])
  print("vs\n")
  print("Computer\n")
  print(rps[computer]) 
  print("Draw!")
else:
  print(rps[player_choice])
  print("vs\n")
  print("Computer\n")
  print(rps[computer]) 
  print("You lose!")
