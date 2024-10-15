s = str(input("Enter Your String: "))
i = 0


while i <= 5:
    if len(s) % 2 != 0:
        print(s[0:1],s[int(len(s)/2):int(len(s)/2)+1],s[-1])
    else:
        print(s[int(len(s)/2-1):int(len(s)/2+1)])
    i += 1
