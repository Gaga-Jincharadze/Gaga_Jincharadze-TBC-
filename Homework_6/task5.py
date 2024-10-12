n = int(input("Enter Your  Number: "))
i = 0

while i <= n:
    print((n - i) * "  ", end="")

    j = i
    while j >= 0:
        print(j,end=" ")
        j += -1
    
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1
