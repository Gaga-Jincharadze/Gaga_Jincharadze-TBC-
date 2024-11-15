string = str(input("Enter Text And I Will Count Letters:"))
char_count = {}

for i in string:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

for i, count in char_count.items():
    print(f"{i} - {count}")
