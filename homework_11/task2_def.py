def gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a
