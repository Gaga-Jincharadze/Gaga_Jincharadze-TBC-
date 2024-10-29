def gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    
    if not (0 < a < 10000 and 0 < b <= 10000):
        print("numbers must be between 1 and 1000.")
        return
        

    print(f"Iterative: {gcd_iterative(a, b)}")
    print(f"Recursive: {gcd_recursive(a, b)}")

if 1 > 0:
    main()