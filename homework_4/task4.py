n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(0,n+1):
    print(a, end=" ")  # Print the current value of 'a'
    a, b = b, a + b
print(f"\nLast member of the sequence: {b - a}") 