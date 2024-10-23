import random
import math

def pi(n):
    counter = 0
    for _ in range(n):
        a, b = random.uniform(0, 1), random.uniform(0, 1)
        if math.sqrt(a**2 + b**2) <= 1:
            counter += 1
    return 4 * counter / n

for n in [100, 1000, 10000, 100000]:
    pi_estimate = pi(n)
    print(f"n = {n}, Pi approximation = {pi_estimate}")