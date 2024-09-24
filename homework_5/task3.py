n = int(input("Enter your Number from 1 to 20: "))
a = 0
b = 1
while a <= n:
    print(a, end=" ")
    a, b = b, a + b