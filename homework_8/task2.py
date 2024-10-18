a = str.lower(input("Enter the first string: "))
b = str.lower(input("Enter the second string: "))

ispossible = True
i = 0
j = 0

while i < len(b):
    found = False 
    while j < len(a):
        if b[i] == a[j]:
            found = True  
            break  
        j += 1

    if not found:
        ispossible = False
        break
    
    j = 0
    i += 1

if ispossible:
    print("Yes")
else:
    print("No")