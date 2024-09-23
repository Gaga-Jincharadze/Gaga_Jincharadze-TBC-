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