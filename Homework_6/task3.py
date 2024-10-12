n = input("Enter Your Number: ")
sum = 0


for i in range (len(n)-1, -1, -1):
    print(n[i], end=" ")
    sum += int(n[i])
print()
print("sum of digits: ", sum)