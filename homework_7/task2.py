String = str(input("Enter String: "))

for i in range(0,len(String)):
        if String[i] not in  {'e','a','o','i','u'}:
            print(String[i], end="")