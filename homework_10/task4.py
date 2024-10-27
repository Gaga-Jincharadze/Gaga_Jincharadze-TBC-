def isprime(number):
    count = 0
    for i in range(1,number+1):
        if  number % i == 0:
            count += 1
    if count == 2:
        print("is prime")
    elif count == 1:
        print("neither")
    else:
        print("is not prime")
        
isprime(10)
isprime(7)
isprime(11)
isprime(1)