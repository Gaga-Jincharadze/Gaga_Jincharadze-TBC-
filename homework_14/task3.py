def fibonacci_generator(n):
    a, b = 0, 1
    result = ()
    for _ in range(n):
        result += (a,)
        a, b = b, a + b
    return result

print("First 5 members: ", fibonacci_generator(5))
print("First 5 members: ", fibonacci_generator(10))
print("First 5 members: ", fibonacci_generator(8))
print("First 5 members: ", fibonacci_generator(15))