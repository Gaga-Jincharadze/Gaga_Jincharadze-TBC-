String = str(input("Enter String: "))

for i in range(0,len(String)):
        if i % 2 == 0 and String[i] != 'e':
            print(String[i], end="")