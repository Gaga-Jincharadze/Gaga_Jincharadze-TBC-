from task2_def import gcd_iterative

def lcm(a, b):
    return (a * b) // gcd_iterative(a, b)

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    
    if not (0 < a < 10000 and 0 < b <= 10000):
        print("Both numbers must be between 1 and 1000.")
        return
    
    print(lcm(a, b))

main()



