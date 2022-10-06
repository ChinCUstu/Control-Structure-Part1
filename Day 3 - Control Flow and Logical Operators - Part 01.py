#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Welcome to the rollercoaser!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")


# ### Exercise Odd or Even

# ##### Instructions: Write a program that works out whether if a given number is an odd or even number.

# In[ ]:


print("Welcome to number checker")
num = int(input("Which number do you want to check? "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")


# ### Nested "if" Statements and "elif" statements

# In[ ]:


print("Welcome to the rollercoaser!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 13:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride.")


# # BMI Calculator 2.0

# #### Instructions: Write a program that interprets the Body Mass Index (BMI) based on a user's weight.

# In[ ]:


print("Welcome to my BMI Calculator 2.0!")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / height ** 2
bmi = round(bmi)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

    


# ## Exercise Leap Year

# #### Instructions: Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366 days, with an extra day in February.

# In[ ]:


print("Welcome to leap year check!")
year = int(input("Input which year you want to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# ### Multiple If Statements

# In[ ]:


print("Welcome to the rollercoaser!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
        
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo. == "Y":
       #Add $3 to their bill
        bill += 3
    print(f"Your final bill is {bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")


# ## Pizza Order

# #### Instructions: Congratulations. You've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# ###### Based on a user's order, work out their final bill

# In[ ]:


print("Welcome to Python Pizza!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    if size == "S":
        bill += 1
    
print(f"Your final bill is ${bill}.")


# ### Logical Operators

# In[ ]:


print("Welcome to the rollercoaser!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age > 44 and age < 56:
        print("Everything is going to bee ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12")
        
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
       #Add $3 to their bill
        bill += 3
    print(f"Your final bill is {bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")


# ### Love Calculator

# ###### Instructions: You are going to write a program that tests the compatibility between two people. We're going to use the super scientific method recommended by BuzzFeed

# In[ ]:


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

T = lower_case_name1.count("t") + lower_case_name2.count("t")
R = lower_case_name1.count("r") + lower_case_name2.count("r")
U = lower_case_name1.count("u") + lower_case_name2.count("u")
E = lower_case_name1.count("e") + lower_case_name2.count("e")
true_total = (T + R + U + E)

L = lower_case_name1.count("l") + lower_case_name2.count("l")
O = lower_case_name1.count("o") + lower_case_name2.count("o")
V = lower_case_name1.count("v") + lower_case_name2.count("v")
E = lower_case_name1.count("e") + lower_case_name2.count("e")
true_love = (L + O + V + E)

# print(f"Your score is {true_total}{true_love}.")

score = f"{true_total}{true_love}"

if score < "10" or score > "90":
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= "40" and score <= "50":
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


# In[ ]:




