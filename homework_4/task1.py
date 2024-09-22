import random

n = int(input("Enter Number of players: "))


for i in range(1,n+1):
    print(random.randint(1,6),random.randint(1,6))