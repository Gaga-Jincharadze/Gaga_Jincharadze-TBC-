number = int(input("Enter Your Number: "))
n = 1

while n < number:
    print(f"divisors of {n}:", end=" ")
    
    i = 1
    count = 0
    while i <= n and count < 3:
        if n % i == 0:
            print(i, end=" ")
            count += 1
        i += 1
    print()
    n += 1