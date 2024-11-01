import random 

numbers = []
new = []

for i in range(50):
    numbers.append(random.randint(1,30))
    
for i in numbers:
    if i not in new:
        new.append(i)

print(len(new))
print(new)