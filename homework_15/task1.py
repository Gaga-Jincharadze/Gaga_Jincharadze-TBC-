import random 

random_nums = [random.randint(0,100) for _ in range(100)]
count = 0

for i in range(0,len(random_nums)):
    if random_nums[i] % 2 == 0:
        count += 1
    
my_tup =  {'even' : count, 'odd' : len(random_nums) - count}     

print(my_tup)
