import random

n = random.randrange(101) 


print(n)  

for i in range(0, 10):
    n1 = int(input("Enter Your Number: "))  

    if n == n1:
        print("You Are Winner")  
        break  
    elif n < n1:
        print("High")  
    else:
        print("Low") 