import random 

numbers = []
new = []

for i in range(50):
    numbers.append(random.randint(1,30))

for i in numbers:
    for _  in range(i):
        new.append(i)
        
print(new)
print(len(new))