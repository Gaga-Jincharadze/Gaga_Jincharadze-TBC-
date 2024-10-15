s = str(input("Enter Your String: "))
sequence = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 
                     'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 
                     'z', 'x', 'c', 'v', 'b', 'n', 'm']

for i in range(0,len(s)):
    if s[i] == 'p':
        print('q', end="")
    elif s[i] == 'l':
        print('a', end="")
    elif s[i] == 'm':
        print('z', end="")
    else:
        a = int(sequence.index(s[i]))+1
        print(sequence[a],end="")