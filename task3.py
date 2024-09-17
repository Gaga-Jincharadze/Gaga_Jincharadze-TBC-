#Task 1
    
import math
X  = float(input("Enter Your X Number: "))
Y  = float(input("Enter Your Y Number: "))

print(math.pow(X , Y))


#Task 2
import random

print(round(random.uniform(0, 1000),2))


# Task 3

import datetime

year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

# Date creation
birth_date = datetime.date(year, month, day)

# Number of the week, where 1 = Monday, 7 = Sunday
N = birth_date.weekday() + 1

if N == 1:
    print("You were born on a Monday")
elif N == 2:
    print("You were born on a Tuesday")
elif N == 3:
    print("You were born on a Wednesday")
elif N == 4:
    print("You were born on a Thursday")
elif N == 5:
    print("You were born on a Friday")
elif N == 6:
    print("You were born on a Saturday")
elif N == 7:
    print("You were born on a Sunday")



#Task 4

import random 

#random value

A = random.choice([1,2,3,4,5,6,7,8,9,10,'A','J','K', 'Q', 'J'])

#random color

B = random.choice(['♣','♦','♥','♠'])

#random card

print(A,B)


