str = str.lower(input("Enter Text: "))

i = 0
j = len(str) - 1
ispalindrome = True

while i > j:
    if str.isalpha(str[i]) == False:
        i += 1
        continue
    if str.isalpha(str[j]) == False:
        j -= 1
        continue
    if str[i] == str[j]:
        ispalindrome = True
    else:
        break
    
    i += 1
    j -= 1
    
if ispalindrome:
    print("Is Palindrome")
else:
    print("Is Not Palindrome")
