import random

n = int(input("Enter Number from 1 to 30: "))
random_numbers = [] 

for _ in range(n):
    random_number = random.randint(0, 1000)
    random_numbers += [random_number] 

for number in random_numbers:
    print(number) 

print("max number is: ", max(random_numbers))