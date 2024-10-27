def factorial(number):
    factorial = 1
    i = 1
    while  i <= number:
        factorial = factorial * i
        i += 1
    return factorial
    
print(factorial(-5) ) 