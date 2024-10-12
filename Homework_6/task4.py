n = int(input("Enter Your Number: "))


for i in range(1,n+2):
    print()
    for j in range(1,i):
        print(j, end=" ")
    if i == n+1:
        for i in range(n,1,-1):
            print()
            for j in range(1,i):
                print(j, end=" ")