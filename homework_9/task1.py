def pi(n):
    sum_series = 0.0
    for i in range(n):
        sum_series += (-1)**i / (2 * i + 1)
    
    x = 4 * sum_series
    return x

values = [10, 100, 10000, 100000]


for n in values:
    x = pi(n)
    print(f"n = {n}, x = {x}")
